import sqlite3

def insertar_usuario(usuario):
    conexion = sqlite3.connect('shock.db')
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuarios VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (usuario.idUsuario, usuario.rol, usuario.nombre, 
                    usuario.apellido, usuario.direccion, usuario.correo, usuario.contraseña))
    conexion.commit()
    conexion.close()
