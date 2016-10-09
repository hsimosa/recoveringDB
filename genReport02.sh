#!/bin/bash


PL=1
declare -i archivos
TX=(`wc -l Inscripcion.txt`)						#Contador de lineas en Inscripcion
archivos=$TX-$PL

echo -e "\n\nTotal archivos de Inscripcion procesados hacia BD: $archivos"	>> Inscripcion.txt 

convedate=$(date +"%a %b %d %H:%M:%S GMT%:z %Y")

echo -e "\n\nADVERTENCIA: En esta fecha, $convedate los datos de la Cedula Catastral de estos registros de Inscripcion han sido capturados debidamente
por el operador" >> Inscripcion.txt
cat Inscripcion.txt | tr '\n' ' '
 


      
