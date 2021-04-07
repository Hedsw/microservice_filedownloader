from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")


baseUrl = 'https://www.instagram.com/explore/'
plusUrl = input('검색할 테그를 입력하세요 : ')
url = baseUrl + quote_plus(plusUrl)

driver = webdriver.Chrome('/home/ubuntu/flasktest/chromedriver')
driver.get(url)

html = dirver.page_source
soup = BeautifulSoup(html)

insta = soup.select('.eLAPa.KL4Bh_9AhH0')

print(insta)

'''
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
img = soup.find_all(class_= re.compile('\\_image+'))

#print(img[0])


n = 1
for i in img:
    imgUrl = i['class']
    with urlopen(imgUrl) as f:
        with open('.img/' + plusUrl + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1
    print(imgUrl)

print('다운로드 완료')
'''