import math

# Solicitar el radio al usuario
radio = float(input("Ingrese el radio de la esfera: "))

# Calcular el volumen de la esfera
volumen = (4/3) * math.pi * (radio ** 3)

# Mostrar el volumen
print(f"El volumen de la esfera con radio {radio} es: {volumen}")