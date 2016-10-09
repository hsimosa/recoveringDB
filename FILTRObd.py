#!/usr/bin/python
# -*- coding: utf8 -*-

# Date: 14.07.2016 18:15:13
# Version: 5
# Revision: 5.0

import config
#import Image, ImageFilter
from PIL import Image
from PIL import ImageFilter
import os, sys, subprocess

im1 = Image.open (config.DIRU+'/IMAGENES/imagen1.jpg')
im = im1.filter(ImageFilter.ModeFilter(1))
im.save(config.DIRU+'/IMAGENES/imagen1.jpg')

boxNroIn = (2213, 488, 2410, 549)
NroIn = im.crop(boxNroIn)
NroIn.save(config.DIRU+'/IMAGENES/NroIn.tif') 

boxEDO = (376, 755, 500, 810)
EDO = im.crop(boxEDO)
EDO.save(config.DIRU+'/IMAGENES/EDO.tif') 

boxMUN = (552, 755, 735, 810)
MUN = im.crop(boxMUN)
MUN.save(config.DIRU+'/IMAGENES/MUN.tif') 

boxPARR = (828, 755, 952, 810)
PARR = im.crop(boxPARR)
PARR.save(config.DIRU+'/IMAGENES/PARR.tif') 

boxSECT = (1050, 755, 1139, 810)
SECT = im.crop(boxSECT)
SECT.save(config.DIRU+'/IMAGENES/SECT.tif') 

boxSS = (1225, 755, 1385, 810)
SS = im.crop(boxSS)
SS.save(config.DIRU+'/IMAGENES/SS.tif') 

boxMAN = (1480, 755, 1625, 810)
MAN = im.crop(boxMAN)
MAN.save(config.DIRU+'/IMAGENES/MAN.tif') 

boxPAR = (1690, 754, 1800, 804)
PAR = im.crop(boxPAR)
PAR.save(config.DIRU+'/IMAGENES/PAR.tif') 

boxNIV = (1888, 754, 1980, 804)
NIV = im.crop(boxNIV)
NIV.save(config.DIRU+'/IMAGENES/NIV.tif') 

boxUND = (2005, 750, 2135, 805)
UND = im.crop(boxUND)
UND.save(config.DIRU+'/IMAGENES/UND.tif') 

boxRIF = (100, 937, 480, 1028)
RIF = im.crop(boxRIF)
RIF.save(config.DIRU+'/IMAGENES/RIF.tif') 

boxNOMBRE = (564, 925, 2292, 1030)
NOMBRE = im.crop(boxNOMBRE)
NOMBRE.save(config.DIRU+'/IMAGENES/NOMBRE.tif') 

boxDIR = (100, 1260, 2317, 1375)
DIR = im.crop(boxDIR)
DIR.save(config.DIRU+'/IMAGENES/DIR.tif') 

