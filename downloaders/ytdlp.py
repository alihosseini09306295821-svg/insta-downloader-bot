import os
import tempfile
import yt_dlp

async def download_from_ytdlp(url: str):
    temp_dir = tempfile.mkdtemp()
    
    ydl_opts = {
        "outtmpl": os.path.join(temp_dir, "%(title)s.%(ext)s"),
        "quiet": True,
        "noplaylist": True,
        "merge_output_format": "mp4",
        "format": "bestvideo+bestaudio/best",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

        if "requested_downloads" in info and info["requested_downloads"]:
            filename = info["requested_downloads"][0]["filepath"]
        else:
            filename = ydl.prepare_filename(info)

    return filename
