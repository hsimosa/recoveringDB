#!/bin/bash
        (
        echo "#Inicio Movimiento de Archivos\n 5%";sleep 1
        echo "# Transfiriendo Archivos\n 20%" ;
        echo "20" ;
        echo "# Transfiriendo Archivos\n 30%" ;
        echo "30" ; sleep 1
        echo "# Transfiriendo Archivos\n 60%" ;
        echo "60" ; sleep 1
        echo "# Transfiriendo Archivos\n 80%" ;
        echo "80" ; 
        echo "# Transfiriendo Archivos\n 100%" ;
        echo "100" ; sleep 1
        echo "# Transferencia Exitosa.\nCierre este dialogo\nantes de oprimir boton proximo archivo." ; 
        ) |
        yad --progress \
          --title="Movimientos de Archivos a ser procesados" \
          --text="Favor Esperar un Momento" \
          --percentage=5 --width=480 --height=90 --on-top   

        if [ "$?" = 1 ] ; then
                zenity --error \
                  --text="         Transmision abortada!!. 
         Repetir proceso de nuevo"
        fi

