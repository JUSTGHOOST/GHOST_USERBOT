from sbb_b import sbb_b

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _jmthonutils, parse_pre, yaml_format

plugin_category = "tools"

@sbb_b.ar_cmd(
    pattern="امته$",
    command=("امته", plugin_category),
    info={
        "header": "To get date and time of message when it posted.",
        "usage": "{tr}when <reply>",
    },
)
async def _(event):
    "To get date and time of message when it posted."
    reply = await event.get_reply_message()
    if reply:
        try:
            result = reply.fwd_from.date
        except Exception:
            result = reply.date
    else:
        result = event.date
    await edit_or_reply(
        event, f"نـشـرت هـذه الـرسالة فـي  : `{yaml_format(result)}`"
    )
