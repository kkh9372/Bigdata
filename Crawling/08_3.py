from selenium import webdriver
import os
from datetime import datetime
import requests as req

# 가상 브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')
# 기상청 도시별 관측 페이지로 이동
browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

# 강릉의 기온 데이터 가져오기
span_data = browser.find_elements_by_css_selector('#weather_table > tbody > tr:nth-child(1) > td:nth-child(6)').text


# 파일저장 디렉토리 생성
directory = "./weather/{:%Y-%m-%d}".format(datetime.now())
if not os.path.exists(directory):
    os.makedirs(directory)

# 파일생성
fname = "{:Weather_%Y-%m-%d-%H-%M.csv}".format(datetime.now())
file = open(directory+'/'+fname,'w', encoding='utf-8')
file.write(span_data)
file.close()

print('데이터 수집 완료')
