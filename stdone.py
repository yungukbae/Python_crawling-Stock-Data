import requests
from bs4 import BeautifulSoup

def get_bs_obj(company_code):

    url = 'https://finance.naver.com/item/main.nhn?code=' + company_code
    req = requests.get(url)
    soup = BeautifulSoup(req.content,'html.parser')
    return soup
def get_candle_chart(company_code):
    soup = get_bs_obj(company_code)

    #종목 명
    name = soup.find("div",{"class":"wrap_company"})
    nme = name.find("a")
    event = nme.text


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

    return{"event":event,"close": close,"high": high,"open": open,"low": low}

company_code = ['028050','047050','096770']

for item in company_code:
    candle_chart = get_candle_chart(item)
    print(candle_chart)

#test3