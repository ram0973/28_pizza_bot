import os
import telebot
from telebot import apihelper
from jinja2 import Template
from app.models.catalog import Pizza
from app import create_app

BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise Exception('Bot token not set')
# {'https':'socks5://userproxy:password@proxy_address:port'}
# we using Tor proxy service: https://www.torproject.org/
PROXY = {'https': 'socks5://127.0.0.1:9050'}
GREETINGS_TEMPLATE = 'app/templates/bot/greetings.md'
CATALOG_TEMPLATE = 'app/templates/bot/catalog.md'
ORDER_TEMPLATE = 'app/templates/bot/order.md'


def pizza_catalog_bot():

    app = create_app(os.getenv('FLASK_ENV') or 'default')

    apihelper.proxy = PROXY
    bot = telebot.TeleBot(BOT_TOKEN)

    with open(CATALOG_TEMPLATE, 'r', encoding='utf8') as catalog_file:
        catalog_template = Template(catalog_file.read())

    with open(GREETINGS_TEMPLATE, 'r', encoding='utf8') as greetings_file:
        greetings_template = Template(greetings_file.read())

    with open(ORDER_TEMPLATE, 'r', encoding='utf8') as order_file:
        order_template = Template(order_file.read())

    @bot.message_handler(commands=['start'])
    def greet(message):
        bot.send_message(message.chat.id, greetings_template.render())

    @bot.message_handler(commands=['menu'])
    def show_catalog(message):
        app.app_context().push()
        pizzas = Pizza.query.all()
        bot.send_message(message.chat.id,
                         catalog_template.render(pizzas=pizzas),
                         parse_mode='Markdown')

    @bot.message_handler(commands=['order'])
    def order_pizza(message):
        app.app_context().push()
        pizza_ids = message.text.split()[1:]
        # pizza ids processes correctly even if we have incorrect input
        pizzas = Pizza.query.filter(Pizza.id.in_(pizza_ids)).all()
        if pizzas:
            order_total = sum(pizza.price for pizza in pizzas)
            bot.send_message(message.chat.id,
                             order_template.render(pizzas=pizzas,
                                                   order_total=order_total),
                             parse_mode='Markdown')

    bot.polling(none_stop=True)
