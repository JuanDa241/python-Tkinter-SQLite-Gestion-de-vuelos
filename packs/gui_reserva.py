import tkinter as tk
from tkinter import ttk, messagebox
from modules.consultas import Reservas, reserva, listaEspera, puestoMenos, puestosDisponibles

class Reserva(tk.Toplevel):
    def __init__(self, parent, numeroVuelo, origen, destino):
        super().__init__(parent, bg= "PaleTurquoise1")
        self.title("Reserva")
        self.campos()
        self.resizable(0,0)
        self.parent = parent
        self.numerovuelo = numeroVuelo
        self.datosReserva(numeroVuelo, origen, destino)

    def volver_a_frame(self):
        self.destroy()
        self.parent.deiconify()

    def campos(self):
        #label
        self.cedula = tk.Label(self, text="Cedúla")
        self.cedula.config(width=14, bg="PaleTurquoise1", fg="black", anchor="w", font=("Comic Sans MS", 12))
        self.cedula.grid(row=0, column=0, padx=10, pady=7)

        self.vuelo = tk.Label(self, text="Numero Vuelo")
        self.vuelo.config(width=14, bg="PaleTurquoise1", fg="black", anchor="w", font=("Comic Sans MS", 12))
        self.vuelo.grid(row=1, column=0, padx=10, pady=7)

        self.destino = tk.Label(self, text="Origen")
        self.destino.config(width=14, bg="PaleTurquoise1", fg="black", anchor="w", font=("Comic Sans MS", 12))
        self.destino.grid(row=2, column=0, padx=10, pady=7)

        self.fecha = tk.Label(self, text="Destino")
        self.fecha.config(width=14, bg="PaleTurquoise1", fg="black", anchor="w", font=("Comic Sans MS", 12))
        self.fecha.grid(row=3, column=0, padx=10, pady=7)

        #ENTRY
        self.valor_cedula=tk.StringVar()
        self.cam_cedula=tk.Entry(self, textvariable=self.valor_cedula)
        self.cam_cedula.config(width=35)
        self.cam_cedula.grid(row=0, column=1, columnspan=2, padx=15)

        self.valor_NumeroVuelo=tk.StringVar()
        self.cam_NumeroVuelo=tk.Entry(self, textvariable=self.valor_NumeroVuelo)
        self.cam_NumeroVuelo.config(width=35)
        self.cam_NumeroVuelo.grid(row=1, column=1, padx=15)

        self.valor_Origen=tk.StringVar()
        self.cam_Origen=tk.Entry(self, textvariable=self.valor_Origen)
        self.cam_Origen.config(width=35)
        self.cam_Origen.grid(row=2, column=1, columnspan=2, padx=15)

        self.valor_Destino=tk.StringVar()
        self.cam_Destino=tk.Entry(self, textvariable=self.valor_Destino)
        self.cam_Destino.config(width=35)
        self.cam_Destino.grid(row=3, column=1, columnspan=2, padx=15)

        #botones
        self.Boton_confirmar = tk.Button(self, text="Confirmar")
        self.Boton_confirmar.config(width=15, bg="light sea green",fg="dark slate gray",activebackground="#5499C7",activeforeground="#000",cursor="hand2", font=("Comic Sans MS", 10), command=self.crearReserva)
        self.Boton_confirmar.grid(row=6, column=1, columnspan=2)

        self.Boton_Regresar = tk.Button(self, text="Regresar")
        self.Boton_Regresar.config(width=10, bg="IndianRed1",fg="red4",activebackground="IndianRed4",activeforeground="black",cursor="hand2", command=self.volver_a_frame, font=("Comic Sans MS", 10))
        self.Boton_Regresar.grid(row=7, column=1, pady=10)

    def datosReserva(self, vuelo, origen,destino):
        self.cam_NumeroVuelo.insert(0, vuelo)
        self.cam_Origen.insert(0, origen)
        self.cam_Destino.insert(0, destino)
    
    def crearReserva(self):
        self.cedula = self.cam_cedula.get()
        self.numeroVuelo = self.cam_NumeroVuelo.get()
        puestos = puestosDisponibles(self.numerovuelo)
        if puestos > 0:
            informacionReserva = Reservas(self.cedula, self.numeroVuelo)
            titulo = 'Confirmación'
            texto = '¿Desea hacer la reserva?'
            m = messagebox.askquestion(titulo,texto)
            if m == 'yes':
                reserva(informacionReserva)
                puestoMenos(self.numeroVuelo)
        else:
            informacionListaEspera = Reservas(self.cedula, self.numeroVuelo)
            titulo = 'Confirmación'
            texto = '¿Desea entrar a la lista de espera?'
            m = messagebox.askquestion(titulo,texto)
            if m == 'yes': 
                listaEspera(informacionListaEspera)
            

        
        


    

   
        
        