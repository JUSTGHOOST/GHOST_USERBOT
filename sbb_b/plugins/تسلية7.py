import io
import os
import random
import textwrap

from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterDocument

from sbb_b import sbb_b

from ..core.managers import edit_or_reply
from ..helpers.functions import deEmojify, hide_inlinebot, waifutxt
from ..helpers.utils import reply_id

plugin_category = "fun"


async def get_font_file(client, channel_id, search_kw=""):
    font_file_message_s = await client.get_messages(
        entity=channel_id,
        filter=InputMessagesFilterDocument,
        limit=None,
        search=search_kw,
    )
    font_file_message = random.choice(font_file_message_s)
    return await client.download_media(font_file_message)


@sbb_b.ar_cmd(
    pattern="نص(?:\s|$)([\s\S]*)",
    command=("نص", plugin_category),
    info={
        "header": "Anime that makes your writing fun.",
        "usage": "{tr}sttxt <text>",
        "examples": "{tr}sttxt hello",
    },
)
async def waifu(animu):
    "⌔︙الأنمي الذي يجعل كتابتك ممتعة"
    text = animu.pattern_match.group(1)
    reply_to_id = await reply_id(animu)
    if not text:
        if animu.is_reply:
            text = (await animu.get_reply_message()).message
        else:
            return await edit_or_reply(
                animu, "` ⌔︙أنت لم تكتب أي نص ، الوايفو سوف تغادر.`"
            )
    text = deEmojify(text)
    await animu.delete()
    await waifutxt(text, animu.chat_id, reply_to_id, animu.client)


# 12 21 28 30
@sbb_b.ar_cmd(
    pattern="هونك(?:\s|$)([\s\S]*)",
    command=("هونك", plugin_category),
    info={
        "header": "Make honk say anything.",
        "usage": "{tr}honk <text/reply to msg>",
        "examples": "{tr}honk How you doing?",
    },
)
async def honk(event):
    "⌯︙اجعل هونك يقول اي شيء."
    text = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    bot_name = "@honka_says_bot"
    if not text:
        if event.is_reply:
            text = (await event.get_reply_message()).message
        else:
            return await edit_delete(event, "** ⌯︙ماذا يفترض أن يقول هونك أعطه نص**")
    text = deEmojify(text)
    await event.delete()
    await hide_inlinebot(event.client, bot_name, text, event.chat_id, reply_to_id)


@sbb_b.ar_cmd(
    pattern="تغريد(?:\s|$)([\s\S]*)",
    command=("تغريد", plugin_category),
    info={
        "header": "Make a cool tweet of your account",
        "usage": "{tr}twt <text/reply to msg>",
        "examples": "{tr}twt sbb_b",
    },
)
async def twt(event):
    "⌔︙قم بعمل تغريدة رائعة من حسابك."
    text = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    bot_name = "@TwitterStatusBot"
    if not text:
        if event.is_reply:
            text = (await event.get_reply_message()).message
        else:
            return await edit_delete(event, "**⌯︙ماذا يفترض بي ان اغرد اكتي نصا**")
    text = deEmojify(text)
    await event.delete()
    await hide_inlinebot(event.client, bot_name, text, event.chat_id, reply_to_id)


@sbb_b.ar_cmd(
    pattern="غلاكس(|ر)(?:\s|$)([\s\S]*)",
    command=("غلاكس", plugin_category),
    info={
        "header": "Make glax the dragon scream your text.",
        "flags": {
            "r": "Reverse the face of the dragon",
        },
        "usage": [
            "{tr}glax <text/reply to msg>",
            "{tr}glaxr <text/reply to msg>",
        ],
        "examples": [
            "{tr}glax Die you",
            "{tr}glaxr Die you",
        ],
    },
)  # WRITED BY - @VUUZZ - @RR7PP
async def glax(event):
    "⌔︙اجعل غلاكس التنين ينفخ نصك."
    cmd = event.pattern_match.group(1).lower()
    text = event.pattern_match.group(2)
    reply_to_id = await reply_id(event)
    bot_name = "@GlaxScremBot"
    c_lick = 1 if cmd == "ر" else 0
    if not text:
        if event.is_reply:
            text = (await event.get_reply_message()).message
        else:
            return await edit_delete(
                event, " ⌯︙ماذا يفترض بـ گلاكـس ان يقول اعطه نصا**"
            )  # WRITED BY - @VUUZZ - @RR7PP
    text = deEmojify(text)
    await event.delete()
    await hide_inlinebot(
        event.client, bot_name, text, event.chat_id, reply_to_id, c_lick=c_lick
    )
    # WRITED BY - @VUUZZ - @RR7PP
