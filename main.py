import telebot
bot = telebot.TeleBot('6959537257:AAEKNIaE-i1l5cWO1uqCiYtzF0a6h78mUaY')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'НАЧНЕМ УБОРКУ, *ДРУЖОК*', parse_mode='Markdown')


@bot.message_handler(commands=['write'])
def main(message):
    bot.send_message(message.chat.id, 'я не скажу куда хозяйка спрятала твои вещи \nможет она сейчас за нами следит??!?!?!?!?!?')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'ЗВОНИ, ОНИ ПОМОГУТ - [112](https://tanki.su/)', parse_mode='Markdown')

bot.infinity_polling()