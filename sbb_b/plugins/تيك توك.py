from telethon import events

from sbb_b import sbb_b

from ..core.managers import edit_or_reply


@sbb_b.ar_cmd(pattern="تيك توك(?: |$)(.*)")
async def _(sbb_b):
    reply_message = await sbb_b.get_reply_message()
    if not reply_message:
        await edit_or_reply(sbb_b, "**♛ ⦙  الرد على الرابط.**")
        return
    if not reply_message.text:
        await edit_or_reply(sbb_b, "**♛ ⦙  الرد على الرابط.**")
        return
    chat = "@fs0bot"
    iqevent = await edit_or_reply(sbb_b, "جاري تحميل الرابط ...")
    async with sbb_b.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1354606430)
            )
            await sbb_b.client.forward_messages(chat, reply_message)
            response = await response
            await sbb_b.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await iqevent.edit("**♛ ⦙  فك الحظر من البوت : @fs0bot**")
            return
        if response.text.startswith("؟"):
            await iqevent.edit("?")
        else:
            await iqevent.delete()
            await sbb_b.client.send_message(sbb_b.chat_id, response.message)
