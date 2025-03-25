/// Solicitar datos al usuario
nivel_usuario = int(input("Ingrese su nivel de acceso (0-5): "))
nivel_requerido = int(input("Ingrese el nivel de acceso requerido (0-5): "))
tarjeta_entrada = input("¿Su tarjeta está activa? (si/no): ")


if tarjeta_entrada == "si":
    tarjeta_activa = True
else:
    tarjeta_activa = False

dias_ultima_contraseña = int(input("Ingrese los días desde el último cambio de contraseña: "))


if nivel_usuario == 0:
    print("Acceso denegado: nivel de acceso insuficiente.")
elif nivel_usuario >= nivel_requerido:
    if tarjeta_activa and dias_ultima_contraseña <= 30:
        print("Acceso permitido.")
    elif not tarjeta_activa:
        print("Acceso denegado: la tarjeta de identificación no está activa.")
    elif dias_ultima_contraseña > 30:
        print("Acceso denegado: debe cambiar su contraseña.")
else:
    print("Acceso denegado: nivel de acceso insuficiente.")
