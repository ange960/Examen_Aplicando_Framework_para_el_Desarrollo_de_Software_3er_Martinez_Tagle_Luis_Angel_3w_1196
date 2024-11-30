#Ejercicio 5
#Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones
print("Martinez Tagle Luis Angel 3w 1196 este programa sirve para almacenar el contacto el nombre, el teléfono y el email.")


class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"{self.nombre}, {self.telefono}, {self.email}"

class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self):
        self.contactos.append(Contacto(input("Nombre: "), input("Teléfono: "), input("Email: ")))

    def listar_contactos(self):
        for c in self.contactos: print(c)

    def buscar_contacto(self):
        nombre = input("Buscar: ")
        for c in self.contactos:
            if c.nombre.lower() == nombre.lower():
                print(c)
                return
        print("No encontrado.")

    def editar_contacto(self):
        nombre = input("Editar: ")
        for c in self.contactos:
            if c.nombre.lower() == nombre.lower():
                c.nombre = input("Nuevo nombre: ")
                c.telefono = input("Nuevo teléfono: ")
                c.email = input("Nuevo email: ")
                print("Contacto editado.")
                return
        print("No encontrado.")

    def cerrar_agenda(self):
        print("Agenda cerrada.")
        exit()

def main():
    agenda = Agenda()
    while True:
        print("\n1. Añadir\n2. Ver\n3. Buscar\n4. Editar\n5. Cerrar")
        opcion = input("Selecciona opción: ")
        if opcion == "1": agenda.añadir_contacto()
        elif opcion == "2": agenda.listar_contactos()
        elif opcion == "3": agenda.buscar_contacto()
        elif opcion == "4": agenda.editar_contacto()
        elif opcion == "5": agenda.cerrar_agenda()

if __name__ == "__main__":
    main()
