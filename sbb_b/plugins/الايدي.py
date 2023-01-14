from telethon.utils import pack_bot_file_id

from sbb_b import sbb_b
from sbb_b.core.logger import logging

from ..core.managers import edit_delete, edit_or_reply

LOGS = logging.getLogger(__name__)


@sbb_b.ar_cmd(pattern="(الايدي|id)(?: |$)(.*)")
async def _(event):
    input_str = event.pattern_match.group(2)
    if input_str:
        try:
            p = await event.client.get_entity(input_str)
        except Exception as e:
            return await edit_delete(event, f"`{str(e)}`", 5)
        try:
            if p.first_name:
                return await edit_or_reply(
                    event, f"آيـدي المُستخدم  : `{input_str}` هـو `{p.id}`"
                )
        except Exception:
            try:
                if p.title:
                    return await edit_or_reply(
                        event, f"آيـدي الدردشــــة  : `{p.title}` هـو `{p.id}` "
                    )
            except Exception as e:
                LOGS.info(str(e))
        await edit_or_reply(event, "قُم بإدخال أسم مُستخدم أو الرد على المُستخدم ")
    elif event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await edit_or_reply(
                event,
                f"ايـدي الدردشــــة   : `{str(event.chat_id)}` .\nايـدي المُستخدم   : `{str(r_msg.sender_id)}` .\n  آيـدي الميديـا  : `{bot_api_file_id}`",
            )
        else:
            await edit_or_reply(
                event,
                f"ايـدي الدردشــــة   : `{str(event.chat_id)}` .\nايـدي المُستخدم   : `{str(r_msg.sender_id)}` .",
            )
