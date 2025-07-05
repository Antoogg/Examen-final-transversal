productos = {
 '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
 '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
 'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
 'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
 'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
 '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
 '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
 'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
 }

stock = {
 '8475HD': [387990,10], 
 '2175HD': [327990,4], 
 'JjfFHD': [424990,1],
 'fgdxFHD': [664990,21], 
 '123FHD': [290890,32], 
 '342FHD': [444990,7],
 'GF75HD': [749990,2], 
 'UWU131HD': [349990,1], 
 'FS1230HD': [249990,0],
 }

def stock_marca(marca):
    stock_total=0

    for modelo, datos in productos.items():
        if datos[0].lower()==marca.lower():
            stock_total+=stock.get(modelo, [0, 0])[1]
    print(f"El stock es: {stock_total}")

def busc_x_precio(p_min, p_max):
    modelos_disp=[]
    for modelo, (precio, cantidad) in stock.items():
        if p_min<=precio<=p_max and cantidad>0:
            marca=productos[modelo][0]
            modelos_disp.append(f"{marca}---{modelo}")

    if modelos_disp:
        modelos_disp.sort()
        print("Los notebooks entre los precios consultados son:", modelos_disp)
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0]=p
        return True
    else:
        return False
    

while True:
    print("""
        \n----- MENÚ PRINCIPAL -----
    1. Stock por marca.
    2. Búsqueda por precio.
    3. Actualizar precio.
    4. Salir.
""")
    try:
        op=int(input("Ingrese una opción: "))
        if op==1:
            marca=input("Ingrese la marca a buscar.")
            stock_marca(marca)

        elif op==2:
            while True:
                try:
                    p_min=int(input("\nIngrese el precio mínimo. "))
                    p_max=int(input("Ingrese el precio máximo. "))
                    busc_x_precio(p_min, p_max)
                    break
                except ValueError:
                    print("¡¡Debe ingresar valores entreros.!!")

        elif op==3:
            while True:
                modelo=input("Ingrese el modelo a actuaizar. ")
                try:
                    p=int(input("Ingrese precio nuevo: "))
                    if actualizar_precio(modelo, p):
                        print("¡¡Precio actualizado.!!")
                    else:
                        print("El modelo no existe. ")
                except ValueError:
                    print("Debe ingresar un precio válido. ")
                otro=input("\n¿Desea actualizar otro precio (si/no)?: ").lower()
                if otro!="si":
                    break

        elif op==4:
            print("Programa finalizado. \n")
            break

        else:
            print("Debe seleccionar una opción válida. ")

    except ValueError:
        print("Ingrese una opción valida.")

