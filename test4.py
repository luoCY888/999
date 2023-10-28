import requests
from binance.client import Client
from time import sleep
client = Client()
while True:
        klines = client.futures_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1MINUTE)
        nowline = klines[-1]
        sleep(1)
        block = float(nowline[2])- float(nowline[3])
        print(block)
        if block > 100:
            dataT = {'value1': 'price - change',
                     'value2': '>100'}
            ifttt_event_url = 'https://maker.ifttt.com/trigger/btc2telegrame/with/key/dONbHcmrzbt2X-IjlflpAr'
            requests.post(ifttt_event_url, json=dataT)
            sleep(60)







