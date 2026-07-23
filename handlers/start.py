from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import ContextTypes

from database.users import add_user
from handlers.join import is_joined, join_markup


def main_menu():
    keyboard = [
        [InlineKeyboardButton("📥 دانلود", callback_data="download")],
        [
            InlineKeyboardButton("📢 کانال", url="https://t.me/HmHermi"),
            InlineKeyboardButton("👨‍💻 پشتیبانی", url="https://t.me/HmHermi"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


WELCOME = (
    "🚀 **Universal Downloader Bot**\n\n"
    "سلام 👋\n\n"
    "به ربات دانلود حرفه‌ای خوش آمدید.\n\n"
    "📷 Instagram\n"
    "🎵 TikTok\n"
    "▶️ YouTube\n"
    "📘 Facebook\n"
    "🐦 X (Twitter)\n\n"
    "━━━━━━━━━━━━━━\n"
    "فقط لینک را ارسال کنید.\n"
    "━━━━━━━━━━━━━━\n\n"
    "👑 Developer: @HmHermi"
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    add_user(user.id, user.username, user.first_name)

    if not await is_joined(context.bot, user.id):
        await update.message.reply_text(
            "🔒 برای استفاده از ربات ابتدا عضو کانال شوید.",
            reply_markup=join_markup(),
        )
        return

    await update.message.reply_text(
        WELCOME,
        reply_markup=main_menu(),
        parse_mode="Markdown",
    )


async def check_join_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if await is_joined(context.bot, query.from_user.id):
        await query.message.edit_text(
            WELCOME,
            reply_markup=main_menu(),
            parse_mode="Markdown",
        )
    else:
        await query.answer(
            "❌ هنوز عضو کانال نشده‌اید.",
            show_alert=True,
        )
