import Packages

def Reportes(P_mtz):
    for reportes in range(0,len(P_mtz)):
        print("Presupuesto de producción: ")
        for reporte in P_mtz[reportes]:
            print(f"{reporte}: {P_mtz[reportes][reporte]}")

##Presupuesto de venta
def Sales_Budget():
    Opcion2 = 1
    while(Opcion2 != 0):
        Packages.Clean()
        print("== PRESUPUESTO DE VENTA ==")
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
            CodArt = 0
            print()

            print("Catalago de Articulos")
            for Diccionario in Packages.mtzArticulos:
                print(Diccionario["CodArticulo"] + ' - ' + Diccionario["NomArticulo"])
                Packages.lstValArticulo.append(Diccionario["CodArticulo"])
            CodArt = input("Ingrese el codigo del articulo a cargar: ")

            if(CodArt in Packages.lstValArticulo):
                for Cont in range(0, 2):
                    TotalVentas = 0
                    for Campo in Packages.dicPVenta:
                        if (Campo == "CodArticulo"):
                            Packages.dicPVenta[Campo] = CodArt
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
    while True:
        Packages.Clean()
        print("== Determinación del saldo de Clientes y Flujo de Entradas ==\n")
        print("1.- Agregar información de un Saldo de Cliente")
        print("2.- Mostrar Reporte de los saldos de Clientes y Flujos de Entradas")
        print("\n0.- Regresar al Menú principal\n")
        Opcion = input("Ingresa la opción a realizar: ")

        if Opcion == "":
            print("ERROR: Por favor selecciona una opción")
            input("presiona la tecla ENTER para continuar...")
            Packages.Clean()

        elif Opcion == "1":
            Packages.Clean()
            print()
            print("== Determinación del saldo de Clientes y Flujo de Entradas ==\n")

            for movimiento in Packages.dicSaldosCliente: 
                ##Saldo de Clientes
                if movimiento == "SaldoCliente":
                    Packages.dicSaldosCliente[movimiento] = float(input("Ingresa el Saldo del Cliente: "))
                ##Ventas
                elif movimiento == "Ventas":
                    Packages.dicSaldosCliente[movimiento] = sum(Packages.lstTotalVS)
                ##Total Cliente
                elif movimiento == "TotalCliente":
                    Packages.dicSaldosCliente[movimiento] = (Packages.dicSaldosCliente["SaldoCliente"] + Packages.dicSaldosCliente["Ventas"])
                
                ##Entradas de Efectivo Por Cobranza
                elif movimiento == "EntCobranza":
                    Packages.dicSaldosCliente[movimiento] = Packages.dicSaldosCliente["SaldoCliente"]
                elif movimiento == "EntCobranza0":
                    Packages.dicSaldosCliente[movimiento] = (Packages.dicSaldosCliente["Ventas"]*0.8)
                elif movimiento == "TotalEnt":
                    Packages.dicSaldosCliente[movimiento] = (Packages.dicSaldosCliente["EntCobranza"] + Packages.dicSaldosCliente["EntCobranza0"])
                
                ##Saldo de Clientes Total
                elif movimiento == "Total":
                    Packages.dicSaldosCliente[movimiento] = (Packages.dicSaldosCliente["TotalCliente"] - Packages.dicSaldosCliente["TotalEnt"])
            Packages.mtzDSCFE.append(Packages.dicSaldosCliente.copy())

        elif Opcion == "2":
            Packages.Clean()
            Reportes(Packages.mtzDSCFE)
            input("presiona la tecla ENTER para continuar...")

        elif Opcion == "0":
            Packages.Clean()
            print("Regresando al Menú principal...")
            break
        
        else:
            print("ERROR: Opción no valida...")
            input("Presiona ENTER para continuar")
            Packages.Clean()

##Presupuesto de Producción
def Production_Budget():
    while True:
        Packages.Clean()
        print("== PRESUPUESTO DE PRODUCCION ==")
        print()
        print("1.- Agregar información de un presupuesto de producción")
        print("2.- Mostrar Reporte de presupuesto de produccion")
        print("\n0.- Regresar al Menú principal\n")
        Opcion  = input("Ingrese la opción a realizar: ")

        if Opcion == "":
            print("ERROR: Por favor selecciona una opción")
            input("presiona la tecla ENTER para continuar...")
            Packages.Clean()

        elif Opcion == "1":
            Packages.Clean()
            CodArt = 0
            print("Catalago de Articulos")
            for Diccionario in Packages.mtzArticulos:
                print(Diccionario["CodArticulo"] + ' - ' + Diccionario["NomArticulo"])
                Packages.lstValArticulo.append(Diccionario["CodArticulo"])
            CodArt = input("Ingrese el codigo del articulo a cargar: ")

            if(CodArt in Packages.lstValArticulo):
                for reportes in range(0,len(Packages.mtzPVenta)):
                    #print("Saldo de Clientes y Flujo de Entradas: ")
                    for reporte in Packages.mtzPVenta[reportes]:
                        if Packages.mtzPVenta[reportes][reporte] == str(CodArt):
                            Packages.dicPresupuestoOp["CodArticulo"] = str(CodArt)
                            for campo in Packages.mtzPVenta[reportes]:
                                if campo == "Semestre" and Packages.mtzPVenta[reportes][campo] == 1:
                                    for valor in Packages.mtzPVenta[reportes]:
                                        if valor == "UnAVender":
                                            Packages.dicPresupuestoOp["UnVender1S"] = Packages.mtzPVenta[reportes][valor]

                                elif campo == "Semestre" and Packages.mtzPVenta[reportes][campo] == 2:
                                    for valor in Packages.mtzPVenta[reportes]:
                                        if valor == "UnAVender":
                                            Packages.dicPresupuestoOp["UnVender2S"] = Packages.mtzPVenta[reportes][valor] = Packages.mtzPVenta[reportes][valor]
                        
                Packages.dicPresupuestoOp["TotalUnVender"] = Packages.dicPresupuestoOp["UnVender1S"] + Packages.dicPresupuestoOp["UnVender2S"]

                Packages.dicPresupuestoOp["InvenFin1"] = float(input("Ingresa el valor del Inventario Final del Semestre 1: "))
                Packages.dicPresupuestoOp["InvenFin2"] = float(input("Ingresa el valor del Inventario Final del Semestre 2: "))
                Packages.dicPresupuestoOp["InvenFinTotal"] = Packages.dicPresupuestoOp["InvenFin2"]

                Packages.dicPresupuestoOp["TotalUN1"] = Packages.dicPresupuestoOp["InvenFin1"] + Packages.dicPresupuestoOp["UnVender1S"]
                Packages.dicPresupuestoOp["TotalUN2"] = Packages.dicPresupuestoOp["InvenFin2"] + Packages.dicPresupuestoOp["UnVender2S"]
                Packages.dicPresupuestoOp["TotalUN"] = Packages.dicPresupuestoOp["TotalUnVender"] + Packages.dicPresupuestoOp["InvenFinTotal"]

                Packages.dicPresupuestoOp["InventarioIni1"] = float(input("Ingresa el valor del Inventario Inicial del Semestre 1: "))
                Packages.dicPresupuestoOp["InventarioIni2"] = float(input("Ingresa el valor del Inventario Inicial del Semestre 2: "))
                Packages.dicPresupuestoOp["InventarioIniTotal"] = Packages.dicPresupuestoOp["InventarioIni1"]

                Packages.dicPresupuestoOp["UnidadesProd1"] = Packages.dicPresupuestoOp["TotalUN1"] - Packages.dicPresupuestoOp["InventarioIni1"]
                Packages.dicPresupuestoOp["UnidadesProd2"] = Packages.dicPresupuestoOp["TotalUN2"] - Packages.dicPresupuestoOp["InventarioIni2"]
                Packages.dicPresupuestoOp["UnidadesProdTotal"] = Packages.dicPresupuestoOp["TotalUN"] - Packages.dicPresupuestoOp["InventarioIniTotal"]

                Packages.mtzPresupuestoOp.append(Packages.dicPresupuestoOp.copy())
                Packages.Clean()

        elif Opcion == "2":
            Packages.Clean()
            Reportes(Packages.mtzPresupuestoOp)
            input("\nPresiona ENTER para continuar")
        
        elif Opcion == "0":
            Packages.Clean()
            print("Regresando al Menú principal...")
            break
        
        else:
            print("ERROR: Opción no valida...")
            input("Presiona ENTER para continuar")
            Packages.Clean()

##Presupuesto de Requerimiento de Materiales
def Materials_Requirement_Budget():
    while True:
        Packages.Clean()
        print("== PRESUPUESTO DE PRODUCCION ==")
        print()
        print("1.- Agregar información de un producto")
        print("2.- Mostrar Reporte de presupuesto de produccion")
        print("\n0.- Regresar al Menú principal\n")
        Opcion  = input("Ingrese la opción a realizar: ")

        if Opcion == "":
            print("ERROR: Por favor selecciona una opción")
            input("presiona la tecla ENTER para continuar...")
            Packages.Clean()

        elif Opcion == "1":
            Packages.Clean()

        elif Opcion == "2":
            Packages.Clean()
        
        elif Opcion == "0":
            Packages.Clean()
            print("Regresando al Menú principal...")
            break
        
        else:
            print("ERROR: Opción no valida...")
            input("Presiona ENTER para continuar")
            Packages.Clean()
##Presupuesto de Compra de Materiales
def Materials_Purchase_Budget():
    while True:
        Packages.Clean()
        print("== PRESUPUESTO DE PRODUCCION ==")
        print()
        print("1.- Agregar información de un producto")
        print("2.- Mostrar Reporte de presupuesto de produccion")
        print("\n0.- Regresar al Menú principal\n")
        Opcion  = input("Ingrese la opción a realizar: ")

        if Opcion == "":
            print("ERROR: Por favor selecciona una opción")
            input("presiona la tecla ENTER para continuar...")
            Packages.Clean()

        elif Opcion == "1":
            Packages.Clean()

        elif Opcion == "2":
            Packages.Clean()
        
        elif Opcion == "0":
            Packages.Clean()
            print("Regresando al Menú principal...")
            break
        
        else:
            print("ERROR: Opción no valida...")
            input("Presiona ENTER para continuar")
            Packages.Clean()
##Determinación del saldo de Proveedores y Flujo de Salidas
def DBSO():
    while True:
        Packages.Clean()
        print("== PRESUPUESTO DE PRODUCCION ==")
        print()
        print("1.- Agregar información de un producto")
        print("2.- Mostrar Reporte de presupuesto de produccion")
        print("\n0.- Regresar al Menú principal\n")
        Opcion  = input("Ingrese la opción a realizar: ")

        if Opcion == "":
            print("ERROR: Por favor selecciona una opción")
            input("presiona la tecla ENTER para continuar...")
            Packages.Clean()

        elif Opcion == "1":
            Packages.Clean()

        elif Opcion == "2":
            Packages.Clean()
        
        elif Opcion == "0":
            Packages.Clean()
            print("Regresando al Menú principal...")
            break
        
        else:
            print("ERROR: Opción no valida...")
            input("Presiona ENTER para continuar")
            Packages.Clean()
##Presupuesto de Mano de Obra Directa
def Direct_Labor_Budget():
    while True:
        Packages.Clean()
        print("== PRESUPUESTO DE PRODUCCION ==")
        print()
        print("1.- Agregar información de un producto")
        print("2.- Mostrar Reporte de presupuesto de produccion")
        print("\n0.- Regresar al Menú principal\n")
        Opcion  = input("Ingrese la opción a realizar: ")

        if Opcion == "":
            print("ERROR: Por favor selecciona una opción")
            input("presiona la tecla ENTER para continuar...")
            Packages.Clean()

        elif Opcion == "1":
            Packages.Clean()

        elif Opcion == "2":
            Packages.Clean()
        
        elif Opcion == "0":
            Packages.Clean()
            print("Regresando al Menú principal...")
            break
        
        else:
            print("ERROR: Opción no valida...")
            input("Presiona ENTER para continuar")
            Packages.Clean()
##Presupuesto de Gastos Indirectos de Fabricación
def IMEB():
    while True:
        Packages.Clean()
        print("== PRESUPUESTO DE PRODUCCION ==")
        print()
        print("1.- Agregar información de un producto")
        print("2.- Mostrar Reporte de presupuesto de produccion")
        print("\n0.- Regresar al Menú principal\n")
        Opcion  = input("Ingrese la opción a realizar: ")

        if Opcion == "":
            print("ERROR: Por favor selecciona una opción")
            input("presiona la tecla ENTER para continuar...")
            Packages.Clean()

        elif Opcion == "1":
            Packages.Clean()

        elif Opcion == "2":
            Packages.Clean()
        
        elif Opcion == "0":
            Packages.Clean()
            print("Regresando al Menú principal...")
            break
        
        else:
            print("ERROR: Opción no valida...")
            input("Presiona ENTER para continuar")
            Packages.Clean()
##Presupuesto de Gastos de Operación
def Operating_Expenses_Budget():
    while True:
        Packages.Clean()
        print("== PRESUPUESTO DE PRODUCCION ==")
        print()
        print("1.- Agregar información de un producto")
        print("2.- Mostrar Reporte de presupuesto de produccion")
        print("\n0.- Regresar al Menú principal\n")
        Opcion  = input("Ingrese la opción a realizar: ")

        if Opcion == "":
            print("ERROR: Por favor selecciona una opción")
            input("presiona la tecla ENTER para continuar...")
            Packages.Clean()

        elif Opcion == "1":
            Packages.Clean()

        elif Opcion == "2":
            Packages.Clean()
        
        elif Opcion == "0":
            Packages.Clean()
            print("Regresando al Menú principal...")
            break
        
        else:
            print("ERROR: Opción no valida...")
            input("Presiona ENTER para continuar")
            Packages.Clean()
##Determinación del Costo Unitario de Productos Terminados
def DUCFP():
    while True:
        Packages.Clean()
        print("== PRESUPUESTO DE PRODUCCION ==")
        print()
        print("1.- Agregar información de un producto")
        print("2.- Mostrar Reporte de presupuesto de produccion")
        print("\n0.- Regresar al Menú principal\n")
        Opcion  = input("Ingrese la opción a realizar: ")

        if Opcion == "":
            print("ERROR: Por favor selecciona una opción")
            input("presiona la tecla ENTER para continuar...")
            Packages.Clean()

        elif Opcion == "1":
            Packages.Clean()

        elif Opcion == "2":
            Packages.Clean()
        
        elif Opcion == "0":
            Packages.Clean()
            print("Regresando al Menú principal...")
            break
        
        else:
            print("ERROR: Opción no valida...")
            input("Presiona ENTER para continuar")
            Packages.Clean()
##Valuación de Inventarios Finales
def Final_Inventory_Valuation():
    while True:
        Packages.Clean()
        print("== PRESUPUESTO DE PRODUCCION ==")
        print()
        print("1.- Agregar información de un producto")
        print("2.- Mostrar Reporte de presupuesto de produccion")
        print("\n0.- Regresar al Menú principal\n")
        Opcion  = input("Ingrese la opción a realizar: ")

        if Opcion == "":
            print("ERROR: Por favor selecciona una opción")
            input("presiona la tecla ENTER para continuar...")
            Packages.Clean()

        elif Opcion == "1":
            Packages.Clean()

        elif Opcion == "2":
            Packages.Clean()
        
        elif Opcion == "0":
            Packages.Clean()
            print("Regresando al Menú principal...")
            break
        
        else:
            print("ERROR: Opción no valida...")
            input("Presiona ENTER para continuar")
            Packages.Clean()
