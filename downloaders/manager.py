from downloaders.api import download_from_api
from downloaders.gallery import download_from_gallery
from downloaders.ytdlp import download_from_ytdlp


async def download(url: str):

    errors = []

    # روش اول: API
    try:
        return await download_from_api(url)
    except Exception as e:
        errors.append(f"API: {e}")

    # روش دوم: gallery-dl
    try:
        return await download_from_gallery(url)
    except Exception as e:
        errors.append(f"Gallery: {e}")

    # روش سوم: yt-dlp
    try:
        return await download_from_ytdlp(url)
    except Exception as e:
        errors.append(f"yt-dlp: {e}")

    raise Exception("\n".join(errors))
