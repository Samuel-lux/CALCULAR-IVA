print("Ingrese el código de producto: ")
code = int(input())
print("Ingrese el nombre del producto: ")
product = input()
print("Ingrese el precio del " + product + " registado con el codigo: " + str(code))
precio = int(input())
iva = precio * 1.12
print("El " + product + " Tiene un valor con IVA incluido de: " + str(iva))
quitar_iva = iva - precio
print("Por lo tanto, estaria pagando de Iva el: " + str(quitar_iva))
print("Resumen del producto: ")
print("Nombre: " + product)
print("Codigo: " + str(code))
print("Precio: " + str(precio))
print("precio total + iva: " + str(iva))
print("Diferencia del IVA: " + str(quitar_iva))

if precio== 0:(
    print("No es posible realizar esta operación")
)
input("******ENTER PARA SALIR*********")


