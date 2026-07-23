from telegram import InlineKeyboardButton, InlineKeyboardMarkup

CHANNEL_USERNAME = "@HmHermi"


async def check_join(bot, user_id):
    try:
        member = await bot.get_chat_member(CHANNEL_USERNAME, user_id)

        if member.status in ["member", "administrator", "creator"]:
            return True

    except:
        pass

    return False


def join_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "📢 عضویت در کانال",
                url="https://t.me/HmHermi"
            )
        ],
        [
            InlineKeyboardButton(
                "✅ عضو شدم",
                callback_data="check_join"
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)
