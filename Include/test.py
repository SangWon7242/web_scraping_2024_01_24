import requests
# requests : 파이썬 HTTP 라이브러리(HTTP, HTTPS 웹 사이트 요청)
# 웹 스크래핑 과정에서 requests 모듈을 이용해서 소스코드 파싱

from bs4 import BeautifulSoup
# HTML 정보로부터 원하는 데이터를 쉽게 가져오는 라이브러리

import pandas as pd

# 웹사이트 URL 설정
url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101'

# requests를 사용하여 웹 페이지 내용 가져오기
response = requests.get(url) # --> 지정 웹사이트에 URL에 GET 요청을 보낸다.

# 웹 페이지의 HTML 내용을 BeautifulSoup 객체로 변환
soup = BeautifulSoup(response.text, 'html.parser')

# a태그이면서 class 이름이 sh_text_headline 녀석을 가져옴
news_headline = soup.find_all('a', class_="sh_text_headline")

# div태그이면서 class 이름이 sh_text_lede 녀석을 가져옴
news_body = soup.find_all('div', class_="sh_text_lede")

# print(news_headline)
# print(news_body)

news_titles = []

# news_headline의 뉴스 타이틀만 출력
for title in news_headline:
    news_titles.append(title.text);

# news_headline의 뉴스 타이틀만 출력
# for body in news_body:
#     print(body.text)

news_title_list = {"뉴스제목" : news_titles}

# 추출한 데이터를 엑셀에 저장
df = pd.DataFrame(news_title_list)
df.to_excel("C:\work\python_projects\뉴스제목.xlsx", index=False)