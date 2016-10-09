#!/bin/bash
        (
        echo "# Procesando datos\n 5%" ;
        echo "5" ; sleep 3
        echo "# Procesando datos\n 20%" ;
        echo "20" ; sleep 4
        echo "# Procesando datos\n 40%" ;
        echo "40" ; sleep 4
        echo "# Procesando datos\n 60%" ;
        echo "60" ; sleep 4
        echo "# Procesando datos\n 80%" ;
        echo "80" ; sleep 4
        echo "# Procesando datos\n 100%" ;
        echo "100" ; sleep 2
        echo "# Proceso terminado.\nRevisar cuidadosamente los datos del Contribuyente\nuse la imagen de Cedula Catastral para corregir.\nCierre este dialogo antes de cargar nuevo archivo." ;
        ) |
        yad --progress \
          --title="Procesando Datos de Contribuyente" \
          --text="Favor Esperar un Momento" \
          --percentage=5 --width=480 --height=90 --on-top \
           

        if [ "$?" = 1 ] ; then
                zenity --error \
                  --text="         Transmision abortada!!. 
         Repetir proceso de nuevo"
        fi

