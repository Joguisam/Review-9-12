# Crea un script que me permita gestionar carros.
# El programa debe:
# 1. Agregar carros a una lista.*
# 2. mostrar todos los carros registrados*
# 3. Eliminar un carro de la lista.
# 4. Editar datos de un carro.
# 5. Salir

# Crea la lista vacia de carros
MenuOpciones = ("1. Agregar carros", "2. Mostrar los carros registrados", "3. eliminar autos", "4. editar datos")

carros = []

for x in MenuOpciones:
    print(x)

opcion = input("seleccione una opcion: ")

    if opcion == "1":
        placa = input("Ingrese el numero de placa: ")
        modelo = input("Ingrese el modelo del auto: ")
        marca = input("Ingrese la marca del auto: ")
        carros.append([placa, modelo, marca])
        print("producto agregado correctamente")
    
    elif opcion == "2":
        if len(carros) == 0:
            print("la lista está vacía.")
        else:
            print("Lista actual: ")
            for i in range(len(carros)):
                print("PLACA   MODELO   MARCA")
                print(f"{carros[i][0]:<8} {carros[i][1]:<8} {carros[i][2]:<8}")
               
    
    elif opcion == "3":
        auto = input("Ingrese el nombre del producto a eliminar: ")
        if auto in carros:
            carros.remove(auto)
            print(f"Elemento eliminado: {auto}")
        else:
            print("El producto no existe en la lista.")
    
    elif opcion == "4":
        auto = input("Ingrese el auto a insertar: ")
        pos_texto = input("Ingrese la posicion donde desea insertarlo: ")

        pos = int(pos_texto)
        if 0 <= pos <= len(carros):
            carros.insert(pos, auto)
            print("Producto insertado correctamente")
        else:
            print("posicion invalida.")

    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion invalida. Intente nuevamente.")

