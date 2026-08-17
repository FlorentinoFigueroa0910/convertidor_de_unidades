def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def metros_a_pies(metros):
    return metros * 3.28084

def psi_a_bar(psi):
    return psi * 0.0689476

def menu():
    print("\n--- CONVERTIDOR DE UNIDADES ---")
    print("1. Celsius a Fahrenheit")
    print("2. Metros a Pies")
    print("3. PSI a Bar")
    print("4. Salir")

while True:
    menu()
    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "1":
        c = float(input("Ingresa la temperatura en °C: "))
        print(f"{c}°C = {celsius_a_fahrenheit(c):.2f}°F")
    elif opcion == "2":
        m = float(input("Ingresa la distancia en metros: "))
        print(f"{m} m = {metros_a_pies(m):.2f} ft")
    elif opcion == "3":
        p = float(input("Ingresa la presión en PSI: "))
        print(f"{p} PSI = {psi_a_bar(p):.4f} bar")
    elif opcion == "4":
        print("¡Programa finalizado!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")