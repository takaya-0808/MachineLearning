from slackbot.bot import respond_to
from slackbot.bot import listen_to
import csv
from slacker import Slacker
import slackbot_settings
import requests
import json

post_list = []

@respond_to("nlp_help")
def Help_nlp(message):
    msg = [
        {
            "fields": [
                {
                    "value": "`nlp_post args[0] args[1] args[2] args[3] args[4]`\n args[0] = *タスク・分野*\n args[1] = *version*\n args[2] = *保存先URL*\n args[3] = *コメント*\n args[4] = *投稿時間*"
                }
            ]
        }
    ]
    message.reply_webapi("",
                        attachments=msg,
                        as_user=True,
                        in_thread=False)



@respond_to("nlp_post (.*)")
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
    post_list.append(msg)

    payload = {
        "token": slackbot_settings.API_TOKEN,
        "channel": channel,
        "attachments": json.dumps(msg)
    }
    res = requests.post(post_url, data=payload)


@respond_to("nlp-list")
def Show_nlp_task(message):
    for i in range(len(post_list)):
        message.reply_webapi(attachments=i)
