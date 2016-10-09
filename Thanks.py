#!/usr/bin/env python

from subprocess import Popen
import time

proc=Popen("zenity --height=250 --width=700 --title='Cierre de Aplicacion' --info --text='Reporte de actividad del dia de hoy procesado satisfactoriamente.'\r'\'\r'\
 Presione OK la aplicacion terminara normalmente en tres segundos y podra apagar computador.'\r'\'\r'\ Gracias'", shell=True )
proc.communicate()

if proc.returncode:
    print "Cancel was pressed"
else:
    print "Ok was pressed"

code_object = compile("""time.sleep(3)""", '<string>', 'exec')
exec code_object



