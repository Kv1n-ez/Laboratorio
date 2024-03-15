print("Bienvenido al cajero automático")
saldo = 1500
usuario = 2020
contraseña = 1234

while True:
    inicio = int(input("Ingrese su Usuario: "))
    if inicio == usuario:
        break
    else:
        print("Número de Tarjeta incorrecta, intente nuevamente:")

while True:
    inicio = int(input("Ingrese su contraseña: "))
    if inicio == contraseña:
        print("¡Contraseña correcta! Bienvenido")
        break
    else:
        print("Contraseña incorrecta, intente nuevamente:")

    print("MENU")
    print("1. Retirar dinero")
    print("2. Mostrar saldo")
    print("3. Salir")
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        retirar = int(input("¿Cuánto desea retirar?: "))
        if retirar > saldo:
            print("El monto deseado excede su saldo actual")
        else:   
            saldo -= retirar
            print("Espere un momento...")
            print("¡Transacción finalizada! Tenga un buen día :)")
    elif opcion == 2:
        print(f"Saldo total: {saldo}")
    elif opcion == 3:
        print("¡Hasta la próxima!")
        exit()
    else:
        print("Opcion incorrecta, intentelo nuevamente")