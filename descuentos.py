print("Bienvenido, Ingrese su zona (Norte, Centro, Sur): ")
zona = input("- ").lower()
print("Gracias. Ahora ingrese su nota: ")
nota = float(input("- "))

descuento = 0

bono = 2500000

if zona == "sur": 
    if nota >= 6.0:
        descuento = 0.25
        desc_por = 25
elif zona == "centro":
    if nota >= 6.0:
        descuento = 0.2
        desc_por = 20
elif zona == "sur":
    if nota >= 5.0 and nota <= 6.0:
        descuento = 0.15
        desc_por = 15
elif zona == "centro":
    if nota >= 4.0 and nota <= 5.0:
        descuento = 0.1
        desc_por = 10
elif zona == "norte":
    descuento = 0.12
    desc_por = 12
    if nota >= 5.5:
        descuento = descuento + 0.5
        desc_por = desc_por + 5

print(desc_por)

desc_a_bono = bono * descuento
bono_final = bono - desc_a_bono

print(f"El bono que recibira es de: {bono_final}, con un descuento de: {desc_por}% / {desc_a_bono}")

