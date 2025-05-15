import time

while True:
    user_opt = int(input("Desea terminar? (1 - SI  | 2 - NO): "))

    if user_opt == 1:
        time.sleep(1)
        print("Saliendo")
        break
    else:
        for i in range(10):
            print(f"Chupalo x {i+1}")
            i+1