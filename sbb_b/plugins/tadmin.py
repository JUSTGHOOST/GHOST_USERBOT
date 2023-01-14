from telethon.errors import BadRequestError
from telethon.errors.rpcerrorlist import UserAdminInvalidError, UserIdInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
from telethon.utils import get_display_name

from sbb_b import sbb_b

from ..core.managers import edit_or_reply
from ..helpers.utils import _format
from . import BOTLOG, BOTLOG_CHATID, extract_time, get_user_from_event

plugin_category = "admin"

# =================== CONSTANT ===================
NO_ADMIN = "انا لست ادمن هنا !"
NO_PERM = "`I don't have sufficient permissions! This is so sed. Alexa play despacito`"


@sbb_b.ar_cmd(
    pattern="ك مؤقت(?:\s|$)([\s\S]*)",
    command=("ك مؤقت", plugin_category),
    info={
        "header": "To stop sending messages permission for that user",
        "description": "Temporary mutes the user for given time.",
        "Time units": {
            "s": "seconds",
            "m": "minutes",
            "h": "Hours",
            "d": "days",
            "w": "weeks",
        },
        "usage": [
            "{tr}tmute <userid/username/reply> <time>",
            "{tr}tmute <userid/username/reply> <time> <reason>",
        ],
        "examples": ["{tr}tmute 2d to test muting for 2 days"],
    },
    groups_only=True,
    require_admin=True,
)
async def tmuter(event):  # sourcery no-metrics
    "To mute a person for specific time"
    catevent = await edit_or_reply(event, "جارى الكتم ......")
    user, reason = await get_user_from_event(event, catevent)
    if not user:
        return
    if not reason:
        return await catevent.edit("اكتب الامر بطريقه صحيحه .")
    reason = reason.split(" ", 1)
    hmm = len(reason)
    cattime = reason[0].strip()
    reason = "".join(reason[1:]) if hmm > 1 else None
    ctime = await extract_time(catevent, cattime)
    if not ctime:
        return
    if user.id == event.client.uid:
        return await catevent.edit("لا استطيع كتم نفسى")
    try:
        await catevent.client(
            EditBannedRequest(
                event.chat_id,
                user.id,
                ChatBannedRights(until_date=ctime, send_messages=True),
            )
        )
        # Announce that the function is done
        if reason:
            await catevent.edit(
                f"المستخدم : {_format.mentionuser(user.first_name ,user.id)}\nتم كتمه فى : {get_display_name(await event.get_chat())}\n"
                f"مده الكتم : {cattime}\n"
                f"السبب : {reason}"
            )
            if BOTLOG:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "#كتم_مؤقت\n"
                    f"المستخدم : [{user.first_name}](tg://user?id={user.id})\n"
                    f"المجموعه : {get_display_name(await event.get_chat())}({event.chat_id})\n"
                    f"مده الكتم : {cattime}\n"
                    f"السبب : {reason}",
                )
        else:
            await catevent.edit(
                f"المستخدم : {_format.mentionuser(user.first_name ,user.id)}\nتم كتمه فى : {get_display_name(await event.get_chat())}\n"
                f"مده الكتم : {cattime}\n"
            )
            if BOTLOG:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    "#كتم_مؤقت\n"
                    f"المستخدم : [{user.first_name}](tg://user?id={user.id})\n"
                    f"المجموعه : {get_display_name(await event.get_chat())}({event.chat_id})\n"
                    f"مده الكتم : {cattime}\n",
                )
        # Announce to logging group
    except UserIdInvalidError:
        return await catevent.edit("`Uh oh my mute logic broke!`")
    except UserAdminInvalidError:
        return await catevent.edit(
            "`Either you're not an admin or you tried to mute an admin that you didn't promote`"
        )
    except Exception as e:
        return await catevent.edit(f"`{e}`")


@sbb_b.ar_cmd(
    pattern="ح مؤقت(?:\s|$)([\s\S]*)",
    command=("ح مؤقت", plugin_category),
    info={
        "header": "To remove a user from the group for specified time.",
        "description": "Temporary bans the user for given time.",
        "Time units": {
            "s": "seconds",
            "m": "minutes",
            "h": "Hours",
            "d": "days",
            "w": "weeks",
        },
        "usage": [
            "{tr}tban <userid/username/reply> <time>",
            "{tr}tban <userid/username/reply> <time> <reason>",
        ],
        "examples": ["{tr}tban 2d to test baning for 2 days"],
    },
    groups_only=True,
    require_admin=True,
)
async def tban(event):  # sourcery no-metrics
    "To ban a person for specific time"
    catevent = await edit_or_reply(event, "جارى الحظر ......")
    user, reason = await get_user_from_event(event, catevent)
    if not user:
        return
    if not reason:
        return await catevent.edit("اكتب الامر بطريقه صحيحه .")
    reason = reason.split(" ", 1)
    hmm = len(reason)
    cattime = reason[0].strip()
    reason = "".join(reason[1:]) if hmm > 1 else None
    ctime = await extract_time(catevent, cattime)
    if not ctime:
        return
    if user.id == event.client.uid:
        return await catevent.edit("لا استطيع كتم نفسى .")
    await catevent.edit("`Whacking the pest!`")
    try:
        await event.client(
            EditBannedRequest(
                event.chat_id,
                user.id,
                ChatBannedRights(until_date=ctime, view_messages=True),
            )
        )
    except UserAdminInvalidError:
        return await catevent.edit(
            "ليس لديك صلاحيات كافيه ."
        )
    except BadRequestError:
        return await catevent.edit(NO_PERM)
    # Helps ban group join spammers more easily
    try:
        reply = await event.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        return await catevent.edit(
            "`I dont have message nuking rights! But still he was banned!`"
        )
    # Delete message and then tell that the command
    # is done gracefully
    # Shout out the ID, so that fedadmins can fban later
    if reason:
        await catevent.edit(
            f"المستخدم : {_format.mentionuser(user.first_name ,user.id)}\nتم حظره فى : {get_display_name(await event.get_chat())}\n"
                f"مده الحظر : {cattime}\n"
            f"السبب : {reason}"
        )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#حظر_مؤقت\n"
                    f"المستخدم : [{user.first_name}](tg://user?id={user.id})\n"
                    f"المجموعه : {get_display_name(await event.get_chat())}({event.chat_id})\n"
                    f"مده الحظر : {cattime}\n"
                f"السبب : {reason}",
            )
    else:
        await catevent.edit(
            f"المستخدم : {_format.mentionuser(user.first_name ,user.id)}\nتم حظره فى : {get_display_name(await event.get_chat())}\n"
                f"مده الحظر : {cattime}\n"
        )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#حظر_مؤقت\n"
                    f"المستخدم : [{user.first_name}](tg://user?id={user.id})\n"
                    f"المجموعه : {get_display_name(await event.get_chat())}({event.chat_id})\n"
                    f"مده الحظر : {cattime}\n",
            )
