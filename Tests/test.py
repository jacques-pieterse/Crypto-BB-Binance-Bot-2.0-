from binance.client2 import Client
import config
from threading import Timer

client = Client(config.API_KEY, config.SECRET_KEY)

def getdata(value):
    if value == 'coin':
        coin = client.coinfutures_account_balance()
        return coin
    
    if value == 'futures':
        futures = client.futures_account_balance()
        return futures

    if value == 'cointrade':
        cointrade = client.coinfutures_position_information()
        return cointrade

    if value == 'cointrade':
        futurestrade = client.coinfutures_position_information()
        return futurestrade
    Timer(5, getdata).start

coin = getdata('coin')
futures = getdata('futures')
cointrade = getdata('cointrade')
futurestrade = getdata('futurestrade')

def display():
    print(coin)
    print(futures)
    print(cointrade)
    print(futurestrade)
    Timer(5, display).start


