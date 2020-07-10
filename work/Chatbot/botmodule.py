from slackbot.bot import respond_to
from slackbot.bot import listen_to

@respond_to("こんにちわ")
def greeting_1(messge):
    messge.reply("こんにちわ!")

@listen_to("コンニチワ")
def greeting_2(messge):
    messge.reply("コンニチワ")


@listen_to("くんにちわ")
def greeting_3(messge):
    messge.reply("ボクはキリンです")