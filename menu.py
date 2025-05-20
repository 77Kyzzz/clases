while True:
    while True:
        try:
            num1 = int(input("Ingresa el primer numero: "))
            num2 = int(input("Ingresa el segundo numero: "))
        except ValueError:
            print("Solo se permiten numeros enteros.")
            continue
        else:
            break

    while True:
        print("---Menu---")
        print(" [1] - Sumar")
        print(" [2] - Restar")
        print(" [3] - Multiplicar")
        print(" [4] - Dividir")
        print(" [5] - Salir")
        print(" [0] - Otros Numeros.")
        try:    
            opc = int(input("Ingresa una opcion: "))
        except ValueError:
            print("Solo se permiten numeros enteros.")
            continue
        
        if opc == 1:
            print("\n")
            print("Suma:")
            print(num1 + num2)
            print("\n")
        elif opc == 2:
            print("\n")
            print("Resta:")
            print(num1 - num2)
            print("\n")
        elif opc == 3:
            print("\n")
            print("multiplicacion")
            print(num1 * num2)
            print("\n")
        elif opc == 4:
            print("\n")
            print("Division")
            print(num1 / num2)
            print("\n")
        elif opc == 5:
            print("\n")
            print("Saliendo...")
            exit()
        elif opc == 0:
            print("\n")
            print("Elije otros numeros")
            print("\n")
            break
        else:
            print("La opcion ingresada no es valida")