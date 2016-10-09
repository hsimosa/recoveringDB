#!/usr/bin/python
# -*- coding: utf8 -*-

# Date: 14.07.2016 18:15:13
# Version: 5
# Revision: 5.0

import subprocess
import sys, os, time, config

# Procedimiento para extraer campos con txt de Cedula Catastral. Esta version No  coloca Firma Digital

a = subprocess.Popen(['gs -sDEVICE=jpeg -sPAPERSIZE=a4 -r300x300 -dLastPage=1 -dBATCH -dNOPAUSE -sOutputFile='+config.DIRU+'/IMAGENES/imagen1.jpg '+config.DIRU+'/GUARDADOS/guardado.pdf'], shell=True).communicate()[0]

a2 = subprocess.Popen(['convert -deskew 40 -normalize '+config.DIRU+'/IMAGENES/imagen1.jpg -antialias '+config.DIRU+'/IMAGENES/imagen.jpg'], shell=True).communicate()[0]

# Hago llamada a los modulos FILTRO.py y TERCERO.py para extraer de la imagen.tif/imagen.jpg las diferentes imagenes de los diferentes campos y sus textos.
c = subprocess.Popen([config.DIROP+'/FILTRObd.py'], shell=True).communicate()[0]

d = subprocess.Popen([config.DIROP+'/TERCERObd.py'], shell=True).communicate()[0]

time.sleep (1)
e = subprocess.Popen([config.DIROP+'/CUARTO.sh'], shell=True).communicate()[0]






