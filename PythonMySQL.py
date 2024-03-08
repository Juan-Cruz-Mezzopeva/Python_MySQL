import tkinter as tk

# Importar modulos restantes de tkinter

from tkinter import *
from tkinter import  ttk
from tkinter import messagebox

# Importar clientes y conexion
from Clientes import *
from Conexion import *

class FormularioClientes:

    global textBoxId
    textBoxId = None

    global textBoxNombre
    textBoxNombre = None
    
    global textBoxApellido
    textBoxApellido = None

    global combo
    combo = None

    global base
    base = None

    global tree
    tree = None

    global groupBox
    groupBox = None


def Formulario():
    global groupBox
    global textBoxId
    global textBoxNombre
    global textBoxApellido
    global combo
    global base
    global tree
    try:
        base = Tk()
        base.geometry("1200x300")
        base.title("Formulario Python")
        groupBox = LabelFrame(base, text='Datos del Personal', padx=5, pady=5)
        groupBox.grid(row=0, column=0, padx=10, pady=10 )

        labelId = Label(groupBox,text="Id", width=13, font=("arial", 12)).grid(row=0, column=0)
        textBoxId = Entry(groupBox)
        textBoxId.grid(row=0, column=1)

        labelNombre = Label(groupBox,text="Nombre", width=13, font=("arial", 12)).grid(row=1, column=0)
        textBoxNombre = Entry(groupBox)
        textBoxNombre.grid(row=1, column=1)

        labelApellido = Label(groupBox,text="Apellido", width=13, font=("arial", 12)).grid(row=2, column=0)
        textBoxApellido = Entry(groupBox)
        textBoxApellido.grid(row=2, column=1)

        labelSexo = Label(groupBox,text="Sexo", width=13, font=("arial", 12)).grid(row=3, column=0)
        seleccionSexo = tk.StringVar()
        combo = ttk.Combobox(groupBox, values= ["Masculino", "Femenino"], textvariable=seleccionSexo )
        combo.grid(row=3, column=1)
        seleccionSexo.set("Masculino")

        Button(groupBox, text="Gruardar", width=10, command=guardarRegistros).grid(row=4, column=0)
        Button(groupBox, text="Modificar", width=10).grid(row=4, column=1)
        Button(groupBox, text="Eliminar", width=10).grid(row=4, column=2)

        groupBox = LabelFrame(base, text='Lista del Personal', padx=5, pady=5)
        groupBox.grid(row=0, column=1, padx=5, pady=5)

        # Crear un Treeview
        # Configurar las columnas

        tree = ttk.Treeview(groupBox, columns=("Id","Nombres","Apellidos", "Sexo"), show="headings", height=5)
        tree.heading("# 1", text="Id")
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 2", text="Nombre")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 3", text="Apellido")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 4", text="Sexo")
        tree.column("# 4", anchor=CENTER)
        tree.pack()

        base.mainloop()

    except ValueError as error:
        print("Error al mostrar la interfaz, error {}".format(error))
    
def guardarRegistros():

    global textBoxNombre, textBoxApellido, combo, groupBox


    try:
        pass
        #Verificar si los widgets de los entry ya estan inicialisados 
        if textBoxNombre is None  or textBoxApellido is None  or combo is None or groupBox is None:
            print("los widgets no estan inicializados")
            return
        
        nombres = textBoxNombre.get()
        apellidos = textBoxApellido.get()
        sexo = combo.get()

        CClientes.ingresarClientes(nombres,apellidos,sexo)
        messagebox.showinfo("Informacion", "los datos fueron guardados")

        #Limpiar los campos

        textBoxNombre.delete(0,END)
        textBoxApellido.delete(0,END)
        
    except ValueError as error:
        print("Error al ingresar los datos {}".format(error))



Formulario()