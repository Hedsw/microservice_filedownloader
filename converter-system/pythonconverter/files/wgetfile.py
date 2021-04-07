from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import urllib.request as urllib2
import re
import requests
import wget
import base64
import os
import urllib
from subprocess import Popen

baseUrl = 'https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_RT/TRMM_3B42RT_Daily.7/2002/01/'
filename = "3B42RT_Daily.20020101.7.nc4"
username = "gogod951"
password = "dbsGUR123@#"

#requests.get(https+baseUrl, auth=HTTPDigestAuth(username, password))
#wget.download(https+baseUrl+filename, filename)

# 아래와 같이 파일 이름에 따라서 불러오게 만들었음 
# 동기식으로 작성.. Synchronous way 
'''
for i in range(5):
    try:
        print(https + baseUrl + filename)
        os.system('wget --user gogod951 --password dbsGUR123@# https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_RT/TRMM_3B42RT_Daily.7/2002/01/%s' %filename)
        #os.system("wget --load-cookies cookies.txt --accept=exe {}".format(url))

    except Exception as e:
            print(" File not found, please refer to the website manually for download link", e)
'''

#여기서 이제 파싱해서 파일 이름을 가져가야한다.. 씨부레 


#for href in soup.find('table').find_all('tr'):
#    print(href.find("a")["href"])

req = urllib.request.Request(baseUrl)
sourcecode = urllib.request.urlopen(baseUrl).read()
soup = BeautifulSoup(sourcecode, 'html.parser')
for href in soup.find("table").find_all('a', href=re.compile("nc4$")):
    fname = href["href"]
    print(fname)

print("Download Finished")



'''
# asynchronously way  -> https://stackoverflow.com/questions/636561/how-can-i-run-an-external-command-asynchronously-from-python
p = Popen(['watch', 'ls'])
for i in range(5):
    try:
        print(https + baseUrl + filename)
        os.system('wget --user gogod951 --password dbsGUR123@# https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_RT/TRMM_3B42RT_Daily.7/2002/01/%s' %filename)
        #os.system("wget --load-cookies cookies.txt --accept=exe {}".format(url))

    except Exception as e:
            print(" File not found, please refer to the website manually for download link", e)
p.terminate()
'''

#wget.download(url, 'success.nc4')


