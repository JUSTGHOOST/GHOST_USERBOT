import asyncio

from . import edit_or_reply, sbb_b

plugin_category = "fun"

@sbb_b.ar_cmd(
    pattern="قلوب$",
    command=("قلوب", plugin_category),
    info={
        "الامر": "**امر تسليه قم بالتجربه بنفسك**",
        "الاستخدام": "{tr}قلوب",
    },
)
async def _(event):
    "animation command"
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await edit_or_reply(event, "🖤")
    animation_chars = [
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
