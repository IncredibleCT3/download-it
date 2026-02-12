import yt_dlp
import os

def download_video(url, output_dir='./download-it/videos'):
    ydl_opts = {
        'paths': {'home': output_dir},
        'outtmpl': {'default': '%(title)s.%(ext)s'},
        'progress_hooks': [my_progress_hook], # function to track progress
        'cookiesfrombrowser': ('chrome',),  # or 'chromium', 'edge', 'brave', etc.
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return {"message": "Download started"}

def download_playlist(url, output_dir='./download-it/videos'):
    newpath = f"{output_dir}\\{get_info(url)}"
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    ydl_opts = {
        'paths': {'home': newpath},
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