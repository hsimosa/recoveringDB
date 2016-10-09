#!/bin/bash
. config.sh
#Concatenamos las variables de CATASTRO

EDO=`cat $DIRU/IMAGENES/EDO.txt`

MUN=`cat $DIRU/IMAGENES/MUN.txt`

PARR=`cat $DIRU/IMAGENES/PARR.txt`

SECT=`cat $DIRU/IMAGENES/SECT.txt`

SS=`cat $DIRU/IMAGENES/SS.txt`

MAN=`cat $DIRU/IMAGENES/MAN.txt`

PAR=`cat $DIRU/IMAGENES/PAR.txt`

NIV=`cat $DIRU/IMAGENES/NIV.txt`

UND=`cat $DIRU/IMAGENES/UND.txt`

Inscripcion=`cat $DIRU/IMAGENES/NroIn.txt`

RIF=`cat $DIRU/IMAGENES/RIF.txt`

Direccion=` tr -d '\n' < $DIRU/IMAGENES/Direccion.txt`

Nombres=` tr -d '\n' < $DIRU/IMAGENES/Nombres.txt`

Catastro=$EDO-$MUN-$PARR-$SECT-$SS-$MAN-$PAR-$NIV-$UND
echo -e "$Inscripcion\r$Catastro\r$RIF\r$Nombres\r$Direccion\r" >> $DIRU/IMAGENES/Datos.txt

