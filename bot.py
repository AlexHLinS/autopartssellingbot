import telebot

import bot_loading_utils

aps = bot_loading_utils.aps_bot()

bot = telebot.TeleBot(aps.token)

@bot.message_handler(func = lambda message: message.text[0]=='/')
def command_parse(message):
    print('command_parse: ', ' from: ', message.chat.username,' command: ', message.text)
    

@bot.message_handler()
def message_parse(message):
    print('message_parse: ',message.text, ' from: ', message.chat.username)


bot.polling()
