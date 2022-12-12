from bs4 import BeautifulSoup
from urllib import request

html = request.urlopen('http://www.yes24.com/Product/Search?domain=ALL&query=python')
soup = BeautifulSoup(html, 'html.parser')

# [1]
# infos = soup.select('#yesSchList .gd_name')
# #infos = soup.select('#yesSchList .itemUnit a.gd_name')
# for info in infos:
#     print(info.text)
# print(len(infos), '권이 검색되었습니다')

# [2]
imgUrls = soup.select('#yesSchList div.itemUnit img')
for imgUrl in imgUrls:
    bookName = imgUrl.attrs['alt'].strip().replace('/', '_')
    imgPath = imgUrl.attrs['data-original']
    print(bookName, imgPath)
    request.urlretrieve(imgPath, 'imgs/' + bookName + '.jpg')