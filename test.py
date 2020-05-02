import telebot
from telebot import types


bot = telebot.TeleBot(token='785582164:AAEKvyMN6TG53HVPiBgLvlXVYR_VdTD5ZXk')


@bot.channel_post_handler(func=lambda message: message.text == 'send')
def some(message: types.Message):
    some = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(
        text='asd', url='https://core.telegram.org/bots/api#message')
    some.add(btn)
    bot.send_message(message.chat.id, text='Lorem ipsum dolor sit amet consectetur adipisicing elit. Mollitia sint commodi dolores consequatur optio. Aut omnis fugit consequatur temporibus a neque architecto. Animi ipsa corrupti officiis. Ipsam nostrum aspernatur praesentium mollitia voluptates deserunt itaque quas delectus, nobis culpa veniam in sapiente quaerat inventore suscipit nisi hic cumque quae dolorum vitae, quos harum. Itaque quam mollitia ipsam enim et eius architecto eveniet quos ex facilis adipisci, dicta recusandae corrupti neque praesentium error est, nisi incidunt. Iste asperiores laudantium beatae incidunt iusto minima consequatur nemo accusantium veritatis aliquid enim, quisquam adipisci, magni, quam similique? Natus aut suscipit voluptates reiciendis hic vero, quia deleniti delectus impedit perspiciatis quas doloremque laborum explicabo doloribus sequi nisi beatae reprehenderit quasi libero id non pariatur sapiente ullam. Ipsum, voluptatem architecto unde ab maiores ducimus veniam, necessitatibus enim deleniti, eum officia deserunt quos perspiciatis! Molestiae ut impedit veniam quis quam, numquam facilis at beatae aspernatur rem, dolorem harum voluptatibus pariatur corporis quasi autem cum commodi repudiandae, culpa odio dignissimos? Modi impedit ipsa voluptates. Rerum ea harum suscipit deserunt ab incidunt laboriosam, in consectetur sequi. Corporis nostrum magnam amet eum placeat magni reiciendis earum dicta sint nesciunt exercitationem blanditiis, explicabo quis quam perspiciatis, fugiat tenetur ab optio recusandae accusantium?', reply_markup=some)


bot.polling(none_stop=True)
