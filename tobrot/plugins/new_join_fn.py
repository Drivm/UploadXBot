import logging

import pyrogram
from tobrot import *

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(
            f"""Hey! This is a private bot. Contact @Auth_r to get access.\n\n<b>Current CHAT ID: <code>{message.chat.id}</code>""",
            parse_mode="html",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('Channel', url='https://t.me/ivbotx')
                    ]
                ]
               )
            )
        # leave chat
        await client.leave_chat(chat_id=message.chat.id, delete=True)
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):

    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Open Help", callback_data = "openHelp_pg1")
            ]
        ]
    )
    await message.reply_text(
        text = f"""𝗛𝗘𝗟𝗣 𝗠𝗢𝗗𝗨𝗟𝗘

Click below to open Command Usage""",
        reply_markup = reply_markup,
        parse_mode = "html",
        disable_web_page_preview=True
    )

