# 빅데이터 수업 과제 #1_1

import urllib.parse
import urllib.request

client_id = "sZiKXpihvQDigy9xtYNC"
client_secret = "f4MMLYZbDt"

# encText = urllib.parse.quote("아이유")
encText = urllib.parse.quote("빅데이터")
encParam = urllib.parse.quote("100")
# url = "https://openapi.naver.com/v1/search/blog.json?query=" + encText
url = "https://openapi.naver.com/v1/search/news.json?query=" + encText

# request parameter 추가적인 파라미터 사이에 '&' 붙여주기
# query / display(결과 10~100개) / start / sort(sim 유사도, date 최신)
# url += "&display=100" + "&sort=date"

print(url)
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
result = response.getcode()

if result == 200:
    response_body = response.read()
    print(response_body.decode('utf-8'))
    with open('naver_api_search_news_bigdata.json', 'w', encoding='utf-8') as f:
        f.write(response_body.decode('utf-8'))

else:
    print("Error code: ", result)
