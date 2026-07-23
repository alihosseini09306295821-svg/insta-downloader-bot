from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from downloaders.manager import download

try:
    from config import BOT_TOKEN
except ImportError:
    BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\n"
        "لینک اینستاگرام (ریل، پست، استوری، کاروسل) رو بفرست تا دانلود کنم."
    )

async def download_instagram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()
    
    if "instagram.com" not in url:
        await update.message.reply_text("❌ لطفا یک لینک معتبر اینستاگرام ارسال کنید.")
        return

    status_msg = await update.message.reply_text("⏳ در حال دانلود...")

    try:
        filename = await download(url)
        
        with open(filename, "rb") as f:
            if filename.lower().endswith(('.mp4', '.mov', '.gif')):
                await update.message.reply_video(
                    f, 
                    caption="✅ دانلود شد توسط بات",
                    supports_streaming=True
                )
            else:
                await update.message.reply_photo(f, caption="✅ دانلود شد")
        
        # پاکسازی
        if os.path.exists(filename):
            os.remove(filename)
            
    except Exception as e:
        error_msg = str(e)
        if "instagram" in error_msg.lower() or "private" in error_msg.lower():
            await status_msg.edit_text("❌ این محتوا خصوصی است یا قابل دانلود نیست.")
        else:
            await status_msg.edit_text(f"❌ خطا: {error_msg[:150]}")

def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN environment variable is not set")
    
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & \~filters.COMMAND, download_instagram))

    print("🚀 ربات اینستاگرام با موفقیت شروع شد...")
    app.run_polling()

if __name__ == "__main__":
    main()
