from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from handlers.start import start
from downloaders.manager import download

from database.users import init_db

import os

TOKEN = os.getenv("BOT_TOKEN")


async def handle_link(update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text

    await update.message.reply_text("⏳ در حال دانلود...")

    try:
        file_path = await download(url)

        with open(file_path, "rb") as f:
            await update.message.reply_document(f)

    except Exception as e:
        await update.message.reply_text(f"❌ خطا:\n{e}")


def main():
    init_db()

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link)
    )

    print("Bot Started...")

    app.run_polling()


if __name__ == "__main__":
    main()
