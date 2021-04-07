from osgeo import gdal
from glob import glob
import numpy as numpy
import matplotlib.pyplot as plt
import os


def nc4converter():
    lists = glob(('nc4file/*.nc4'))
    print(lists)

    try:
            #print(glob('*.nc4'))
            lists = glob(('nc4file/*.nc4'))
            
            for i in range(len(lists)):
                os.system('gdal_translate -sds %s output.tif' %lists[i])
                print("gdal_translate is done")
                os.system('gdal_merge.py -separate -o final_output.tif output*tif')
                os.system('mv final_output.tif geoTIFfile/geotif_%s.tif' %i)
                print("gdal_merge is done")
                os.system('rm output*tif')
                print("rm is done")
                print(" nc4f files are converted ")

    except Exception as e:
                print(" File not found, please refer to the website manually for download link", e)
    return True

nc4converter()
