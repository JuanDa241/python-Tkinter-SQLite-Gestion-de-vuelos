import tkinter as tk
from tkinter import ttk, messagebox
from modules.consultas import Usuario, DeleteClientes, actualizar, Cliente

class Usuarios(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, bg= "PaleTurquoise1")
        self.title("Usuarios")
        self.Tabla_Usuarios()
        self.resizable(0,0)
        self.campos()
        self.parent = parent
    #Metodo para volver a la ventana principal
    def volver_a_frame(self):
        self.destroy()
        self.parent.deiconify()
    
    #Tabla para mostrar la informacion de los usuarios
    def Tabla_Usuarios(self):
        informacionUser = Usuario()
        self.tabla = ttk.Treeview(self)
        self.tabla.config(columns=('nombre','apellido','edad'))
        self.tabla.grid(row=1,column=3, columnspan=4, rowspan=6, padx=15)

        self.tabla.tag_configure("oddrow", background="white")
        self.tabla.tag_configure("evenrow", background="PaleTurquoise1")

        self.tabla.heading("#0", text="DOCUMENTO")
        self.tabla.column("#0",width=120, anchor= "center")
        self.tabla.heading("#1",text="NOMBRE")
        self.tabla.column("#1",width=80, anchor= "center")
        self.tabla.heading("#2",text="APELLIDO")
        self.tabla.column("#2",width=80, anchor= "center")
        self.tabla.heading("#3",text="EDAD")
        self.tabla.column("#3",width=80, anchor= "center")

        #Mostrar la informacion en la tablas
        for i in informacionUser:
            self.tabla.insert('',i[0], text=i[0], values=(i[1],i[2],i[3]))
    
    
    def update(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            titulo = 'Alerta'
            texto = 'Por favor, seleccionar un elemento de la tabla para actualizar un usuario'
            messagebox.showwarning(titulo, texto)
        else:
             self.Editar()
            
    def campos(self):
        self.usuario = tk.Label(self, text="")
        self.usuario.config(width=20,bg="PaleTurquoise1")
        self.usuario.grid( columnspan=3,row=0, column=0, padx=10, pady=10)

        #titulos de los label
        self.cedula = tk.Label(self, text="Cedúla")
        self.cedula.config(bg="PaleTurquoise1", fg="black", anchor="e", font=("Comic Sans MS", 10))
        self.cedula.grid(row=1, column=0,)
            
        self.nombre = tk.Label(self, text="Nombre")
        self.nombre.config(bg="PaleTurquoise1", fg="black", anchor="w", font=("Comic Sans MS", 10))
        self.nombre.grid(row=2, column=0)

        self.apellido = tk.Label(self, text="Apellido")
        self.apellido.config(bg="PaleTurquoise1", fg="black", anchor="w", font=("Comic Sans MS", 10))
        self.apellido.grid(row=3, column=0)

        self.edad = tk.Label(self, text="Edad")
        self.edad.config(bg="PaleTurquoise1", fg="black", anchor="w", font=("Comic Sans MS", 10))
        self.edad.grid(row=4, column=0)

        #campos de valor "Entry"
        self.valor_cedula=tk.StringVar()
        self.cam_cedula=tk.Entry(self, textvariable=self.valor_cedula)
        self.cam_cedula.config(width=30)
        self.cam_cedula.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

        self.valor_nombre=tk.StringVar()
        self.cam_nombre=tk.Entry(self, textvariable=self.valor_nombre)
        self.cam_nombre.config(width=30)
        self.cam_nombre.grid(row=2, column=1, padx=5, pady=5, columnspan=2)

        self.valor_apellido=tk.StringVar()
        self.cam_apellido=tk.Entry(self, textvariable=self.valor_apellido)
        self.cam_apellido.config(width=30)
        self.cam_apellido.grid(row=3, column=1, padx=5, pady=5, columnspan=2)

        self.valor_edad=tk.StringVar()
        self.cam_edad=tk.Entry(self, textvariable=self.valor_edad)
        self.cam_edad.config(width=30)
        self.cam_edad.grid(row=4, column=1, padx=5, pady=5, columnspan=2)
    
        #botones
        self.Boton_Regresar = tk.Button(self, text="Regresar")
        self.Boton_Regresar.config(width=10, bg="IndianRed1",fg="red4",activebackground="IndianRed4",activeforeground="black",cursor="hand2", command=self.volver_a_frame, font=("Comic Sans MS", 10))
        self.Boton_Regresar.grid(row=12, column=4, pady=10)

        self.Boton_Actualizar = tk.Button(self, text="Actualizar")
        self.Boton_Actualizar.config(width=14, bg="DarkOrchid1", fg="dark slate gray", activebackground="orchid4", activeforeground="black", cursor="hand2",command=self.update, font=("Comic Sans MS", 10))
        self.Boton_Actualizar.grid(row=12, column=1, pady=20)

        self.Boton_Guardar = tk.Button(self, text="Guardar")
        self.Boton_Guardar.config(width=14, bg="DarkOrchid1", fg="dark slate gray", activebackground="orchid4", activeforeground="black", cursor="hand2",command=self.Guardar, font=("Comic Sans MS", 10))
        self.Boton_Guardar.grid(row=12, column=2, padx=15, pady=20)

        self.Boton_Eliminar = tk.Button(self, text="Eliminar")
        self.Boton_Eliminar.config(width=10, bg="IndianRed1",fg="dark slate gray",activebackground="IndianRed4",activeforeground="black",cursor="hand2",command=self.Borrar, font=("Comic Sans MS", 10))
        self.Boton_Eliminar.grid(row=12, column=3,padx=30)

    def Borrar(self):
        self.documento = self.tabla.item(self.tabla.selection())['text']
        i = messagebox.askquestion('Informacion','¿Desea eliminar?')
        if i == 'yes':
           DeleteClientes(self.documento)
           self.Tabla_Usuarios()

    def Editar(self):
        self.eliminar()
        self.documento = self.tabla.item(self.tabla.selection())['text']
        self.nombre = self.tabla.item(self.tabla.selection())['values'][0]
        self.apellido = self.tabla.item(self.tabla.selection())['values'][1]
        self.edad = self.tabla.item(self.tabla.selection())['values'][2]
        self.cam_cedula.insert(0, self.documento)
        self.cam_nombre.insert(0, self.nombre)
        self.cam_apellido.insert(0, self.apellido)
        self.cam_edad.insert(0, self.edad)

    def Guardar(self):
        self.documento = self.valor_cedula.get()
        self.nombre = self.valor_nombre.get()
        self.apellido = self.valor_apellido.get()
        self.edad = self.valor_edad.get()
        client = Cliente(self.documento,self.nombre, self.apellido, self.edad)
        actualizar(client, self.documento)
        self.eliminar()
        self.Tabla_Usuarios()
    
    def eliminar(self):
        self.valor_cedula.set("")
        self.valor_nombre.set("")
        self.valor_apellido.set("")
        self.valor_edad.set("")
