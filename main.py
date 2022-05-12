# 10 May 2022
# Author: Nasir Hossain Akash
# Python 3.10.4



import redis
from os import getenv
from pyrogram import Client, filters
from dotenv import load_dotenv
import asyncio
import logging
logging.basicConfig(level=logging.INFO)



load_dotenv('config.env')





API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
SESSION = getenv("SESSION")
REDIS_URI = getenv("REDIS_URI")
REDIS_PASSWORD = getenv("REDIS_PASSWORD")
REDIS_URL = str(REDIS_URI).split(":")[0]
REDIS_PORT = str(REDIS_URI).split(":")[1]

r = redis.Redis(
    host=REDIS_URL,
    port=REDIS_PORT, 
    password=REDIS_PASSWORD)


app = Client(name="NoovosAFKBot",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)


def is_afk():
    if str(r.get(name="AFK"),"UTF-8")=="True":
        return True
    else:
        return False

def get_reason():
    reason = str(r.get(name="REASON"),"UTF-8")
    return reason

def set_reason(reason):
    r.set(name="REASON",value=reason)


@app.on_message(filters.me & filters.regex('^.afk'))
async def set_afk(client, message):
    reason = message.text.replace('.afk', """""").strip()
    r.set(name="AFK",value="True")
    set_reason(reason=reason)
    await message.edit(f"__Going AFK__\n__Reason: {reason}__\n\n__Made with ❤️ by__\n**__@NovoosEcosystem__**")
    await asyncio.sleep(2)
    await message.delete()

@app.on_message(filters.me & filters.text)
async def disable(client, message):
    r.set(name="AFK", value="False")



@app.on_message(filters.private)
async def afk(client, message):
    if is_afk():
        reason = get_reason()
        await message.reply(f"__Hello {message.chat.first_name}__\n__Currently I am AFK__\n__Reason: {reason}__\n\n**__Made with ❤️ by__**\n**__@NovoosEcosystem__** ")




app.run()
