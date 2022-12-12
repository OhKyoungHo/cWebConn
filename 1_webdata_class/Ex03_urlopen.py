
# urlretrieve(): 파일로 바로 저장
# urlopen(): 파일로 바로 저장하기 않고 메모리에 로딩을 한다.

""" [참고] 파일저장 기본방식
    f = open('a.txt','w')
    f.write("테스트 내용")
    f.close()

    위의 과정을 with 문으로 간략하게 close 필요없음
    with open("a.txt","w") as f:
        f.write("테스트 내용")
"""

from urllib import request as req
url ='https://www.google.com/logos/doodles/2022/seasonal-holidays-2022-6753651837109831.3-law.gif'
site = req.urlopen(url)
page = site.read()
imgName ='data/google.png'
with open(imgName, 'wb') as file:
    file.write(page)

url1 = 'https://t1.daumcdn.net/daumtop_chanel/op/20200723055344399.png'
site1 = req.urlopen(url1)
page1 = site1.read()
imgName1 ='data/daum.png'
with open(imgName1, 'wb') as file:
    file.write(page1)