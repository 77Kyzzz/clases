cant_h = 0
nombre_h = ""
a_exp_h = 0
cant_el = 0
cant_no = 0

while True:

    try:
        cant_h = int(input("Ingrese la cantidad de superheroes: "))
    except ValueError:
        print("Ingresa un numero entero.")

    else:
        for i in range(1, cant_h+1):

            nombre_h = input(f"Ingresa el nombre del superheroe {i}: ")

        while True:
            try:
                a_exp_h = int(input(f"¿Cuántos años de experiencia tiene el superheroe {i}? "))
                if a_exp_h < 0:
                    print("La experiencia no puede ser negativa. Intente nuevamente.")
                    continue
                break
            except ValueError:
                print("Ingresa un número entero válido.")

        if a_exp_h > 60:
            print(f"{nombre_h} Tiene mas de {a_exp_h} años de experiencia: ELITE")
            cant_el = cant_el + 1

        elif a_exp_h <= 60:
            print(f"{nombre_h} Tiene menos de {a_exp_h} años de experiencia: NOVATO")
            cant_no = cant_no + 1

        print(f"La cantidad de superheroes ELITE es: {cant_el}")
        print(f"La cantidad de superheroes NOVATOS es: {cant_no}")
