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

    allcointrades = client.coinfutures_position_information()
    cointrades = allcointrades[10], allcointrades[24]

    
    return render_template('index.html', my_coinbalances=coinfuturesbal, my_usdbalances=usdfuturesbal, my_cointrades=cointrades)

@app.route('/coin-data')
def coindata():
    coinfuturesbal = client.coinfutures_account_balance()

    allcointrades = client.coinfutures_position_information()
    cointrades = allcointrades[10], allcointrades[24]


    return render_template('coin-data.html', my_coinbalances=coinfuturesbal, my_cointrades=cointrades)

@app.route('/usd-data')
def usddata():
    usdfuturesbal = client.futures_account_balance()

    return render_template('usd-data.html', my_usdbalances=usdfuturesbal)

@app.route('/buy')
def buy():
    return 'buy'

@app.route('/sell')
def sell():
    return 'sell'

