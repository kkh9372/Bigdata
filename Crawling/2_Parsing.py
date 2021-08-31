"""
날짜 : 2021/08/30
이름 : 김관후
내용 : 파이선 HTML 페이지 파싱하기 실습

파싱(Parsing) - 마크업 문서(반정형)에서 특정 태그의 데이터를 추출 처리하는 과정
"""
import  requests as req
from bs4 import BeautifulSoup as bs # bs4 설치(console -> pip install bs4

# 페이지 요청
url = 'https://news.naver.com/main/home.naver'
html = req.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
#print(html)

# 페이지 파싱
dom = bs(html, 'html.parser')
#titles =  dom.select('#section_it > div.com_list > div > ul > li > a > strong')
#print(titles)

# 파싱 데이터 출력
#for tit in titles:
    #print(tit.text)

# 다음 랭킹뉴스 1위 ~ 5위까지 출력력
url_daum = 'https://news.daum.net/ranking/popular'
html_daum = req.get(url_daum, headers={'User-Agent': 'Mozilla/5.0'}).text
#print(html_daum)

dom_daum = bs(html_daum, 'html.parser')
daum_titles = dom_daum.select('#mArticle > div.rank_news > ul.list_news2 > li > div.cont_thumb > strong > a')

for i in range(5):
    print('%d위 : %s' % (i+1, daum_titles[i].text))