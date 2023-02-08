import re

from telethon import Button, events
from telethon.events import CallbackQuery

from razan.CMD.aomari import *
from sbb_b import sbb_b

from ..Config import Config
from ..core import check_owner
from ..sql_helper.globals import gvarstatus

ROE = ""
ROZADM = "من هنا يمكنك ايجاد جميع"
ITPIC = (
    gvarstatus("HELP_PIC") or "https://telegra.ph/file/52b904e1545c942a93d8b.jpg"
)
RAZAN = Config.TG_BOT_USERNAME

if Config.TG_BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await sbb_b.get_me()
        if query.startswith("الاوامر") and event.query.user_id == sbb_b.uid:
            buttons = [
                
                [
                    Button.inline("البوت", data="BOTCMD4"),
                    Button.inline("الجروب", data="admincmd_s"),
                ],
                [
                    Button.inline("التسلية", data="TASLIACMD"),
                    Button.inline("الادوات", data="toolsed1"),
                ],
                [
                    Button.inline("التحميل", data="DOWMANLODE4"),
                    Button.inline("الازرار", data="ITBUTT"),
                ],
                [
                    Button.inline("اضافات", data="EXTRACMD"),
                    Button.inline("الميوزك", data="MSHKLMSIC"),
                ],[Button.url("• المطـور •", "https://t.me/xXx_JR")],

            ]
            result = builder.article(
                title="sbb_b",
                buttons=buttons,
                link_preview=False,
            )
            if ITPIC and ITPIC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(ITPIC, buttons=buttons, link_preview=False)
            elif ITPIC:
                result = builder.document(
                    ITPIC, title="sbb_b", buttons=buttons, link_preview=False
                )
        await event.answer([result] if result else None)


@sbb_b.ar_cmd(pattern="الاوامر")
async def repo(event):
    start = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await sbb_b.inline_query(start, "الاوامر")
    await response[0].click(event.chat_id)
    await event.delete()

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"MAIN")))
@check_owner
async def _(event):
    butze = [
        
        [
            Button.inline("البوت", data="BOTCMD4"),
            Button.inline("الجروب", data="admincmd_s"),
        ],
        [
            Button.inline("التسلية", data="TASLIACMD"),
            Button.inline("الادوات", data="toolsed1"),
        ],
        [
            Button.inline("التحميل", data="DOWMANLODE4"),
            Button.inline("الازرار", data="ITBUTT"),
        ],
        [
            Button.inline("اضافات", data="EXTRACMD"),
            Button.inline("الميوزك", data="MSHKLMSIC"),
        ],[Button.url("• المطـور •", "https://t.me/xXx_JR")],
    ]
    await event.edit(buttons=butze)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ITBUTT")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MAIN")]]
    await event.edit(ITBUTT, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"MSHKLMSIC")))
async def varssett(event):
        butze=[
            [
                Button.inline("تشغيل المكالمة", data="rozlve"),
                Button.inline("انهاء المكالمة", data="endcalrz"),
            ],
            [
                Button.inline("مغادرة المكالمة", data="leaveVoicechatroz"),
                Button.inline("انضمام للمكالمة", data="joinVoicecharoz"),
            ],
            [
                Button.inline("قائمة التشغيل", data="get_playlistroz"),
                Button.inline("تشغيل صوتي", data="play_audioroze"),
            ],
            [
                Button.inline("ايقاف مؤقت", data="pause_streamroz"),
                Button.inline("تخطي التشغيل", data="skip_srazan"),
            ],
            [Button.inline("القائمة الرئيسية", data="MAIN")],
        ]
        await event.edit(ROE, buttons=butze)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"rozlve")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MSHKLMSIC")]]
    await event.edit(rozlve, buttons=buttons, link_preview=False)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"endcalrz")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MSHKLMSIC")]]
    await event.edit(endcalrz, buttons=buttons, link_preview=False)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"leaveVoicechatroz")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MSHKLMSIC")]]
    await event.edit(leaveVoicechatroz, buttons=buttons, link_preview=False)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"joinVoicecharoz")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MSHKLMSIC")]]
    await event.edit(joinVoicecharoz, buttons=buttons, link_preview=False)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"get_playlistroz")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MSHKLMSIC")]]
    await event.edit(get_playlistroz, buttons=buttons, link_preview=False)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"play_audioroze")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MSHKLMSIC")]]
    await event.edit(play_audioroze, buttons=buttons, link_preview=False)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"pause_streamroz")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MSHKLMSIC")]]
    await event.edit(pause_streamroz, buttons=buttons, link_preview=False)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"skip_srazan")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="MSHKLMSIC")]]
    await event.edit(skip_srazan, buttons=buttons, link_preview=False)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"EXTRACMD")))
@check_owner
async def _(event):
    butze = [
        [
            Button.inline("الترجمة", data="ALIVETRG"),
            Button.inline("التوجيه", data="SAVETECXT"),
            Button.inline("حالتي", data="R7ALTIE"),
        ],
        [
            Button.inline("", data=""),
            Button.inline("خاص", data="PVIT"),
            Button.inline("الارسال الوهمي", data="SACAMF"),
        ],
        [
            Button.inline("حماية الخاص", data="HEMAIREF"),
            Button.inline("", data=""),
            Button.inline("البروفيل", data="PROFUIECMD"),
        ],
        [
            Button.inline("الاذكار", data="AZKARIT"),
            Button.inline("الكتابة", data="KTABAFE"),
            Button.inline("التاك و المنشن", data="TAGE4E"),
        ],
        [
            Button.inline("⌫", data="EXTRAC7"),
            Button.inline("⌦", data="EXTRAC7"),
        ],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=butze)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"HEMAIREF")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(HEMAIREF, buttons=buttons, link_preview=False)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"PVIT")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(PVIT, buttons=buttons, link_preview=False)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"AZKARIT")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(AZKARIT, buttons=buttons, link_preview=False)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"KTABAFE")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(KTABAFE, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"EXTRAC7")))
@check_owner
async def _(event):
    butze = [
        [
            Button.inline("ملصق متحرك", data="VASCHER"),
            Button.inline("تحويل صورة", data="STIKERPIC"),
        ],
        [
            Button.inline("تحويل متحركة", data="TOGIDEF"),
            Button.inline("تحويل لملف", data="ITESRAZAN"),
        ],
        [
            Button.inline("تحويل لكتابة", data="LTABAMEKF"),
            Button.inline("الملف لصورة", data="AJMTHOEF"),
        ],
        [
            Button.inline("تحويل ملصق", data="PICYEYS"),
            Button.inline("تحويل صوتي", data="JISORO"),
        ],
        [
            Button.inline("⌫", data="EXTRACMD"),
            Button.inline("⌦", data="EXTRACMD"),
        ],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=butze)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"DOWMANLODE4")))
@check_owner
async def _(event):
    butze = [
        [
            Button.inline("تحميل فيديو", data="YOUTUBECCMD"),
            Button.inline("تحميل صوتي", data="YOUTUBECMD"),
        ],
        [
            Button.inline("بحث", data="ALIVETSM"),
            Button.inline("تيك توك", data="ALIVEFDO"),
        ],
        [
            Button.inline("", data=""),
            Button.inline("", data=""),
        ],
        [
            Button.inline("", data=""),
            Button.inline("", data=""),
        ],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=butze)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"INSTAGRAMCMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="DOWMANLODE4")]]
    await event.edit(INSTAGRAMCMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"YOUTUBECMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="DOWMANLODE4")]]
    await event.edit(YOUTUBECMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"YOUTUBECCMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="DOWMANLODE4")]]
    await event.edit(YOUTUBECCMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVETSM")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="DOWMANLODE4")]]
    await event.edit(ALIVETSM, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEFDO")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="DOWMANLODE4")]]
    await event.edit(ALIVEFDO, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"BENTRSTCMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="DOWMANLODE4")]]
    await event.edit(BENTRSTCMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"YIOFDD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="DOWMANLODE4")]]
    await event.edit(YIOFDD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"PICSERACJ")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="DOWMANLODE4")]]
    await event.edit(PICSERACJ, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"PICYEYS")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRAC7")]]
    await event.edit(PICYEYS, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"AJMTHOEF")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRAC7")]]
    await event.edit(AJMTHOEF, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"JISORO")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRAC7")]]
    await event.edit(JISORO, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"LTABAMEKF")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRAC7")]]
    await event.edit(LTABAMEKF, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ITESRAZAN")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRAC7")]]
    await event.edit(ITESRAZAN, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TOGIDEF")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRAC7")]]
    await event.edit(TOGIDEF, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"STIKERPIC")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRAC7")]]
    await event.edit(STIKERPIC, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"VASCHER")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRAC7")]]
    await event.edit(VASCHER, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TAGE4E")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(TAGE4E, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"PROFUIECMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(PROFUIECMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"SACAMF")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(SACAMF, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"R7ALTIE")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(R7ALTIE, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"SALACMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(SALACMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"DATECMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(DATECMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"COROONA")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(COROONA, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"SAVETECXT")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(SAVETECXT, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVETRG")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="EXTRACMD")]]
    await event.edit(ALIVETRG, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"BOTCMD4")))
@check_owner
async def _(event):
    butze = [
        [
            Button.inline("الفحص", data="ALICES"),
            Button.inline("سليب ميديا", data="IMSLEEPF"),
        ],
        [
            Button.inline("", data=""),
            Button.inline("", data=""),
        ],
        [
            Button.inline("سرعة الانترنت", data="ALNTDOS"),
            Button.inline("اعادة تشغيل", data="ALIVEAUD"),
        ],
        [
            Button.inline("تحديث السورس", data="UPDATE4E"),
            Button.inline("السليب", data="ALIVESLB"),
        ],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=butze)


#


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALICVEINLI")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="BOTCMD4")]]
    await event.edit(ALICVEINLI, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEAUD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="BOTCMD4")]]
    await event.edit(ALIVEAUD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVESLB")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="BOTCMD4")]]
    await event.edit(ALIVESLB, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"IMSLEEPF")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="BOTCMD4")]]
    await event.edit(IMSLEEPF, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"UPDATE4E")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="BOTCMD4")]]
    await event.edit(UPDATE4E, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALICES")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="BOTCMD4")]]
    await event.edit(ALICES, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALNTDOS")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="BOTCMD4")]]
    await event.edit(ALNTDOS, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"toolsed1")))
@check_owner
async def _(event):
    buttons = [
        [
            Button.inline("اذاعة للخاص", data="BROADEV1"),
            Button.inline("اذاعة للجروب", data="BRWAADV1"),
            Button.inline("اضافة اعضاء", data="ADDMEM7"),
        ],
        [
            Button.inline("الانتحال", data="CLIONEACMD"),
            Button.inline("الغاء الانتحال", data="ALIVEMEE"),
            Button.inline("الايدي", data="ALIVEDIII"),
        ],
        [
            Button.inline("ايدي", data="KSHFCMD"),
            Button.inline("التقليد", data="ADDTKLED"),
            Button.inline("ايقاف التقليد", data="STOPAZAG"),
        ],
        [
            Button.inline("⌫", data="TOOLCMD2"),
            Button.inline("⌦", data="TOOLSR3"),
        ],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEMEE")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="toolsed1")]]
    await event.edit(ALIVEMEE, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ADDMEM7")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="toolsed1")]]
    await event.edit(ADDMEM7, buttons=buttons, link_preview=False)


#######################################################################


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TOOLSR3")))
@check_owner
async def _(event):
    buttons = [
        [
            Button.inline("الساعه", data="ALWKTECMD"),
            Button.inline("بايو وقتي", data="BIOEIDS"),
        ],
        [
            Button.inline("الصورة الوقتية", data="DKZUTOPIC"),
            Button.inline("دردشة وقتية", data="GROIPSDE"),
        ],
        [
            Button.inline("⌫", data="toolsed1"),
            Button.inline("⌦", data="TOOLCMD2"),
        ],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"GROIPSDE")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLSR3")]]
    await event.edit(GROIPSDE, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"DKZUTOPIC")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLSR3")]]
    await event.edit(DKZUTOPIC, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"BIOEIDS")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLSR3")]]
    await event.edit(BIOEIDS, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALWKTECMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLSR3")]]
    await event.edit(ALWKTECMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TOOLCMD2")))
@check_owner
async def _(event):
    buttons = [
        [
            Button.inline("اسم الاغنيه", data="FINDSONGIT"),
            Button.inline("التكلم", data="ALN6KCMD"),
            Button.inline("التليجراف", data="TELEHTMED"),
        ],
        [
            Button.inline("كرر", data="TKRAR3ADI"),
            Button.inline("بوت نشر (مكرر)", data="MKRRR5"),
            Button.inline("سبام", data="SPAM3AAH"),
        ],
        [
            Button.inline("ايقاف التكرار", data="STOPTKRARE"),
            Button.inline("وسبام", data="FGKHEF8"),
            Button.inline("وقت الرسالة", data="MSGTIME"),
        ],
        [
            Button.inline("⌫", data="TOOLSR3"),
            Button.inline("⌦", data="toolsed1"),
        ],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=buttons, link_preview=False)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"FINDSONGIT")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCMD2")]]
    await event.edit(FINDSONGIT, buttons=buttons, link_preview=False)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"MSGTIME")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCMD2")]]
    await event.edit(MSGTIME, buttons=buttons, link_preview=False)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEDIII")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="toolsed1")]]
    await event.edit(ALIVEDIII, buttons=buttons, link_preview=False)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALN6KCMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCMD2")]]
    await event.edit(ALN6KCMD, buttons=buttons, link_preview=False)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALMKD5D")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCMD2")]]
    await event.edit(ALMKD5D, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"NOAZAJ4")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCMD2")]]
    await event.edit(NOAZAJ4, buttons=buttons, link_preview=False)


#
@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TELEHTMED")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCMD2")]]
    await event.edit(TELEHTMED, buttons=buttons, link_preview=False)


# TELEHTMED


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TKRAR3ADI")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCMD2")]]
    await event.edit(TKRAR3ADI, buttons=buttons, link_preview=False)


# ثثثث


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"MKRRR5")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCMD2")]]
    await event.edit(MKRRR5, buttons=buttons, link_preview=False)


# ويو جوا


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"FGKHEF8")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCMD2")]]
    await event.edit(FGKHEF8, buttons=buttons, link_preview=False)


# اي


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"SPAM3AAH")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCMD2")]]
    await event.edit(SPAM3AAH, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"STOPTKRARE")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TOOLCMD2")]]
    await event.edit(STOPTKRARE, buttons=buttons, link_preview=False)


######


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"BROADEV1")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="toolsed1")]]
    await event.edit(BROADEV1, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"BRWAADV1")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="toolsed1")]]
    await event.edit(BRWAADV1, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"CLIONEACMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="toolsed1")]]
    await event.edit(CLIONEACMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIBACK")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="toolsed1")]]
    await event.edit(ALIBACK, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"KSHFCMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="toolsed1")]]
    await event.edit(KSHFCMD, buttons=buttons, link_preview=False)


#
@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ADDTKLED")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="toolsed1")]]
    await event.edit(ADDTKLED, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"STOPAZAG")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="toolsed1")]]
    await event.edit(STOPAZAG, buttons=buttons, link_preview=False)


##


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TASLIACMD")))
@check_owner
async def _(event):
    buttons = [
        [
            Button.inline("الترفيه", data="TRFEHCMD"),
            Button.inline("التسلية", data="TSLEACMD"),
        ],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TSLEACMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TASLIACMD")]]
    await event.edit(TSLEACMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TRFEHCMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="TASLIACMD")]]
    await event.edit(TRFEHCMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"admincmd_s")))
@check_owner
async def _(event):
    buttons = [
        [
            Button.inline("حظر", data="bancmd"),
            Button.inline("الغاء حظر", data="unbancmd"),
            Button.inline("المحظورين", data="ALIVEMHA"),
        ],
        [
            Button.inline("كتم", data="ALIVEcatm"),
            Button.inline("الغاء كتم", data="unmutecmd"),
            Button.inline("طرد", data="KICKCMD"),
        ],
        [
            Button.inline("تثبيت", data="ALIVEbin"),
            Button.inline("الغاء التثبيت", data="ALIVEunbin"),
            Button.inline("رفع ادمن", data="ALIVEadmin"),
        ],
        [Button.inline("⌫", data="admin2"), Button.inline("⌦", data="ADMSS4")],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"admin2")))
@check_owner
async def _(event):
    buttons = [
        [
            Button.inline("تنزيل ادمن", data="ALIVEtnadmin"),
            Button.inline("وضع صورة", data="ALIVEsod"),
            Button.inline("حذف الصورة", data="ALIVESOR"),
        ],
        [
            Button.inline("تفليش", data="ALIVETFL"),
            Button.inline("الاحداث", data="ALIVEADV"),
            Button.inline("صلاحيات المجموعة", data="GROUPHP"),
        ],
        [
            Button.inline("الحظر العام", data="GADMIN"),
            Button.inline("الحظر المؤقت", data="TADMIN"),
        ],
        [
            Button.inline("الكتم العام", data="GMUTE"),
            Button.inline("الكتم المؤقت", data="TMUTE"),
        ],
        [
            Button.inline("ادمن عام", data="ALIVErfe"),
            Button.inline("ازاله ادمن عام", data="ALIVEnzl"),
        ],
        [
            Button.inline("⌫", data="admi3"),
            Button.inline("⌦", data="admincmd_s"),
        ],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=buttons, link_preview=False)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"GROUPHP")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admin2")]]
    await event.edit(GROUPHP, buttons=buttons, link_preview=False)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVETFL")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVETFL, buttons=buttons, link_preview=False)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"GADMIN")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admin2")]]
    await event.edit(GADMIN, buttons=buttons, link_preview=False)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TADMIN")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admin2")]]
    await event.edit(TADMIN, buttons=buttons, link_preview=False)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"GMUTE")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admin2")]]
    await event.edit(GMUTE, buttons=buttons, link_preview=False)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"TMUTE")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admin2")]]
    await event.edit(TMUTE, buttons=buttons, link_preview=False)

@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"admi3")))
@check_owner
async def _(event):
    buttons = [
        [
            Button.inline("", data=""),
            Button.inline("", data=""),
            Button.inline("اضافة ترحيب", data="ALIVETRSB"),
        ],
        [
            Button.inline("ايقاف الترحيب", data="ALIVEundf"),
            Button.inline("الترحيبات", data="ALIVETRS"),
            Button.inline("منع كلمة", data="ALMN3CMD"),
        ],
        [
            Button.inline("الغاء منع", data="A3ALMN3"),
            Button.inline("قائمة المنع", data="LISTBLCK"),
            Button.inline("مسح المحظورين", data="UMBLCTR"),
        ],
        [Button.inline("⌫", data="ADMSS4"), Button.inline("⌦", data="admin2")],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALMN3CMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admi3")]]
    await event.edit(ALMN3CMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ADMSS4")))
@check_owner
async def _(event):
    buttons = [
        [
            Button.inline("اضافة رد", data="RDAJFDA"),
            Button.inline("ايقاف رد", data="RSTOPRD"),
            Button.inline("حذف الردود", data="ALLRDSTOP"),
        ],
        [
            Button.inline("الردود", data="ALLRD5"),
            Button.inline("احصائيات", data="ALMSHRFE1"),
            Button.inline("اطردني", data="MELICLW"),
        ],
        [
            Button.inline("المحذوفين", data="ACCD5SS"),
            Button.inline("", data=""),
        ],
        [
            Button.inline("⌫", data="admincmd_s"),
            Button.inline("⌦", data="admi3"),
        ],
        [Button.inline("القائمة الرئيسية", data="MAIN")],
    ]
    await event.edit(ROE, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ACCD5SS")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(ACCD5SS, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALMSHRFE1")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(ALMSHRFE1, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVETRS")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(ALIVETRS, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"MELICLW")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(MELICLW, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALLRD5")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(ALLRD5, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALLRDSTOP")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(ALLRDSTOP, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"RSTOPRD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(RSTOPRD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"RDAJFDA")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="ADMSS4")]]
    await event.edit(RDAJFDA, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"UMBLCTR")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admi3")]]
    await event.edit(UMBLCTR, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"LISTBLCK")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admi3")]]
    await event.edit(LISTBLCK, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"A3ALMN3")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admi3")]]
    await event.edit(A3ALMN3, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVETRS")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admi3")]]
    await event.edit(ALIVETRS, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEundf")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admi3")]]
    await event.edit(ALIVEundf, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVETRSB")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admi3")]]
    await event.edit(ALIVETRSB, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVETSV")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admi3")]]
    await event.edit(ALIVETSV, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEunTHR")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admi3")]]
    await event.edit(ALIVEunTHR, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVETHR")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVETHR, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEgma")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVEgma, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEADV")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVEADV, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVErfe")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVErfe, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEnzl")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVEnzl, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVESOR")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVESOR, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEsod")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVEsod, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEtnadmin")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admin2")]]
    await event.edit(ALIVEtnadmin, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEbin")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEbin, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEunbin")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEunbin, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEadmin")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEadmin, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"KICKCMD")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(KICKCMD, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEMHA")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEMHA, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"bancmd")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEBand, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"unbancmd")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEunban, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"ALIVEcatm")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEcatm, buttons=buttons, link_preview=False)


@sbb_b.tgbot.on(CallbackQuery(data=re.compile(rb"unmutecmd")))
@check_owner
async def _(event):
    buttons = [[Button.inline("رجوع", data="admincmd_s")]]
    await event.edit(ALIVEuncatm, buttons=buttons, link_preview=False)
