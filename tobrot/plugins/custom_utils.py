
import string
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# https://stackoverflow.com/questions/62173294/how-can-i-keep-save-the-user-input-in-dictionary

PRE_DICT = {}
CAP_DICT = {}
IMDB_TEMPLATE = {}

async def prefix_set(client, message):
    '''  /setprefix command '''
    lm = await message.reply_text(
        text="Setting up...",
    )
    user_id_ = message.from_user.id 
    u_men = message.from_user.mention
    pre_send = message.text.split(" ", maxsplit=1)
    reply_to = message.reply_to_message
    if len(pre_send) > 1:
        txt = pre_send[1]
    elif reply_to is not None:
        txt = reply_to.text
    else:
        txt = ""
    prefix_ = txt
    PRE_DICT[user_id_] = prefix_

    pre_text = await lm.edit_text(f"<b>Custom filename prefix saved:</b> <spoiler><code>{txt}</code></spoiler>", parse_mode="html")
    

async def caption_set(client, message):
    '''  /setcaption command '''

    lk = await message.reply_text(
        text="Setting up...",
    )
    user_id_ = message.from_user.id 
    u_men = message.from_user.mention
    cap_send = message.text.split(" ", maxsplit=1)
    reply_to = message.reply_to_message
    if len(cap_send) > 1:
        txt = cap_send[1]
    elif reply_to is not None:
        txt = reply_to.text
    else:
        txt = ""
    caption_ = txt
    CAP_DICT[user_id_] = caption_
    try:
        txx = txt.split("#", maxsplit=1)
        txt = txx[0]
    except:
        pass 
    cap_text = await lk.edit_text(f" <b>Custom caption saved:<b/> <tg-spoiler><code>{txt}</code></tg-spoiler>", parse_mode="html")


async def template_set(client, message):
    '''  /settemplate command '''
    lm = await message.reply_text(
        text="Checking input...",
    )
    user_id_ = message.from_user.id 
    u_men = message.from_user.mention
    tem_send = message.text.split(" ", maxsplit=1)
    reply_to = message.reply_to_message
    if len(tem_send) > 1:
        txt = tem_send[1]
    elif reply_to is not None:
        txt = reply_to.text
    else:
        txt = ""
    if txt == "":
        await lm.edit_text("Send custom template")
        return
    else:
        template_ = txt
        IMDB_TEMPLATE[user_id_] = template_
    
        await lm.edit_text(f" <b>Custom IMDb Template saved:</b> <code>{txt}</code>", parse_mode="html")


    '''

    await message.reply_text(
        text="Send me new filename prefix",
        #reply_to_message_id=message.reply_to_message.message_id,
        parse_mode="markdown",
    )
    try:
        ask_: Message = await bot.listen(message.from_user.id)
        if ask_.text and (ask_.text.startswith("/") is False):
            await ask_.delete(True)
            user_id_ = message.from_user.id
            prefix_ = ask_.text
            #await SetupPrefix(ask_.text, user_id=cb.from_user.id, editable=cb.message)
            set_pre[user_id_] = prefix_
            save_dict(set_pre)
            ascii_ = ''.join([i if (i in string.digits or i in string.ascii_letters or i == " ") else "" for i in text])
            #await db.set_prefix(user_id, prefix=text)
            await message.reply_text(
                text=f"<b>Filename prefix saved:</b> `{ascii_}`",
            )

        elif ask_.text and (ask_.text.startswith("/") is True):
            await message.reply_text(
                text="Current process cancelled",
                #reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("◀️ Back", callback_data="openSettings")]])
            )
    except TimeoutError:
        await message.send_message(
            message.reply_to_message.from_user.id,
            text="Sorry, 5 Minutes Passed! Send me Text Again to Set.",
        )
            #reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("◀️ Back", callback_data="openSettings")]])
     '''
