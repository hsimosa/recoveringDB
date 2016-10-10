#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Date created 01.07.2016
# Copyright (c) 2013: Ricardo Il Grande (ricardoilgrande@gmail.com),
# Hector Simosa (hsimosa@gmail.com)
#
# Development Status: Production/Stable
# Environment:Console
# Programming Language: Python-Twisted
# Date:10.10.2016 16:50:44
# Version: 4
# Revision: 0
#
# This program is based on free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# You should have a copy of the GNU Lesser General Public
# License. Write to the Free Software Foundation, Inc.,
#  51 Franklin St, Fifth Floor.

import logging
import os
import subprocess
import gtk
import pygtk
pygtk.require('2.0')
from PIL import Image
import psutil
import MySQLdb
import config

logging.basicConfig(filename='./tmp/log', level=logging.DEBUG, format='%(levelname)s[%(asctime)s]: %(message)s')


os.system('./genTEXTOS.sh')  # Genera archivos TXT en limpio al inicio de las operaciones

Inscripcion = 0
class Clientes:
    def conectar(self):
        conexion = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="", db="")
        cursor = conexion.cursor()
        return cursor

    def __init__(self):
        self.bdpointer = self.conectar()

        # Initialising widgets and packing it into window
        self.mainWindow = gtk.Window(gtk.WINDOW_TOPLEVEL)
        color = gtk.gdk.color_parse('#FFFFCC')  # To change the color again, just modify it again
        self.mainWindow.modify_bg(gtk.STATE_NORMAL, color)
        self.mainWindow.set_title("Envia datos de Contribuyentes a la Base de Datos")
        self.mainWindow.set_position("center")
        self.mainWindow.set_size_request(900, 400)
        self.mainWindow.connect("destroy", self.destroy)	
       
        hbox = gtk.HBox(spacing=6)
        
        self.image = gtk.Image()				
        self.image.set_from_file("icon1.png")
        fix = gtk.Fixed()
        fix.put(self.image, 20, 20)
            
        self.vbox = gtk.VBox()
        self.vbox.set_border_width(10)
        
        self.mainWindow.add(self.vbox)
          
        self.table = gtk.Table(7, 4, True)  # creates a table with 7 rows and 5 columns
        self.table.set_border_width(10)
        self.table.set_row_spacings(3)
        self.table.set_col_spacings(3)
        self.vbox.pack_start(fix, False, True, 0)
        self.vbox.pack_start(self.table, False, True, 0)
        label = gtk.Label("Archivo a procesar:")
        self.table.attach(label, 0, 1, 0, 1)
        self.entry1 = gtk.Entry(max=10)
        self.table.attach(self.entry1, 1, 2, 0, 1)

        label = gtk.Label("Inscripcion :")
        self.table.attach(label, 0, 1, 1, 2)
        self.entry2 = gtk.Entry(max=8)
        self.table.attach(self.entry2, 1, 3, 1, 2)

        label = gtk.Label("Catastro :")
        self.table.attach(label, 0, 1, 2, 3)
        self.entry3 = gtk.Entry(max=36)
        self.table.attach(self.entry3, 1, 3, 2, 3)

        label = gtk.Label("RIF :")
        self.table.attach(label, 0, 1, 3, 4)
        self.entry4 = gtk.Entry(max=12)
        self.table.attach(self.entry4, 1, 3, 3, 4)

        label = gtk.Label("Nombre :")
        self.table.attach(label, 0, 1, 4, 5)
        self.entry5 = gtk.Entry(max=128)
        self.table.attach(self.entry5, 1, 3, 4, 5)

        label = gtk.Label("Direccion :")
        self.table.attach(label, 0, 1, 5, 6)
        self.entry6 = gtk.Entry(max=180)
        self.table.attach(self.entry6, 1, 3, 5, 6)

        label = gtk.Label("Archivos faltantes :")
        self.table.attach(label, 0, 1, 6, 7)
        self.entry7 = gtk.Entry(max=10)
        self.table.attach(self.entry7, 1, 2, 6, 7)

        separator = gtk.HSeparator()
        self.vbox.pack_start(separator, False, True, 5)
        self.hbox = gtk.HBox(False, 0)
        self.vbox.pack_start(self.hbox, True, True, 0)
        self.tooltips = gtk.Tooltips()

        # creating buttons and packing it into window

        button = gtk.Button('Inicio')
        self.hbox.pack_start(button, True, True, 2)
        button.connect('clicked', self.on_inicio_clicked)
        self.tooltips.set_tip(button, "Va a dar inicio a reconstruccion base de datos de contribuyentes.")

        button = gtk.Button('Proximo Archivo')
        self.hbox.pack_start(button, True, True, 2)
        button.connect('clicked', self.on_proximo_clicked)
        self.tooltips.set_tip(button,
                              "Va a mostrar nuevo archivo de Inscripcion con datos de contribuyentes a ser revisado/corregido para enviar a la BD.")

        button = gtk.Button('Reportar')
        self.hbox.pack_start(button, True, True, 2)
        button.connect('clicked', self.on_reportar_clicked)
        self.tooltips.set_tip(button, "Va a enviar archivo para ser reportado con deficiencias de digitalizacion.")

        button = gtk.Button('Enviar a BD')
        self.hbox.pack_start(button, True, True, 2)
        button.connect('clicked', self.on_enviar_clicked)
        self.tooltips.set_tip(button, "Va a enviar datos de contribuyentes ya revisados a base de datos.")

        button = gtk.Button("Cerrar")
        self.hbox.pack_start(button, True, True, 2)
        button.connect_object("clicked", gtk.Widget.destroy, self.mainWindow)
        self.tooltips.set_tip(button, "Cerrar aplicacion")

        separator = gtk.HSeparator()
        self.vbox.pack_start(separator, False, True, 5)

        self.mainWindow.show_all()
        gtk.main()

    # 1er Boton Inicio
    def on_inicio_clicked(self, widget, data=None):
        # 1ro. Aca se debe iniciar el proceso global de mv files existentes en /archivo hacia /PROCESAR/ para aplicar OCR, etc, etc
        subprocess.Popen(['./pbar_MA.sh'], stdout=subprocess.PIPE, shell=True)
        subprocess.Popen(['rsync -r /home/hector/archivos/* PROCESAR/'], shell=True)

        # 2do. Contar cantidad de archivos en folder procesar
        path, dirs, files = os.walk('PROCESAR').next()
        archivos = self.entry7.set_text(str(len(files)))

        # 3ro. Extraer la primera pagina del PDF de los Archivos en /PROCESAR
        #print 'En ejecucion paso 3ro'	#PRINT PARA CHEQUEAR
        print
        os.system(
            'for file in PROCESAR/*; do gs -dSAFER -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile="${file%.pdf}-p1.pdf" -dFirstPage=1 -dLastPage=1 "$file" ; done')
        os.system('rename -f s/\-p1.pdf$/\.pdf/ ./PROCESAR/*-p1.pdf')  # Renombra la primera pagina de los PDF

    # 2do Boton
    def on_proximo_clicked(self, widget, data=None):
        # 4to. Crear archivo guardado.pdf con el primer file del folder /PROCESAR y luego moverlo hacia /GUARDADOS
        orden = subprocess.Popen(['./proximo.sh'], stdout=subprocess.PIPE, shell=True).communicate()[0]
        proximo = orden.strip()
        print 'proximo=', proximo
        self.entry1.set_text(str(proximo))

        # 2doA. Contar cantidad de archivos a procesar nuevamente
        path, dirs, files = os.walk('PROCESAR').next()
        archivos = self.entry7.set_text(str(len(files)))

        # 5to. Iniciar OCR para recabar datos	
        subprocess.Popen(['./pbar_TX2.sh'], stdout=subprocess.PIPE, shell=True)
        subprocess.Popen([config.DIROP + '/OCRbd.py'], shell=True).communicate()[0]
		
        # 6to. Extraer data para mostrar en GUI
        lines = open('./IMAGENES/Datos.txt').read().splitlines()  # luego extraigo con: lines[0] etc etc

        inscripcion = self.entry2.set_text(lines[0])
        catastro = self.entry3.set_text(lines[1])
        rif = self.entry4.set_text(lines[2])
        nombre = self.entry5.set_text(lines[3])
        direccion = self.entry6.set_text(lines[4])

        # 2doB. Mostrar imagen del PDF en proceso de revision
        im1 = Image.open('IMAGENES/imagen1.jpg')
        im2 = im1.resize((1200, 2000), Image.BILINEAR)
        im2.show()

    # 3er Boton
    def on_reportar_clicked(self, widget):
        global Inscripcion
        Inscripcion = self.entry1.get_text()

        repara = open('Reparacion.txt', 'a+')
        repara.write(repr(Inscripcion) + '\n')
        repara.close()

        for proc in psutil.process_iter():
            if proc.name() == "display":
                proc.kill()

        # After sending data clear all the text from the text entries
        self.entry1.set_sensitive(True)
        self.entry1.set_text("")
        self.entry2.set_sensitive(True)
        self.entry2.set_text("")
        self.entry3.set_sensitive(True)
        self.entry3.set_text("")
        self.entry4.set_sensitive(True)
        self.entry4.set_text("")
        self.entry5.set_sensitive(True)
        self.entry5.set_text("")
        self.entry6.set_sensitive(True)
        self.entry6.set_text("")

    # 4to Boton envia a la BD
    def on_enviar_clicked(self, widget, data=None):  # Send Contribuyentes data to DB
        global Inscripcion
        Inscripcion = self.entry1.get_text()
        self.inscripcion = (self.entry2.get_text()).strip()
        self.catastro = (self.entry3.get_text()).strip()
        print "Catastro:", self.catastro
        self.rif = (self.entry4.get_text()).strip()
        self.nombre = (self.entry5.get_text()).strip()
        self.direccion = (self.entry6.get_text()).strip()
        self.filename = self.inscripcion + '.pdf'  # Este va para designar archivo que se guardara en BD.

        orden = "INSERT IGNORE INTO contribuyentes (inscripcion, catastro, rif, nombre, direccion, archivo)"
        datos = "VALUES ('" + self.inscripcion + "','" + self.catastro + "','" + self.rif + "','" + self.nombre + "','" + self.direccion + "','" + self.filename + "')"
        self.comando = orden + datos
        self.bdpointer.execute(self.comando)

        subprocess.Popen(['./pbar_TX.sh'], shell=True)  # Inicio transferencia hacia BD

        reporte = open('Inscripcion.txt', 'a+')
        reporte.write(repr(Inscripcion) + '\n')
        reporte.close()

        for proc in psutil.process_iter():
            if proc.name() == "display":
                proc.kill()

        # after sending data clear all the text from the text entries
        self.entry1.set_sensitive(True)
        self.entry1.set_text("")
        self.entry2.set_sensitive(True)
        self.entry2.set_text("")
        self.entry3.set_sensitive(True)
        self.entry3.set_text("")
        self.entry4.set_sensitive(True)
        self.entry4.set_text("")
        self.entry5.set_sensitive(True)
        self.entry5.set_text("")
        self.entry6.set_sensitive(True)
        self.entry6.set_text("")

        self.mainWindow.show()

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        subprocess.Popen(['python Thanks.py'], shell=True)

    # 5to Boton
    def on_cerrar_clicked(self):
        #main_quit()

        # Este debe capturar la variable Inscripcion de arriba para generar reporte enviados a BD que le envia reporte al Supervisor
        subprocess.Popen([config.DIROP + '/sendPDF.py'], shell=True)

        # Este debe capturar la variable Inscripcion de arriba para generar reporte falla que le envia reporte al Supervisor
        subprocess.Popen([config.DIROP + '/sendPDFfix.py'], shell=True)

    def main(self):
        gtk.main()

Clientes()
gtk.main()
