#Ejercicio 4
#Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división.
print("Martinez Tagle Luis Angel 3w 1196 este programa trata sobre una  calculadora ")

class Calculadora:
    # Constructor para inicializar los valores
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    # Método para calcular la suma
    def suma(self):
        return self.num1 + self.num2
    
    # Método para calcular la resta
    def resta(self):
        return self.num1 - self.num2
    
    # Método para calcular la multiplicación
    def multiplicacion(self):
        return self.num1 * self.num2
    
    # Método para calcular la división
    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: No se puede dividir por cero"

# Solicitar los valores de los números
num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))

# Crear un objeto de la clase Calculadora
calculadora = Calculadora(num1, num2)

# Realizar las operaciones y mostrar los resultados
print(f"La suma de {num1} y {num2} es: {calculadora.suma()}")
print(f"La resta de {num1} y {num2} es: {calculadora.resta()}")
print(f"La multiplicación de {num1} y {num2} es: {calculadora.multiplicacion()}")
print(f"La división de {num1} entre {num2} es: {calculadora.division()}")
