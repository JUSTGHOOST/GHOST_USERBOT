from telethon import functions
from telethon.errors import ChatAdminRequiredError, UserAlreadyInvitedError
from telethon.tl.types import Channel, Chat, User
from sbb_b import sbb_b
from sbb_b.core.managers import edit_delete, edit_or_reply
from sbb_b.helpers.utils import mentionuser

plugin_category = "extra"


async def get_group_call(chat):
    if isinstance(chat, Channel):
        result = await sbb_b(functions.channels.GetFullChannelRequest(channel=chat))
    elif isinstance(chat, Chat):
        result = await sbb_b(functions.messages.GetFullChatRequest(chat_id=chat.id))
    return result.full_chat.call


async def chat_vc_checker(event, chat, edits=True):
    if isinstance(chat, User):
        await edit_delete(event, "الامر يستعمل فى المجموعات فقط .")
        return None
    result = await get_group_call(chat)
    if not result:
        if edits:
            await edit_delete(event, "لا يوجد مكالمة شغالة !")
        return None
    return result


async def parse_entity(entity):
    if entity.isnumeric():
        entity = int(entity)
    return await sbb_b.get_entity(entity)


@sbb_b.ar_cmd(
    pattern="بدء مكالمة",
    command=("vcstart", plugin_category),
    info={
        "header": "To end a stream on Voice Chat.",
        "description": "To end a stream on Voice Chat",
        "usage": "{tr}vcstart",
        "examples": "{tr}vcstart",
    },
)
async def start_vc(event):
    "To start a Voice Chat."
    vc_chat = await sbb_b.get_entity(event.chat_id)
    gc_call = await chat_vc_checker(event, vc_chat, False)
    if gc_call:
        return await edit_delete(event, "المكالمة شغاله من قبل !")
    try:
        await sbb_b(
            functions.phone.CreateGroupCallRequest(
                peer=vc_chat,
                title="ITALIA VC",
            )
        )
        await edit_delete(event, "تم بدء مكالمة ✓")
    except ChatAdminRequiredError:
        await edit_delete(event, "انته لست ادمن هنا !", time=20)


@sbb_b.ar_cmd(
    pattern="انهاء المكالمة",
    command=("vcend", plugin_category),
    info={
        "header": "To end a stream on Voice Chat.",
        "description": "To end a stream on Voice Chat",
        "usage": "{tr}vcend",
        "examples": "{tr}vcend",
    },
)
async def end_vc(event):
    "To end a Voice Chat."
    vc_chat = await sbb_b.get_entity(event.chat_id)
    gc_call = await chat_vc_checker(event, vc_chat)
    if not gc_call:
        return
    try:
        await sbb_b(functions.phone.DiscardGroupCallRequest(call=gc_call))
        await edit_delete(event, "تم انهاء المكالمة ✓")
    except ChatAdminRequiredError:
        await edit_delete(event, "انته لست ادمن هنا !", time=20)
