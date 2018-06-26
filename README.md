# Telegram Bot for Pizzeria

<img src="https://github.com/ram0973/28_pizza_bot/blob/master/screenshot.png"
width="476" height="417">

This application written in Python 3 for a small Pizzeria shop.

Application implements:
1) The admin area in which worker of pizzeria can add and edit
 pizza assortment;
2) [Telegram](https://telegram.org/) bot, which allow customer to see
the pizzeria menu and calculate the cost of the order.

The admin panel protected with
[HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication).
Application have 2 databases: Pizza and Size, the first store assortment
of pizzeria, the second - standard pizza sizes. Database stored
in the Sqlite database.

# Setup: Linux/Windows
```bash
$ git clone https://github.com/ram0973/28_pizza_bot
$ cd 28_pizza_bot
$ python3 -m venv ./venv # Windows: python -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt # Windows: pip install ...
$ # Windows: set instead of export
$ export FLASK_ENV=development
$ export SECRET_KEY='SOME_KEY'
$ export AUTH_USERNAME='some_admin_username' # needed for admin page
$ export AUTH_PASSWORD='some_admin_password' # needed for admin page
$ # export DATABASE_URL or DEV_DATABASE_URL if you need
$ flask database drop
$ flask database seed
$ # deactivate
```

# How to Use

Step 1. We will use socks5 proxy

Install and run Tor proxy, by default it will run on 127.0.0.1:9050:

[On Linux](https://www.torproject.org/docs/debian)
[On Windows](https://www.torproject.org/docs/faq#NTService)

Or you can also use other SOCKS5 proxies, just change PROXY setting
in:
```
# app/bot/__init__.py:
PROXY = {'https': 'socks5://127.0.0.1:9050'}
```

Step 2. Register new telegram bot for development purposes, get the new
token: [@BotFather](https://telegram.me/botfather)

(If you can't view this page, use Tor browser, or just find and add
@botfather in Telegram, then enter command: /newbot)

```
$ # the token below is not actual, you need to register a new one
$ # Windows: set instead of export
$ export BOT_TOKEN="110831855:AAE_GbIeVAUwk11O12vq4UeMnl20iADUtM"
```

Step 3. Launch for view admin page
```
$ flask run
```
Then open http://127.0.0.1:5000/

Step 4. Launch for Telegram bot running
```
$ flask telegram_bot
```
Open Telegram app, go to your bot's page, and write commands:
```
/start - Greetings
/menu - Pizzeria menu
/order 1 3 4 - List ordered pizzas and calculate total price
```

# Play with flask shell

```bash
$ flask shell
>>> pprint(dir(db))
>>> pprint(Pizza.query.all())
>>> pprint(Size.query.all())
>>> exit()
```

# Tests
```bash
$ flask tests
```

# Extra info
You can use these tools with Sqlite db:

[Sqlite console app](https://www.sqlite.org/download.html)

[Desktop Sqlite DB Browser](http://sqlitebrowser.org/)

# Project Goals

The code is written for educational purposes.
Training course for web-developers - [DEVMAN.org](https://devman.org)

