import asyncio
import base64
import os
import time
from subprocess import PIPE
from subprocess import run as runapp

from sbb_b import sbb_b

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import progress
from ..helpers.tools import media_type

menu_category = "tools"

@sbb_b.ar_cmd(
    pattern="base(?: |$)([\s\S]*)",
    command=("base", menu_category),
    info={
        "header": "Find the base64 encoding or decoding of the given string.",
        "flags": {
            "-e": "Use this to encode the given text.",
            "-d": "use this to decode the given text.",
        },
        "usage": ["{tr}base -e <text to encode>", "{tr}base -d <encoded text>"],
        "examples": ["{tr}base -d TGVnZW5kVXNlckJvdA==", "{tr}base -e LegendUserBot"],
    },
)
async def endecrypt(event):
    "To encode or decode the string using base64"
    reply_msg = await event.get_reply_message()
    mediatype = media_type(reply_msg)
    type = event.text[6:9]
    if reply_msg:
        tol = reply_msg.text
    else:
        tol = event.text[9:]
    if tol == "":
        return await edit_delete(event, "استخدم الامر بطريقه صحيحه !\nencode : `.base -e`\ndecode : `.base -d`")
    if "-e" in type:
        if tol:
            try:
                result = base64.b64encode(bytes(tol, "utf-8")).decode("utf-8")
                results = f"**Encoded : **\n\n`{result}`"
                return await edit_or_reply(event, results)
            except Exception as e:
                return await edit_or_reply(event, e)
        elif mediatype is None:
            result = base64.b64encode(bytes(f"{reply_msg.message}", "utf-8")).decode(
                "utf-8"
            )
            results = f"**Encoded : **\n\n`{result}`"
        else:
            legendevent = await edit_or_reply(event, "`Encoding ...`")
            c_time = time.time()
            downloaded_file_name = await event.client.download_media(
                reply_msg,
                Config.TMP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, legendevent, c_time, "trying to download")
                ),
            )
            legendevent = await edit_or_reply(event, "`Encoding ...`")
            with open(downloaded_file_name, "rb") as image_file:
                results = base64.b64encode(image_file.read()).decode("utf-8")
            os.remove(downloaded_file_name)
        await edit_or_reply(event, results, file_name="encodedfile.txt", caption="It's Encoded")
        return
    elif "-d" in type:
        try:
            lething = str(base64.b64decode(bytes(tol, "utf-8"), validate=True))[2:]
            await edit_or_reply(event, "**Decoded  :**\n\n`" + lething[:-1] + "`")
        except Exception as e:
            await edit_delete(event, f"**Error:**\n__{e}__")
    else:
        await edit_delete(event, "give me flags")
