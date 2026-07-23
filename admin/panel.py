from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import ContextTypes

from config import ADMIN_ID


async def panel(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ شما ادمین نیستید.")
        return

    keyboard = [
        [
            InlineKeyboardButton(
                "📊 آمار کاربران",
                callback_data="admin_stats",
            )
        ],
        [
            InlineKeyboardButton(
                "📢 پیام همگانی",
                callback_data="admin_broadcast",
            )
        ],
        [
            InlineKeyboardButton(
                "👥 مدیریت کاربران",
                callback_data="admin_users",
            )
        ],
        [
            InlineKeyboardButton(
                "📋 لاگ‌ها",
                callback_data="admin_logs",
            )
        ],
        [
            InlineKeyboardButton(
                "⚙️ تنظیمات",
                callback_data="admin_settings",
            )
        ],
    ]

    await update.message.reply_text(
        "👑 پنل مدیریت",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )
