from typing import List, Dict, Set

# Clase Libro
class Libro:
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        # Usamos una tupla para los atributos inmutables
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    @property
    def titulo(self):
        return self.info[0]

    @property
    def autor(self):
        return self.info[1]

    def __str__(self):
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn}, Categoría: {self.categoria})"


# Clase Usuario
class Usuario:
    def __init__(self, nombre: str, user_id: str):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados: List[Libro] = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.user_id}, Libros prestados: {len(self.libros_prestados)}"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros: Dict[str, Libro] = {}  # Diccionario con ISBN como clave
        self.usuarios: Dict[str, Usuario] = {}  # Diccionario de usuarios por ID
        self.ids_usuarios: Set[str] = set()  # Conjunto de IDs únicos

    def agregar_libro(self):
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        categoria = input("Ingrese la categoría del libro: ")
        isbn = input("Ingrese el ISBN del libro: ")
        libro = Libro(titulo, autor, categoria, isbn)
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print("Este libro ya existe en la biblioteca.")

    def quitar_libro(self):
        isbn = input("Ingrese el ISBN del libro a eliminar: ")
        if isbn in self.libros:
            eliminado = self.libros.pop(isbn)
            print(f"Libro eliminado: {eliminado}")
        else:
            print("No se encontró el libro con ese ISBN.")

    def registrar_usuario(self):
        nombre = input("Ingrese el nombre del usuario: ")
        user_id = input("Ingrese el ID de usuario: ")
        if user_id not in self.ids_usuarios:
            usuario = Usuario(nombre, user_id)
            self.usuarios[user_id] = usuario
            self.ids_usuarios.add(user_id)
            print(f"Usuario registrado: {usuario}")
        else:
            print("El ID de usuario ya existe.")

    def baja_usuario(self):
        user_id = input("Ingrese el ID del usuario a eliminar: ")
        if user_id in self.usuarios:
            eliminado = self.usuarios.pop(user_id)
            self.ids_usuarios.remove(user_id)
            print(f"Usuario eliminado: {eliminado.nombre}")
        else:
            print("No se encontró un usuario con ese ID.")

    def prestar_libro(self):
        isbn = input("Ingrese el ISBN del libro a prestar: ")
        user_id = input("Ingrese el ID del usuario: ")
        if isbn in self.libros and user_id in self.usuarios:
            libro = self.libros.pop(isbn)
            self.usuarios[user_id].libros_prestados.append(libro)
            print(f"Libro prestado: {libro.titulo} a {self.usuarios[user_id].nombre}")
        else:
            print("No se pudo realizar el préstamo. Verifique ISBN y usuario.")

    def devolver_libro(self):
        isbn = input("Ingrese el ISBN del libro a devolver: ")
        user_id = input("Ingrese el ID del usuario: ")
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro
                    print(f"Libro devuelto: {libro.titulo}")
                    return
        print("No se encontró el libro en los préstamos de este usuario.")

    def buscar_libro(self):
        criterio = input("Buscar por (titulo/autor/categoria): ").lower()
        valor = input("Ingrese el valor de búsqueda: ")
        resultados = []
        for libro in self.libros.values():
            if (criterio == "titulo" and valor.lower() in libro.titulo.lower()) or \
               (criterio == "autor" and valor.lower() in libro.autor.lower()) or \
               (criterio == "categoria" and valor.lower() in libro.categoria.lower()):
                resultados.append(libro)

        if resultados:
            print("Resultados de la búsqueda:")
            for r in resultados:
                print(r)
        else:
            print("No se encontraron libros que coincidan con la búsqueda.")

    def listar_prestados(self):
        user_id = input("Ingrese el ID del usuario: ")
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")


if __name__ == "__main__":
    biblioteca = Biblioteca()

    while True:
        print("\n--- Sistema de Biblioteca Digital ---")
        print("1. Agregar libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar libros prestados")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            biblioteca.agregar_libro()
        elif opcion == "2":
            biblioteca.quitar_libro()
        elif opcion == "3":
            biblioteca.registrar_usuario()
        elif opcion == "4":
            biblioteca.baja_usuario()
        elif opcion == "5":
            biblioteca.prestar_libro()
        elif opcion == "6":
            biblioteca.devolver_libro()
        elif opcion == "7":
            biblioteca.buscar_libro()
        elif opcion == "8":
            biblioteca.listar_prestados()
        elif opcion == "9":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intente de nuevo.")
