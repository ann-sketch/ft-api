import requests, json,re
from bs4 import BeautifulSoup
from get_crypto_price import get_crypto_price

url = "https://top-nft-sales.p.rapidapi.com/sales/1d"

headers = {
    'x-rapidapi-host': "top-nft-sales.p.rapidapi.com",
    'x-rapidapi-key': "3bb7733b69msh9b45fd6403e7b90p1b3a2ejsnf58e6b59a35a"
    }

response = requests.request("GET", url, headers=headers)

result = response.json()

import time
initial = time.time()

c = 0

with open('data.json', 'w') as outfile:
    for i in result:
        res = requests.get(i['nft_url'])
        soup = BeautifulSoup(res.content, 'html.parser')
        img_url = soup.find('img', class_='img-thumbnail img-fluid')

        i['img_url'] =  re.search(r'(?<=src=").*?(?=")', str(img_url)).group()
        i['price'] = int(int(i['price'].replace("$", "").replace("k", "000")) / get_crypto_price(source = "bitstamp", crypto="eth", pair = "usd"))

        c+=1
        print(c, len(result))
    json.dump(result, outfile)

end = time.time()
print(end - initial)