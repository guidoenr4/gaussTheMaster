# Gauss The Master
    # @autor: Guido Enrique
    # @last-version: 18/2/2020 - 12:32

from distutils.core import setup

import login,comprobarDatos,info,message

def run():
    info.camera.takePicture()
    today_date = info.clock().today_date()
    ipAddress = info.ip.ipAddress()

    user = comprobarDatos.leerCredenciales()[0]
    pw = comprobarDatos.leerCredenciales()[1]

    contenido = info.description(fecha=today_date,ipAddress=ipAddress)

    msg = message.createMessage(user=user,subject='[gauss-the-master]: New login report',body=contenido.cuerpo(),picturepath='C:\GaussTheMaster\snap.png')

    print(contenido.cuerpo())

if __name__ == '__main__':
    if not comprobarDatos.hayDatos('C:\GaussTheMaster\credentials.txt'):
        login.logearse()
    else: run()







