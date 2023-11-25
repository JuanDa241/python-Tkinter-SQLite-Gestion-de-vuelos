import tkinter as tk
from tkinter import ttk, messagebox
from packs.gui_informacion import Informacion
from packs.gui_reserva import Reserva
from packs.gui_verReserva import VerReserva
from packs.gui_listaEspera import ListaEspera
from packs.gui_Usuarios import Usuarios
from modules.consultas import Cliente, InsertData, ShowVuelo, buscar

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root,width=300,height=300, bg="PaleTurquoise1")
        self.root = root
        self.pack()
        self.campos()
        self.limpiar()
        self.barra_menu()
        self.Tabla_Datos()
    
    #Barra de opciones
    def barra_menu (self):
        self.barra_menu = tk.Menu()
        self.root.config(menu=self.barra_menu, width=100, height=100)

        self.menu_home = tk.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label="Home", menu=self.menu_home)
        self.menu_home.add_command(label="Exit", command=self.root.destroy)

        self.menu_reservas = tk.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label="Reservas", command=self.abrir_vereserva)

        self.menu_listEspera = tk.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label="Lista de espera", command=self.abrir_listaEspera)    

        self.menu_Usuario = tk.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label="Usuarios", command=self.abrir_Usuarios)    
    
    #Metodo Abrir ventana  para ver las reservas existentes
    def abrir_vereserva(self):
        self.root.withdraw()
        self.verReser = VerReserva(self.root)
    #Metodo para abrir la ventana de lista de espera
    def abrir_listaEspera(self):
        self.root.withdraw()
        self.listEspera = ListaEspera(self.root)
    #Metodo para abrir la ventana para ver la informacion de los usuarios
    def abrir_Usuarios(self):
        self.root.withdraw()
        self.listEspera = Usuarios(self.root)
    #Metodo para abrir la ventana para hacer las reservas
    def abrir_ventana_reserva(self):
        self.root.withdraw()
        self.reser = Reserva(self.root, self.numeroVuelo, self.origen, self.destino)     
    #Metodo para abrir la ventana para ver la informacion de un vuelo seleccionado
    def abrir_ventana_informacion(self):
        self.root.withdraw()
        informacion = Informacion(self.root, self.idVuelos)
        

    def campos(self):
        #titulos de los label
        self.usuario = tk.Label(self, text="Registros de usuarios")
        self.usuario.config(width=20,bg="PaleTurquoise1", fg="black", font=("Comic Sans MS", 15, "bold"))
        self.usuario.grid( columnspan=3,row=0, column=0, padx=10, pady=10)
        
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

        self.vuelos = tk.Label(self, text="Vuelos")
        self.vuelos.config(bg="PaleTurquoise1", fg="black", anchor="w", font=("Comic Sans MS", 15))
        self.vuelos.grid(row=0, column=3, columnspan=1)

        #campos de valor "Entry"
        self.valor_cedula=tk.IntVar()
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

        self.valor_edad=tk.IntVar()
        self.cam_edad=tk.Entry(self, textvariable=self.valor_edad)
        self.cam_edad.config(width=30)
        self.cam_edad.grid(row=4, column=1, padx=5, pady=5, columnspan=2)

        self.valor_Vuelo=tk.StringVar()
        self.cam_Vuelo=tk.Entry(self, textvariable=self.valor_Vuelo)
        self.cam_Vuelo.config(width=50)
        self.cam_Vuelo.grid(row=0, column=4, padx=5, pady=5, columnspan=2)

        #botones
        self.Boton_Registrar = tk.Button(self, text="Registrar")
        self.Boton_Registrar.config(width=10, bg="light sea green",fg="dark slate gray",activebackground="cornflower blue",activeforeground="black",cursor="hand2", command=self.crearUsuario, font=("Comic Sans MS", 10))
        self.Boton_Registrar.grid(row=6, column=0, padx=30)

        self.Boton_Nuevo = tk.Button(self, text="Nuevo")
        self.Boton_Nuevo.config(width=10, bg="spring green",fg="dark slate gray",activebackground="sea green",activeforeground="PaleTurquoise1",cursor="hand2", command=self.nuevoUsuario, font=("Comic Sans MS", 10, "bold"))
        self.Boton_Nuevo.grid(row=6, column=1)

        self.Boton_Limpiar = tk.Button(self, text="Limpiar")
        self.Boton_Limpiar.config(width=10, bg="IndianRed1",fg="dark slate gray",activebackground="IndianRed4",activeforeground="black",cursor="hand2", command=self.limpiar, font=("Comic Sans MS", 10))
        self.Boton_Limpiar.grid(row=6, column=2,padx=30)
        
        self.Boton_Filtrar = tk.Button(self, text="Buscar", command=self.filtrar)
        self.Boton_Filtrar.config(width=15, bg="light sea green",fg="dark slate gray",activebackground="cornflower blue",activeforeground="black",cursor="hand2", font=("Comic Sans MS", 10))
        self.Boton_Filtrar.grid(row=0, column=6)

        self.Boton_Reservar = tk.Button(self, text="Reservar", command=self.reserva)
        self.Boton_Reservar.config(width=14, bg="light sea green", fg="dark slate gray", activebackground="cornflower blue", activeforeground="black", cursor="hand2", font=("Comic Sans MS", 10))
        self.Boton_Reservar.grid(row=8, column=5, pady=20)

        self.Boton_Informacion = tk.Button(self, text="Informacion", command=self.idvuelo)
        self.Boton_Informacion.config(width=14, bg="RoyalBlue1", fg="dark slate gray", activebackground="cornflower blue", activeforeground="black", cursor="hand2", font=("Comic Sans MS", 10))
        self.Boton_Informacion.grid(row=8, column=6, pady=20)

        self.Boton_Actualizar = tk.Button(self, text="Actualizar", command=self.actualizar)
        self.Boton_Actualizar.config(width=14, bg="DarkOrchid1", fg="dark slate gray", activebackground="orchid4", activeforeground="black", cursor="hand2", font=("Comic Sans MS", 10))
        self.Boton_Actualizar.grid(row=8, column=4, pady=20)
        
        # Tabla para mostrar toda la informacion de los vuelos
    def Tabla_Datos(self):
        informacionVuelos = ShowVuelo()
        self.tabla = ttk.Treeview(self)
        self.tabla.config(columns=('origen','destino','fecha','horario','precio','puestosDisponibles'))
        self.tabla.grid(row=1,column=3, columnspan=4, rowspan=6, padx=15)

        self.tabla.tag_configure("oddrow", background="white")
        self.tabla.tag_configure("evenrow", background="PaleTurquoise1")

        self.tabla.heading("#0", text="NUMERO VUELO")
        self.tabla.column("#0",width=120, anchor= "center")
        self.tabla.heading("#1",text="ORIGEN")
        self.tabla.column("#1",width=100)
        self.tabla.heading("#2",text="DESTINO")
        self.tabla.column("#2",width=85)
        self.tabla.heading("#3",text="FECHA")
        self.tabla.column("#3",width=80, anchor= "center")
        self.tabla.heading("#4",text="HORARIO")
        self.tabla.column("#4",width=60, anchor= "center")
        self.tabla.heading("#5",text="PRECIO")
        self.tabla.column("#5",width=80, anchor= "center")
        self.tabla.heading("#6",text="PUESTOS DISPONIBLES")   
        self.tabla.column("#6",width=130, anchor= "center")

        #Mostrar la informacion en la tabla
        for i in informacionVuelos:
            self.tabla.insert('',i[0], text=i[0], values=(i[1],i[2],i[3],i[4],i[5],i[6]))
    # Metodo para habilitar los entry y los botenes de registrar y limpiar 
    # al momento de registar un nuevo usuario
    def nuevoUsuario(self):
        self.cam_cedula.config(state="normal")
        self.cam_nombre.config(state="normal")
        self.cam_apellido.config(state="normal")
        self.cam_edad.config(state="normal")

        self.Boton_Registrar.config(state="normal")
        self.Boton_Limpiar.config(state="normal")

    def crearUsuario(self):
        self.cedula = self.cam_cedula.get()
        self.nombre = self.cam_nombre.get()
        self.apellido = self.cam_apellido.get()
        self.edad = self.cam_edad.get()

        informacion = Cliente(self.cedula, self.nombre, self.apellido, self.edad)
        titulo = 'Crear usuario'
        texto = 'Usuario creado con exito'
        m = messagebox.showinfo(titulo, texto)
        InsertData(informacion)

    def limpiar(self):
         self.cedula = None
         self.valor_cedula.set("")
         self.valor_nombre.set("")
         self.valor_apellido.set("")
         self.valor_edad.set("")

         self.cam_cedula.config(state="disabled")
         self.cam_nombre.config(state="disabled")
         self.cam_apellido.config(state="disabled")
         self.cam_edad.config(state="disabled")

         self.Boton_Registrar.config(state="disabled")
         self.Boton_Limpiar.config(state="disabled")
    
    def filtrar(self):
        busqueda = self.cam_Vuelo.get()
        informacionVuelos = self.tabla.get_children()
        for informacionVuelo in informacionVuelos:
            self.tabla.delete(informacionVuelo)
        try:
            datos = buscar(busqueda)
            for i in datos:
                self.tabla.insert('',i[0], text=i[0], values=(i[1],i[2],i[3],i[4],i[5],i[6]))
        except:
            titulo = 'Buscar'
            texto = 'No se encontro'
            messagebox.showerror(titulo,texto)
        

    def reserva(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            titulo = 'Alerta'
            texto = 'Por favor, seleccionar un elemento de la tabla para reservar un vuelo'
            messagebox.showwarning(titulo, texto)
        else:
            self.numeroVuelo = self.tabla.item(self.tabla.selection())['text']
            self.origen = self.tabla.item(self.tabla.selection())['values'][0]
            self.destino = self.tabla.item(self.tabla.selection())['values'][1]
            self.abrir_ventana_reserva()
            return self.numeroVuelo, self.origen, self.destino
    
    def idvuelo(self):
        self.idVuelos = self.tabla.item(self.tabla.selection())['text']
        self.abrir_ventana_informacion()

    def actualizar(self):
        self.Tabla_Datos()


    