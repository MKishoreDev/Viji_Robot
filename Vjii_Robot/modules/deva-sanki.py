import asyncio
import os
import requests
import datetime
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom, version
from Vjii_Robot.events import register
from Vjii_Robot import telethn as borg
from Vjii_Robot import StartTime, dispatcher
from Vjii_Robot.modules.helper_funcs.chat_status import dev_plus
from telethon.tl.types import ChannelParticipantsAdmins

edit_time = 5
""" =======================deva====================== """
file1 = "https://telegra.ph/file/9c6af9e3ff7d8f79401ff.jpg"
file2 = "https://telegra.ph/file/6dd2657a06adc333a2233.jpg"
file3 = "https://telegra.ph/file/f66bc2e78216218a807e8.jpg"
file4 = "https://telegra.ph/file/b95ab1317155821c08385.jpg"
file5 = "https://telegra.ph/file/1e1b256fa78b2b8496cd9.jpg"
""" =======================deva====================== """

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@borg.on(events.NewMessage(from_users=[5078096037], pattern="^/deva ?(.*)"))
async def hmm(yes):
    chat = await yes.get_chat()
    x = await yes.get_reply_message()
    name = x.sender.first_name if yes.is_reply else yes.sender.first_name
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    omega = "**Try To Reply Your Lover ✨🥀**"
    love = "https://telegra.ph/file/8e6536dcd782e4710c985.mp4"
    if not yes.is_reply:
        await borg.send_file(yes.chat_id, file=love, caption=omega)
        return

    pm_caption = f"** ♡ I Love You {name}**\n\n"
    pm_caption += f"**♡ My Heart Is For You ✨🥀**\n\n"
    pm_caption += f"**♡ Be My GirlFriend 💕**\n\n"
    pm_caption += f"**♡ Your Boyfriend :** {yes.sender.first_name} 🥺"
    on = await borg.send_file(yes.chat_id, file=file1, caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2)

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file4)

    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file5)

    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file1)

    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file2)

    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file3)

    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok7, file=file4)

    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(yes.chat_id, ok8, file=file5)
