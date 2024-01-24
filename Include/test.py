import requests
# requests : 파이썬 HTTP 라이브러리(HTTP, HTTPS 웹 사이트 요청)
# 웹 스크래핑 과정에서 requests 모듈을 이용해서 소스코드 파싱

from bs4 import BeautifulSoup
# HTML 정보로부터 원하는 데이터를 쉽게 가져오는 라이브러리

# 웹사이트 URL 설정
url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101'

# requests를 사용하여 웹 페이지 내용 가져오기
response = requests.get(url) # --> 지정 웹사이트에 URL에 GET 요청을 보낸다.

# 웹 페이지의 HTML 내용을 BeautifulSoup 객체로 변환
soup = BeautifulSoup(response.text, 'html.parser')

# 모든 h1 태그 찾기
news_headline = soup.find_all('a', class_="sh_text_headline")

news_body = soup.find_all('div', class_="sh_text_lede")

print(news_headline)
print(news_body)

# news_headline의 뉴스 타이틀만 출력
# for news_title in news_headline:
#     print(news_title.text)

# news_headline의 뉴스 타이틀만 출력
for body in news_body:
    print(body.text)
