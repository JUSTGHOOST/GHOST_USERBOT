import random
import re
import time
from datetime import datetime
from platform import python_version

import requests
from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from sbb_b import StartTime, sbb_b, jmthonversion

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import jmthonalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_category = "utils"

normzltext = "0123456789"
namerzfont = Config.TI_IT or "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗"

@sbb_b.ar_cmd(
    pattern="فحص$",
    command=("alive", plugin_category),
    info={
        "header": "To check bot's alive status",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    ANIME = None
    cat_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    if "ANIME" in cat_caption:
        data = requests.get("https://animechan.vercel.app/api/random").json()
        ANIME = f"**“{data['quote']}” - {data['character']} ({data['anime']})**"
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    catevent = await edit_or_reply(event, "`Checking...`")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or ""
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or ""
    CAT_IMG = gvarstatus("ALIVE_PIC")
    tg_bot = Config.TG_BOT_USERNAME
    TM = time.strftime("%I:%M")
    for normal in TM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                TM = TM.replace(normal, namefont)
    caption = cat_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        ANIME=ANIME,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        catver=jmthonversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
        TM=TM,
        tg_bot=tg_bot,
    )
    if CAT_IMG:
        CAT = list(CAT_IMG.split())
        PIC = random.choice(CAT)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await catevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                catevent,
                f"**Media Value Error!!**\n__Change the link by __`.setdv`\n\n**__Can't get media from this link :-**__ `{PIC}`",
            )
    else:
        await edit_or_reply(
            catevent,
            caption,
        )


temp = """{ALIVE_TEXT}
{EMOJI}  𝐌𝐄 : {mention}
{EMOJI} 𝐓𝐈𝐌𝐄 : {TM}
{EMOJI} 𝐌𝐘 𝐁𝐎𝐓 : {tg_bot}
{EMOJI} 𝐃𝐕 : @IT_DS."""


def jmthonalive_text():
    EMOJI = gvarstatus("ALIVE_EMOJI") or ""
    cat_caption = "**Catuserbot is Up and Running**\n"
    cat_caption += f"**{EMOJI} Telethon version :** `{version.__version__}\n`"
    cat_caption += f"**{EMOJI} Catuserbot Version :** `{jmthonversion}`\n"
    cat_caption += f"**{EMOJI} Python Version :** `{python_version()}\n`"
    cat_caption += f"**{EMOJI} Master:** {mention}\n"
    return cat_caption
