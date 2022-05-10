# 11 May 2022
# Author: Nasir Hossain Akash
# Python 3.10.4
# Pyrogram Session String Generator


from os import remove
import re
from pyrogram import Client 

API_ID = int(input("Your Telegram API_ID: "))
API_HASH = input("Your Telegram API_HASH: ")

app = Client(name="bot2",api_id=API_ID,api_hash=API_HASH)
app.start()
s = app.export_session_string()
app.send_message('me',s)
print("**Your Session String Generated***")
print("***Check Saved Message***")
remove('bot2.session')

