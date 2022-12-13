from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import request
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, quote

import time, csv, json, folium
import cx_Oracle as oci

conn = oci.connect('scott/tiger@192.168.0.26:1521/xe')
print(conn.version)

driver = webdriver.Chrome('../webdrive/chromedriver.exe')
driver.implicitly_wait(1)

map_osm = folium.Map(location=[37.572807,126.975918])

with open('./data/치정.csv','a',encoding='utf-8-sig') as f:

    for page_num in range(1,8):
        driver.get('http://xn--9n3b23etshra259e96ao8h.kr/?c=Cat06&p=%d' % page_num)

        html = driver.page_source
        time.sleep(1)

        soup = BeautifulSoup(html,'html.parser')

        name = soup.select('.sbj')
        addr = soup.select('#bbslist tr>td:nth-child(3)')
        tel = soup.select('#bbslist tr>td:nth-child(4)')

        for addr, tel, name, in zip(addr,tel,name) :
            print(addr.text.strip(),tel.text.strip(),name.text.strip())

            vworld_apikey = 'BB68F9B0-D068-3F5A-956A-52342E38F074'
            url = "http://api.vworld.kr/req/address?service=address&request=getCoord&type=ROAD&refine=false&key=%s&" % (
                vworld_apikey) + urlencode({quote_plus('address'): addr.text.strip()}, encoding='UTF-8')
            print(url)

            request = Request(url)
            response = urlopen(request)
            rescode = response.getcode()
            print(response)
            if rescode == 200:
                response_body = response.read().decode('utf-8')
                #print(response_body)
            else:
                print('error code:', rescode)

            try:
                jsonData = json.loads(response_body)
                lat = float(jsonData['response']['result']['point']['y'])
                lng = float(jsonData['response']['result']['point']['x'])
                # print('lat:{}, lng:{}'.format(lat, lng))
            except:
                print('error :', Exception)
                lat = ""
                lng = ""

            sql = f"insert into store_info values('{name.text}','{addr.text}','{tel.text}','{lat}','{lng}')"

            cursor = conn.cursor()

            cursor.execute(sql)

            cursor.close()

            data =[name.text.strip(), tel.text.strip(),addr.text.strip(),lat,lng]

            cout = csv.writer(f)  # csv.writer 를 f 랑 연결한다 / 이거하나를 꼭 가지고있어주장
            cout.writerow(data)  # 하나씩 읽어준다

            if lat != "":

                folium.Marker(location=[lat, lng],
                              popup=f"'{name.text}'",
                              icon=folium.Icon(color='red', icon='info-sign')).add_to(map_osm)

map_osm.save('./map/1.html')

conn.commit()
conn.close()

driver.close()

