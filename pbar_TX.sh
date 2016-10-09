#!/bin/bash
        (
        echo "#Inicio Carga de Datos\n 5%";sleep 2
        echo "# Cargando datos\n 20%" ;
        echo "20" ; sleep 1
        echo "# Cargando datos\n 40%" ;
        echo "40" ; sleep 1
        echo "# Transmitiendo\n 60%" ;
        echo "60" ; sleep 1
        echo "# Transmitiendo\n 80%" ;
        echo "80" ; sleep 1
        echo "# Transmitiendo\n 100%" ;
        echo "100" ; sleep 1
        echo "# Transferencia Exitosa.\nCierre este dialogo\nantes de cargar nuevo archivo." ; 
        ) |
        yad --progress \
          --title="Transferencia hacia Base de Datos Contribuyente" \
          --text="Favor Esperar un Momento" \
          --percentage=5 --width=480 --height=90 --on-top   

        if [ "$?" = 1 ] ; then
                zenity --error \
                  --text="         Transmision abortada!!. 
         Repetir proceso de nuevo"
        fi

