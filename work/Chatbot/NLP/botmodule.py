from slackbot.bot import respond_to
from slackbot.bot import listen_to
import csv

@respond_to("こんにちわ")
def greeting_1(messge):
    messge.reply("こんにちわ!")

@listen_to("コンニチワ")
def greeting_2(messge):
    messge.reply("コンニチワ")


@listen_to("くんにちわ")
def greeting_3(messge):
    messge.reply("ボクはキリンです")

@respond_to("Give me (.*)")
def Create_nlp_tasks(message, params):
    #channel_id = message.channel._body("name")
    #print(channel_id)
    text = message.body["text"]
    options = []
    for i,v in enumerate(params):
        options.append
    send_user = message.channel._client.users[message.body['user']][u'name']
    print(text)
    message.send("Your message is {}".format(params))
    args = [row for row in csv.reader([params], delimiter='　')][0]
    message.send(args[0])
    print(args)