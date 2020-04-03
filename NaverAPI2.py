import requests
from urllib.parse import quote

def call(keyword, start):
    encText = quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=100" + "&start=" + str(start)
    result = requests.get(url=url, headers = {"X-Naver-Client-Id":"","X-Naver-Client-Secret":""})

    print(result)
    return result.json()