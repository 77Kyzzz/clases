import random

intentos = 3
limite1 = int(input("Ingresa el limite 1: "))
limite2 = int(input("Ingresa el limite 2: "))
zona_random = random.randint(min(limite1, limite2), max(limite1, limite2))

while intentos > 0:
    zona_elegida = int(input(f"Intenta adivinar el numero: ({limite1} - {limite2}): "))
    print(f"Zona elegida: {zona_elegida}, Zona random: {zona_random}")

    if zona_elegida == zona_random:
        print("Felicidades Ganaste!")
        break
    elif abs(zona_elegida - zona_random) in [1, 2, 3]:
        print("Muy cerca!")
    else:
        print("Muy lejos!")
    
    intentos -= 1

if intentos == 0:
    print(f"Perdiste nt. la zona era: {zona_random}")