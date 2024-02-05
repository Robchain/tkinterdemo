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