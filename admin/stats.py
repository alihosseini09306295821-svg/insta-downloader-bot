from telegram import Update
from telegram.ext import ContextTypes
from config import ADMIN_ID
import sqlite3


async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:
        return

    conn = sqlite3.connect("database/users.db")
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM users")
    users = cur.fetchone()[0]

    conn.close()

    await update.message.reply_text(
        f"""📊 آمار ربات

👤 تعداد کاربران: {users}
"""
    )
