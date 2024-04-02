#ABSTRACCIÓN
#1:
class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
    def alimentar(self):
        print(f"{self.nombre} está siendo alimentado.")
    def hacer_sonido(self):
        pass  
class Perro(Animal):
    def hacer_sonido(self):
        print("Guau!")
class Gato(Animal):
    def hacer_sonido(self):
        print("Miau!")
class Vaca(Animal):
    def hacer_sonido(self):
        print("Muuu!")
#programa principal
if __name__ == "__main__":
    perro = Perro("Rex", 3, "Perro")
    gato = Gato("Garfield", 5, "Gato")
    vaca = Vaca("Margarita", 2, "Vaca")
    perro.alimentar()
    perro.hacer_sonido()
    gato.alimentar()
    gato.hacer_sonido()
    vaca.alimentar()
    vaca.hacer_sonido()

  #2:
class Coche:
    def __init__(self, modelo, año, velocidad=0):
        self.modelo = modelo
        self.año = año
        self.velocidad = velocidad
    
    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"El coche {self.modelo} ha acelerado a {self.velocidad} km/h.")
    
    def frenar(self, decremento):
        if self.velocidad - decremento >= 0:
            self.velocidad -= decremento
            print(f"El coche {self.modelo} ha frenado a {self.velocidad} km/h.")
        else:
            print("El coche ya está detenido.")

#programa principal
if __name__ == "__main__":
    coche1 = Coche("Toyota", 2020)
    coche2 = Coche("Ford", 2018, 50)

    coche1.acelerar(20)
    coche2.frenar(30)
  
  #3:
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.calificacion = None
    
    def tomar_examen(self, calificacion):
        self.calificacion = calificacion
        print(f"El estudiante {self.nombre} ha tomado el examen y ha obtenido una calificación de {calificacion}.")
    
    def mostrar_informacion(self):
        print(f"Información del estudiante:\nNombre: {self.nombre}\nEdad: {self.edad}\nGrado: {self.grado}")
        if self.calificacion is not None:
            print(f"Calificación: {self.calificacion}")

#Programa principal
if __name__ == "__main__":
    estudiante1 = Estudiante("Juan", 16, "10mo grado")
    estudiante2 = Estudiante("Maria", 17, "11vo grado")

    estudiante1.tomar_examen(85)
    estudiante2.tomar_examen(90)

    estudiante1.mostrar_informacion()
    estudiante2.mostrar_informacion()
  
  #4:
class Tienda:
    def __init__(self, nombre, direccion, tipo):
        self.nombre = nombre
        self.direccion = direccion
        self.tipo = tipo
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Se ha agregado el producto {producto} a la tienda {self.nombre}.")
    
    def vender_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
            print(f"Se ha vendido el producto {producto} en la tienda {self.nombre}.")
        else:
            print(f"El producto {producto} no está disponible en la tienda {self.nombre}.")

#programa principal
if __name__ == "__main__":
    tienda1 = Tienda("Supermercado XYZ", "Calle Principal 123", "Supermercado")
    tienda2 = Tienda("Tienda de Ropa ABC", "Avenida Central 456", "Ropa")

    tienda1.agregar_producto("Manzanas")
    tienda1.agregar_producto("Leche")
    tienda2.agregar_producto("Camiseta")
    tienda2.agregar_producto("Pantalones")

    tienda1.vender_producto("Manzanas")
    tienda2.vender_producto("Camiseta")
    tienda1.vender_producto("Plátanos")

#ENCAPSULAMIENTO
#1
class Persona:
    def __init__(self, nombre, edad, genero):
        self._nombre = nombre
        self._edad = edad
        self._genero = genero
    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nombre):
        self._nombre = nombre
    def get_edad(self):
        return self._edad
    def set_edad(self, edad):
        self._edad = edad
    def get_genero(self):
        return self._genero
    def set_genero(self, genero):
        self._genero = genero
#Programa principal
if __name__ == "__main__":
    persona1 = Persona("Juan", 25, "Masculino")
    print("Información de la persona:")
    print("Nombre:", persona1.get_nombre())
    print("Edad:", persona1.get_edad())
    print("Género:", persona1.get_genero())
    persona1.set_edad(30)
    persona1.set_genero("Femenino")
    print("\nInformación actualizada de la persona:")
    print("Nombre:", persona1.get_nombre())
    print("Edad:", persona1.get_edad())
    print("Género:", persona1.get_genero())

#2
class CuentaBancaria:
    def __init__(self, saldo, numero_cuenta):
        self.saldo = saldo
        self.numero_cuenta = numero_cuenta
    def get_saldo(self):
        return self.saldo

    def set_saldo(self, nuevo_saldo):
        self.saldo = nuevo_saldo
    def get_numero_cuenta(self):
        return self.numero_cuenta
    def set_numero_cuenta(self, nuevo_numero_cuenta):
        self.numero_cuenta = nuevo_numero_cuenta

# Programa principal
if __name__ == "__main__":
    # Crear una instancia de la clase CuentaBancaria
    cuenta1 = CuentaBancaria(1000, "123456789")
    # Obtener información de la cuenta utilizando los métodos get
    print("Información de la cuenta:")
    print("Saldo:", cuenta1.get_saldo())
    print("Número de cuenta:", cuenta1.get_numero_cuenta())
    # Actualizar información de la cuenta utilizando los métodos set
    cuenta1.set_saldo(1500)
    cuenta1.set_numero_cuenta("987654321")
    # Recuperar la información actualizada de la cuenta
    print("\nInformación actualizada de la cuenta:")
    print("Saldo actualizado:", cuenta1.get_saldo())
    print("Número de cuenta actualizado:", cuenta1.get_numero_cuenta())


#3
class Libro:
    def __init__(self, titulo, autor, genero):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
    def get_titulo(self):
        return self._titulo
    def set_titulo(self, titulo):
        self._titulo = titulo
    def get_autor(self):
        return self._autor
    def set_autor(self, autor):
        self._autor = autor
    def get_genero(self):
        return self._genero
    def set_genero(self, genero):
        self._genero = genero

#Programa principal
if __name__ == "__main__":
    # Crear una instancia de la clase Libro
    libro1 = Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", "Fantasía")
    # Obtener información del libro utilizando los métodos get
    print("Información del libro:")
    print("Título:", libro1.get_titulo())
    print("Autor:", libro1.get_autor())
    print("Género:", libro1.get_genero())
    # Actualizar información del libro utilizando los métodos set
    libro1.set_titulo("Harry Potter y la cámara secreta")
    libro1.set_autor("J.K. Rowling")
    libro1.set_genero("Fantasía épica")
    # Recuperar la información actualizada del libro
    print("\nInformación actualizada del libro:")
    print("Título actualizado:", libro1.get_titulo())
    print("Autor actualizado:", libro1.get_autor())
    print("Género actualizado:", libro1.get_genero())
  #4:
  class Factura:
    def __init__(self, numero_factura, fecha_emision, monto):
        self._numero_factura = numero_factura
        self._fecha_emision = fecha_emision
        self._monto = monto
    def get_numero_factura(self):
        return self._numero_factura
    def set_numero_factura(self, numero_factura):
        self._numero_factura = numero_factura
    def get_fecha_emision(self):
        return self._fecha_emision
    def set_fecha_emision(self, fecha_emision):
        self._fecha_emision = fecha_emision
    def get_monto(self):
        return self._monto
    def set_monto(self, monto):
        self._monto = monto
#Programa principal
if __name__ == "__main__":
    # Crear una instancia de la clase Factura
    factura1 = Factura("F2022001", "2022-04-01", 1500.0)
    # Obtener información de la factura utilizando los métodos get
    print("Información de la factura:")
    print("Número de factura:", factura1.get_numero_factura())
    print("Fecha de emisión:", factura1.get_fecha_emision())
    print("Monto:", factura1.get_monto())
    # Actualizar información de la factura utilizando los métodos set
    factura1.set_fecha_emision("2022-04-02")
    factura1.set_monto(2000.0)
    # Recuperar la información actualizada de la factura
    print("\nInformación actualizada de la factura:")
    print("Fecha de emisión actualizada:", factura1.get_fecha_emision())
    print("Monto actualizado:", factura1.get_monto())


#USO DE OBJETOS:
#1:
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestamo = False
    def prestar(self):
        if not self.prestamo:
            self.prestamo = True
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print("El libro ya está prestado.")
    def devolver(self):
        if self.prestamo:
            self.prestamo = False
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print("El libro no estaba prestado.")
class Biblioteca:
    def prestar_libro(self, libro):
        libro.prestar()
    def devolver_libro(self, libro):
        libro.devolver()
#Programa principal
if __name__ == "__main__":
    # Crear libros
    libro1 = Libro("Harry Potter y la piedra filosofal", "J.K. Rowling")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez")
    # Crear biblioteca
    biblioteca = Biblioteca()
    # Prestar y devolver libros
    biblioteca.prestar_libro(libro1)
    biblioteca.prestar_libro(libro1)  # Intentar prestar el mismo libro nuevamente
    biblioteca.devolver_libro(libro1)
    biblioteca.devolver_libro(libro2)  # Intentar devolver un libro que no estaba prestado

#2:
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def __str__(self):
        return f"{self.nombre}: ${self.precio:.2f}"
class Factura:
    def __init__(self, numero_factura, fecha_emision):
        self.numero_factura = numero_factura
        self.fecha_emision = fecha_emision
        self.productos = []
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado a la factura.")
    def imprimir_factura(self):
        print("Factura:")
        print(f"Número de factura: {self.numero_factura}")
        print(f"Fecha de emisión: {self.fecha_emision}")
        print("Productos:")
        for producto in self.productos:
            print("-", producto)
#Programa Principal
if __name__ == "__main__":
    # Crear productos
    producto1 = Producto("Camisa", 25.99)
    producto2 = Producto("Pantalón", 39.99)
    # Crear factura
    factura = Factura("F2022001", "2022-04-01")
    # Agregar productos a la factura
    factura.agregar_producto(producto1)
    factura.agregar_producto(producto2)
    # Imprimir factura
    factura.imprimir_factura()

#3:
class Rueda:
    def __init__(self, tamaño):
        self.tamaño = tamaño
    def __str__(self):
        return f"Rueda de tamaño {self.tamaño}"
class Carro:
    def __init__(self, rueda_delantera_izquierda, rueda_delantera_derecha, rueda_trasera_izquierda, rueda_trasera_derecha):
        self.rueda_delantera_izquierda = rueda_delantera_izquierda
        self.rueda_delantera_derecha = rueda_delantera_derecha
        self.rueda_trasera_izquierda = rueda_trasera_izquierda
        self.rueda_trasera_derecha = rueda_trasera_derecha
    def mover(self):
        print("El carro está en movimiento.")
    def cambiar_ruedas(self, nueva_rueda):
        self.rueda_delantera_izquierda = nueva_rueda
        self.rueda_delantera_derecha = nueva_rueda
        self.rueda_trasera_izquierda = nueva_rueda
        self.rueda_trasera_derecha = nueva_rueda
        print("Las ruedas del carro han sido cambiadas.")
#programa principal
if __name__ == "__main__":
    # Crear instancias de la clase Rueda
    rueda_delantera_izquierda = Rueda(18)
    rueda_delantera_derecha = Rueda(18)
    rueda_trasera_izquierda = Rueda(18)
    rueda_trasera_derecha = Rueda(18)
    # Crear instancia de la clase Carro
    carro = Carro(rueda_delantera_izquierda, rueda_delantera_derecha, rueda_trasera_izquierda, rueda_trasera_derecha)
    # Imprimir información inicial del carro
    print("Carro creado con las siguientes ruedas:")
    print("Rueda delantera izquierda:", carro.rueda_delantera_izquierda)
    print("Rueda delantera derecha:", carro.rueda_delantera_derecha)
    print("Rueda trasera izquierda:", carro.rueda_trasera_izquierda)
    print("Rueda trasera derecha:", carro.rueda_trasera_derecha)
    # Cambiar las ruedas del carro
    nueva_rueda = Rueda(20)
    carro.cambiar_ruedas(nueva_rueda)
    # Imprimir información después de cambiar las ruedas
    print("\nDespués de cambiar las ruedas, el carro tiene las siguientes ruedas:")
    print("Rueda delantera izquierda:", carro.rueda_delantera_izquierda)
    print("Rueda delantera derecha:", carro.rueda_delantera_derecha)
    print("Rueda trasera izquierda:", carro.rueda_trasera_izquierda)
    print("Rueda trasera derecha:", carro.rueda_trasera_derecha)

#4:
class Tienda:
    def __init__(self, productos_disponibles):
        self.productos_disponibles = productos_disponibles
        self.lista_compras = []
    def agregar_producto_disponible(self, producto):
        self.productos_disponibles.append(producto)
        print(f"Producto '{producto}' agregado a la lista de productos disponibles.")
    def mostrar_productos_disponibles(self):
        print("Productos disponibles en la tienda:")
        for producto in self.productos_disponibles:
            print("-", producto)
    def agregar_a_lista_compras(self, producto):
        if producto in self.productos_disponibles:
            self.lista_compras.append(producto)
            print(f"Producto '{producto}' agregado a la lista de compras.")
        else:
            print(f"El producto '{producto}' no está disponible en la tienda.")
    def mostrar_lista_compras(self):
        print("Lista de compras del cliente:")
        for producto in self.lista_compras:
            print("-", producto)
    def pagar_cuenta(self):
        total = sum(self.productos_disponibles[producto] for producto in self.lista_compras)
        print(f"Total a pagar: ${total:.2f}")
        self.lista_compras = []
        print("Gracias por su compra. La lista de compras ha sido vaciada.")
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
    def agregar_a_lista_compras(self, tienda, producto):
        tienda.agregar_a_lista_compras(producto)
    def pagar_cuenta(self, tienda):
        tienda.pagar_cuenta()
# Programa Principal
if __name__ == "__main__":
    # Crear una tienda con algunos productos disponibles
    tienda = Tienda(["Manzanas", "Plátanos", "Naranjas"])
    tienda.agregar_producto_disponible("Peras")
    # Mostrar productos disponibles en la tienda
    tienda.mostrar_productos_disponibles()
    # Crear un cliente
    cliente = Cliente("Juan")
    # Cliente agrega productos a su lista de compras
    cliente.agregar_a_lista_compras(tienda, "Manzanas")
    cliente.agregar_a_lista_compras(tienda, "Naranjas")
    # Mostrar lista de compras del cliente
    tienda.mostrar_lista_compras()
    # Cliente paga la cuenta
    cliente.pagar_cuenta(tienda)
    # Mostrar productos disponibles después de pagar la cuenta
    tienda.mostrar_productos_disponibles()
