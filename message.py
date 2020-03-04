import imghdr
import smtplib
import os.path
from email.message import EmailMessage

def createMessage(user,subject,body,picturepath):
    msg = EmailMessage()
    msg['Subject']= subject
    msg['From'] = user
    msg['To'] = user
    msg.set_content(body)
    if os.path.isfile(picturepath):
        with open(picturepath, 'rb') as archivoAttacheado:
            file_data = archivoAttacheado.read()
            file_type = imghdr.what(archivoAttacheado.name)
            file_name = archivoAttacheado.name
            msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
    return msg

def enviar(unMensaje,user,password):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)  # servidor y puerto al que se conecta
    smtp.ehlo()  # esto nos identifica en la red
    smtp.starttls()  # encripta el trafico
    smtp.ehlo()
    smtp.login(user,password)  # se logea en el servidor con tus credenciales
    smtp.send_message(unMensaje)

