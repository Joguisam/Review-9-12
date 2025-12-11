inventario_carros = []

def agregar_carro():
    """Opción 1: Agrega un nuevo carro a la lista."""
    print("\n--- Agregar Carro ---")
    marca = input("Introduce la marca: ")
    modelo = input("Introduce el modelo: ")
    try:
        año = int(input("Introduce el año: "))
        nuevo_carro = {'marca': marca, 'modelo': modelo, 'año': año}
        inventario_carros.append(nuevo_carro)
        print(f"Carro '{marca} {modelo}' agregado con éxito.")
    except ValueError:
        print("Error: El año debe ser un número entero.")

def mostrar_carros():
    """Opción 2: Muestra todos los carros en la lista."""
    print("\n--- Inventario de Carros ---")
    if not inventario_carros:
        print("No hay carros registrados.")
    else:
        for i, carro in enumerate(inventario_carros):
            print(f"{i+1}. Marca: {carro['marca']}, Modelo: {carro['modelo']}, Año: {carro['año']}")
    print("----------------------------")

def eliminar_carro():
    """Opción 3: Elimina un carro de la lista por su índice."""
    mostrar_carros()
    if not inventario_carros:
        return

    try:
        num_carro = int(input("Introduce el número del carro a eliminar (ej. 1): "))
        indice = num_carro - 1
        if 0 <= indice < len(inventario_carros):
            carro_eliminado = inventario_carros.pop(indice)
            print(f"Carro '{carro_eliminado['marca']} {carro_eliminado['modelo']}' eliminado.")
        else:
            print("Número de carro no válido.")
    except ValueError:
        print("Entrada no válida. Introduce el número de la lista.")

def editar_carro():
    """Opción 4: Edita los datos de un carro existente."""
    mostrar_carros()
    if not inventario_carros:
        return

    try:
        num_carro = int(input("Introduce el número del carro a editar (ej. 1): "))
        indice = num_carro - 1
        if 0 <= indice < len(inventario_carros):
            print(f"Editando: {inventario_carros[indice]['marca']} {inventario_carros[indice]['modelo']}")
           
            inventario_carros[indice]['marca'] = input(f"Nueva marca (actual: {inventario_carros[indice]['marca']}): ") or inventario_carros[indice]['marca']
            inventario_carros[indice]['modelo'] = input(f"Nuevo modelo (actual: {inventario_carros[indice]['modelo']}): ") or inventario_carros[indice]['modelo']
            print("Datos del carro actualizados.")
        else:
            print("Número de carro no válido.")
    except ValueError:
        print("Entrada no válida. Introduce el número de la lista.")

# ----------------------------------------------------
# NUEVA FUNCIÓN Y CAMBIO EN LA TUPLA DEL MENÚ
# ----------------------------------------------------

def mostrar_formato_ejemplo():
    """Opción 5: Muestra un ejemplo de formato de datos usando un diccionario."""
    
    ejemplo_diccionario = {
        'marca': 'Ford',
        'modelo': 'Fiesta',
        'año': 2020,
        'color': 'Rojo'
    }
    print(ejemplo_diccionario)


OPCIONES_MENU = (
    (1, "Agregar carro", agregar_carro),
    (2, "Mostrar carros", mostrar_carros),
    (3, "Eliminar carro", eliminar_carro),
    (4, "Editar datos de un carro", editar_carro),
    (5, "Mostrar formato de datos de ejemplo", mostrar_formato_ejemplo),
    (6, "Salir del programa", None)
)

def mostrar_menu():
    print("\n========== MENÚ DE GESTIÓN DE CARROS ==========")
    for opcion, descripcion, _ in OPCIONES_MENU:
        print(f"{opcion}. {descripcion}")
    print("===============================================")

def main():
    opcion_elegida = None
  
    while opcion_elegida != 6: 
        mostrar_menu()
        try:
            opcion_elegida = int(input("Introduce el número de tu opción: "))
            
            accion = None
            for opcion, _, func in OPCIONES_MENU:
                if opcion == opcion_elegida:
                    accion = func
                    break
            
            if accion:
                accion()
            elif opcion_elegida == 6:
                print("Saliendo del programa. ¡Hasta pronto!")
            else:
                print("Opción no válida. Por favor, introduce un número del menú.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")

if __name__ == "__main__":
    main()