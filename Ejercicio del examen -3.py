#Ejercicio 3
#Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo  
print("Martinez Tagle Luis Angel 3w 1196 este programa imprimira el valor de los lados y el tipo de triangulo  ")
class Triangulo:
    # Constructor para inicializar los atributos
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c
    
    # Método para imprimir el valor del lado más grande
    def lado_mayor(self):
        lado_max = max(self.lado_a, self.lado_b, self.lado_c)
        print(f"El lado más grande tiene un valor de: {lado_max}")
    
    # Método para determinar el tipo de triángulo
    def tipo_triangulo(self):
        if self.lado_a == self.lado_b == self.lado_c:
            print("El triángulo es equilátero.")
        elif self.lado_a == self.lado_b or self.lado_a == self.lado_c or self.lado_b == self.lado_c:
            print("El triángulo es isósceles.")
        else:
            print("El triángulo es escaleno.")

# Solicitar los lados del triángulo
lado_a = float(input("Introduce el valor del primer lado: "))
lado_b = float(input("Introduce el valor del segundo lado: "))
lado_c = float(input("Introduce el valor del tercer lado: "))

# Crear un objeto de la clase Triangulo
triangulo = Triangulo(lado_a, lado_b, lado_c)

# Llamar a los métodos
triangulo.lado_mayor()
triangulo.tipo_triangulo()
