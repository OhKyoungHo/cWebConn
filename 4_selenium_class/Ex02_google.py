'''
1. 크롬웹드라이버로 구글 사이트 열기

2. 실제 크롬창에서 '파이썬'라고 검색버튼을 누른다.
    개발자모드(F12)에서 이 부분을 보면
    <input name='q' value='파이썬'~~ >
    그리고 'google검색' 버튼이 type='submit' 인거 확인
'''

from selenium import webdriver
# [1]. webdrive 객체생성
driver = webdriver.Chrome('./webdrive/chromedriver.exe')
driver.implicitly_wait(3)

driver.get('https://www.google.com')

#----------------------------------------------
# [2]
# name이 q인 것 찾기
search_bt = driver.find_element_by_name('q')
search_bt.send_keys('세즈카')
search_bt.submit()

# 네이버
driver1 = webdriver.Chrome('./webdrive/chromedriver.exe')
driver1.implicitly_wait(3)

driver1.get('https://www.naver.com')
search_bt = driver1.find_element_by_name('query')
search_bt.send_keys('세즈카')
search_bt.submit()

# 다음
driver2 = webdriver.Chrome('./webdrive/chromedriver.exe')
driver2.implicitly_wait(3)

driver2.get('https://www.daum.net')
search_bt = driver2.find_element_by_name('q')
search_bt.send_keys('세즈카')
search_bt.submit()
