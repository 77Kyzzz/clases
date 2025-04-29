import random
zona = random.randint(1,50)
zona_ele = int(input("Ingresa la zona elegida (1-50): "))

intentos = 1

print(zona)

while intentos < 3:
    if zona_ele == zona:
        print("Tesoro encontrado! felicidades, pirata!")
        intentos = intentos + 1
    elif zona_ele.min(zona):
       print("Muy cerca")
       intentos = intentos + 1
    else:
       print("Muy lejos")
       intentos = intentos + 1

print("xd")