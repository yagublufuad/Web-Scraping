from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse
import os

from time import time
from time import sleep


'''
The script showcases an example of web scraping utilizing the Python API of a website dedicated to real-time tracking of cryptocurrency fluctuations. 
The website, named CoinMarketCap, can be accessed via the following link: https://coinmarketcap.com/api/.
The scripts requires following arguments: URL to the webpage the lists fluctuations, the number of currencies to be retrieved, API key, path to the csv file to write the fluctuations, the number of iteration and the frequency of retrievals.

The API key could be generated after creating an account. A key could be used 333 times a day.
'''

def api_runner(url,limit,api_key,csv_file):
    global df
    parameters = {
      'start':'1',
      'limit':str(limit),
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': api_key,
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)

    df2 = pd.json_normalize(data['data'])
    df2['Timestamp'] = pd.to_datetime('now')
    df = df.append(df2)

    # Checking if the CSV file already exists
    if not os.path.isfile(csv_file):
        df.to_csv(csv_file, header='column_names')
    else:
        df2.to_csv(csv_file, mode='a', header=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Amazon Web Scraping')
    parser.add_argument('--url', type=str,required=True,default="https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
                        help='URL to the webpage the lists fluctuations')
    parser.add_argument('--limit', type=int,required=True,
                        help='The number of currencies to be listed')                    
    parser.add_argument('--api_key', type=str,required=True,
                        help='API key')
    parser.add_argument('--csv_file', type=str,required=True,
                        help='Path to the CSV to write tracked prices')                        
    parser.add_argument('--num_iterations', type=int,required=True,
                        help='The number of iterations')                        
    parser.add_argument('--sleep_duration_minutes', type=float,required=True,
                        help='Frequency by which the price should be checked (The unit is minutes)')                        
    
    args = parser.parse_args()
    
    # Creating an empty dataframe to append the retrieved data
    df=pd.DataFrame()
        
    for i in range(args.num_iterations):
        api_runner(args.url,args.limit,args.api_key,args.csv_file)
        print('API Runner completed')
        sleep(args.sleep_duration_minutes * 60) #sleep for 30 minute
    exit()