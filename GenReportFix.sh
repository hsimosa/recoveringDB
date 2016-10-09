#!/bin/bash

#Inscripcion.txt tiene lista de archivos procesados que NO tienen problemas
PL=1
declare -i archivos
TX=(`wc -l Reparacion.txt`)						#Contador de lineas en Inscripcion
archivos=$TX-$PL

echo -e "\n\nTotal archivos de Inscripcion procesados con problemas: $archivos"	>> Reparacion.txt 

echo -e "\n\nADVERTENCIA: los datos de la Cedula Catastral de estos registros de Inscripcion no pueden ser capturados
Cosas a comprobar:
-Se debe procesar el archivo para estos numero de inscripcion nuevamente.
-Al digitalizar los documentos cerciorese la cedula entra perfectamente en el escaner.
-Cerciorese los valores para la resolucion sean los correctos" >> Reparacion.txt
cat Reparacion.txt | tr '\n' ' '
 
#python WritePDF.py aplicado a Inscripcion.txt Genera el reporte en formato PDF.

SCRIPT_PATH="WritePDF.py" 
PYTHON="/usr/bin/python"

# call script via the interrupter     
$PYTHON $SCRIPT_PATH Reparacion.txt

      
