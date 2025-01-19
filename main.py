import telebot

API_TOKEN = '7683347022:AAHSL_FH0p_jJjqU3H-4dzckKRSNA1QB14k'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text.lower() == "нет":
        bot.reply_to(message, "Підора атвєт.")
    if message.text.lower() == "да":
        bot.reply_to(message, "Підора єда")
    if message.text.lower() == "русский военный корабль":
        bot.reply_to(message, "Йди нахуй!")
    if message.text.lower() == "руский военый корабль":
        bot.reply_to(message, "Йди нахуй!")
    if message.text.lower() == "а":
        bot.reply_to(message, "хуй на.")
    if message.text.lower() == "не":
        bot.reply_to(message, "Рука в гавнє.")
    if message.text.lower() == "бля":
        bot.reply_to(message, "Фу, бля! Фу, бля! Фу, бля! Фу, бля! Мои opp'ы не знают валюты, кроме рубля Фу, бля! Фу, бля! Фу, бля! Фу, бля! Для них выход из бедности — это петля")


bot.polling(timeout=60, long_polling_timeout=60)
