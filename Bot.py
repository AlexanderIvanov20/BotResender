from Resender.models import MessageGroup, MessageChannel
import telebot
from telebot import types
import os
import django
from datetime import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BotSender.settings')
django.setup()

bot = telebot.TeleBot(token='1077949754:AAGTCrVh6NpXWIM-R7Rez4SHcCx5mM6aXck')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_creds(message: types.Message):
    user_id = message.from_user.id
    name = f'{message.from_user.first_name} {message.from_user.last_name}'
    username = message.from_user.username
    date_message = message.date
    return user_id, name, username, date_message


@bot.message_handler(content_types=['photo', 'document'])
def get_message_with_photo(message: types.Message):
    file_id = message.photo[1].file_id
    file = bot.get_file(file_id)
    downloaded_file = bot.download_file(file.file_path)

    user_id, name, username, date_message = get_creds(message)
    current_message = MessageGroup.objects.create(
        user_id=user_id,
        name=name,
        username=username,
        date=date_message
    )
    with open(os.path.join(BASE_DIR, 'BotResender', 'BotSender', 'media',
                           'photos', f'{file_id}.png'), 'wb') as new_file:
        new_file.write(downloaded_file)

    if message.caption is not None:
        caption = message.caption
        current_message.text = caption
        print(caption)
    current_message.save()


@bot.message_handler(content_types=['text'])
def get_mesage(message: types.Message):
    text = message.text

    user_id, name, username, date_message = get_creds(message)
    current_message = MessageGroup.objects.create(
        user_id=int(user_id),
        name=name,
        username=username,
        date=datetime.fromtimestamp(date_message),
        text=text
    )
    print(text)


@bot.channel_post_handler(content_types=['photo', 'document'])
def get_message_with_photo(message: types.Message):
    file_id = message.photo[1].file_id
    file = bot.get_file(file_id)
    downloaded_file = bot.download_file(file.file_path)

    current_message = MessageChannel.objects.create(
        date=message.date,
        message_id=message.message_id
    )
    with open(os.path.join(BASE_DIR, 'BotResender', 'BotSender', 'media',
                           'photos', f'{file_id}.png'), 'wb') as new_file:
        new_file.write(downloaded_file)

    if message.caption is not None:
        caption = message.html_caption
        current_message.text = caption
        print(caption)
    current_message.save()


@bot.channel_post_handler(content_types=['text'],
                          func=lambda message: message.text != 'send')
def get_mesage(message: types.Message):
    text = message.html_text
    date = message.date
    message_id = message.message_id

    current_message = MessageChannel.objects.create(
        date=message.date,
        message_id=message.message_id,
        text=text
    )

    if 'reply_markup' in message.json:
        current_message.url = message.json[
            'reply_markup']['inline_keyboard'][0][0]['url']
    current_message.save()


bot.polling(none_stop=True)
