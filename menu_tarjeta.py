deuda = 100000
cupo = 0
saldo_t = 500000

while True:
    #opc = realizar pago de cupo, simular nuevas compras (sumadas todas las compras se restan al cupo disp)
    print("==========")
    print("---MENU---")
    print("==========")
    print("[1] Pago de tarjeta.")
    print("[2] Compras.")
    print("[3] salir.")
    try:
        opc = int(input("Ingresa la opcion: "))
    except ValueError:
        print("Solo se permiten numeros enteros.")
        continue

    if opc == 1:
        print(f"Tu deuda es de: {deuda}.")
        print("-----")
        print(f"Tu saldo actual es de: {saldo_t}")
        try:
            monto_pago = int(input("cual es el monto que deseas ingresar?: "))
        except ValueError:
            print("Solo se permiten numeros enteros")
            continue

        if monto_pago < 0:
            print("Solo se permiten numeros enteros positivos.")
        elif monto_pago > 500000:
            print("El monto supera el cupo/saldo de la tarjeta. Ingresa otro por favor")
        else:
            print("Pago exitoso.")
            deuda = deuda - monto_pago
            saldo_t = saldo_t - monto_pago
            print(f"El saldo actual de la tarjeta es: {saldo_t}")
            if deuda > 0:
                print(f"Su nueva deuda es: {deuda}")
                print(f"El saldo de la tarjeta actual es: {saldo_t}")
            else:
                print("Deuda saldada. Gracias!")

    elif opc == 2:
        print(f"El saldo actual de la tarjeta es de: {saldo_t}")
        c_compras = int(input("Ingresa la cantidad de compras: "))
        ms_compras = []
        for c in range(1, c_compras+1):
            m_compra = int(input("Ingresa el monto de tu compra."))
            if m_compra < 0:
                print("El monto debe ser mayor o igual a cero")
            else:
                ms_compras.append(m_compra)
                sum_com = sum(ms_compras)
                #Realizar compra
                saldo_t = saldo_t - sum_com

    elif opc == 3:
        print("Saliendo del programa.")
        break
    
    else:
        print("Opcion no valida.")
        