import pandas as pd
import requests
import datetime

class API:
    API_URL = 'https://api.coingecko.com/api/v3/coins/{}/market_chart?vs_currency={}&days={}&interval=daily'

    def fetchData(self, coin, currency, days):
        req = requests.get(self.API_URL.format(coin, currency, days))
        if req.status_code == 200:
            res = req.json()
            prices = res['prices']
            data = {}

            for i in prices:
                data[i[0]] = i[1]
            
            df = pd.DataFrame(data.items(), columns=['time', currency.upper()])
            df['time'] = pd.to_datetime(df['time'], unit="ms")
            df.set_index("time", inplace=True)
            return df
        else:
            return None