from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import ContextTypes

from config import ADMIN_ID
from database.users import total_users


async def panel(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ شما ادمین نیستید.")
        return

    keyboard = [
        [InlineKeyboardButton("📊 آمار کاربران", callback_data="admin_stats")],
        [InlineKeyboardButton("📢 پیام همگانی", callback_data="admin_broadcast")],
        [InlineKeyboardButton("👥 مدیریت کاربران", callback_data="admin_users")],
        [InlineKeyboardButton("📋 لاگ‌ها", callback_data="admin_logs")],
        [InlineKeyboardButton("⚙️ تنظیمات", callback_data="admin_settings")],
    ]

    await update.message.reply_text(
        "👑 پنل مدیریت",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def admin_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.from_user.id != ADMIN_ID:
        return

    if query.data == "admin_stats":

        count = get_users_count()

        await query.message.reply_text(
            f"📊 آمار ربات\n\n👤 تعداد کاربران: {count}"
        )

    elif query.data == "admin_broadcast":

        await query.message.reply_text(
            "🚧 این بخش در مرحله بعد تکمیل می‌شود."
        )

    elif query.data == "admin_users":

        await query.message.reply_text(
            "🚧 این بخش در مرحله بعد تکمیل می‌شود."
        )

    elif query.data == "admin_logs":

        await query.message.reply_text(
            "🚧 این بخش در مرحله بعد تکمیل می‌شود."
        )

    elif query.data == "admin_settings":

        await query.message.reply_text(
            "🚧 این بخش در مرحله بعد تکمیل می‌شود."
        )
