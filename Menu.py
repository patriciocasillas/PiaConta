import Packages

Clean = lambda: Packages.os.system('cls')
Clean()

def Menu():
    Clean()
    print("=SISTEMA DE CONTABILIDAD FACPYA=")
    print("=    PRESUPUESTO MAESTRO       =")
    print()
    print("1.-Presupuesto de Operación")
    print("2.-Presupuesto Financiero")
    print()
    print("0.-Salir")
    print()
    CtlMenu = int(input("Ingrese la opcion a realizar: "))

    if (str(CtlMenu) == ""):
        print("ERROR: POR FAVOR SELECCIONA UNA OPCIÓN")
        input("Presiona la tecla ENTER para continuar...")
        Clean()
        Menu()
    elif (CtlMenu == 1):
        Clean()
        Operation_Budget()
    elif (CtlMenu == 2):
        Clean()
        Financial_Budget()
    elif (CtlMenu == 0):
        print("Saliendo del sistema...")
        Packages.sys.exit()
    else:
        print("ERROR: VALOR INGRESADO NO VALIDO")
        input("Presiona la tecla ENTER para continuar...")
        Clean()
        Menu()
        

def Operation_Budget():
    CtlOB = 1
    while(CtlOB != 0):
        print()
        print("=Presupuesto de Operación=")
        print()
        print("1.-Presupuesto de venta")
        print("2.-Determinación del saldo de Clientes y Flujo de Entradas")
        print("3.-Presupuesto de Producción")
        print("4.-Presupuesto de Requerimiento de Materiales")
        print("5.-Presupuesto de Compra de Materiales")
        print("6.-Determinación del saldo de Proveedores y Flujo de Salidas")
        print("7.-Presupuesto de Mano de Obra Directa")
        print("8.-Presupuesto de Gastos Indirectos de Fabricación")
        print("9.-Presupuesto de Gastos de Operación")
        print("10.-Determinación del Costo Unitario de Productos Terminados")
        print("11.-Valuación de Inventarios Finales")
        print()
        print("0.-Regresar al menu principal")
        print()
        CtlOB = input("Ingrese la opcion a realizar: ")

        if (CtlOB == ""):
            print("Por favor selecciona una opción")
            input("presiona la tecla Enter para continuar")
            Clean()
        elif (int(CtlOB) == 0):
            Clean()
            Menu()
        elif(int(CtlOB) == 1):
            Clean()
            Packages.Sales_Budget()
            Clean()
        elif(int(CtlOB) == 2):
            Clean()
            Packages.DCBI()
            Clean()
        elif(int(CtlOB) == 3):
            Clean()
            Packages.Production_Budget()
            Clean()
        elif(int(CtlOB) == 4):
            Clean()
            Packages.Materials_Requirement_Budget()
            Clean()
        elif(int(CtlOB) == 5):
            Clean()
            Packages.Materials_Purchase_Budget()
            Clean()
        elif(int(CtlOB) == 6):
            Clean()
            Packages.DBSO()
            Clean()
        elif(int(CtlOB) == 7):
            Clean()
            Packages.Direct_Labor_Budget()
            Clean()
        elif(int(CtlOB) == 8):
            Clean()
            Packages.IMEB()
            Clean()
        elif(int(CtlOB) == 9):
            Clean()
            Packages.Operating_Expenses_Budget
            Clean()
        elif(int(CtlOB) == 10):
            Clean()
            Packages.DUCFP
            Clean()
        elif(int(CtlOB) == 11):
            Clean()
            Packages.Final_Inventory_Valuation()
            Clean()
        else:
            print("Valor seleccionado no valido")
            input("presiona la tecla Enter para continuar")
            Clean()

def Financial_Budget():
    CtlFB = 1
    while (CtlFB != 0):
        print()
        print("=Presupuesto Financiero=")
        print()
        print("1.-Estado de Costo de Producción y Ventas")
        print("2.-Estado de Resultados")
        print("3.-Estado de Flujo de Efectivo")
        print("4.-Balance General")
        print()
        print("0.-Regresar al menu principal")
        print()
        CtlFB = input("Ingrese la opcion a realizar: ")

        if (CtlFB == ""):
            print("Por favor selecciona una opción")
            input("presiona la tecla Enter para continuar")
            Clean()
        elif int(CtlFB) == 0:
            Clean()
            Menu()
        elif int(CtlFB) == 1:
            Clean()
            Packages.SCPS()
            Clean()
        elif int(CtlFB) == 2:
            Clean()
            Packages.Statement_Income()
            Clean()
        elif int(CtlFB) == 3:
            Clean()
            Packages.Cash_Flow_Statement()
            Clean()
        elif int(CtlFB) == 4:
            Clean()
            Packages.Balance_Sheet()
            Clean()
        else:
            print("Valor seleccionado no valido")
            input("presiona la tecla Enter para continuar")
            Clean()
