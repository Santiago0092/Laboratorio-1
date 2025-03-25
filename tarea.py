tarea_1 = "Tarea 1"
dias_limite_1 = 10
dias_real_1 = 12

tarea_2 = "Tarea 2"
dias_limite_2 = 5
dias_real_2 = 5

i = 1
while i <= 2:
    if i == 1:
        nombre_tarea = tarea_1
        dias_limite = dias_limite_1
        dias_real = dias_real_1
    else:
        nombre_tarea = tarea_2
        dias_limite = dias_limite_2
        dias_real = dias_real_2
    
    if dias_real > dias_limite:
        retraso_dias = dias_real - dias_limite
        porcentaje_retraso = (retraso_dias / dias_limite) * 100
    else:
        retraso_dias = 0
        porcentaje_retraso = 0.0
    
    print("Tarea:", nombre_tarea)
    print("Retraso:", retraso_dias, "días")
    print("Porcentaje de retraso:", (porcentaje_retraso, ), "%\n")
    
    i += 1
