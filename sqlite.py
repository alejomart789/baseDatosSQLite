import sqlite3
from productos import Productos 

conn = sqlite3.connect('shock.db')
c = conn.cursor()

''' 
conn.execute(
    """CREATE TABLE productos (
    codigo INT PRIMARY KEY NOT NULL,
    nombre STRING NOT NULL,
    categoria STRING NOT NULL,
    stock INTEGER NOT NULL,
    precio INTEGER NOT NULL
    );
    """)
'''

# c.execute("INSERT INTO usuarios VALUES (4,'user','pedro','castro','nn','pedro.castro@gmail.com','petrosqui2020')")
# conn.commit()

# Insertar productos

prd_1 = Productos(1, 'mause gamer', 'ratones', 10, 25000)
prd_2 = Productos(2, 'teclado txr', 'teclados', 5, 35000)
prd_3 = Productos(3, 'pantalla lcd', 'pantallas', 2, 250000)
prd_4 = Productos(4, 'portatil lenovo', 'portatiles', 10, 2500000)
prd_5 = Productos(5, 'Silla gamer', 'sillas', 8, 350000)
prd_6 = Productos(6, 'torre', 'torres', 25, 350000)

many_pruductos = [
    (prd_1.codigo, prd_1.nombre, prd_1.categoria, prd_1.stock, prd_1.precio),
    (prd_2.codigo, prd_2.nombre, prd_2.categoria, prd_2.stock, prd_2.precio),
    (prd_3.codigo, prd_3.nombre, prd_3.categoria, prd_3.stock, prd_3.precio),
    (prd_4.codigo, prd_4.nombre, prd_4.categoria, prd_4.stock, prd_4.precio),
    (prd_5.codigo, prd_5.nombre, prd_5.categoria, prd_5.stock, prd_5.precio)
]

# c.executemany("INSERT INTO productos VALUES (?, ?, ?, ?, ?)", many_pruductos)
# conn.commit()

# Visualizar todas los datos de la tabla
c.execute("SELECT * FROM productos WHERE codigo=?", (1,))
productos = c.fetchall()
print(productos)

# Insertar un productos

def insertar_producto(producto):
    c.executemany("INSERT INTO producto VALUES (?, ?, ?, ?, ?)", 
                (producto.codigo, producto.nombre, producto.categoria, producto.stock, producto.precio))
    conn.commit()

insertar_producto(prd_6)

conn.close()