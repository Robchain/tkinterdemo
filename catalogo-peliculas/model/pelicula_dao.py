from .conexion_db import ConexionDB
from tkinter  import messagebox


def crear_tabla():
    conexion = ConexionDB()

    sql =  '''CREATE TABLE peliculas (
                id_pelicula INTEGER,
                nombre VARCHAR(100),
                duracion VARCHAR(10),
                genero VARCHAR(100),
                PRIMARY KEY(id_pelicula AUTOINCREMENT)
                )'''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Crear registro"
        mensaje = "Registro de película creado exitosamente."
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = " Crear registro"
        mensaje = "la tabla ya esta registrada."
        messagebox.showwarning(titulo, mensaje)

def borrar_tabla():
    conexion = ConexionDB()
    sql = "DROP TABLE peliculas"
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = " Borrar registro"
        mensaje = "la tabla de la base de datos se borro con exito."
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = " Borrar registro"
        mensaje = "No hay tabla para borrar."
        messagebox.showerror(titulo, mensaje)

class  Pelicula:
    def __init__(self,nombre, duracion, genero ):
        self.id_pelicula= None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
    def __str__(self):
        return f'Pelicula[{self.id_pelicula}, {self.nombre},{self.duracion} ,{self.genero}]'

def guardar(pelicula):
    conexion = ConexionDB()
    sql = f"""INSERT INTO peliculas (nombre, duracion, genero) VALUES('{pelicula.nombre}','{pelicula.duracion}','{pelicula.genero}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo='Conexion al Registro'
        mensaje="Error en la conexión a la Base de Datos.\nRevise el servidor y los permisos."
        messagebox.showerror(titulo,mensaje)

def listar():
    conexion = ConexionDB()
    lista_peliculas = []
    sql = 'SELECT * FROM peliculas'

    try:
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = "Conexion al Registro"
        mensaje = "No se pudo realizar la consulta a la base de datos.\nVerifique si la tabla existe o\ntenemos acceso a ella."
        messagebox.showwarning(titulo, mensaje)
    return lista_peliculas

def edita(pelicula, id_pelicula):
    conexion = ConexionDB()
    sql = f"""UPDATE peliculas SET nombre ='{pelicula.nombre}', duracion = '{pelicula.duracion}',
    genero = '{pelicula.genero}'
    WHERE id_pelicula = {id_pelicula}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = "Edicion de datos"
        mensaje = "No se a podido editar este registro"
        messagebox.showwarning(titulo, mensaje)
