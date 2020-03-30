import requests

req = requests.get('https://finance.naver.com/item/main.nhn?code=263750#')

#HTTP 소스 가져오기
html = req.text

#HTTP header 가져오기
header = req.headers

#HTTP Status 가져오기 (200:정상)
status = req.status_code

is_ok = req.ok

print(is_ok)