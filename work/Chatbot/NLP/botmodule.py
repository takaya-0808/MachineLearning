from slackbot.bot import respond_to
from slackbot.bot import listen_to
import csv
from slacker import Slacker
import slackbot_settings
import requests
import json
import markdown

post_list = []

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



@respond_to("nlp_post (.*)")
def NlpPost(message, params):

    send_user = message.channel._client.users[message.body['user']][u'name']
    args = [row for row in csv.reader([params], delimiter=' ')][0]
    cmd = args.pop(0)
    
    if cmd == "-h":
        msg = HelpPost()
    elif cmd == "-r":
        ReadPost()
    elif cmd == "w":
        args.append(send_user)
        Writepost(args)
    elif cmd == "u":
        UpdatePost()
    else:
        message.reply(slackbot_settings.DEFAULT_REPLY)

    post_url = "https://slack.com/api/chat.postMessage"
    channel = "# general"
    msg = [
        {
            "title": "NLPタスク研　発表宣言",
            "title_link": "https://docs.google.com/presentation/u/1/d/1lOhvruuxl1RiOZ_X5I5dhWuippm8Ay4_/edit#slide=id.g8c3f507bc5_0_10",  
            "color": "#3104B4",
            "fields": [
                {
                    "title": "担当者名",
                    "value": send_user
                },
                {
                    "title": "タスク・分野名",
                    "value": "hoge"
                },
                {
                    "title": "version",
                    "value": "hoge"
                },
                {
                    "title": "コメント",
                    "value": "hoge"
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

    msg = [
        {
            "title": "NLPタスク研　発表宣言",
            "title_link": args[3],  
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
def ReadPost():

def UpdatePost():



@respond_to("nlp-list")
def Show_nlp_task(message):
    for i in range(len(post_list)):
        message.reply_webapi(attachments=i)

"""
@respond_to("nlp_hoge")
def markdown(message):
    text = '''
    # 【第9回】自然言語タスク研究会
    ##############################################################
    - 今週の会に投稿したい人は、
        1. ↓ :hand: を押して下さい！
        2. *Survey予定のタスク・分野名* を返信 して下さい。
        - 〆切： 来週の水曜日 までに、
        3. Google Drive に「元データ」「PDF」の アップロードお願いします。
        4. このチャンネルに、【Survey 結果】 (テンプレ)    を投稿して下さい。
    - 今週の会で 発表 したい人は、
        1.　↓ :microphone: を押して下さい！
            - 日曜 〆切。
            -  Microsoft Teams で行います。
            - 日〜水曜 の間で １時間くらいの予定。
        2. 発表予定者は、来週の予定を ↓に入力お願いします...。
            - Google スプレッドシート 
                - 参加できない時間帯に名前を書く。
    ############################################################## 
    '''
    slack = Slacker(slackbot_settings.API_TOKEN)

    #md = markdown.Markdown() # ---(*1)
    #html = md.convert(text) # ---(*2)
    #print(html)
    slack.chat.post_message('# general' text, as_user=True)
"""