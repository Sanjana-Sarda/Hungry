import requests
from bs4 import BeautifulSoup
import json

def min_price (product, ratings, stores, quantity):
    val = 0
    for store in stores:
        if (store=='Walmart'):
            headers = {
                'Host': 'www.walmart.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
            }   

            params = (
                ('q', product),
            )

            url = 'https://www.walmart.com/search'
            html_text = requests.get(url, headers=headers, params=params, verify=True).text
            soup = BeautifulSoup(html_text, 'html.parser')
            scripts =  soup.find_all('script')
            for a in range (30, 45):
                if (len(scripts[a])==1 and len(scripts[a].contents[0])>10000):
                    val = a
                    break
            match = json.loads(soup.find_all('script')[val].contents[0])['props']['pageProps']['initialData']['searchResult']['itemStacks'][0]['items'][0]
            #unitprice = match['unitprice']
            print (match['priceInfo'])#['unitPrice'])
    return ...

product = 'sugar'
stores = ['Walmart']
quantity = "1 lb"
ratings = []
print(min_price(product, ratings, stores, quantity))