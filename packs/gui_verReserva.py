import tkinter as tk
from tkinter import ttk, messagebox
from modules.consultas import busquedaReserva, DeleteReservas, EliminarPuestos, consultaListaEspera, reserva, Reservas, puestoMenos, DeleteLispera

class VerReserva(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, bg= "PaleTurquoise1")
        self.title("Reserva")
        self.campos()
        self.Tabla_Datos()
        self.resizable(0,0)
        self.parent = parent

    def volver_a_frame(self):
        self.destroy()
        self.parent.deiconify()

    def Tabla_Datos(self):
        informacionReservas = busquedaReserva()
        self.tabla = ttk.Treeview(self)
        self.tabla.config(columns=('nombre','apellido','numeroVuelo','origen','destino','fecha','horario'))
        self.tabla.grid(row=1,column=1, columnspan=3, rowspan=6, padx=15)

        self.tabla.tag_configure("oddrow", background="white")
        self.tabla.tag_configure("evenrow", background="PaleTurquoise1")

        self.tabla.heading("#0", text="NUMERO RESERVA")
        self.tabla.column("#0",width=120, anchor= "center")
        self.tabla.heading("#1",text="NOMBRE")
        self.tabla.column("#1",width=80, anchor= "center")
        self.tabla.heading("#2",text="APELLIDO")
        self.tabla.column("#2",width=80, anchor= "center")
        self.tabla.heading("#3",text="NUMERO VUELO")
        self.tabla.column("#3",width=100, anchor= "center")
        self.tabla.heading("#4",text="ORIGEN")
        self.tabla.column("#4",width=80, anchor= "center")
        self.tabla.heading("#5",text="DESTINO")
        self.tabla.column("#5",width=130, anchor= "center")
        self.tabla.heading("#6",text="FECHA")
        self.tabla.column("#6",width=90, anchor= "center")
        self.tabla.heading("#7",text="HORARIO")
        self.tabla.column("#7",width=90, anchor= "center")

        #Mostrar informacion en la tabla 
        for i in informacionReservas:
            self.tabla.insert('',i[0], text=i[0], values=(i[1],i[2],i[3],i[4],i[5],i[6],i[7]))

    def campos(self):
        self.usuario = tk.Label(self, text="")
        self.usuario.config(width=20,bg="PaleTurquoise1")
        self.usuario.grid( columnspan=3,row=0, column=0, padx=10, pady=10)

        self.Boton_Regresar = tk.Button(self, text="Regresar")
        self.Boton_Regresar.config(width=10, bg="IndianRed1",fg="red4",activebackground="IndianRed4",activeforeground="black",cursor="hand2", command=self.volver_a_frame, font=("Comic Sans MS", 10))
        self.Boton_Regresar.grid(row=8, column=3, pady=10)

        self.Boton_Eliminar = tk.Button(self, text="Eliminar")
        self.Boton_Eliminar.config(width=10, bg="IndianRed1",fg="dark slate gray",activebackground="IndianRed4",activeforeground="black",cursor="hand2", font=("Comic Sans MS", 10), command=self.eliminarReserva)
        self.Boton_Eliminar.grid(row=8, column=2,padx=30)

    def eliminarReserva(self):
        seleccion = self.tabla.selection() 
        if not seleccion:
            titulo = 'Alerta'
            texto = 'Por favor, seleccionar un elemento de la tabla para eliminar'
            messagebox.showwarning(titulo, texto)
        else:
            self.numeroReserva = self.tabla.item(self.tabla.selection())['text']
            self.numeroVuelo = self.tabla.item(self.tabla.selection())['values'][2]
            titulo = 'Confirmación'
            texto = '¿Desea eliminar la reserva?'
            m = messagebox.askquestion(titulo,texto)
            if m == 'yes':
                DeleteReservas(self.numeroReserva)
                EliminarPuestos(self.numeroVuelo)

                espera=consultaListaEspera(self.numeroVuelo)
                if espera != None:
                    self.numeroEspera=espera[0]
                    self.documento=espera[2]
                    self.numeroVuelo=espera[1]
                    datos=Reservas(self.documento,self.numeroVuelo)
                    reserva(datos)
                    puestoMenos(self.numeroVuelo)
                    DeleteLispera(self.numeroEspera)
                self.Tabla_Datos()
