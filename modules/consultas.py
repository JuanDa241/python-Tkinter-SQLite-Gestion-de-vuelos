from .conexion import Conexion
from tkinter import messagebox

##consulta para ingresar personas
class Cliente():

    def __init__(self, Documento, Nombre, Apellido, Edad):
        self.documento=Documento
        self.nombre=Nombre
        self.apellido=Apellido
        self.edad=Edad
        
    def __str__(self):
        return f"cliente[{self.documento},'{self.nombre}','{self.apellido}',{self.edad}]"
    
def InsertData(Cliente):
        Conected=Conexion()
    
        sql=f'''
            INSERT INTO cliente(documento, nombre, apellido, edad)
            VALUES({Cliente.documento},'{Cliente.nombre}','{Cliente.apellido}',{Cliente.edad})
        '''
        try:
            Conected.conexion.execute(sql)
            Conected.CloseConexion()
        except:
            titulo='Ingreso de datos'
            texto='No se ha podido insertar datos'
            messagebox.showerror(titulo, texto)  

def actualizar(Cliente):
    conected = Conexion()

    sql=f'''
        UPDATE cliente
        SET  nombre=nombre, apellido=apellido, edad=edad
        WHERE documento={Cliente.documento}
    '''

    try:
        conected.conexion.execute(sql)
        conected.CloseConexion()
    except:
        titulo='Actualizar cliente'
        texto='No pudimos actualizar el cliente'
        messagebox.showerror(titulo,texto)



def ShowVuelo():
    conected=Conexion()
    lista=[]

    sql='''
        SELECT numeroVuelo, origen, destino, fecha, horario, precio, puestosDisponibles
        FROM vuelo
    '''
    try:
        lista= conected.conexion.execute(sql)
        dato = lista.fetchall()
        conected.CloseConexion()
        return dato
    except:
        titulo='Vuelos'
        texto='No encontramos los vuelos'
        messagebox.showerror(titulo,texto)

def buscar(busqueda):
    conected=Conexion()
    lista=[]

    sql=f'''
        SELECT * FROM vuelo WHERE origen LIKE '%{busqueda}%' OR destino LIKE '%{busqueda}%' OR fecha LIKE '%{busqueda}%'
    '''

    try:
        lista = conected.conexion.execute(sql)
        dato = lista.fetchall()
        conected.CloseConexion()
        return dato
    except:
        titulo='Buscar'
        texto='No encontramos la busqueda'
        messagebox.showerror(titulo,texto)

#Reserva Vuelos
class Reservas():

    def __init__(self, Documento, numeroVuelo):
        self.documento=Documento
        self.numerovuelo=numeroVuelo
        infoVuelo(self.numerovuelo)

    def __str__(self):
        return f"reservas[{self.documento},{self.numerovuelo}]"

def reserva(Reservas):
    conected=Conexion()
    
    sql=f'''
        INSERT INTO reserva(documento, numeroVuelo) VALUES ({Reservas.documento},{Reservas.numerovuelo})
    '''

    try:
        conected.conexion.execute(sql)
        conected.CloseConexion()

    except:
        titulo='Reserva'
        texto='No encontramos la reserva'
        messagebox.showerror(titulo,texto)

def listaEspera(Reservas):
    conected=Conexion()
 
    sql=f'''
        INSERT INTO listaEspera(numerovuelo, documento) VALUES ({Reservas.numerovuelo},{Reservas.documento})
    '''

    try:
        conected.conexion.execute(sql)
        conected.CloseConexion()
    except:
        titulo='Lista Espera'
        texto='No se pudo estar es la lista de espera'
        messagebox.showerror(titulo,texto) 

def infoVuelo(Reservas):
    conected = Conexion()

    sql=f'''
        SELECT * FROM vuelo 
        WHERE numeroVuelo = {Reservas}
    '''

    try:
        dato = conected.conexion.execute(sql)
        informacion = dato.fetchone()
        conected.CloseConexion()
        return informacion
    except:
        titulo='Vuelo'
        texto='No podemos encontrar informacion sobre el vuelo :('
        messagebox.showerror(titulo,texto)

class PuestoReserva():

    def __init__(self, PuestosDisponibles, PuestosReservados):
        self.puestosDisponibles=PuestosDisponibles
        self.puestosReservados=PuestosReservados

    def __str__(self):
        return f"vuelo[{self.puestosDisponibles},{self.puestosReservados}]"

def puestoMenos(PuestoReserva):
    conected=Conexion()

    sql=f'''
        UPDATE vuelo
        SET puestosDisponibles = puestosDisponibles - 1,
            puestosReservados = puestosReservados + 1
        WHERE numeroVuelo = {PuestoReserva}
    '''

    try:
        conected.conexion.execute(sql)
        conected.CloseConexion()
    except:
        titulo='Reserva'
        texto='No pudimos ocupar el puesto'
        messagebox.showerror(titulo,texto)

def EliminarPuestos(PuestoReserva):
        conected=Conexion()

        sql=f'''
            UPDATE vuelo
            SET puestosDisponibles = puestosDisponibles + 1,
                puestosReservados = puestosReservados - 1
            WHERE numeroVuelo = {PuestoReserva}
        '''

        try:
            conected.conexion.execute(sql)
            conected.CloseConexion()
        except:
            titulo='Reserva'
            texto='No pudimos liberar el puesto'
            messagebox.showerror(titulo,texto)

def puestosDisponibles(Reservas):
    conected = Conexion()

    sql=f'''
        SELECT puestosDisponibles FROM vuelo
        WHERE numeroVuelo = {Reservas}
    '''

    try:
        resultado = conected.conexion.execute(sql).fetchone()
        conected.CloseConexion()
        if resultado:
            return resultado[0]
        else:
            raise ValueError("Vuelo no encontrado")
    except:
        titulo='Puesto disponibles'
        texto='No pudimos calcular los puestos disponible'
        messagebox.showerror(titulo,texto) 

#CLASE RESERVAS VUELOS
class Reservas():

    def __init__(self, Documento, numeroVuelo):
        self.documento=Documento
        self.numerovuelo=numeroVuelo

    def __str__(self):
        return f"reservas[{self.documento},{self.numerovuelo}]"

#ELIMINAR LAS RESERVAS
def DeleteReservas(Reservas):
    conected = Conexion()

    sql=f'''
        DELETE FROM reserva
        WHERE numeroReserva={Reservas}
    '''
    try:
        conected.conexion.execute(sql)
        conected.CloseConexion()
    except:
        titulo='Eliminar reserva'
        texto='No pudimos eliminar la reserva'
        messagebox.showerror(titulo,texto)


#ELIMINAR LISTA DE ESPERA
def DeleteLispera(Reservas):
    conected = Conexion()

    sql=f'''
        DELETE FROM listaEspera
        WHERE numeroEspera={Reservas}
    '''
    try:
        conected.conexion.execute(sql)
        conected.CloseConexion()
    except:
        titulo='Eliminar en lista de espera'
        texto='No pudimos eliminarte de la lista de espera'
        messagebox.showerror(titulo,texto)

#BUSQUEDA EN RESERVAS
def busquedaReserva():
    conected= Conexion()

    sql=f'''
        SELECT T2.numeroReserva, T1.nombre, T1.apellido, T3.numeroVuelo, T3.origen, T3.destino, T3.fecha, T3.horario
        FROM cliente T1
        INNER JOIN reserva T2
        ON T1.documento = T2.documento
        INNER JOIN vuelo T3
        ON T3.numeroVuelo = T2.numeroVuelo
    '''

    try:
        dato = conected.conexion.execute(sql)
        resultados = dato.fetchall() 
        conected.CloseConexion()
        return resultados
    except:
        titulo='Buscar reserva'
        texto='No pudimos encontrar la informacion de la reserva'
        messagebox.showerror(titulo,texto)

#BUSQUEDA DE LISTA DE ESPERA
def BusquedaLispera():
    conected= Conexion()

    sql=f'''
        SELECT T1.numeroEspera, T2.documento, T2.nombre, T2.apellido, T3.origen, T3.destino
        FROM listaEspera T1
        INNER JOIN cliente T2
        ON T1.documento = T2.documento
        INNER JOIN vuelo T3
        ON T1.numeroVuelo = T3.numeroVuelo
    '''

    try:
        dato = conected.conexion.execute(sql)
        resultados = dato.fetchall() 
        conected.CloseConexion()
        return resultados
    except:
        titulo='Buscar reserva'
        texto='No pudimos encontrar la informacion de la reserva'
        messagebox.showerror(titulo,texto)

#Mostrar clientes
def Usuario():
    conected=Conexion()
    lista=[]

    sql='''
        SELECT documento, nombre, apellido, edad
        FROM cliente
    '''
    try:
        lista= conected.conexion.execute(sql)
        dato = lista.fetchall()
        conected.CloseConexion()
        return dato
    except:
        titulo='Vuelos'
        texto='No encontramos los vuelos'
        messagebox.showerror(titulo,texto)

#ELIMINAR DATOS
def DeleteClientes(Cliente):
    conected = Conexion()

    sql=f'''
        DELETE FROM cliente
        WHERE documento={Cliente}
    '''
    try:
        conected.conexion.execute(sql)
        conected.CloseConexion()
    except:
        titulo='Eliminar Cliente'
        texto='No pudimos eliminarte'
        messagebox.showerror(titulo,texto)

def actualizar(Cliente, documento):
    conected = Conexion()

    sql=f'''
        UPDATE cliente
        SET  nombre ='{Cliente.nombre}', apellido = '{Cliente.apellido}', edad = {Cliente.edad}
        WHERE documento = {documento}
    '''
 
    try:
        conected.conexion.execute(sql)
        conected.CloseConexion()
    except:
        titulo='Actualizar cliente'
        texto='No pudimos actualizar el cliente'
        messagebox.showerror(titulo,texto)

#consulta

def consultaListaEspera(numeroVuelo):
    conected = Conexion()
    lista=[]

    sql=f'''
        SELECT * FROM listaEspera
        WHERE numeroVuelo = {numeroVuelo}
    '''

    try:
        lista=conected.conexion.execute(sql)
        dato=lista.fetchall()
        conected.CloseConexion()
        if dato:
            return dato[0]
    except:
        titulo=''
        texto=''
        messagebox.showerror(titulo,texto)