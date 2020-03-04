import os.path

def archivoVacio(rutaArchivo):
    archivo=open(rutaArchivo,'r')
    contenido=archivo.read()
    archivo.close()
    if contenido == '': return True
    else: return False

def existeArchivo(rutaArchivo):
    return os.path.isfile(rutaArchivo)

def hayDatos(filepath):
    if (existeArchivo(filepath)):
        if (archivoVacio(filepath)):
            return False
        else: return True
    else: return False

def crearArchivo(rutaArchivo):
    nuevoArchivo = open(rutaArchivo,'w')
    nuevoArchivo.close()

def grabarArchivo(user,password):
    archivo=open('C:\GaussTheMaster\credentials.txt','w')
    archivo.write(user)
    archivo.write('\n')
    archivo.write(password)
    archivo.close()

def leerCredenciales():
    credentials = open('C:\GaussTheMaster\credentials.txt','r')
    username=credentials.readline()
    password=credentials.readline()
    credentials.close()
    return [username,password]



