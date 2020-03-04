from tkinter import *
import comprobarDatos


def logearse():
    root = Tk()
    root.title('gauss-the-master')
    root.resizable(False, False)  # es para ver si la podes mover (X,Y)
    root.iconbitmap('interfaz/gaussIco.ico')
    root.geometry('800x500')  # pixeles de tamaño al iniciarse
    root.config(bg='purple')  # color de fondo

    background = PhotoImage(file='interfaz/background.png')
    backgroundLabel = Label(root, image=background).place(x=-2, y=0)

    gmailEntry=Entry(bg='black',fg='medium spring green',font='Consolas 12')
    gmailEntry.place(x=350,y=205)
    passwordEntry=Entry(bg='black',fg='cyan',font='Consolas 12',show='*')
    passwordEntry.place(x=350,y=260)

    def guardarDatos():
        user=gmailEntry.get()
        password=passwordEntry.get()
        confirmacionLabel=Label(root,text='Datos guardados exitosamente',font='Helvetica 10',bg='black',fg='medium spring green').place(x=300,y=300)
        comprobarDatos.grabarArchivo(user,password)

    button = Button(root,text='Guardar',bg='black',fg='medium spring green',activebackground='purple',font='Consolas 12',command = guardarDatos)
    button.place(x=350,y=350)

    root.mainloop()

