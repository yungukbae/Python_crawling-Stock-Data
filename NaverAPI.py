import requests
from urllib.parse import urlparse

keyword = ""
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
result = requests.get(urlparse(url).geturl(),headers = {"X-Naver-Client-Id":"YOUR_CLIENT_ID","X-NAVER-CLIENT-Secret":"YOUR_CLIENT_SECRET"})

json_pbj = result.json()
print(json_pbj)