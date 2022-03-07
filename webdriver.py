from flask import Flask, jsonify
from threading import Thread
import asyncio
from getpass import getuser
from telethon import TelegramClient, sync
# from replit import db


api_id = '19592265'
api_hash = 'fe7694b2765e664c3d79337d5c496f5d'
channel_name = 'chegghero'

# client = TelegramClient('xxx', api_id, api_hash).start()

# get all the channels that I can access
# channels = {d.entity.username: d.entity
#             for d in client.get_dialogs()
#             if d.is_channel}

# # choose the one that I want list users from
# channel = channels[channel_name]

app = Flask('')


@app.route('/')
def home():
    return 'M GOOD'


def run():
    app.run(host="0.0.0.0", port=0000)


def keep_alive():
    Corona_borealis = Thread(target=run)
    Corona_borealis.start()


@app.route('/file')
def ping():
    return jsonify(data=list(db["joined"]))
