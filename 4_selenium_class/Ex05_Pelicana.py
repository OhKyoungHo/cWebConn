from selenium import webdriver
from bs4 import BeautifulSoup
import time

# [1]. webdrive 객체생성
driver = webdriver.Chrome('./webdrive/chromedriver.exe')
driver.implicitly_wait(3)

# [연습]
for page_no in range(1,11):
    driver.get('https://pelicana.co.kr/store/stroe_search.html?page=%d' % page_no)
    html = driver.page_source
    # print(html)
    time.sleep(5)

    soup = BeautifulSoup(html, 'html.parser')

    store = soup.select('.table tr> td:nth-child(1)')
    # print(store)
    tel = soup.select('.table tr> td:nth-child(3)')
    # print(tel)
    for store, tel in zip(store, tel):
        #길 경우 if else로 자르는 기능 만들어서 해보기
        print(store.text.strip(), tel.text.strip())