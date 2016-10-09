#!/bin/bash

rm IMAGENES/*
echo -n > files.lst					#Debo blanquear files.lst cada vez se inicia la tarea
ls -X ./PROCESAR >>files.lst		#OK hace lista correcta y ordenada 
FILE=files.lst
read line1 <$FILE
proximo=$line1						#Este es el archivo proximo a ser revisado para corregir/agregar cedula catastral registrada en BD
echo "$proximo"						#Confirma es el primero que debe salir

#Renombrar y Mover archivo para procesarlo
mv ./PROCESAR/"$proximo" ./PROCESAR/guardado.pdf
mv ./PROCESAR/guardado.pdf ./GUARDADOS/									
