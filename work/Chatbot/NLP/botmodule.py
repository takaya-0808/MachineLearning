from slackbot.bot import respond_to
from slackbot.bot import listen_to
import csv
from slacker import Slacker
import slackbot_settings
import requests
import json

"""
@respond_to("こんにちわ")
def greeting_1(messge):
    messge.reply("こんにちわ!")

@listen_to("コンニチワ")
def greeting_2(messge):
    messge.reply("コンニチワ")

@listen_to("くんにちわ")
def greeting_3(messge):
    messge.reply("ボクはキリンです")
"""

@respond_to("Give me (.*)")
def Create_nlp_tasks(message, params):

    send_user = message.channel._client.users[message.body['user']][u'name']
    args = [row for row in csv.reader([params], delimiter='　')][0]
    
    post_url = "https://slack.com/api/chat.postMessage"
    channel = "# general"
    msg = [
        {
            "color": "#3104B4",
            "fields": [
                {
                    "title": "担当者名",
                    "value": send_user
                },
                {
                    "title": "タスク・分野名",
                    "value": args[0]
                },
                {
                    "title": "時間",
                    "value": args[1]
                }
            ]
        }
    ]

    payload = {
        "token": slackbot_settings.API_TOKEN,
        "channel": channel,
        "attachments": json.dumps(msg)
    }
    res = requests.post(post_url, data=payload)
    #message.send_webapi("NLPタスク研:", json.dumps(msg))