import httpx
import json
import re
import asyncio
from typing import Optional

async def download_from_api(url: str) -> str:
    """
    تلاش برای دانلود از طریق API غیررسمی اینستاگرام
    """
    try:
        # استخراج shortcode از لینک
        shortcode = extract_shortcode(url)
        if not shortcode:
            raise ValueError("Shortcode پیدا نشد")

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "application/json",
            "X-IG-App-ID": "936619743392459",  # یکی از App ID های رایج
        }

        async with httpx.AsyncClient(timeout=20.0) as client:
            # روش 1: GraphQL
            response = await client.get(
                f"https://www.instagram.com/reel/{shortcode}/?__a=1&__d=dis",
                headers=headers
            )
            
            if response.status_code == 200:
                data = response.json()
                # استخراج لینک رسانه (این بخش نیاز به تنظیم دقیق داره)
                # ...

        # فعلاً به ytdlp فال‌بک می‌کنیم (پایدارتره)
        from .ytdlp import download_from_ytdlp
        return await download_from_ytdlp(url)

    except Exception as e:
        # فال‌بک به ytdlp
        from .ytdlp import download_from_ytdlp
        return await download_from_ytdlp(url)


def extract_shortcode(url: str) -> Optional[str]:
    """استخراج shortcode از لینک اینستاگرام"""
    patterns = [
        r"instagram\.com/(?:p|reel|tv)/([A-Za-z0-9_-]+)",
        r"instagram\.com/stories/[^/]+/(\d+)",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None
