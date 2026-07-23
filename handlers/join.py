from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ChatMemberStatus

CHANNEL = "@HmHermi"


async def is_joined(bot, user_id):
    try:
        member = await bot.get_chat_member(CHANNEL, user_id)

        return member.status in [
            ChatMemberStatus.MEMBER,
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER,
        ]

    except Exception:
        return False


def join_markup():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📢 عضویت در کانال",
                    url="https://t.me/HmHermi",
                )
            ],
            [
                InlineKeyboardButton(
                    "✅ عضو شدم",
                    callback_data="joined",
                )
            ],
        ]
    )
