import asyncio
from collections import deque

from . import edit_or_reply, sbb_b


@sbb_b.ar_cmd(pattern="غبي$")
async def _(event):
    animation_interval = 1
    animation_ttl = range(14)
    event = await edit_or_reply(event, "⌔∮ يتم رمي عقلك في القمامه")
    animation_chars = [
        "⌯︙عقلك ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
        "⌯︙عقلك ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
        "⌯︙عقلك ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",
        "⌯︙عقلك ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",
        "⌯︙عقلك ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",
        "⌯︙عقلك ➡️ 🧠\n\n🧠<(^_^ <)         🗑",
        "⌯︙عقلك ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
        "⌯︙عقلك ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
        "⌯︙عقلك ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
        "⌯︙عقلك ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
        "⌯︙عقلك ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
        "⌯︙عقلك ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
        "⌯︙عقلك ➡️ 🧠\n\n           (> ^_^)>🗑",
        "⌯︙عقلك ➡️ 🧠\n\n           <(^_^ <)🗑",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 14])


@sbb_b.ar_cmd(pattern="نعم$")
async def _(event):
    animation_interval = 0.8
    animation_ttl = range(5)
    event = await edit_or_reply(event, "نعم !")
    animation_chars = [
        "نعممم ؟",
        "نعمممممم 🙄",
        "مالك ف حاجه ؟",
        "ف حاجه ولا اى 🤔\nhttps://telegra.ph/file/f3b760e4a99340d331f9b.jpg",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 5], link_preview=True)

@sbb_b.ar_cmd(pattern="مربعات$")
async def _(event):
    animation_interval = 0.3
    animation_ttl = range(15)
    event = await edit_or_reply(event, "مـربـعات....")
    animation_chars = [
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬛⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬛⬜⬛⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛",
        "⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬛\n⬛⬜⬛⬜⬛\n⬛⬜⬜⬜⬛\n⬛⬛⬛⬛⬛",
        "⬜⬜⬜\n⬜⬛⬜\n⬜⬜⬜",
        "[👉🔴👈]",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 15])


@sbb_b.ar_cmd(pattern="حلويات$")
async def _(event):
    event = await edit_or_reply(event, "حلويات")
    deq = deque(list("🍦🍧🍩🍪🎂🍰🧁🍫🍬🍭"))
    for _ in range(100):
        await asyncio.sleep(0.4)
        await event.edit("".join(deq))
        deq.rotate(1)


@sbb_b.ar_cmd(pattern="نار$")
async def _(event):
    event = await edit_or_reply(event, "احـراق")
    await event.edit("احـرقه")
    await asyncio.sleep(0.8)
    await event.edit("ليييي")
    await asyncio.sleep(0.8)
    await event.edit("كب عليه البنزين بسرعه 😂")
    await asyncio.sleep(0.8)
    await event.edit("لا والنبى 😭")
    await asyncio.sleep(0.8)
    await event.edit("اخرس خالص 😠")
    await asyncio.sleep(0.8)
    await event.edit("😭")
    await asyncio.sleep(0.8)
    await event.edit("يلا احرقه بسرعه 😂😠🔥")
    await asyncio.sleep(0.8)
    await event.edit("🔥")
