#from osgeo import gdal
from glob import glob
import numpy as numpy
import matplotlib.pyplot as plt
import os
import threading
import gdal, osr

from netCDF4 import Dataset
import rasterio
from rasterio.transform import from_origin

lists = glob('files/nc4file/*.nc4')


nc = Dataset(lists[0],'r')

print(nc)

lat = nc.variables['latitude'][:]
lon = nc.variables['longitude'][:]
et = nc.variables['Evapotranspiration'][:]

transform = from_origin(68.175 , 37.025 , 0.05, 0.05)

profile = {'driver': 'GTiff', 'height': et.shape[1], 'width': et.shape[0], 'count': 1, 'dtype': str(et.dtype), 'transform': transform}
with rasterio.open(r'D:\Weather data\test.tif', 'w', crs='EPSG:4326', **profile) as dst:
     dst.write(et,1)