import telebot

TOKEN = "1749510446:AAHxNInkX-ItzJN5OTf4z8_Y5trQTR3mZLc"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, \ c{message.chat.username}")

@bot.message_handler(content_types=['photo'])
def nice_meme(message:telebot.types.Message):
    bot.reply_to(message, 'Nice meme lol')

bot.polling()