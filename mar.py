comida_favorita = ["Hamburguesa", "Lasaña", "Helado de chocolate"]


pedir_mas = "si"

while pedir_mas == "si":
    
    
    eleccion = int(input("cual desea de las opciones:[1],[2] o [3]: "))
    indice_maquina = eleccion - 1
    print(f"gracias por elegir {comida_favorita[indice_maquina]}")
    
    
    
    pedir_mas = input("¿Desea elegir otra comida? (si/no): ")


print("¡Gracias por comer con nosotros, vuelva pronto!")