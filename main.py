# Bases de datos CRUD
import funciones

nombreLocal = "Shock"

class Usuarios:
    def __init__(self, idUsuario, rol, nombre, apellido, direccion, correo, contraseña):
        self.idUsuario = idUsuario
        self.rol = rol
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.correo = correo
        self.contraseña = contraseña


print(f"Bienvenido a la base de datos de {nombreLocal}")
print("==========================================")
opcion = int(input("""Ingrese una opcion:
1. Listar
2. Agregar
"""))

if opcion == 1:
    opcion = int(input("""
    1. Listar todos los usuarios
    Seleccione una opcion: """))

    if opcion == 1:
        print("Registro de usuarios:")
        funciones.listar_usuarios()

if opcion == 2:
    opcion = int(input("""
    1. Agregar nuevo usuario
    Seleccione una opcion: """))

    if opcion == 1:
        print("""
        ingrese los siguientes datos:""")

        idUsuario = int(input("Id del usuario:"))
        rol = input("rol: ")
        nombre = input("Nombre del usuario:")
        apellido = input("apellido: ")
        direccion = input("Direccion del usuario:")
        correo = input("Correo del usuario:")
        contraseña = input("Contraseña del usuario:")

        user = Usuarios(idUsuario, rol, nombre, apellido, direccion, correo, contraseña)
        funciones.insertar_usuario(user)

