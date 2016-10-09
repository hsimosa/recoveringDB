#!/usr/bin/python
# -*- coding: utf8 -*-

# Date: 14.07.2016 18:15:13
# Version: 5
# Revision: 5.0

import subprocess
import sys, os, config

# Extraigo la informacion TXT de los datos de la imagen de campos xxx.tif mediante aplicacion de:

def main():
	
    Inscripcion = subprocess.Popen(['./TESS2TXT.sh '+config.DIRU+'/IMAGENES/NroIn.tif '+config.DIRU+'/IMAGENES/NroIn'], shell=True).communicate()[0]

    EDO = subprocess.Popen(['./TESS2TXT.sh '+config.DIRU+'/IMAGENES/EDO.tif '+config.DIRU+'/IMAGENES/EDO'], shell=True).communicate()[0]

    MUN = subprocess.Popen(['./TESS2TXT.sh '+config.DIRU+'/IMAGENES/MUN.tif '+config.DIRU+'/IMAGENES/MUN'], shell=True).communicate()[0]

    PARR = subprocess.Popen(['./TESS2TXT.sh '+config.DIRU+'/IMAGENES/PARR.tif '+config.DIRU+'/IMAGENES/PARR'], shell=True).communicate()[0]

    SECT = subprocess.Popen(['./TESS2TXT.sh '+config.DIRU+'/IMAGENES/SECT.tif '+config.DIRU+'/IMAGENES/SECT'], shell=True).communicate()[0]

    SS = subprocess.Popen(['./TESS2TXT.sh '+config.DIRU+'/IMAGENES/SS.tif '+config.DIRU+'/IMAGENES/SS'], shell=True).communicate()[0]

    MAN = subprocess.Popen(['./TESS2TXT.sh '+config.DIRU+'/IMAGENES/MAN.tif '+config.DIRU+'/IMAGENES/MAN'], shell=True).communicate()[0]

    PAR = subprocess.Popen(['./TESS2TXT.sh '+config.DIRU+'/IMAGENES/PAR.tif '+config.DIRU+'/IMAGENES/PAR'], shell=True).communicate()[0]

    NIV = subprocess.Popen(['./TESS2TXT.sh '+config.DIRU+'/IMAGENES/NIV.tif '+config.DIRU+'/IMAGENES/NIV'], shell=True).communicate()[0]

    UND = subprocess.Popen(['./TESS2TXT.sh '+config.DIRU+'/IMAGENES/UND.tif '+config.DIRU+'/IMAGENES/UND'], shell=True).communicate()[0]

    RIF = subprocess.Popen(['./TESS2TXT.sh '+config.DIRU+'/IMAGENES/RIF.tif '+config.DIRU+'/IMAGENES/RIF'], shell=True).communicate()[0]

    Nombres = subprocess.Popen(['./TESS2TXT.sh '+config.DIRU+'/IMAGENES/NOMBRE.tif '+config.DIRU+'/IMAGENES/Nombres'], shell=True).communicate()[0]

    Direccion = subprocess.Popen(['./TESS2TXT.sh '+config.DIRU+'/IMAGENES/DIR.tif '+config.DIRU+'/IMAGENES/Direccion'], shell=True).communicate()[0]

if __name__ == '__main__':

    main()
