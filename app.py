from flask import Flask
from flask import Flask, render_template
import config
from binance.client2 import Client

app = Flask(__name__)
client = Client(config.API_KEY, config.SECRET_KEY)

@app.route('/')
def index():
    coinfuturesbal = client.coinfutures_account_balance()
    usdfuturesbal = client.futures_account_balance()
    return render_template('index.html', my_coinbalances=coinfuturesbal, my_usdbalances=usdfuturesbal)

@app.route('/buy')
def buy():
    return 'buy'

@app.route('/sell')
def sell():
    return 'sell'

