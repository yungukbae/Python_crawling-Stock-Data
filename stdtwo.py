import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/item/main.nhn?code=005930'
req = requests.get(url)
soup = BeautifulSoup(req.content,'html.parser')

#전일(close)
first = soup.find("td",{"class":"first"})
blind = first.find("span",{"class":"blind"})
close = blind.text

#고가(high)
table = soup.find("table",{"class":"no_info"})
trs = table.find_all("tr")
first_tr = trs[0]
tds = first_tr.find_all("td")
second_tds = tds[1]
high = second_tds.find("span",{"class":"blind"}).text

#시가(open)
second_tr = trs[1]
tds_second_tr = second_tr.find_all("td")
first_td_in_second_tr = tds_second_tr[0]
open = first_td_in_second_tr.find("span",{"class":"blind"}).text

#저가(low)
second_td_in_second_tr = tds_second_tr[1]
low = second_td_in_second_tr.find("span",{"class":"blind"}).text

print("전일:"+close+"\n")
print("고가:"+high+"\n")
print("시가:"+open+"\n")
print("저가:"+low+"\n")


