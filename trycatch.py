#diviisones por zero = ZeroDivisionError
#tipos de datos = TypeError (cadena por numero)
#Error de valores = ValueError (ingresar int en string)
#Archivo no encontrado = FileExistsError (no encuentra el archivo)
#Error de sintaxsis  = SyntaxError (error de syntaxis en el codigo)


"""try:
    #codigo que genera exepcion
    num = 0
    num = int(input("Ingresa un numero: "))
    resultado = num/2
except FileExistsError as div_excepcion:
    print(f"Se produjo un error: {div_excepcion}")
else:
    print("No se produjo ninguna excepcion")
finally:
    print("Este bloque se ejecuta siempre")"""

while True:
    try:
        edad = int(input("Ingresa tu edad: "))
    except ValueError as e:
        print(f"Error, solo se permiten numeros enteros. {e}")
    else:
        break