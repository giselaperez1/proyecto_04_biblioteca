#importo modulos e inicializo coloerama
from colorama import Fore, init
import os
init(autoreset=True)

#Portada del proyecto
os.system('cls')
print(Fore.YELLOW+'''
 ______   _  __      __   _        _                                                            
|_   _ \ (_)[  |    [  | (_)      / |_                                                          
  | |_) |__  | |.--. | | __  .--.`| |-.---. .---. ,--.                                          
  |  __'[  | | '/'`\ | |[  / .'`\ | |/ /__\/ /'`\`'_\ :                                         
 _| |__) | | |  \__/ | | | | \__. | || \__.| \__.// | |,                                        
|_______[___[__;.__.[___[___'.__.'\__/'.__.'.___.\'-;__/                                        
   ______ _______         _      ____  _____      _    _________ ________   ______      _       
 .' ___  |_   __ \       / \    |_   \|_   _|    / \  |  _   _  |_   __  |.' ___  |    / \      
/ .'   \_| | |__) |     / _ \     |   \ | |     / _ \ |_/ | | \_| | |_ \_/ .'   \_|   / _ \     
| |   ____ |  __ /     / ___ \    | |\ \| |    / ___ \    | |     |  _| _| |         / ___ \    
\ `.___]  _| |  \ \_ _/ /   \ \_ _| |_\   |_ _/ /   \ \_ _| |_   _| |__/ \ `.___.'\_/ /   \ \_  
 `._____.|____| |___|____| |____|_____|\____|____| |____|_____| |________|`.____ .|____| |____| 



      ______ ______
    _/      Y      \_
   // ~~ ~~ | ~~ ~  \\
  // ~ ~ ~~ | ~~~ ~~ \\      
 //________.|.________\\     by Gisela Perez
`----------`-'----------'                    
''')
input()
#fin portada del proyecto


#clase libro para los libros de nuestra biblioteca
class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.disponible = True

#clase usuario
class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        #lista vacia paera los libros prestados
        self.libros_prestados = []

#clase biblioteca 
class Biblioteca:
    def __init__(self):
        #lista vacia de libros para alamcenarlos al guardarlos 
        self.libros = []
        # Diccionario que almacena usuarios por Id
        self.usuarios = {}  

# Función para agregar un libro a la biblioteca.
    def agregar_libro(self):
        os.system('cls')
        print(Fore.YELLOW + "Añadir libro")
        titulo = input("Título: ")
        autor = input("Autor: ")
        año = input("Año: ")
# para comprobar  si el libro ya está registrado en la biblioteca
        for libro in self.libros:
            if libro.titulo == titulo and libro.autor == autor and libro.año == año:
                print(Fore.RED + "Este libro ya está registrado en la biblioteca.")
                input(Fore.CYAN + "Pulsa Enter para continuar...")
                return
#si no esta registrado se agregaa la lsista de los libros 
        self.libros.append(Libro(titulo, autor, año))
        print(Fore.GREEN + "Libro añadido correctamente.")
        input(Fore.CYAN + "Pulsa Enter para continuar...")

#funcion para mosdtar los librops prestados o dispopnibkles que hay 
    def mostrar_libros(self, disponibles=True):
        os.system('cls')
        print(Fore.YELLOW + ("Mostrar Libros Disponibles" if disponibles else "Mostrar Libros Prestados"))
        
        libros = [libro for libro in self.libros if libro.disponible == disponibles]
        if libros:
            for libro in libros:
                print(f"{libro.titulo} - {libro.autor}")
        else:
            print(Fore.RED + "No hay libros para mostrar")
        input(Fore.CYAN + "Pulsa Enter para continuar...")

#funciion parta registar un nuevo usuario 
    def registrar_usuario(self):
        os.system('cls')
        print(Fore.YELLOW + "Registrar usuario")
        nombre = input("Nombre del usuario: ")
        user_id = input("ID único del usuario: ")
#comprobamos si el id ya se ha registrado antes 
        if user_id in self.usuarios:
            print(Fore.RED + f"El usuario con ID '{user_id}' ya está registrado. Por favor, elige otro ID.")
        else:
            self.usuarios[user_id] = Usuario(nombre, user_id)
            print(Fore.GREEN + f"Usuario '{nombre}' registrado con éxito (ID: {user_id}).")

        input(Fore.CYAN + "pulsa Enter para continuar...")

#funcion para mostar los usuarios ya registrados 
    def listar_usuarios(self):
        os.system('cls')
        print(Fore.YELLOW + "Listar usuarios")
        if self.usuarios:
            for usuario in self.usuarios.values():
                print(f"Nombre: {usuario.nombre} | ID: {usuario.user_id}")
        else:
            print(Fore.RED + "No hay usuarios registrados.")
        input(Fore.CYAN + "Pulsa Enter para continuar...")

#funciin para eliminar usuarios 
    def eliminar_usuario(self):
        os.system('cls')
        print(Fore.YELLOW + "Eliminar usuario")
        user_id = input("ID del usuario: ")
        if user_id in self.usuarios and not self.usuarios[user_id].libros_prestados:
            del self.usuarios[user_id]
            print(Fore.GREEN + "Usuario eliminado.")
        else:
            print(Fore.RED + "No se puede eliminar el usuario porque tiene libros prestados o no existe.")
        input(Fore.CYAN + "Pulsa Enter para continuar...")

#funcion para prestar libros 
    def prestar_libro(self):
        os.system('cls')
        print(Fore.YELLOW + "Prestar libro")
        user_id = input("ID del usuario: ")
        #para comprobar que el usuario existe 
        if user_id not in self.usuarios:
            print(Fore.RED + "Usuario no encontrado.")
            input(Fore.CYAN + "Pulsa Enter para continuar...")
            return
        titulo = input("Título del libro: ")
        #para bsucar y marcar el libro como no disponibkle 
        for libro in self.libros:
            if libro.titulo == titulo and libro.disponible:
                libro.disponible = False
                self.usuarios[user_id].libros_prestados.append(libro)
                print(Fore.YELLOW + "Libro prestado.")
                input(Fore.CYAN + "Pulsa Enter para continuar...")
                return
        print(Fore.RED + "Libro no disponible o no encontrado.")
        input(Fore.CYAN + "Pulsa Enter para continuar...")

#funcion para devolver un libro 
    def devolver_libro(self):
        os.system('cls')
        print(Fore.YELLOW + "Devolver libro")
        user_id = input("ID del usuario: ")
        if user_id not in self.usuarios:
            print(Fore.RED + "Usuario no encontrado.")
            input(Fore.CYAN + "Pulsa Enter para continuar...")
            return
        usuario = self.usuarios[user_id]
        titulo = input("Título del libro: ")

        #busco el libro en lols libros prestados y devuelvo
        for libro in usuario.libros_prestados:
            if libro.titulo == titulo:
                libro.disponible = True
                usuario.libros_prestados.remove(libro)
                print(Fore.GREEN + "Libro devuelto.")
                input(Fore.CYAN + "Pulsa Enter para continuar...")
                return
        print(Fore.RED + "Error al devolver el libro")
        input(Fore.CYAN + "Pulsa Enter para continuar...")
#funcion para iniciar ka biblioteca y se muestre el menu inicial 
def iniciar_biblioteca():
    biblioteca = Biblioteca()
    #bucle while para mostar el menu principal 
    while True:
        os.system('cls')
        print(Fore.YELLOW + "\n--- Menú Biblioteca ---")
        print("1. Usuarios")
        print("2. Libros")
        print("3. Biblioteca")
        print(Fore.RED +"4. Salir")
        opcion = input(Fore.CYAN + "Seleccione una opción: ")
#opcion usuaruios del menu
        if opcion == "1":
            while True:
                os.system('cls')
                print(Fore.YELLOW + "Usuarios")
                print("1. Registrar usuario")
                print("2. Listar usuarios")
                print("3. Eliminar usuario")
                print(Fore.RED +"4. Volver atrás")
                sub_opcion = input("Seleccione una opción: ")
                if sub_opcion == "1":
                    biblioteca.registrar_usuario()
                elif sub_opcion == "2":
                    biblioteca.listar_usuarios()
                elif sub_opcion == "3":
                    biblioteca.eliminar_usuario()
                elif sub_opcion == "4":
                    break
                else:
                    print(Fore.RED + "Opción no valida")
                    input(Fore.CYAN + "Pulsa Enter para continuar...")
#opocion libros del menu principal 
        elif opcion == "2":
            while True:
                os.system('cls')
                print(Fore.YELLOW + "Libros")
                print("1. Añadir libro")
                print("2. Mostrar libros disponibles")
                print("3. Mostrar libros prestados")
                print(Fore.RED +"4. Volver")
                sub_opcion = input("Seleccione una opción: ")
                if sub_opcion == "1":
                    biblioteca.agregar_libro()
                elif sub_opcion == "2":
                    biblioteca.mostrar_libros(True)
                elif sub_opcion == "3":
                    biblioteca.mostrar_libros(False)
                elif sub_opcion == "4":
                    break
                else:
                    print(Fore.RED + "Opción no valida")
                    input(Fore.CYAN + "Pulsa Enter para continuar...")
#opcion Biblioteca del menu principal 
        elif opcion == "3":
            while True:
                os.system('cls')
                print(Fore.YELLOW + "Biblioteca")
                print("1. Prestar libro")
                print("2. Devolver libro")
                print(Fore.RED +"3. Volver atrás")
                sub_opcion = input("Seleccione una opción: ")
                if sub_opcion == "1":
                    biblioteca.prestar_libro()
                elif sub_opcion == "2":
                    biblioteca.devolver_libro()
                elif sub_opcion == "3":
                    break
                else:
                    print(Fore.RED + "Opción no valida")
                    input(Fore.CYAN + "Pulsa Enter para continuar...")

        elif opcion == "4":
            break
        else:
            print(Fore.RED + "Opción no valida")
            input(Fore.CYAN + "Pulsa Enter para continuar...")
#llamo a la funcion 
iniciar_biblioteca()

