from slackbot.bot import respond_to
from slackbot.bot import listen_to
import csv
from slacker import Slacker
import slackbot_settings
import requests
import json
import markdown

dict_post = {}                  
@respond_to("nlp_post (.*)")
def NlpPost(message, params):

    args = [row for row in csv.reader([params], delimiter=' ')][0]
    cmd = args.pop(0)

    send_user = message.channel._client.users[message.body['user']][u'name']
    channel_id = message.body['channel']
    channel_info = message.channel._client.channels[channel_id]
    chl = channel_info['name']
    channel = "# general"

    if cmd == "-h":
        channel = chl
        msg = HelpPost()

    elif cmd == "-r":
        if not send_user in dict_post:
            message.reply(slackbot_settings.DEFAULT_REPLY)
            return 
        channel = chl
        msg = ReadPost(send_user)
    
    elif cmd == "-w":
        dict_post[send_user] = args
        args.append(send_user)
        msg = WritePost(args)

    elif cmd == "-u":
        if not send_user in dict_post:
            message.reply(slackbot_settings.DEFAULT_REPLY)
            return 
        
        msg = UpdatePost(args,send_user)

    else:
        message.reply(slackbot_settings.DEFAULT_REPLY)
        return

    payload = {
        "token": slackbot_settings.API_TOKEN,
        "channel": channel,
        "username": "nlp_bot_v2",
        "attachments": json.dumps(msg)
    }
    res = requests.post("https://slack.com/api/chat.postMessage", data=payload)


def HelpPost():

    msg = [
        {
            "color": "#3104B4",
            "fields": [
                {
                    "value": "`nlp_post`\n -r : Read NLP_post's content\n -u : Update NLP_post's content\n -h : Help message\n -w : Write NLP_post' content"
                }
            ]
        }
    ]
    return msg

def WritePost(args):

    return CreateJson(args)

def ReadPost(name):

    dict_list = dict_post[name]
    dict_list.append(name)
    return CreateJson(dict_list)

def UpdatePost(args,name):
    
    dict_list = dict_post[name]
    dict_list.append(name)

    for i in range(len(args)//2):
        cmd = args.pop(0)

        if cmd == "-T":
            dict_list[0] = args[0]
        elif cmd == "-V":
            dict_list[1] = args[0]
        elif cmd == "-C":
            dict_list[2] = args[0]
        else:
            pass
        args.pop(0)

    return CreateJson(dict_list)

def CreateJson(lists):

    s = lists[3]
    msg = [
        {
            "title": "NLPタスク研　発表宣言",
            "title_link": s[1:len(lists[3])-1], 
            "color": "#3104B4",
            "fields": [
                {
                    "title": "担当者名",
                    "value": lists[4]
                },
                {
                    "title": "タスク・分野名",
                    "value": lists[0]
                },
                {
                    "title": "version",
                    "value": lists[1]
                },
                {
                    "title": "コメント",
                    "value": lists[2]
                }
            ]
        }
    ]
    return msg
