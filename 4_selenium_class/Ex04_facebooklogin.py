from selenium import webdriver

usr ='ketty1061@naver.com'
pwd ='11218957'

# [1]. webdrive 객체생성
driver = webdriver.Chrome('./webdrive/chromedriver.exe')
driver.implicitly_wait(3)

driver.get('https://www.facebook.com')

email = driver.find_element_by_id('email')
passwd = driver.find_element_by_id('pass')

email.send_keys(usr)
passwd.send_keys(pwd)

btn = driver.find_element_by_name('login')
btn.click()
driver.implicitly_wait(2)

# -----------------
# [1]. webdrive 객체생성
# driver1 = webdriver.Chrome('./webdrive/chromedriver.exe')
# driver1.implicitly_wait(3)
#
# driver1.get('https://accounts.kakao.com/login/?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fwww.daum.net')
#
# email = driver1.find_element_by_name('loginKey')
# passwd = driver1.find_element_by_name('password')
#
# email.send_keys(usr)
# passwd.send_keys(pwd)
#
# btn = driver1.find_element_by_class_name('btn_g highlight')
# btn.click()
# driver1.implicitly_wait(2)