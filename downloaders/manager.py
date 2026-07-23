from .api import download_from_api
from .gallery import download_from_gallery
from .ytdlp import download_from_ytdlp

async def download(url: str):
    methods = [
        download_from_api,      # اول API
        download_from_gallery,  # بعد gallery-dl
        download_from_ytdlp,    # آخرین گزینه
    ]

    last_error = None
    for method in methods:
        try:
            return await method(url)
        except Exception as e:
            last_error = e
            continue

    raise Exception(f"همه روش‌ها شکست خوردند: {last_error}")
