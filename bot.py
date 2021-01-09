import telebot

import bot_loading_utils

aps = bot_loading_utils.aps_bot()

bot = telebot.TeleBot(aps.token)

@bot.message_handler(func = lambda message: message.text[0]=='/')
def command_parse(message):
    print('command_parse: ', ' from: ', message.chat.first_name,' command: ', message.text, ' text: ',aps.parse_command(message.text)[0] )
    print(aps.bot_commands.keys())
    bot.send_message(message.chat.id, aps.parse_command(message.text)[0])
    

@bot.message_handler()
def message_parse(message):
    print('message_parse: ',message.text, ' from: ', message.chat.first_name)
    bot.send_message(message.chat.id, str(aps.parse_text(message.text)))

bot.polling()
