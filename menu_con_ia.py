while True:
    # Encabezado de la calculadora
    print("\033[1;36m" + "=" * 50)
    print(" " * 15 + "CALCULADORA AVANZADA")
    print("=" * 50 + "\033[0m")
    print("\n")

    # Ingreso de números con validación
    while True:
        try:
            print("\033[1;33m" + "Ingresa los números para operar:" + "\033[0m")
            num1 = int(input("  Primer número:  "))
            num2 = int(input("  Segundo número: "))
            print("\n")
            break
        except ValueError:
            print("\033[1;31m" + "Error: Solo se permiten números enteros. Intenta nuevamente." + "\033[0m")
            print("\n")

    # Menú de operaciones
    while True:
        print("\033[1;34m" + "╔══════════════════════════════╗")
        print("║         MENÚ PRINCIPAL       ║")
        print("╠══════════════════════════════╣")
        print("║ \033[1;32m1\033[1;34m - Sumar                    ║")
        print("║ \033[1;32m2\033[1;34m - Restar                   ║")
        print("║ \033[1;32m3\033[1;34m - Multiplicar              ║")
        print("║ \033[1;32m4\033[1;34m - Dividir                  ║")
        print("║ \033[1;31m0\033[1;34m - Cambiar números          ║")
        print("║ \033[1;31m5\033[1;34m - Salir del programa       ║")
        print("╚══════════════════════════════╝" + "\033[0m")
        print("\n")

        try:
            opc = int(input("\033[1;35m" + "Selecciona una opción (0-5): " + "\033[0m"))
        except ValueError:
            print("\033[1;31m" + "Error: Debes ingresar un número válido." + "\033[0m")
            print("\n")
            continue

        # Operaciones
        if opc == 1:
            print("\n")
            print("\033[1;32m" + "═" * 30)
            print(f" RESULTADO: {num1} + {num2} = {num1 + num2}")
            print("═" * 30 + "\033[0m")
            print("\n")
        elif opc == 2:
            print("\n")
            print("\033[1;32m" + "═" * 30)
            print(f" RESULTADO: {num1} - {num2} = {num1 - num2}")
            print("═" * 30 + "\033[0m")
            print("\n")
        elif opc == 3:
            print("\n")
            print("\033[1;32m" + "═" * 30)
            print(f" RESULTADO: {num1} × {num2} = {num1 * num2}")
            print("═" * 30 + "\033[0m")
            print("\n")
        elif opc == 4:
            try:
                print("\n")
                print("\033[1;32m" + "═" * 30)
                print(f" RESULTADO: {num1} ÷ {num2} = {num1 / num2:.2f}")
                print("═" * 30 + "\033[0m")
                print("\n")
            except ZeroDivisionError:
                print("\033[1;31m" + "Error: No se puede dividir por cero." + "\033[0m")
                print("\n")
        elif opc == 0:
            print("\n")
            print("\033[1;33m" + "Puedes ingresar nuevos números..." + "\033[0m")
            print("\n")
            break
        elif opc == 5:
            print("\n")
            print("\033[1;36m" + "=" * 50)
            print(" " * 15 + "¡Gracias por usar la calculadora!")
            print("=" * 50 + "\033[0m")
            print("\n")
            exit()
        else:
            print("\033[1;31m" + "Opción no válida. Por favor ingresa un número del 0 al 5." + "\033[0m")
            print("\n")