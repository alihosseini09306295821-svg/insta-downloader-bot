from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import ContextTypes

from database.users import add_user
from handlers.join import check_join, join_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    add_user(
        user.id,
        user.username,
        user.first_name,
    )

    joined = await check_join(
        context.bot,
        user.id,
    )

    if not joined:
        await update.message.reply_text(
            "🔒 برای استفاده از ربات ابتدا باید عضو کانال شوید.",
            reply_markup=join_keyboard(),
        )
        return

    keyboard = [
        [
            InlineKeyboardButton(
                "📥 دانلود رسانه",
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

    await update.message.reply_text(
        """
╔════════════════════╗
🚀 Universal Media Downloader
╚════════════════════╝

سلام 👋

به ربات دانلود حرفه‌ای خوش آمدید.

📷 Instagram
🎵 TikTok
▶️ YouTube
📘 Facebook
🐦 X (Twitter)

فقط لینک را ارسال کنید.

━━━━━━━━━━━━━━━
👑 Developer
@HmHermi
        """,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )
