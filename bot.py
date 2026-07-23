import os

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

from handlers.start import start, check_join_callback
from handlers.join import is_joined, join_markup
from downloaders.manager import download

from database.users import init_db, add_user

from admin.panel import panel, admin_callback
from admin.broadcast import broadcast, handle_broadcast

TOKEN = os.getenv("BOT_TOKEN")


async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message:
        return

    # اگر ادمین در حالت پیام همگانی باشد
    if await handle_broadcast(update, context):
        return

    user = update.effective_user

    add_user(
        user.id,
        user.username,
        user.first_name,
    )

    if not await is_joined(context.bot, user.id):
        await update.message.reply_text(
            "🔒 ابتدا عضو کانال شوید.",
            reply_markup=join_markup(),
        )
        return

    url = update.message.text.strip()

    await update.message.reply_text("⏳ در حال دانلود...")

    try:
        file_path = await download(url)

        if file_path.lower().endswith(
            (".mp4", ".mov", ".mkv", ".webm")
        ):
            with open(file_path, "rb") as video:
                await update.message.reply_video(video)
        else:
            with open(file_path, "rb") as file:
                await update.message.reply_document(file)

        if os.path.exists(file_path):
            os.remove(file_path)

    except Exception as e:
        await update.message.reply_text(f"❌ {e}")


def main():

    init_db()

    app = (
        Application.builder()
        .token(TOKEN)
        .build()
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("panel", panel))
    app.add_handler(CommandHandler("broadcast", broadcast))

    app.add_handler(
        CallbackQueryHandler(
            check_join_callback,
            pattern="^joined$",
        )
    )

    app.add_handler(CallbackQueryHandler(admin_callback))

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_link,
        )
    )

    print("Bot Started...")

    app.run_polling()


if __name__ == "__main__":
    main()
