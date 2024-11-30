#Ejercicio 1
#Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno.
print("Martinez Tagle Luis Angel 3w 1196 este programa muestra el nombre y la nota del alumno ")
class Alumno:
    # Constructor para inicializar los atributos
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    # Método para imprimir los datos del alumno
    def imprimir_datos(self):
        print(f"Nombre del alumno: {self.nombre}")
        print(f"Nota: {self.nota}")
    
    # Método para evaluar si el alumno ha aprobado o no
    def resultado(self):
        if self.nota >= 5:
            print(f"{self.nombre} ha aprobado.")
        else:
            print(f"{self.nombre} ha suspendido.")

# Creación de un objeto de la clase Alumno
nombre = input("Introduce el nombre del alumno: ")
nota = float(input("Introduce la nota del alumno: "))

alumno = Alumno(nombre, nota)

# Llamar a los métodos
alumno.imprimir_datos()
alumno.resultado()
