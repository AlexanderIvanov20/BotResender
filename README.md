# BotResender
A bot that broadcasts messages from a channel and a group to the site. The bot is developed in the Python programming language using the pyTelegramBotAPI module.

The bot takes into account: the presence of a picture in a message (saves it to the database), records the sender of the message from whom the message was forwarded (forward), shows if the message was in response to another (reply), etc.

Admin panel - implemented on the Django framework. The backend is responsible for storing and managing images, displaying a certain number (set in the form) of messages on the site.
