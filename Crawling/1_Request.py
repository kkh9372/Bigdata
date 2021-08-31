"""
날짜 : 2021/08/30
이름 : 김관후
내용 : 파이선 HTML 페이지 요청하기 실습
"""
import  requests as req    # requests 설치(console -> pip install requests

url = 'https://www.naver.com/'

# 페이지 요청하기
html = req.get(url).text
print(html)
