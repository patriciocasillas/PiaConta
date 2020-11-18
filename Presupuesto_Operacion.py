import Packages

##Funciones
##Presupuesto de venta
def Sales_Budget():
    Opcion2 = 1
    while(Opcion2 != 0):
        Packages.Clean()
        print("==PRESUPUESTO DE VENTA==")
        print("")
        print("1.- Agregar información de un producto")
        print("2.- Mostrar Reporte de presupuesto de venta")
        print("\n0.- Regresar al Menú principal\n")
        Opcion2 = int(input("Ingresa la opción a realizar: "))

        if (str(Opcion2) == ""):
            print("Por favor selecciona una opción")
            input("presiona la tecla Enter para continuar")
            Packages.Clean()
        elif (Opcion2 == 1):
            Packages.Clean()
            Opcion3 = 0
            print()

            print("Catalago de Articulos")
            for Diccionario in Packages.mtzArticulos:
                print(Diccionario["CodArticulo"] + ' - ' + Diccionario["NomArticulo"])
                Packages.lstValArticulo.append(Diccionario["CodArticulo"])
            Opcion3 = input("Ingrese el codigo del articulo a cargar: ")

            if(Opcion3 in Packages.lstValArticulo):
                for Cont in range(0, 2):
                    TotalVentas = 0
                    for Campo in Packages.dicPVenta:
                        if (Campo == "CodArticulo"):
                            Packages.dicPVenta[Campo] = Opcion3
                        elif (Campo == "Semestre"):
                            Packages.dicPVenta[Campo] = (Cont + 1)
                        elif (Campo == "UnAVender" or Campo == "Pventa"):
                            Packages.dicPVenta[Campo] = float(input("Ingresa la cantidad de " + Campo + " para el " + str(Cont + 1)  + "° semestre: "))
                        else:
                            Packages.dicPVenta[Campo] = Packages.dicPVenta["UnAVender"] * Packages.dicPVenta["Pventa"]
                            TotalVentas += Packages.dicPVenta[Campo]
                            Packages.lstTotalVS.append(TotalVentas)
                    Packages.mtzPVenta.append(Packages.dicPVenta.copy())
                    Packages.Clean()
            else:
                print("ERROR: El codigo de articulo no es valido...")
                input("Presiona ENTER para continuar")
                Packages.Clean()
        
        elif (Opcion2 == 2):
            Packages.Clean()
            print("=Reporte Presupuesto de Venta=")
            print()
            for reporte in Packages.mtzPVenta:
                print(reporte)
            print("Total Venta Anual = ",sum(Packages.lstTotalVS))
            input("Presiona ENTER para continuar")

        elif (Opcion2 == 0):
            Packages.Clean()
            print("Regresando al Menú principal...")
            break
        
        else:
            print("ERROR: Opción no valida...")
            input("Presiona ENTER para continuar")
            Packages.Clean()

##Determinación del saldo de Clientes y Flujo de Entradas
def DCBI():
    print()
    print("== Determinación del saldo de Clientes y Flujo de Entradas ==")
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
