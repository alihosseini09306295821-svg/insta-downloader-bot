from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ChatMemberHandler
from telegram.constants import ChatMemberStatus
import yt_dlp
import os
from datetime import datetime

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@HmHermi"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌟 سلام دوست عزیز! 👋\n"
        "برای استفاده از ربات، ابتدا در کانال ما عضو شوید: @HmHermi\n"
        "پس از عضویت، لینک اینستاگرام خود را ارسال کنید ✨"
    )

async def check_membership(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """Check if user is member of the required channel"""
    try:
        user_id = update.effective_user.id
        member = await context.bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]
    except Exception:
        return False

async def download_instagram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text

    # عضویت اجباری
    if not await check_membership(update, context):
        await update.message.reply_text(
            "🌟 برای دانلود محتوا، ابتدا باید در کانال @HmHermi عضو شوید!\n"
            "بعد از عضویت دوباره لینک رو بفرست ✨"
        )
        return

    if "instagram.com" not in url:
        await update.message.reply_text("🌟 لطفا یک لینک معتبر اینستاگرام ارسال کنید.")
        return

    await update.message.reply_text("⏳ در حال دانلود ویدیو... صبور باش دوست من ✨")

    try:
        ydl_opts = {
            "outtmpl": "downloaded.%(ext)s",
            "quiet": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        download_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "rb") as f:
            await update.message.reply_video(
                f,
                caption=f"✅ دانلود با موفقیت انجام شد! 🎥\n"
                        f"📅 تاریخ دانلود: {download_date}\n"
                        f"🌟 لذت ببرید! عضو کانال @HmHermi باشید"
            )

        os.remove(filename)

    except Exception as e:
        await update.message.reply_text(f"❌ خطا در دانلود: {str(e)}")

async def handle_chat_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """تشخیص عضویت جدید در کانال (با مدیریت کامل خطا)"""
    try:
        if hasattr(update, 'chat_member') and update.chat_member and update.chat_member.new_chat_member:
            new_status = update.chat_member.new_chat_member.status
            if new_status in [ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                user = update.chat_member.new_chat_member.user
                await context.bot.send_message(
                    chat_id=user.id,
                    text="🎉 تبریک می‌گم! حالا عضو کانال @HmHermi هستی.\n"
                         "لینک اینستاگرام مورد نظرت رو بفرست تا برات دانلود کنم ✨"
                )
    except Exception:
        pass  # جلوگیری از هرگونه کرش

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app