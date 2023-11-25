import tkinter as tk
from tkinter import ttk, messagebox
from modules.consultas import infoVuelo

class Informacion(tk.Toplevel):
    def __init__(self, parent, idvuelos):
        super().__init__(parent, bg="PaleTurquoise1")
        self.title("Informacion")
        self.campos()
        self.resizable(0,0)
        self.parent = parent
        self.idVuelos = idvuelos
        self.mostrarInformacion()

    def volver_a_frame(self):
        self.destroy()
        self.parent.deiconify()

    def campos(self):
        #label
        self.numeroVuelo = tk.Label(self, text="Número Vuelo")
        self.numeroVuelo.config(width=15, bg="PaleTurquoise1", fg="black", anchor="w", font=("Comic Sans MS", 12))
        self.numeroVuelo.grid(row=0, column=0, padx=10, pady=7)

        self.origen = tk.Label(self, text="Origen")
        self.origen.config(width=15, bg="PaleTurquoise1", fg="black", anchor="w", font=("Comic Sans MS", 12))
        self.origen.grid(row=1, column=0, padx=10, pady=7)

        self.destino = tk.Label(self, text="Destino")
        self.destino.config(width=15, bg="PaleTurquoise1", fg="black", anchor="w", font=("Comic Sans MS", 12))
        self.destino.grid(row=2, column=0, padx=10, pady=7)

        self.fecha = tk.Label(self, text="Fecha")
        self.fecha.config(width=15, bg="PaleTurquoise1", fg="black", anchor="w", font=("Comic Sans MS", 12))
        self.fecha.grid(row=3, column=0, padx=10, pady=7)

        self.Horario = tk.Label(self, text="Horario")
        self.Horario.config(width=15, bg="PaleTurquoise1", fg="black", anchor="w", font=("Comic Sans MS", 12))
        self.Horario.grid(row=4, column=0, padx=10, pady=7)

        self.Precio = tk.Label(self, text="Precio")
        self.Precio.config(width=15, bg="PaleTurquoise1", fg="black", anchor="w", font=("Comic Sans MS", 12))
        self.Precio.grid(row=5, column=0, padx=10, pady=7)

        self.capacidad = tk.Label(self, text="Capacidad")
        self.capacidad.config(width=15, bg="PaleTurquoise1", fg="black", anchor="w", font=("Comic Sans MS", 12))
        self.capacidad.grid(row=6, column=0, padx=10, pady=7)

        self.puestosDisponibles = tk.Label(self, text="Puestos Disponibles")
        self.puestosDisponibles.config(width=15, bg="PaleTurquoise1", fg="black", anchor="w", font=("Comic Sans MS", 12))
        self.puestosDisponibles.grid(row=7, column=0, padx=13, pady=7)

        self.puestosOcupados = tk.Label(self, text="Puestos Ocupados")
        self.puestosOcupados.config(width=15, bg="PaleTurquoise1", fg="black", anchor="w", font=("Comic Sans MS", 12))
        self.puestosOcupados.grid(row=8, column=0, padx=10, pady=7)

        self.puestosReservados = tk.Label(self, text="puestos Reservados")
        self.puestosReservados.config(width=15, bg="PaleTurquoise1", fg="black", anchor="w", font=("Comic Sans MS", 12))
        self.puestosReservados.grid(row=9, column=0, padx=10, pady=7)

        #ENTRY
        self.valor_NumeroVuelo=tk.StringVar()
        self.cam_NumeroVuelo=tk.Entry(self, textvariable=self.valor_NumeroVuelo)
        self.cam_NumeroVuelo.config(width=40)
        self.cam_NumeroVuelo.grid(row=0, column=1, padx=15, pady=8)

        self.valor_Origen=tk.StringVar()
        self.cam_Origen=tk.Entry(self, textvariable=self.valor_Origen)
        self.cam_Origen.config(width=40)
        self.cam_Origen.grid(row=1, column=1, padx=15, pady=8, columnspan=2)

        self.valor_Destino=tk.StringVar()
        self.cam_Destino=tk.Entry(self, textvariable=self.valor_Destino)
        self.cam_Destino.config(width=40)
        self.cam_Destino.grid(row=2, column=1, padx=15, pady=8, columnspan=2)

        self.valor_Fecha=tk.StringVar()
        self.cam_Fecha=tk.Entry(self, textvariable=self.valor_Fecha)
        self.cam_Fecha.config(width=40)
        self.cam_Fecha.grid(row=3, column=1, padx=15, pady=8, columnspan=2)

        self.valor_Horario=tk.StringVar()
        self.cam_Horario=tk.Entry(self, textvariable=self.valor_Horario)
        self.cam_Horario.config(width=40)
        self.cam_Horario.grid(row=4, column=1, padx=15, pady=8, columnspan=2)

        self.valor_Precio=tk.StringVar()
        self.cam_Precio=tk.Entry(self, textvariable=self.valor_Precio)
        self.cam_Precio.config(width=40)
        self.cam_Precio.grid(row=5, column=1, padx=15, pady=8, columnspan=2)

        self.valor_Capacidad=tk.StringVar()
        self.cam_Capacidad=tk.Entry(self, textvariable=self.valor_Capacidad)
        self.cam_Capacidad.config(width=40)
        self.cam_Capacidad.grid(row=6, column=1, padx=15, pady=8, columnspan=2)

        self.valor_PuestosD=tk.StringVar()
        self.cam_PuestosD=tk.Entry(self, textvariable=self.valor_PuestosD)
        self.cam_PuestosD.config(width=40)
        self.cam_PuestosD.grid(row=7, column=1, padx=15, pady=8, columnspan=2)

        self.valor_PuestosO=tk.StringVar()
        self.cam_PuestosO=tk.Entry(self, textvariable=self.valor_PuestosO)
        self.cam_PuestosO.config(width=40)
        self.cam_PuestosO.grid(row=8, column=1, padx=15, pady=8, columnspan=2)

        self.valor_PuestosR=tk.StringVar()
        self.cam_PuestosR=tk.Entry(self, textvariable=self.valor_PuestosR)
        self.cam_PuestosR.config(width=40)
        self.cam_PuestosR.grid(row=9, column=1, padx=15, pady=8, columnspan=2)

        #botones
        self.Boton_Regresar = tk.Button(self, text="Regresar")
        self.Boton_Regresar.config(width=10, bg="IndianRed1",fg="red4",activebackground="IndianRed4",activeforeground="#000",cursor="hand2", command=self.volver_a_frame, font=("Comic Sans MS", 10))
        self.Boton_Regresar.grid(row=10, column=1, pady= 10)

    def mostrarInformacion(self):
        informacion = infoVuelo(self.idVuelos)
        self.cam_NumeroVuelo.insert(0, informacion[0])
        self.cam_Origen.insert(0, informacion[1])
        self.cam_Destino.insert(0, informacion[2])
        self.cam_Fecha.insert(0, informacion[3])
        self.cam_Horario.insert(0, informacion[4])
        self.cam_Precio.insert(0, informacion[5])
        self.cam_Capacidad.insert(0, informacion[6])
        self.cam_PuestosD.insert(0, informacion[7])
        self.cam_PuestosO.insert(0, informacion[8])
        self.cam_PuestosR.insert(0, informacion[9])
       


        