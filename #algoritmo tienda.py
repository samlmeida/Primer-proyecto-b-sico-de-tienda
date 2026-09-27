#algoritmo tienda
cliente = input ("Escribe tu nombre (si eres cliente VIP por favor añade las siglas VIP al final de tu nombre)")
catalogo = {
    'ram 8 gb' : 60,
    'ssd 1tb' : 60,
    'cpu' : 50,
    'refrigeracion' : 40,
    'targeta madre' : 50,
    'torre completa' : 100
}
subtotal = 0
compra = input ("¿Qué desea comprar (Ram 8 gb, SSD 1tb, CPU, Refrigeracion, Targeta madre, Torre completa)?:").lower().strip()
if compra in catalogo:
        subtotal += catalogo[compra]
        print("su subtotal es:", subtotal)
else:
        print("Producto no disponible. Por favor elija otro producto.")
while True:
    segunda_compra = input("¿Desea comprar algo más? (si/no): ").lower().strip()
    
    if segunda_compra == "no":
        break
        
    compra = input("¿Qué otro producto deseas agregar?: ").lower().strip()
    
    if compra in catalogo:
        subtotal += catalogo[compra]
        print("Su subtotal es:", subtotal)
    else:
        print("Producto no disponible. Por favor elija otro producto.")
total = subtotal
if "VIP" in cliente:
    total *= 0.9
if total > 100:
    total *= 0.95
print ('su total a pagar es:', total)
print ("gracias por comprar", cliente)