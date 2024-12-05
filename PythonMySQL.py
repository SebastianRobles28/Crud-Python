import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Clientes import *
from Conexion import *

global base, texBoxId, texBoxNombres, texBoxApellidos, groupBox, tree

def Formulario():
    global texBoxId, texBoxNombres, texBoxApellidos, combo, base, groupBox, tree

    try:
        base = tk.Tk()
        base.geometry("1200x300")
        base.title("Formulario Python")

        groupBox = LabelFrame(base, text="Datos del Personal", padx=5, pady=5)
        groupBox.grid(row=0, column=0, padx=10, pady=10)

        labelid = Label(groupBox, text="id:", width=13, font=("arial", 12)).grid(row=0, column=0)
        texBoxId = Entry(groupBox)
        texBoxId.grid(row=0, column=1)

        labelNombres = Label(groupBox, text="Nombres:", width=13, font=("arial", 12)).grid(row=1, column=0)
        texBoxNombres = Entry(groupBox)
        texBoxNombres.grid(row=1, column=1)

        labelApellidos = Label(groupBox, text="Apellidos:", width=13, font=("arial", 12)).grid(row=2, column=0)
        texBoxApellidos = Entry(groupBox)
        texBoxApellidos.grid(row=2, column=1)

        labelSexo = Label(groupBox, text="Sexo:", width=13, font=("arial", 12)).grid(row=3, column=0)
        seleccionSexo = tk.StringVar()
        combo = ttk.Combobox(groupBox, values=["Masculino", "Femenino"], textvariable=seleccionSexo)
        combo.grid(row=3, column=1)
        seleccionSexo.set("Masculino")

        Button(groupBox, text="Guardar", width=10, command=guardarRegistros).grid(row=4, column=0)
        Button(groupBox, text="Modificar", width=10,command=modificarRegistros).grid(row=4, column=1)
        Button(groupBox, text="Eliminar", width=10, command=EliminarRegistros).grid(row=4, column=2)

        groupBox2 = LabelFrame(base, text="Lista del Personal", padx=5, pady=5)
        groupBox2.grid(row=0, column=1, padx=5, pady=5)

        tree = ttk.Treeview(groupBox2, columns=("Id", "Nombres", "Apellidos", "Sexo"), show='headings', height=5)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Id")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Nombres")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Apellidos")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="Sexo")

        for row in CClientes.mostrarClientes():
            tree.insert("", "end", values=row)

        tree.bind("<<TreeviewSelect>>", seleccionarRegistro)

        tree.pack()

        base.mainloop()

    except Exception as error:
        print(f"Error al mostrar la interfaz: {error}")

def guardarRegistros():
    global texBoxNombres, texBoxApellidos, combo, groupBox, tree

    try:
        if texBoxNombres is None or texBoxApellidos is None or combo is None:
            print("Los widgets no están inicializados")
            return

        nombres = texBoxNombres.get()
        apellidos = texBoxApellidos.get()
        sexo = combo.get()

        if not nombres or not apellidos or not sexo:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return

        CClientes.ingresarClientes(nombres, apellidos, sexo)
        messagebox.showinfo("Información", "Los datos fueron guardados.")

        actualizarTreeView()

        texBoxNombres.delete(0, END)
        texBoxApellidos.delete(0, END)

    except Exception as error:
        print(f"Error al guardar los datos: {error}")
        messagebox.showerror("Error", "Hubo un problema al guardar los datos.")

def actualizarTreeView():
    global tree

    try:
        tree.delete(*tree.get_children())

        clientes = CClientes.mostrarClientes()

        if not clientes:
            print("No hay clientes para mostrar.")
            return

        for row in clientes:
            tree.insert("", "end", values=row)

    except Exception as error:
        print(f"Error al actualizar el TreeView: {error}")
        messagebox.showerror("Error", "Hubo un problema al actualizar la tabla.")

def seleccionarRegistro(event):
    try:
        itemseleccionado = tree.focus()

        if itemseleccionado:
            values = tree.item(itemseleccionado)["values"]

            texBoxId.delete(0, END)
            texBoxId.insert(0, values[0])
            texBoxNombres.delete(0, END)
            texBoxNombres.insert(0, values[1])
            texBoxApellidos.delete(0, END)
            texBoxApellidos.insert(0, values[2])
            combo.set(values[3])

    except ValueError as error:
        print("Error al seleccionar registro: {}".format(error))


def modificarRegistros():
    global texBoxId,texBoxNombres, texBoxApellidos, combo, groupBox, tree

    try:
        if texBoxId is None or texBoxNombres is None or texBoxApellidos is None or combo is None:
            print("Los widgets no están inicializados")
            return
        
        idUsuario = texBoxId.get()

        nombres = texBoxNombres.get()
        apellidos = texBoxApellidos.get()
        sexo = combo.get()

        if not nombres or not apellidos or not sexo:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return

        CClientes.modificarClientes(idUsuario,nombres, apellidos, sexo)
        messagebox.showinfo("Información", "Los datos fueron actualizados")

        actualizarTreeView()
        texBoxId.delete(0, END)
        texBoxNombres.delete(0, END)
        texBoxApellidos.delete(0, END)

    except Exception as error:
        print(f"Error al guardar los datos: {error}")
        messagebox.showerror("Error", "Hubo un problema al modificar los datos.")


def EliminarRegistros():
    global texBoxId,texBoxNombres,texBoxApellidos

    try:
        if texBoxId is None :
            print("Los widgets no están inicializados")
            return
        
        idUsuario = texBoxId.get()


        CClientes.EliminarClientes(idUsuario)
        messagebox.showinfo("Información", "Los datos fueron Eliminados")

        actualizarTreeView()
        texBoxId.delete(0, END)
        texBoxNombres.delete(0, END)
        texBoxApellidos.delete(0, END)

    except Exception as error:
        print(f"Error al guardar los datos: {error}")
        messagebox.showerror("Error", "Hubo un problema al modificar los datos.")

Formulario()
