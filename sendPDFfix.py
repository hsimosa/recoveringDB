#!/usr/bin/python
# -*- coding: utf-8 -*-

#Envia reporte de falla en archivos pdf
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
from email.Utils import formatdate
import os

gmail_user = "XXX@gmail.com"
gmail_pwd = ""

def mail(to, subject, text, attach):
   msg = MIMEMultipart()
   fecha = formatdate(localtime=True)
   msg['From'] 		= gmail_user
   msg['To'] 		= to
   msg['Subject'] 	= subject
   #msg['Date']    	= fecha
   msg.attach(MIMEText(text))

   part = MIMEBase('application', 'octet-stream')
   part.set_payload(open(attach, 'rb').read())
   Encoders.encode_base64(part)
   part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
   msg.attach(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()

mail( 'ZZZZ@gmail.com',
   "Relacion de archivos Inscripcion malos",
   "Confirmacion de envio de las siguientes numeros de inscripcion en fecha:"+formatdate(localtime=True),
   "Reparacion.pdf")
   

   
