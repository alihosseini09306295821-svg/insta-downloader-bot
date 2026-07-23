from telegram import Update
from telegram.ext import ContextTypes

from config import ADMIN_ID
from database.users import get_all_users

broadcast_mode = {}


async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ شما ادمین نیستید.")
        return

    broadcast_mode[update.effective_user.id] = True

    await update.message.reply_text(
        "📢 پیام همگانی فعال شد.\n\n"
        "پیام موردنظر را ارسال کنید."
    )


async def handle_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    if user_id != ADMIN_ID:
        return False

    if not broadcast_mode.get(user_id):
        return False

    users = get_all_users()

    success = 0
    failed = 0

    for uid in users:
        try:
            await context.bot.copy_message(
                chat_id=uid,
                from_chat_id=update.effective_chat.id,
                message_id=update.message.message_id,
            )
            success += 1
        except:
            failed += 1

    broadcast_mode[user_id] = False

    await update.message.reply_text(
        f"✅ پیام همگانی انجام شد.\n\n"
        f"✔ موفق: {success}\n"
        f"❌ ناموفق: {failed}"
    )

    return True
