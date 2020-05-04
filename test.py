import telebot
from telebot import types


bot = telebot.TeleBot(token='785582164:AAEKvyMN6TG53HVPiBgLvlXVYR_VdTD5ZXk')


@bot.channel_post_handler(func=lambda message: message.text == 'send')
def some(message: types.Message):
    some = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(
        text='asd', url='https://core.telegram.org/bots/api#message')
    some.add(btn)
    foto = open('sierra-mac-apple-os-x-gory.jpg', 'rb')
    bot.send_photo(chat_id=message.chat.id, photo=foto,
                   caption='Lorem ipsum dolor sit amet consectetur adipisicing elit. ', reply_markup=some)


bot.polling(none_stop=True)
