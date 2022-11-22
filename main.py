# Bases de datos CRUD
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
opcion = input("Ingrese una opcion: ")
