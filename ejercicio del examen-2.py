#Ejercicio 2
#Realizar un programa que tenga una clase Persona con las siguientes características. La clase tendrá como atributos el nombre y la edad de una persona.
print("Martinez Tagle Luis Angel 3w 1196 este programa pondra el nombre y la edad  ")

class Persona:
    # Constructor para inicializar los atributos
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    # Método para mostrar los datos de la persona
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
    
    # Método para determinar si la persona es mayor de edad
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} es menor de edad.")

# Creación de un objeto de la clase Persona
nombre = input("Introduce el nombre del placoson : ")
edad = int(input("Introduce la edad del guapote : "))

persona = Persona(nombre, edad)

# Llamar a los métodos
persona.mostrar_datos()
persona.es_mayor_de_edad()
