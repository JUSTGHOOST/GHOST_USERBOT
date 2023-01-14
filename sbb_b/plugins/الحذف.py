import re
from asyncio import sleep

from telethon.tl.types import (
    InputMessagesFilterDocument,
    InputMessagesFilterEmpty,
    InputMessagesFilterGeo,
    InputMessagesFilterGif,
    InputMessagesFilterMusic,
    InputMessagesFilterMyMentions,
    InputMessagesFilterPhotos,
    InputMessagesFilterUrl,
    InputMessagesFilterVideo,
)

from sbb_b import sbb_b

from . import BOTLOG, BOTLOG_CHATID

Tnsmeet1 = {}
Tnsmeet1 = {
    "ا": InputMessagesFilterPhotos,
    "ل": InputMessagesFilterDocument,
    "ر": InputMessagesFilterUrl,
    "س": InputMessagesFilterEmpty,
    "ئ": InputMessagesFilterGif,
    "ج": InputMessagesFilterVideo,
    "م": InputMessagesFilterMusic,
    "ي": InputMessagesFilterMyMentions,
    "ع": InputMessagesFilterGeo,
}


@sbb_b.ar_cmd(pattern="مسح(?:\s|$)([\s\S]*)")
async def iq(cloneiq):
    chat = await cloneiq.get_input_chat()
    msgs = []
    count = 0
    input_str = cloneiq.pattern_match.group(1)
    iqype = re.findall(r"\w+", input_str)
    try:
        p_type = iqype[0].replace("-", "")
        input_str = input_str.replace(iqype[0], "").strip()
    except IndexError:
        p_type = None
    error = ""
    result = ""
    await cloneiq.delete()
    reply = await cloneiq.get_reply_message()
    if reply:
        if input_str and input_str.isnumeric():
            if p_type is not None:
                for ty in p_type:
                    if ty in Tnsmeet1:
                        async for msg in cloneiq.client.iter_messages(
                            cloneiq.chat_id,
                            limit=int(input_str),
                            offset_id=reply.id - 1,
                            reverse=True,
                            filter=Tnsmeet1[ty],
                        ):
                            count += 1
                            msgs.append(msg)
                            if len(msgs) == 50:
                                await cloneiq.client.delete_messages(chat, msgs)
                                msgs = []
                        if msgs:
                            await cloneiq.client.delete_messages(chat, msgs)
                    elif ty == "s":
                        error += f"\n**♛ ⦙   هنـاك خطـا فـي تركـيب الجمـلة 🔩 :**"
                    else:
                        error += (
                            f"\n\n♛ ⦙   `{ty}`  **هنـاك خطـا فـي تركـيب الجمـلة 🔩 :**"
                        )
            else:
                count += 1
                async for msg in cloneiq.client.iter_messages(
                    cloneiq.chat_id,
                    limit=(int(input_str) - 1),
                    offset_id=reply.id,
                    reverse=True,
                ):
                    msgs.append(msg)
                    count += 1
                    if len(msgs) == 50:
                        await cloneiq.client.delete_messages(chat, msgs)
                        msgs = []
                if msgs:
                    await cloneiq.client.delete_messages(chat, msgs)
        elif input_str and p_type is not None:
            if p_type == "s":
                try:
                    cont, inputstr = input_str.split(" ")
                except ValueError:
                    cont = "error"
                    inputstr = input_str
                cont = cont.strip()
                inputstr = inputstr.strip()
                if cont.isnumeric():
                    async for msg in cloneiq.client.iter_messages(
                        cloneiq.chat_id,
                        limit=int(cont),
                        offset_id=reply.id - 1,
                        reverse=True,
                        search=inputstr,
                    ):
                        count += 1
                        msgs.append(msg)
                        if len(msgs) == 50:
                            await cloneiq.client.delete_messages(chat, msgs)
                            msgs = []
                else:
                    async for msg in cloneiq.client.iter_messages(
                        cloneiq.chat_id,
                        offset_id=reply.id - 1,
                        reverse=True,
                        search=input_str,
                    ):
                        count += 1
                        msgs.append(msg)
                        if len(msgs) == 50:
                            await cloneiq.client.delete_messages(chat, msgs)
                            msgs = []
                if msgs:
                    await cloneiq.client.delete_messages(chat, msgs)
            else:
                error += f"\n♛ ⦙   `{ty}`  **هنـاك خطـا فـي تركـيب الجمـلة 🔩 :** "
        elif input_str:
            error += f"\n♛ ⦙   **هنـاك خطـا فـي تركـيب الجمـلة 🔩 :**"
        elif p_type is not None:
            for ty in p_type:
                if ty in Tnsmeet1:
                    async for msg in cloneiq.client.iter_messages(
                        cloneiq.chat_id,
                        min_id=cloneiq.reply_to_msg_id - 1,
                        filter=Tnsmeet1[ty],
                    ):
                        count += 1
                        msgs.append(msg)
                        if len(msgs) == 50:
                            await cloneiq.client.delete_messages(chat, msgs)
                            msgs = []
                    if msgs:
                        await cloneiq.client.delete_messages(chat, msgs)
                else:
                    error += f"\n♛ ⦙   `{ty}`  **هنـاك خطـا فـي تركـيب الجمـلة 🔩 :**"
        else:
            async for msg in cloneiq.client.iter_messages(
                chat, min_id=cloneiq.reply_to_msg_id - 1
            ):
                count += 1
                msgs.append(msg)
                if len(msgs) == 50:
                    await cloneiq.client.delete_messages(chat, msgs)
                    msgs = []
            if msgs:
                await cloneiq.client.delete_messages(chat, msgs)
    elif p_type is not None and input_str:
        if p_type != "s" and input_str.isnumeric():
            for ty in p_type:
                if ty in Tnsmeet1:
                    async for msg in cloneiq.client.iter_messages(
                        cloneiq.chat_id, limit=int(input_str), filter=Tnsmeet1[ty]
                    ):
                        count += 1
                        msgs.append(msg)
                        if len(msgs) == 50:
                            await cloneiq.client.delete_messages(chat, msgs)
                            msgs = []
                    if msgs:
                        await cloneiq.client.delete_messages(chat, msgs)
                elif ty == "s":
                    error += f"\n**♛ ⦙   لا تستطـيع استـخدام امر التنظيف عبر البحث مع الاضافه 🔎**"
                else:
                    error += f"\n♛ ⦙   `{ty}`  **هنـاك خطـا فـي تركـيب الجمـلة 🔩 :**"
        elif p_type == "s":
            try:
                cont, inputstr = input_str.split(" ")
            except ValueError:
                cont = "error"
                inputstr = input_str
            cont = cont.strip()
            inputstr = inputstr.strip()
            if cont.isnumeric():
                async for msg in cloneiq.client.iter_messages(
                    cloneiq.chat_id, limit=int(cont), search=inputstr
                ):
                    count += 1
                    msgs.append(msg)
                    if len(msgs) == 50:
                        await cloneiq.client.delete_messages(chat, msgs)
                        msgs = []
            else:
                async for msg in cloneiq.client.iter_messages(
                    cloneiq.chat_id, search=input_str
                ):
                    count += 1
                    msgs.append(msg)
                    if len(msgs) == 50:
                        await cloneiq.client.delete_messages(chat, msgs)
                        msgs = []
            if msgs:
                await cloneiq.client.delete_messages(chat, msgs)
        else:
            error += f"\n♛ ⦙   `{ty}`  **هنـاك خطـا فـي تركـيب الجمـلة 🔩 :**"
    elif p_type is not None:
        for ty in p_type:
            if ty in Tnsmeet1:
                async for msg in cloneiq.client.iter_messages(
                    cloneiq.chat_id, filter=Tnsmeet1[ty]
                ):
                    count += 1
                    msgs.append(msg)
                    if len(msgs) == 50:
                        await cloneiq.client.delete_messages(chat, msgs)
                        msgs = []
                if msgs:
                    await cloneiq.client.delete_messages(chat, msgs)
            elif ty == "s":
                error += f"\n**♛ ⦙   لا تستطـيع استـخدام امر التنظيف عبر البحث مع الاضافه 🔎**"
            else:
                error += f"\n♛ ⦙   `{ty}`  **هنـاك خطـا فـي تركـيب الجمـلة 🔩 :**"
    elif input_str.isnumeric():
        async for msg in cloneiq.client.iter_messages(chat, limit=int(input_str) + 1):
            count += 1
            msgs.append(msg)
            if len(msgs) == 50:
                await cloneiq.client.delete_messages(chat, msgs)
                msgs = []
        if msgs:
            await cloneiq.client.delete_messages(chat, msgs)
    else:
        error += "\n**♛ ⦙   لم يتـم تحـديد الرسـالة أرسل  (.الاوامر ) و رؤية اوامر التنظيف  📌**"
    if msgs:
        await cloneiq.client.delete_messages(chat, msgs)
    if count > 0:
        result += (
            "تـم الأنتـهاء من التـنظيف السـريع  ✅  \nلقـد  تـم حـذف \nعـدد  "
            + str(count)
            + " من الـرسائـل "
        )
    if error != "":
        result += f"\n\n**♛ ⦙  عـذرا هنـاك خطـأ ❌:**{error}"
    if result == "":
        result += "**♛ ⦙   لا تـوجد رسـائل لـتنظيفها ♻️**"
    hi = await cloneiq.client.send_message(cloneiq.chat_id, result)
    if BOTLOG:
        await cloneiq.client.send_message(
            BOTLOG_CHATID, f"**♛ ⦙   حـذف الـرسائل 🗳️** \n{result}"
        )
    await sleep(5)
    await hi.delete()
