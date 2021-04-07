'''
File Size Linux.. In terminal..
sudo du -sh
'''
from bs4 import BeautifulSoup
import urllib.request as urllib2
import re
import requests
import wget
import os
import threading

filenames = []

def filenamesget(url):
    baseUrl = 'https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_RT/TRMM_3B42RT_Daily.7/2002/01/'
    req = urllib2.Request(baseUrl)
    sourcecode = urllib2.urlopen(baseUrl).read()
    soup = BeautifulSoup(sourcecode, 'html.parser')

    xml = "xml"
    for href in soup.find("table").find_all('a', href=re.compile("nc4")):
        fname = href["href"]
        filenames.append(fname)
        
    setfile = set(filenames)
    filenames.clear()
    list_set = list(setfile)
    list_set.sort()
    for i in list_set:
        if xml not in i:
            filenames.append(i)
    print(filenames)
    
# download files into converter-system folder - 1 
def downloader(filename,urls):
    
    try:
        os.system('wget -P files/nc4file/ --user gogod951 --password dbsGUR123@# https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_RT/TRMM_3B42RT_Daily.7/2002/01/%s' %filename)
    except Exception as e:
        print(" File not found, please refer to the website manually for download link", e)


def starter(urls):
    filenamesget("wow") # File name collector
    
    for name in filenames:
        processThread = threading.Thread(target=downloader, args=(name,filenames)) # parameters and functions have to be passed separately
        processThread.start() # START THE THREAD
        #processThread.join()
    return True

starter("WoW")