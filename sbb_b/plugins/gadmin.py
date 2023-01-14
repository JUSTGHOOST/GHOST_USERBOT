import asyncio
import contextlib
from datetime import datetime

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
from telethon.utils import get_display_name

from sbb_b import sbb_b

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _format
from ..sql_helper import gban_sql_helper as gban_sql
from ..sql_helper.mute_sql import is_muted, mute, unmute
from . import BOTLOG, BOTLOG_CHATID, admin_groups, get_user_from_event

plugin_category = "admin"

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)


@sbb_b.ar_cmd(
    pattern="ح عام(?:\s|$)([\s\S]*)",
    command=("ح عام", plugin_category),
    info={
        "header": "To ban user in every group where you are admin.",
        "description": "Will ban the person in every group where you are admin only.",
        "usage": "{tr}gban <username/reply/userid> <reason (optional)>",
    },
)
async def catgban(event):  # sourcery no-metrics
    "To ban user in every group where you are admin."
    cate = await edit_or_reply(event, "جارى الحظر .......")
    start = datetime.now()
    user, reason = await get_user_from_event(event, cate)
    if not user:
        return
    if user.id == sbb_b.uid:
        return await edit_delete(cate, "`why would I ban myself`")
    if gban_sql.is_gbanned(user.id):
        await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}) محظور عام بالفعل ."
        )
    else:
        gban_sql.catgban(user.id, reason)
    san = await admin_groups(event.client)
    count = 0
    sandy = len(san)
    if sandy == 0:
        return await edit_delete(cate, "`you are not admin of atleast one group` ")
    await cate.edit(
        f"جارى حظر [{user.first_name}](tg://user?id={user.id}) من {len(san)} مجموعات ."
    )
    for i in range(sandy):
        try:
            await event.client(EditBannedRequest(san[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            achat = await event.client.get_entity(san[i])
            await event.client.send_message(
                BOTLOG_CHATID,
                f"`You don't have required permission in :`\n**Chat :** {get_display_name(achat)}(`{achat.id}`)\n`For banning here`",
            )
    end = datetime.now()
    cattaken = (end - start).seconds
    if reason:
        await cate.edit(
            f"المستخدم : [{user.first_name}](tg://user?id={user.id})\nتم حظره من  {count} مجموعات انت ادمن فيها .\n المده :{cattaken} ثانيه .\nالسبب : {reason}"
        )
    else:
        await cate.edit(
            f"المستخدم : [{user.first_name}](tg://user?id={user.id})\nتم حظره من  {count} مجموعات انت ادمن فيها .\n المده :{cattaken} ثانيه ."
        )
    if BOTLOG and count != 0:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#حظر_عام\
                \nالمستخدم : [{user.first_name}](tg://user?id={user.id})\
                \nالايدي : {user.id}\
                \nالسبب : {reason}\
                \nتم حظره من {count} مجموعات\
                \nالمده : {cattaken} seconds",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#حظر_عام\
                \nالمستخدم : [{user.first_name}](tg://user?id={user.id})\
                \nالايدي : {user.id}\
                \nتم حظره من {count} مجموعات\
                \nالمده : {cattaken} ثانيه .",
            )
        with contextlib.suppress(BadRequestError):
            if reply:
                await reply.forward_to(BOTLOG_CHATID)
                await reply.delete()


@sbb_b.ar_cmd(
    pattern="الغاء ح عام(?:\s|$)([\s\S]*)",
    command=("الغاء ح عام", plugin_category),
    info={
        "header": "To unban the person from every group where you are admin.",
        "description": "will unban and also remove from your gbanned list.",
        "usage": "{tr}ungban <username/reply/userid>",
    },
)
async def catgban(event):
    "To unban the person from every group where you are admin."
    cate = await edit_or_reply(event, "جارى الغاء الحظر ......")
    start = datetime.now()
    user, reason = await get_user_from_event(event, cate)
    if not user:
        return
    if gban_sql.is_gbanned(user.id):
        gban_sql.catungban(user.id)
    else:
        return await edit_delete(
            cate,
            f"[{user.first_name}](tg://user?id={user.id}) ليس محظور عام .",
        )
    san = await admin_groups(event.client)
    count = 0
    sandy = len(san)
    if sandy == 0:
        return await edit_delete(cate, "`you are not even admin of atleast one group `")
    await cate.edit(
        f"جارى الغاء حظر [{user.first_name}](tg://user?id={user.id}) من {len(san)} مجموعات ."
    )
    for i in range(sandy):
        try:
            await event.client(EditBannedRequest(san[i], user.id, UNBAN_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            achat = await event.client.get_entity(san[i])
            await event.client.send_message(
                BOTLOG_CHATID,
                f"`You don't have required permission in :`\n**Chat :** {get_display_name(achat)}(`{achat.id}`)\n`For Unbanning here`",
            )
    end = datetime.now()
    cattaken = (end - start).seconds
    if reason:
        await cate.edit(
            f"المستخدم : [{user.first_name}](tg://user?id={user.id})\nتم الغاء حظره من  {count} مجموعات انت ادمن فيها .\n المده :{cattaken} ثانيه .\n**Reason :** `{reason}`"
        )
    else:
        await cate.edit(
            f"المستخدم : [{user.first_name}](tg://user?id={user.id})\nتم الغاء حظره من  {count} مجموعات انت ادمن فيها .\n المده :{cattaken} ثانيه ."
        )

    if BOTLOG and count != 0:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#الغاء_حظر_عام\
                \nالمستخدم : [{user.first_name}](tg://user?id={user.id})\
                \nالايدي : {user.id}\
                \nالسبب : {reason}\
                \nتم الغاء حظره من {count} مجموعات\
                \nالمده : {cattaken} seconds",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#الغاء_حظر_عام\
                \nالمستخدم : [{user.first_name}](tg://user?id={user.id})\
                \nالايدي : {user.id}\
                \nتم الغاء حظره من {count} مجموعات\
                \nالمده : {cattaken} ثانيه .",
            )


@sbb_b.ar_cmd(
    pattern="المحظورين عام$",
    command=("المحظورين عام", plugin_category),
    info={
        "header": "Shows you the list of all gbanned users by you.",
        "usage": "{tr}listgban",
    },
)
async def gablist(event):
    "Shows you the list of all gbanned users by you."
    gbanned_users = gban_sql.get_all_gbanned()
    GBANNED_LIST = "المحظورين عام :\n"
    if len(gbanned_users) > 0:
        for a_user in gbanned_users:
            if a_user.reason:
                GBANNED_LIST += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
            else:
                GBANNED_LIST += (
                    f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) \n"
                )
    else:
        GBANNED_LIST = "لا يوجد محظورين عام ."
    await edit_or_reply(event, GBANNED_LIST)


@sbb_b.ar_cmd(
    pattern="ك عام(?:\s|$)([\s\S]*)",
    command=("ك عام", plugin_category),
    info={
        "header": "To mute a person in all groups where you are admin.",
        "description": "It doesnt change user permissions but will delete all messages sent by him in the groups where you are admin including in private messages.",
        "usage": "{tr}gmute username/reply> <reason (optional)>",
    },
)
async def startgmute(event):
    "To mute a person in all groups where you are admin."
    if event.is_private:
        await event.edit("جارى الكتم ......")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == sbb_b.uid:
            return await edit_or_reply(event, "لا استطيع كتم نفسى .")
        userid = user.id
    try:
        user = await event.client.get_entity(userid)
    except Exception:
        return await edit_or_reply(event, "`Sorry. I am unable to fetch the user`")
    if is_muted(userid, "gmute"):
        return await edit_or_reply(
            event,
            f"{_format.mentionuser(user.first_name ,user.id)} مكتوم عام من قبل .",
        )
    try:
        mute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, f"**خطأ**\n`{e}`")
    else:
        if reason:
            await edit_or_reply(
                event,
                f"المستخدم : {_format.mentionuser(user.first_name ,user.id)}\nتم كتمه عام ✓\nالسبب : {reason}",
            )
        else:
            await edit_or_reply(
                event,
                f"المستخدم : {_format.mentionuser(user.first_name ,user.id)}\nتم كتمه عام ✓",
            )
    if BOTLOG:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#كتم_عام\n"
                f"المستخدم : {_format.mentionuser(user.first_name ,user.id)} \n"
                f"السبب : `{reason}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#كتم_عام\n"
                f"المستخدم : {_format.mentionuser(user.first_name ,user.id)} \n",
            )
        if reply:
            await reply.forward_to(BOTLOG_CHATID)


@sbb_b.ar_cmd(
    pattern="الغاء ك عام(?:\s|$)([\s\S]*)",
    command=("الغاء ك عام", plugin_category),
    info={
        "header": "To unmute the person in all groups where you were admin.",
        "description": "This will work only if you mute that person by your gmute command.",
        "usage": "{tr}ungmute <username/reply>",
    },
)
async def endgmute(event):
    "To remove gmute on that person."
    if event.is_private:
        await event.edit("جارى الغاء الكتم .....")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == sbb_b.uid:
            return await edit_or_reply(event, "اسف لا استطيع كتم نفسي .")
        userid = user.id
    try:
        user = await event.client.get_entity(userid)
    except Exception:
        return await edit_or_reply(event, "`Sorry. I am unable to fetch the user`")
    if not is_muted(userid, "gmute"):
        return await edit_or_reply(
            event, f"{_format.mentionuser(user.first_name ,user.id)} ليس مكتوم عام ."
        )
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, f"**خطأ**\n`{e}`")
    else:
        if reason:
            await edit_or_reply(
                event,
                f"المستخدم : {_format.mentionuser(user.first_name ,user.id)}\nتم الغاء كتمه عام ✓\nالسبب : {reason}",
            )
        else:
            await edit_or_reply(
                event,
                f"المستخدم : {_format.mentionuser(user.first_name ,user.id)}\nتم الغاء كتمه عام ✓",
            )
    if BOTLOG:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الغاء_كتم_عام\n"
                f"المستخدم : {_format.mentionuser(user.first_name ,user.id)} \n"
                f"السبب : `{reason}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الغاء_كتم_عام\n"
                f"المستخدم : {_format.mentionuser(user.first_name ,user.id)} \n",
            )


@sbb_b.ar_cmd(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()
