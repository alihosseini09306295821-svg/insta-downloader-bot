from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import ContextTypes

from database.users import add_user
from handlers.join import (
    is_joined,
    join_markup,
)


def main_menu():

    keyboard = [
        [
            InlineKeyboardButton(
                "📥 دانلود",
                callback_data="download"
            )
        ],
        [
            InlineKeyboardButton(
                "📢 کانال",
                url="https://t.me/HmHermi"
            ),
            InlineKeyboardButton(
                "👨‍💻 پشتیبانی",
                url="https://t.me/HmHermi"
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


WELCOME = """
╔════════════════════╗
🚀 Universal Downloader
╚════════════════════╝

سلام 👋

به ربات دانلود حرفه‌ای خوش آمدید.

📷 Instagram
