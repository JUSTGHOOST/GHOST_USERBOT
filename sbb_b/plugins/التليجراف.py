import os
from datetime import datetime

from PIL import Image
from telegraph import Telegraph, exceptions, upload_file
from urlextract import URLExtract

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_or_reply
from . import BOTLOG, BOTLOG_CHATID, sbb_b

LOGS = logging.getLogger(__name__)


extractor = URLExtract()
telegraph = Telegraph()
r = telegraph.create_account(short_name=Config.TELEGRAPH_SHORT_NAME)
auth_url = r["auth_url"]


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


@sbb_b.ar_cmd(pattern="(ت(ل)?يج(راف)?) ?(م|ميديا)(?:\s|$)([\s\S]*)")
async def _(event):
    sbb_bevent = await edit_or_reply(event, "جار انشاء رابط تليجراف ...")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"انشاء حساب تليجراف جديد {auth_url} لهذه الجلسة .",
        )
    event.pattern_match.group(5)
    if not event.reply_to_msg_id:
        return await sbb_bevent.edit(
            "قم بالرد على هذه الرسالة للحصول على رابط تليجراف فورا**",
        )

    start = datetime.now()
    r_message = await event.get_reply_message()
    input_str = (event.pattern_match.group(4)).strip()
    if input_str in ["ميديا", "م"]:
        downloaded_file_name = await event.client.download_media(
            r_message, Config.TEMP_DIR
        )
        await sbb_bevent.edit(f"تم التحميل الى {downloaded_file_name}**")
        if downloaded_file_name.endswith((".webp")):
            resize_image(downloaded_file_name)
        try:
            media_urls = upload_file(downloaded_file_name)
        except exceptions.TelegraphException as exc:
            await sbb_bevent.edit(f"** ⌔∮ خطأ : **\n**{exc}**")
            os.remove(downloaded_file_name)
        else:
            end = datetime.now()
            ms = (end - start).seconds
            os.remove(downloaded_file_name)
            await sbb_bevent.edit(
                f"الرابط : [إضغط هنا](https://telegra.ph{media_urls[0]})\
                    \nالوقت المأخوذ : {ms} ثانية .",
                link_preview=True,
            )
