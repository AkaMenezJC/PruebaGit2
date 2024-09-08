"""
Proyecto software de escritorio
"""
from tkinter import *
import os
from PIL import Image,ImageTk,ImageColor
from tkinter.messagebox  import *

#Ventana
root= Tk ()
root.title("ProjectSoft")
root.geometry ()


#Centrar ventana
#root.eval ("tk::PlaceWindow . center")
Width_root= 500
Height_root=600

#Centrar ventana metodo dinámico.
Width_Screen= root.winfo_screenwidth()
Height_Screen= root.winfo_screenheight()


#Carga de carpeta principal
Folderprimary= os.path.dirname (__file__)

#Carpetas secundarias
FolderGraphicsIMG= os.path.join(Folderprimary, "GraphicsIMG")

#Subcarpetas secundarias
FolderIcon= os.path.join(FolderGraphicsIMG, "Icon")
FolderIMG=  os.path.join(FolderGraphicsIMG, "IMG")

#Carga de icono en la ventana
root.iconbitmap(os.path.join(FolderIcon, "Icon_1.ico"))

#Carga de la imagen de fondo
FondoIMG= ImageTk.PhotoImage(Image.open(os.path.join(FolderIMG, "Fondo_o.png")).resize((500,500)))
Fondo= Label(image= FondoIMG,)
Fondo.grid (row= 5,
            column = 0)

#Etiquetas, usuario y contraseña. (Salida texto y entrada de teclado)
User= Label(root,
            text="Usuario",
            border= 10,
            )
User.grid(row= 0, column= 0)
UserEntry= Entry(root,
                 background= "wheat1",)
UserEntry.grid(row= 1,
               column= 0)
UserEntry.insert(0, "Ej: Jcuartas")
UserEntry.bind("<Button-1>",
               lambda e : UserEntry.delete (0,END))

#Etiqueta y string contraseña
Password= Label(root,
                text="Contraseña")
Password.grid(row= 2, column= 0)
PasswordEntry= Entry(root,
                     background= "wheat1",)
PasswordEntry.grid(row= 3,
                   column= 0)
PasswordEntry.insert(0,"*"*9)
PasswordEntry.bind("<Button-1>",
                   lambda e : PasswordEntry.delete (0,END))

#Base de registro con tupla.
UserCreate= ("Jcuartas", "Jd199923.")


#Botton de envio, funcion o evento.
def button_env():
    UserReg= UserEntry.get()
    PasswordReg= PasswordEntry.get()
    if PasswordReg not in UserCreate or UserReg not in UserCreate:
        showwarning("Error",
                 """¡Usuario o contraseña incorrecto!
                 \nImportante: recuerda escribir bien tu contraseña
                 \n\n¡Intentalo nuevamente!""")
    elif UserReg in UserCreate and PasswordReg in UserCreate:
        showinfo("Bienvenido",
                 "¡Usuario y contraseña correcto!\nAhora puedes acceder a nuestro sistema.")
    else:
        pass
#Evento de boton en la ventana y comando a desencadenar
Button_Send= Button (root,
                     text="Enviar",
                     command= button_env,
                     background= "darkgoldenrod",
                    )
Button_Send.grid(row= 4, column= 0)



#Ejecución permanente de la ventana
root.mainloop ()