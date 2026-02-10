import json
from fastapi import requests
import yt_dlp
import os
from fastapi.responses import StreamingResponse

# def download_video(url):
#     ydl_opts = {
#         # 'paths': {'home': output_dir},
#         'outtmpl': {'default': '%(title)s.%(ext)s'},
#         'progress_hooks': [my_progress_hook]
#     }
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info = ydl.extract_info(url, download=False)

#     video_url = info["url"]
#     filename = f"{info['title']}.mp4"

#     return video_url, filename


def download_video(url: str):
    ydl_opts = {'quiet': True, 'extract_flat': False}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    
    video_url = info["url"]
    filename = info["title"]
    channel = info["uploader"]
    duration = info["duration"]
    
    # Stream video to client
    response = requests.get(video_url, stream=True)

    return StreamingResponse(
        response.iter_content(chunk_size=8192),
        media_type="video/mp4",
        headers={"Content-Disposition": f"attachment; filename={filename}.mp4"},
        metadata={"filename": filename, "channel": channel, "duration": duration}
    )


def download_playlist(url, output_dir="downloads"):
    if os.path.isdir(output_dir):
        print(f"Output directory {output_dir} exists.")
    else:
        print(f"Output directory {output_dir} does not exist")
        return

    newpath = f"{output_dir}\\{get_info(url)}"

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

    with open("demofile.txt", "a") as f:
        f.write(json.dumps(info))

    # Check if it's a playlist
    if 'entries' in info:
        return info.get('entries')
    elif 'id' in info:
        return info
    else:
        return("Unknown format")
    
url = "https://youtu.be/pFtxR-O78sY?si=ADM3xLFZAeldB4gm"
download_video(url)