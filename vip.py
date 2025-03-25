codigo d:# 
//Solicitar datos 

monto_compra = float(input("Ingrese el monto total de la compra: $"))
es_vip = input("¿Es miembro VIP? (si/no): ") == "si"
tiene_codigo_descuento = input("¿Tiene un código de descuento especial? (si/no): ") == "si"


descuento = 0


if monto_compra > 100:
    descuento += 20


if es_vip:
    descuento += 10


if tiene_codigo_descuento:
    descuento += 5


monto_final = monto_compra * (1 - descuento / 100)


print(f"Descuento aplicado: {descuento}%")
print(f"Total a pagar después del descuento: ${monto_final}")
