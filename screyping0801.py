import requests
from bs4 import BeautifulSoup
result = requests.get('https://doda.jp/dcfront/history/historyList/?selectionStatusCategory=2')
username = 'coinbra3b@hotmail.com'
password = 'korontan3b'
info01 = BeautifulSoup(result.text,'html.parser')
#info02 = info01.find_all('div',class_='yjnSub_list_text')
info02 = info01.find_all('div',class_='listDateSet')

for news in info02:
    print(news.getText())
