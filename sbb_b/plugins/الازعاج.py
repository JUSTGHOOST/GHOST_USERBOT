from sbb_b import sbb_b

from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.echo_sql import addecho, is_echo, remove_echo
from . import get_user_from_event


@sbb_b.ar_cmd(pattern="ازعاج$")
async def echo(event):
    if event.reply_to_msg_id is None:
        return await edit_or_reply(event, "يرجى الرد على الشخص الذي تريد ازعاجه .")
    sbb_bevent = await edit_or_reply(event, "يتم تفعيل هذا الامر انتظر قليلا .")
    user, rank = await get_user_from_event(event, sbb_bevent, nogroup=True)
    if not user:
        return
    reply_msg = await event.get_reply_message()
    chat_id = event.chat_id
    user_id = reply_msg.sender_id
    if event.is_private:
        chat_name = user.first_name
        chat_type = "Personal"
    else:
        chat_name = event.chat.title
        chat_type = "Group"
    user_name = user.first_name
    user_username = user.username
    if is_echo(chat_id, user_id):
        return await edit_or_reply(event, "تم تفعيل وضع الازعاج على الشخص بنجاح ✓")
    try:
        addecho(chat_id, user_id, chat_name, user_name, user_username, chat_type)
    except Exception as e:
        await edit_delete(sbb_bevent, f"خطأ\n`{str(e)}`")
    else:
        await edit_or_reply(
            sbb_bevent,
            "تم تفعيل امر الازعاج على هذا الشخص\nسيتم تقليد جميع رسائله هنا",
        )


@sbb_b.ar_cmd(pattern="الغاء الازعاج$")
async def echo(event):
    if event.reply_to_msg_id is None:
        return await edit_or_reply(event, "يجب عليك الرد على المستخدم لتقليد رسائله")
    reply_msg = await event.get_reply_message()
    user_id = reply_msg.sender_id
    chat_id = event.chat_id
    if is_echo(chat_id, user_id):
        try:
            remove_echo(chat_id, user_id)
        except Exception as e:
            await edit_delete(sbb_bevent, f"خطأ: \n`{e}`")
        else:
            await edit_or_reply(event, "تم ايقاف الازعاج لهذا المستخدم")
    else:
        await edit_or_reply(event, "لم يتم تفعيل الازعاج على هذا المستخدم اصلا")


@sbb_b.ar_cmd(incoming=True, edited=False)
async def samereply(event):
    if is_echo(event.chat_id, event.sender_id) and (
        event.message.text or event.message.sticker
    ):
        await event.reply(event.message)
