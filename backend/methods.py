import yt_dlp
import os
from pathlib import Path
from pydantic import BaseModel


class Video(BaseModel):
    url: str

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT_DIR = BASE_DIR / "videos"


def download_video(video: Video, output_dir: str | Path = DEFAULT_OUTPUT_DIR):
    output_path = Path(output_dir).resolve()
    output_path.mkdir(parents=True, exist_ok=True)
    ydl_opts = {
        'paths': {'home': str(output_path)},
        'outtmpl': {'default': '%(title)s.%(ext)s'},
        'progress_hooks': [my_progress_hook], # function to track progress
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video.url])

    return {"message": "Download started"}

def download_playlist(url, output_dir: str | Path = DEFAULT_OUTPUT_DIR):
    output_path = Path(output_dir).resolve() / get_info(url)
    output_path.mkdir(parents=True, exist_ok=True)

    ydl_opts = {
        'paths': {'home': str(output_path)},
        'outtmpl': {'default': '%(title)s.%(ext)s'},
        'progress_hooks': [my_progress_hook], # function to track progress
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def my_progress_hook(d):
    if d['status'] == 'downloading':
        print(f"Downloading: {d['_percent_str']} at {d['_speed_str']} ETA {d['_eta_str']}")
    elif d['status'] == 'finished':
        print(f"Done downloading {d['filename']}")

def get_info(url):
    """Get information about a video or playlist without downloading"""
    ydl_opts = {
        'quiet': False,
        'no_warnings': False,
        'extract_flat': 'in_playlist'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    # Check if it's a playlist
    if 'entries' in info:
        print(f"Playlist Title: {info.get('title')}")
        return info.get('title', 'unknown')
    else:
        return("This is not a playlist")