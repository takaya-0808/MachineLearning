from slackbot.bot import respond_to
from slackbot.bot import listen_to
import csv
from slacker import Slacker
import slackbot_settings
import requests
import json
import markdown

@respond_to("nlp_help")
def Help_nlp(message):
    msg = [
        {
            "fields": [
                {
                    "value": "`nlp_post args[0] args[1] args[2] args[3]`\n args[0] = *タスク・分野*\n args[1] = *version*\n args[2] = *コメント*\n args[3] = *保存先URL*"
                }
            ]
        }
    ]
    message.reply_webapi("",
                        attachments=msg,
                        as_user=True,
                        in_thread=False)


dict_post = {}                  
@respond_to("nlp_post (.*)")
def NlpPost(message, params):

    send_user = message.channel._client.users[message.body['user']][u'name']
    args = [row for row in csv.reader([params], delimiter=' ')][0]
    cmd = args.pop(0)
    print(cmd)
    post_url = "https://slack.com/api/chat.postMessage"
    channel = "# general"
    
    print(dict_post)
    if cmd == "-h":
        msg = HelpPost()

    elif cmd == "-r":
        channel_id = message.body['channel']
        channel_info = message.channel._client.channels[channel_id]
        channel = channel_info['name']
        msg = ReadPost(send_user)
    
    elif cmd == "-w":
        dict_post[send_user] = args
        args.append(send_user)
        msg = WritePost(args)

    elif cmd == "-u":
        
        UpdatePost()

    else:
        message.reply(slackbot_settings.DEFAULT_REPLY)

    payload = {
        "token": slackbot_settings.API_TOKEN,
        "channel": channel,
        "attachments": json.dumps(msg)
    }
    res = requests.post(post_url, data=payload)


def HelpPost():

    msg = [
        {
            "color": "#3104B4",
            "fields": [
                {
                    "value": "`nlp_post `\n -r : Read NLP_post's content\n -u : Update NLP_post's content\n -h : Help message\n -w : Write NLP_post' content"
                }
            ]
        }
    ]
    return msg

def WritePost(args):
    s = args[3]
    print(args)
    msg = [
        {
            "title": "NLPタスク研　発表宣言",
            "title_link": s[1:len(args[3])-1],  
            "color": "#3104B4",
            "fields": [
                {
                    "value": "担当者名",
                    "value": args[4]
                },
                {
                    "title": "タスク・分野名",
                    "value": args[0]
                },
                {
                    "title": "version",
                    "value": args[1]
                },
                {
                    "title": "コメント",
                    "value": args[2]
                }
            ]
        }
    ]

def ReadPost(name):

    dict_list = dict_post[name]
    print(dict_list)
    msg = [
        {
            "title": "NLPタスク研　発表宣言",
            "title_link": dict_list[3],  
            "color": "#3104B4",
            "fields": [
                {
                    "value": "担当者名",
                    "value": name
                },
                {
                    "title": "タスク・分野名",
                    "value": dict_list[0]
                },
                {
                    "title": "version",
                    "value": dict_list[1]
                },
                {
                    "title": "コメント",
                    "value": dict_list[2]
                }
            ]
        }
    ]
    return msg

def UpdatePost(args):
    pass    

