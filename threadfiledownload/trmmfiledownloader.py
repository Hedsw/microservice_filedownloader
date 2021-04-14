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
from xml.etree.ElementTree import parse

from xml.etree.ElementTree import parse

# FILE LINK GET FROM XML
tree = parse('../XMLfiles/trmmdownloader.xml')
root = tree.getroot()
trmm = root.findall("TRMM_RT")
link = [x.findtext("LINK") for x in trmm]
filenames = []

# BRING FILE NAME FROM LINK 
def filenamesget(url):
    baseUrl = link[0]
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
        os.system('wget -P files/nc4file/ --user gogod951 --password dbsGUR123@# %s/%s' %(link[0],filename))
    except Exception as e:
        print(" File not found, please refer to the website manually for download link", e)

def starter(urls):
    filenamesget(link[0]) # File name collector
    
    for name in filenames:
        processThread = threading.Thread(target=downloader, args=(name,filenames)) # parameters and functions have to be passed separately
        processThread.start() # START THE THREAD
    # Join Thread HERE. Because For loop is over, then other Thread will be started. before then next Thread should be waited.
    processThread.join()
    return True
starter(link[0])
