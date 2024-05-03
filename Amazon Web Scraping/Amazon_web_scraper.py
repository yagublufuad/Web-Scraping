from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime
import csv
import pandas
import argparse
import os

'''
The script demonstrates a simple example for Web Scraping for Amazon Website. With the link of an arbitrary item, we are tracking the price and writing to a CSV file.
The frequency of checking the price could be specified by the user.
The scripts requires three arguments: URL of the desired item, user agent, and path to the csv file to write the tracked prices.

One can access the unique user agent using https://httpbin.org/get.
'''

def check_price(URL,user_agent,csv_file):

    while(True):
        headers = {"User-Agent": user_agent, "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
        page = requests.get(URL, headers=headers)
        soup1 = BeautifulSoup(page.content, "html.parser")
        soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
        title = soup2.find(id='productTitle')
        price = soup2.find(id='priceblock_ourprice')
        if title and price:
            title = title.get_text()
            price = price.get_text()
            break

    price = price.strip()[1:]
    title = title.strip()

    current_date_time = datetime.datetime.now()

    formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M")

    header = ['Title', 'Price', 'Date']
    data = [title, formatted_date_time]
    
    if not os.path.exists(csv_file):
        write_mode = 'w'
    else:
        write_mode = 'a+'
        
    with open(csv_file, write_mode, newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        if write_mode == 'w':
            writer.writerow(header)
        writer.writerow(data)


        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Amazon Web Scraping')
    parser.add_argument('--URL', type=str,required=True,
                        help='URL of the Amazon item that needs to be tracked')
    parser.add_argument('--user_agent', type=str,required=True,
                        help='User agent could be accessed with https://httpbin.org/get')                    
    parser.add_argument('--csv_file', type=str,required=True,
                        help='path to the CSV that holds the list of prices tracked by the script')
    parser.add_argument('--period_T', type=int,required=True,
                        help='Frequency by which the price should be checked (The unit is seconds)')                        
    
    args = parser.parse_args()
    while(True):
        check_price(args.URL,args.user_agent,args.csv_file)
        time.sleep(args.period_T)
    
        
        