# UTF-8
# Copyright (c) 5MysterySD 2022

import re
import datetime 

from tobrot import LOGGER
from tobrot.helper_funcs.display_progress import humanbytes, TimeFormatter
from tobrot.plugins import is_appdrive_link, is_gdtot_link, is_hubdrive_link 
from tobrot.helper_funcs.direct_link_generator import url_link_generate, gdtot, appdrive_dl, hubdrive 
from tobrot.helper_funcs.exceptions import DirectDownloadLinkException

drive_list = ['driveapp.in', 'gdflix.pro', 'drivelinks.in', 'drivesharer.in', 'driveflix.in', 'drivebit.in', 'drivehub.in', 'driveace.in']

async def url_parser(client, message):
   
    op = await message.reply_text(
        text="`Fetching Data . . .`",
        quote=True,
    )
    user_id = message.from_user.id 
    u_men = message.from_user.mention
    url_parse = message.text.split(" ", maxsplit=1)
    reply_to = message.reply_to_message
    if len(url_parse) > 1:
        url = url_parse[1]
    elif reply_to is not None:
        url = reply_to.text
    else:
        url = None
    if url is not None:
        oo = await op.edit_text(
            text=f"**URL Parsing Initiated**\n\n **Link**: `{url}`\n\nFetching Data....",
            disable_web_page_preview=True,
        )
        try:
            trigger, bypassed_url = await bypass_link(url)
        except Exception as e:
            not_ok = await op.edit_text(
                text=f"**URL Parsing Error**\n\n`{e}` ",
                disable_web_page_preview=True,
            )
            return 
        if trigger is True:
            ok = await oo.edit_text(
                text="**Url Parsing Stopped**\n\n Check your link first, if i can parse it or not !!",
                disable_web_page_preview=True,
            )
            return 
        else:
            tell = await oo.edit_text(
                 text=f"**URL Parsed**\n\n**Link** : `{url}`\n\n**Bypassed**: `{bypassed_url}`\n",
                 disable_web_page_preview=True,
            )
    else:
        oo = await op.edit_text(
            text="**Send Link Along with Command :**\n/parser(BotName) `{link}`\n\n **Reply to a Link :**\n/parser(BotName) to Link \n\n**SUPPORTED SITES**\n__Coming Soon__",
        )
        return


async def bypass_link(text_url: str):
    
    if "zippyshare.com" in text_url \
        or "osdn.net" in text_url \
        or "mediafire.com" in text_url \
        or "https://uptobox.com" in text_url \
        or "cloud.mail.ru" in text_url \
        or "github.com" in text_url \
        or "yadi.sk" in text_url  \
        or "hxfile.co" in text_url  \
        or "https://anonfiles.com" in text_url  \
        or "letsupload.io" in text_url  \
        or "fembed.net" in text_url  \
        or "fembed.com" in text_url  \
        or "femax20.com" in text_url  \
        or "fcdn.stream" in text_url  \
        or "feurl.com" in text_url  \
        or "naniplay.nanime.in" in text_url  \
        or "naniplay.nanime.biz" in text_url  \
        or "naniplay.com" in text_url  \
        or "layarkacaxxi.icu" in text_url  \
        or "sbembed.com" in text_url  \
        or "streamsb.net" in text_url  \
        or "sbplay.org" in text_url  \
        or "1drv.ms" in text_url  \
        or "pixeldrain.com" in text_url  \
        or "antfiles.com" in text_url  \
        or "streamtape.com" in text_url  \
        or "https://bayfiles.com" in text_url  \
        or "1fichier.com" in text_url  \
        or "solidfiles.com" in text_url  \
        or "krakenfiles.com" in text_url  \
        or "gplinks.co" in text_url  \
        or "katdrive.net" in text_url  \
        or "drivefire.co" in text_url  \
        or "drivebuzz.icu" in text_url  \
        or "gadrive.vip" in text_url  \
        or "linkvertise.com" in text_url  \
        or "droplink.co" in text_url  \
        or "gofile.io" in text_url  \
        or "ouo.io" in text_url  \
        or "ouo.press" in text_url  \
        or "upindia.mobi" in text_url  \
        or "uploadfile.cc" in text_url  \
        or "adf.ly" in text_url  \
        or "https://sourceforge.net" in text_url  \
        or "https://master.dl.sourceforge.net" in text_url  \
        or "androiddatahost.com" in text_url  \
        or "androidfilehost.com" in text_url  \
        or "sfile.mobi" in text_url  \
        or "wetransfer.com" in text_url  \
        or "we.tl" in text_url  \
        or "corneey.com" in text_url \
        or "sh.st" in text_url \
        or "racaty.net" in text_url:
            try:
                url_string = url_link_generate(text_url)
                return False, url_string
            except DirectDownloadLinkException as e:
                LOGGER.info(f'{text_url}: {e}')
    elif is_hubdrive_link(text_url):
        try:
            info_parsed = hubdrive(text_url)
            url_string = f"**Name** : `{info_parsed['title']}`\n **File size** : `{info_parsed['File Size']}`\n**File Owner** : `{info_parsed['File Owner']}`\n**Error Type** : `{info_parsed['error']}`\n **GDrive URL** : `{info_parsed['gdrive_url']}`"
            return False, url_string
        except DirectDownloadLinkException as e:
            LOGGER.info(f'{text_url}: {e}')
    elif is_gdtot_link(text_url):
        try:
            info_parsed = gdtot(text_url)
            url_string = f"**Name** : `{info_parsed['title']}` \n**File Size** : `{info_parsed['size']}` \n**Date** : `{info_parsed['date']}` \n**GDrive URL** : `{info_parsed['gdrive_link']}`"
            return False, url_string
        except DirectDownloadLinkException as e:
            LOGGER.info(f'{text_url}: {e}')
    elif is_appdrive_link(text_url) or any(x in text_url for x in drive_list):
        try:
            is_direct = False
            info_parsed = appdrive_dl(text_url, is_direct)
            if info_parsed['error'] == True:
                url_string = f"**Parsing Error**: \n `{info_parsed['error_message']}`"
            else:
                url_string = f"**Name** : `{info_parsed['name']}`\n**Format** : `{info_parsed['format']}`\n**File Size** : `{info_parsed['size']}`\n **Link Type** : `{info_parsed['link_type']}`\n**GDrive URL** : `{info_parsed['gdrive_link']}`"
            return False, url_string
        except Exception as e:
            url_string = f" **Internal Error**: \n `{e}`"
            return False, url_string 
        except DirectDownloadLinkException as er:
            LOGGER.info(f'{text_url}: {er}')
            return False, er
    elif "kolop.icu" in text_url:
        try:
            info_parsed = url_link_generate(text_url)
            if info_parsed['error'] == True:
                url_string = f"**Parsing Error**: \n `{info_parsed['error_message']}`"
            else:
                url_string = f"**Name** : `{info_parsed['title']}`\n**File Size** : `{info_parsed['File Size']}`\n**Mime Type** : `{info_parsed['File Type']}`\n**File Owner** : `{info_parsed['File Owner']}`\n**GDrive URL** : `{info_parsed['gdrive_url']}`"
            return False, url_string
        except Exception as e:
            url_string = f"**Internal Error**: \n `{e}`"
            return False, url_string 
        except DirectDownloadLinkException as er:
            LOGGER.info(f'{text_url}: {er}')
            return False, er
    elif "mdisk.me" in text_url:
        try:
            info_parsed = url_link_generate(text_url)
            men_user = 'tg://user?id={info_parsed["from"]}'
            url_string = f"**Name** : `{info_parsed['filename']}` \n**File Size** : `{humanbytes(info_parsed['size'])}` \n**Duration** : `{TimeFormatter(info_parsed['duration']*1000)}` \n💾 **Resolution** : `{info_parsed['width']} × {info_parsed['height']}` \n**Uploaded On** : `{datetime.datetime.utcfromtimestamp(info_parsed['ts']/1000).strftime('%I:%M:%S %p %d %B, %Y')}` \n**File Uploader** : <a href='{men_user}'>{info_parsed['display_name']}</a> ( `{info_parsed['from']}` ) \n**Download URL** : `{info_parsed['download']}`"
            return False, url_string
        except DirectDownloadLinkException as er:
            LOGGER.info(f'{text_url}: {er}')
    else:
        return True, None

