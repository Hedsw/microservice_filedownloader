
from osgeo import gdal
from glob import glob
import numpy as numpy
import matplotlib.pyplot as plt
import os
import threading
import time

name = []
filenames = []
#print("Test")

def nc4converter(i,lists):
    try:
        os.system('mkdir files/outputtif/%s' %i)
        os.system('gdal_translate -sds %s files/outputtif/%s/output.tif' %(lists[i], i))
        time.sleep(0.01)
        os.system('gdal_merge.py -separate -o files/outputtif/%s/final_output.tif files/outputtif/%s/output*tif' %(i,i))
        os.system('mv files/outputtif/%s/final_output.tif files/geotiffiles/geotif_%s.tif' %(i,i))
        #os.system('rm files/geoTIFfile/%s/geoFiles/output*tif' %i)
        #os.system('rm -rf files/outputtif/*')
    except Exception as e:
        print(" File not found, please refer to the website manually for download link", e)

    return True

def starter():
    os.system('rm -rf files/nc4file/*1')
    lists = glob('files/nc4file/*.nc4')
    
    for i in range(len(lists)):
        
        processThread = threading.Thread(target=nc4converter, args=(i,lists)) # parameters and functions have to be passed separately
        processThread.start() # START THE THREAD
        #processThread.join()
        #nc4converter(i, lists) 
    return True

#starter()
