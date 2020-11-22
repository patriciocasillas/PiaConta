import Packages

def Reportes(P_mtz):
    for reportes in range(0,len(P_mtz)):
        print("\nReporte: ")
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
                Packages.dicPresupuestoOp["InvenFinTotal"] =  Packages.dicPresupuestoOp["InvenFin2"]

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
        print("== Presupuesto de Requerimiento de Materiales ==")
        print()
        print("1.- Agregar información de un producto")
        print("2.- Mostrar Reporte de Presupuesto de Requerimiento de Materiales")
        print("\n0.- Regresar al Menú principal\n")
        Opcion  = input("Ingrese la opción a realizar: ")

        if Opcion == "":
            print("ERROR: Por favor selecciona una opción")
            input("presiona la tecla ENTER para continuar...")
            Packages.Clean()

        elif Opcion == "1":
            Packages.Clean()
            print("Catalago de Articulos")
                ##Catalogo de Articulos
            for DiccionarioArticulos in Packages.mtzArticulos:
                print(DiccionarioArticulos["CodArticulo"] + ' - ' + DiccionarioArticulos["NomArticulo"])
                Packages.lstValArticulo.append(DiccionarioArticulos["CodArticulo"])
            CodArt = input("Ingrese el codigo del articulo a cargar: ")

            if(CodArt in Packages.lstValArticulo):
                Packages.Clean()
                ##Mostrar Catalogo de Materiales
                print("Catalago de Materiales")
                for DiccionarioMateriales in Packages.mtzMateriales:
                    print(DiccionarioMateriales ["CodMaterial"] + ' - ' + DiccionarioMateriales ["NomMaterial"])
                    Packages.lstValArticulo.append(DiccionarioMateriales["CodMaterial"])
                CodMat = input("Ingrese el codigo del Articulos a cargar: ")
                Packages.Clean()

                if(CodMat in Packages.lstValArticulo):
                    Packages.dicPresupuestoReqMat["CodMaterial"] = CodMat
                    ##Obtener  Unidades a producir
                    for reportes in range(0,len(Packages.mtzPresupuestoOp)):
                        for reporte in Packages.mtzPresupuestoOp[reportes]:
                            if reporte == "UnVender1S":
                                Packages.dicPresupuestoReqMat["UnidadesProd1S"] = Packages.mtzPresupuestoOp[reportes][reporte]
                            elif reporte == "UnVender2S":
                                Packages.dicPresupuestoReqMat["UnidadesProd2S"] = Packages.mtzPresupuestoOp[reportes][reporte]
                            elif reporte == "UnidadesProdTotal":
                                Packages.dicPresupuestoReqMat["UnidadesProdTotal"] = Packages.mtzPresupuestoOp[reportes][reporte]
                    ##Solicitud de informacion
                    Packages.dicPresupuestoReqMat["RequerimientoMat1S"] = float(input("Ingresa el Requerimiento de Material para el Semestre 1: "))
                    Packages.dicPresupuestoReqMat["RequerimientoMat2S"] = float(input("Ingresa el Requerimiento de Material para el Semestre 2: "))
                    Packages.dicPresupuestoReqMat["RequerimientoMatTotal"] = Packages.dicPresupuestoReqMat["RequerimientoMat2S"]

                    Packages.dicPresupuestoReqMat["TotalMatRequerido1S"] = Packages.dicPresupuestoReqMat["UnidadesProd1S"] * Packages.dicPresupuestoReqMat["RequerimientoMat1S"]
                    Packages.dicPresupuestoReqMat["TotalMatRequerido2S"] = Packages.dicPresupuestoReqMat["UnidadesProd2S"] * Packages.dicPresupuestoReqMat["RequerimientoMat2S"]
                    Packages.dicPresupuestoReqMat["TotalMatRequeridoTotal"] = Packages.dicPresupuestoReqMat["RequerimientoMatTotal"] * Packages.dicPresupuestoReqMat["UnidadesProdTotal"]
                    Packages.mtzPresupuestoReqMat.append(Packages.dicPresupuestoReqMat.copy())

                    for reportes in range(0,len(Packages.mtzPresupuestoReqMat)):
                        for reporte in Packages.mtzPresupuestoReqMat[reportes]:
                            if reporte == "TotalMatRequerido1S":
                                Packages.lstTotalRequerimientos1S.append(Packages.mtzPresupuestoReqMat[reportes][reporte])
                            elif reporte == "TotalMatRequerido2S":
                                Packages.lstTotalRequerimientos2S.append(Packages.mtzPresupuestoReqMat[reportes][reporte])
                            elif reporte == "TotalMatRequeridoTotal":
                                Packages.lstTotalReq.append(Packages.mtzPresupuestoReqMat[reportes][reporte])
                    
                    Packages.dicTotalRequerimientos["CodMaterial"] = CodMat
                    Packages.dicTotalRequerimientos["Total1S"] = sum(Packages.lstTotalRequerimientos1S)
                    Packages.dicTotalRequerimientos["Total2S"] = sum(Packages.lstTotalRequerimientos2S)
                    Packages.dicTotalRequerimientos["TotalReq"] = sum(Packages.lstTotalReq)
                    Packages.mtzTotalRequerimientos.append(Packages.dicTotalRequerimientos.copy())

                else:
                    print("ERROR: El codigo de articulo no es valido...")
                    input("Presiona ENTER para continuar")
        elif Opcion == "2":
            Packages.Clean()
            Reportes(Packages.mtzPresupuestoReqMat)
            print("Total de Requerimientos (gramos)")
            Reportes(Packages.mtzTotalRequerimientos)
            input("Presiona ENTER para continuar")
        
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
        print("== Presupuesto de Compra de Materiales ==")
        print()
        print("1.- Agregar información de un producto")
        print("2.- Mostrar Reporte de Presupuesto de Compra de Materiales")
        print("\n0.- Regresar al Menú principal\n")
        Opcion  = input("Ingrese la opción a realizar: ")

        if Opcion == "":
            print("ERROR: Por favor selecciona una opción")
            input("presiona la tecla ENTER para continuar...")
            Packages.Clean()

        elif Opcion == "1":
            Packages.Clean()
            ##Mostrar Catalogo de Materiales
            print("Catalago de Materiales")
            for DiccionarioMateriales in Packages.mtzMateriales:
                print(DiccionarioMateriales ["CodMaterial"] + ' - ' + DiccionarioMateriales ["NomMaterial"])
                Packages.lstValArticulo.append(DiccionarioMateriales["CodMaterial"])
            CodMat = input("Ingrese el codigo del Articulo a cargar: ")
            Packages.Clean()

            if(CodMat in Packages.lstValArticulo):
                for dic in range(0,len(Packages.mtzTotalRequerimientos)):
                    for registro in Packages.mtzTotalRequerimientos[dic]:
                        if registro == "Total1S":
                            Packages.dicPresupuestoCompraMat["ReqMat1"] = Packages.mtzTotalRequerimientos[dic][registro]
                        elif registro == "Total2S":
                            Packages.dicPresupuestoCompraMat["ReqMat2"] = Packages.mtzTotalRequerimientos[dic][registro]
                        elif registro == "TotalReq":
                            Packages.dicPresupuestoCompraMat["ReqMatTotal"] = Packages.mtzTotalRequerimientos[dic][registro]

                Packages.dicPresupuestoCompraMat["InventarioFin1"] = float(input("Ingresa el valor del Inventario Final del Semestre 1: "))
                Packages.dicPresupuestoCompraMat["InventarioFin2"] = float(input("Ingresa el valor del Inventario Final del Semestre 2: "))
                Packages.dicPresupuestoCompraMat["InventarioFinTotal"] = Packages.dicPresupuestoCompraMat["InventarioFin2"]

                Packages.dicPresupuestoCompraMat["TotalMateeriales1"] = Packages.dicPresupuestoCompraMat["InventarioFin1"] + Packages.dicPresupuestoCompraMat["ReqMat1"]
                Packages.dicPresupuestoCompraMat["TotalMateeriales2"] = Packages.dicPresupuestoCompraMat["InventarioFin2"] + Packages.dicPresupuestoCompraMat["ReqMat2"]
                Packages.dicPresupuestoCompraMat["TotalMateeriales"] = Packages.dicPresupuestoCompraMat["InventarioFinTotal"] + Packages.dicPresupuestoCompraMat["ReqMatTotal"]

                Packages.dicPresupuestoCompraMat["InventarioIni1"] = float(input("Ingresa el valor del Inventario Inicial del Semestre 1: "))
                Packages.dicPresupuestoCompraMat["InventarioIni2"] = float(input("Ingresa el valor del Inventario Inicial del Semestre 2: "))
                Packages.dicPresupuestoCompraMat["InventarioIniTotal"] = Packages.dicPresupuestoCompraMat["InventarioIni1"]

                Packages.dicPresupuestoCompraMat["MatCompra1"] = Packages.dicPresupuestoCompraMat["TotalMateeriales1"] - Packages.dicPresupuestoCompraMat["InventarioIni1"]
                Packages.dicPresupuestoCompraMat["MatCompra2"] = Packages.dicPresupuestoCompraMat["TotalMateeriales2"] - Packages.dicPresupuestoCompraMat["InventarioIni2"]
                Packages.dicPresupuestoCompraMat["MatCompraTotal"] = Packages.dicPresupuestoCompraMat["TotalMateeriales"] - Packages.dicPresupuestoCompraMat["InventarioIniTotal"]

                Packages.dicPresupuestoCompraMat["PrecioComp1"] = float(input("Ingresa el Precio de Compra del Semestre 1: "))
                Packages.dicPresupuestoCompraMat["PrecioComp2"] = float(input("Ingresa el Precio de Compra del Semestre 2: "))

                Packages.dicPresupuestoCompraMat["TotalMateial1"] = Packages.dicPresupuestoCompraMat["MatCompra1"] * Packages.dicPresupuestoCompraMat["PrecioComp1"]
                Packages.lstTotalComp1.append(Packages.dicPresupuestoCompraMat["TotalMateial1"])
                Packages.dicPresupuestoCompraMat["TotalMateial2"] = Packages.dicPresupuestoCompraMat["MatCompra2"] * Packages.dicPresupuestoCompraMat["PrecioComp2"]
                Packages.lstTotalComp2.append(Packages.dicPresupuestoCompraMat["TotalMateial2"])
                Packages.dicPresupuestoCompraMat["TotalMateial"] = Packages.dicPresupuestoCompraMat["TotalMateial1"] + Packages.dicPresupuestoCompraMat["TotalMateial2"]
                Packages.lstTotalComp.append(Packages.dicPresupuestoCompraMat["TotalMateial"])

                Packages.dicTotalCompras["Semestre1"] = sum(Packages.lstTotalComp1)
                Packages.dicTotalCompras["Semestre2"] = sum(Packages.lstTotalComp2)
                Packages.dicTotalCompras["Total"] = sum(Packages.lstTotalComp)

                Packages.mtzPresupuestoCompraMat.append(Packages.dicPresupuestoCompraMat)
                Packages.mtzTotalComp.append(Packages.dicTotalCompras)

        elif Opcion == "2":
            Packages.Clean()
            Reportes(Packages.mtzPresupuestoCompraMat)
            print("== Compras Totales ==")
            print(f"Semestre 1 = {sum(Packages.lstTotalComp1)}")
            print(f"Semestre 2 = {sum(Packages.lstTotalComp2)}")
            print(f"Total = {sum(Packages.lstTotalComp)}")
            input("Presiona ENTER para continuar")
        
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
        print("== Determinación del saldo de Proveedores y Flujo de Salidas ==")
        print()
        print("1.- Agregar información de un producto")
        print("2.- Mostrar Reporte de Determinación del saldo de Proveedores y Flujo de Salidas")
        print("\n0.- Regresar al Menú principal\n")
        Opcion  = input("Ingrese la opción a realizar: ")

        if Opcion == "":
            print("ERROR: Por favor selecciona una opción")
            input("presiona la tecla ENTER para continuar...")
            Packages.Clean()

        elif Opcion == "1":
            Packages.Clean()
            for dic in range(0,len(Packages.mtzTotalComp)):
                for registro in Packages.mtzTotalComp[dic]:
                    if registro == "Total":
                        Packages.dicSaldoProveedores["Compras"] = Packages.mtzTotalComp[dic][registro]

            Packages.dicSaldoProveedores["SaldoProveedores"] = float(input("Ingresa el Saldo de Proveedores: "))
            Packages.dicSaldoProveedores["TotalProveedores"] = Packages.dicSaldoProveedores["SaldoProveedores"] + Packages.dicSaldoProveedores["Compras"]
            Packages.dicSaldoProveedores["SalidaXProveedor1"] = Packages.dicSaldoProveedores["SaldoProveedores"]
            Packages.dicSaldoProveedores["SalidaXProveedor2"] = Packages.dicSaldoProveedores["Compras"] * 0.5
            Packages.dicSaldoProveedores["TotalSalidas"] = Packages.dicSaldoProveedores["SalidaXProveedor1"] + Packages.dicSaldoProveedores["SalidaXProveedor2"]
            Packages.dicSaldoProveedores["SaldoProveedoresTotal"] = Packages.dicSaldoProveedores["TotalProveedores"] - Packages.dicSaldoProveedores["TotalSalidas"]
            Packages.mtzSaldoProveedores.append(Packages.dicSaldoProveedores)

        elif Opcion == "2":
            Packages.Clean()
            Reportes(Packages.mtzSaldoProveedores)
            input("Presiona ENTER para continuar")
        
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
