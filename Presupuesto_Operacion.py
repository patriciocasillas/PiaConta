mtzArticulos = []
mtzPVenta = []
dicArticulos = dict(CodArticulo="", NomArticulos= "")
dicPVenta = dict(CodArticulo = "", UnAVender = 0, Pventa = 0, Semestre = 0)
lstValArticulo = []

dicArticulos["CodArticulo"] = "1"
dicArticulos["NomArticulo"] = "CL"
mtzArticulos.append(dicArticulos.copy())

dicArticulos["CodArticulo"] = "2"
dicArticulos["NomArticulo"] = "CE"
mtzArticulos.append(dicArticulos.copy())

dicArticulos["CodArticulo"] = "3"
dicArticulos["NomArticulo"] = "CR"
mtzArticulos.append(dicArticulos.copy())

##Presupuesto de venta
def Sales_Budget():
    Opcion2 = ""
    while(Opcion2 != "N"):
        print()
        print("==PRESUPUESTO DE VENTA==")
        print("")
        Opcion2 = input("¿Deseas agregar informacion de un producto (S/N): ")
        if (Opcion2.upper() == "S"):
            Opcion3 = 0
            print()

            print("Catalago de Articulos")
            for Diccionario in mtzArticulos:
                print(Diccionario["CodArticulo"] + ' - ' + Diccionario["NomArticulo"])
                lstValArticulo.append(Diccionario["CodArticulo"])
            Opcion3 = input("Ingrese el codigo del articulo a cargar: ")

            if(Opcion3 in lstValArticulo):
                for Cont in range(0, 2):
                    for Campo in dicPVenta:
                        if (Campo == "CodArticulo"):
                            dicPVenta[Campo] = Opcion3
                        elif (Campo == "Semestre"):
                            dicPVenta[Campo] = (Cont + 1)
                        else:
                            dicPVenta[Campo] = float(input("Ingresa la cantidad de " + Campo + " para el " + str(Cont + 1)  + "° semestre: "))
                    mtzPVenta.append(dicPVenta.copy())
                print(mtzPVenta)                   

            else:
                print("El codigo de articulo no es valida...")
                print()

        elif (Opcion2.upper() == "N"):
                    print()
                    print("Regresando al menú principal...")
                    print()
                    Opcion2 = "N"

        else:
            print()
            print("Opcion no valida...")
            print()

##Determinación del saldo de Clientes y Flujo de Entradas
def DCBI():
    print()
##Presupuesto de Producción
def Production_Budget():
    print()
##Presupuesto de Requerimiento de Materiales
def Materials_Requirement_Budget():
    print()
##Presupuesto de Compra de Materiales
def Materials_Purchase_Budget():
    print()
##Determinación del saldo de Proveedores y Flujo de Salidas
def DBSO():
    print()
##Presupuesto de Mano de Obra Directa
def Direct_Labor_Budget():
    print()
##Presupuesto de Gastos Indirectos de Fabricación
def IMEB():
    print()
##Presupuesto de Gastos de Operación
def Operating_Expenses_Budget():
    print()
##Determinación del Costo Unitario de Productos Terminados
def DUCFP():
    print()
##Valuación de Inventarios Finales
def Final_Inventory_Valuation():
    print()