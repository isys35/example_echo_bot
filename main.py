import telebot

token = "5749201894:AAHNmzEsHeLEIaABJWH4sbEdDltn3hxCMzk"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start", "help"])
def welcome_message(message):
    bot.reply_to(message, "Добро пожаловать в Эхо бот")


@bot.message_handler(content_types=["text"])
def echo(message):
    result_messages = message.text.split(" ")
    for index, message_text in enumerate(result_messages):
        # 1-ое слово: <слово, из сообщения пользователя>
        index += 1
        result = f"{index}-ое слово: {message_text}"
        bot.send_message(message.from_user.id, result)



bot.infinity_polling()