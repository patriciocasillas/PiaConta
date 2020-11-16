import Packages

Clean = lambda: Packages.os.system('cls')
Clean()

def Menu():
    print("=SISTEMA DE CONTABILIDAD FACPYA=")
    print("=    PRESUPUESTO MAESTRO       =")
    print()
    print("1.-Presupuesto de Operación")
    print("2.-Presupuesto Financiero")
    print()
    CtlMenu = int(input("Ingrese la opcion a realizar: "))
    
    if CtlMenu == 0:
        print("saliendo del sistema...")
    elif CtlMenu == 1:
        Packages.Operation_Budget()
    elif CtlMenu == 2:
        Packages.Financial_Budget()
    else:
        print("Opción seleccionada no valida...")
        input("presiona la tecla Enter para continuar")
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
        CtlOB = int(input("Ingrese la opcion a realizar: "))

        if (CtlOB == 0):
            Clean()
            Menu()
        elif(CtlOB == 1):
            print("1")
            Clean()
        elif(CtlOB == 2):
            print("2")
            Clean()
        elif(CtlOB == 3):
            print("3")
            Clean()
        elif(CtlOB == 4):
            print("4")
            Clean()
        elif(CtlOB == 5):
            print("5")
            Clean()
        elif(CtlOB == 6):
            print("6")
            Clean()
        elif(CtlOB == 7):
            print("7")
            Clean()
        elif(CtlOB == 8):
            print("8")
            Clean()
        elif(CtlOB == 9):
            print("9")
            Clean()
        elif(CtlOB == 10):
            print("10")
            Clean()
        elif(CtlOB == 11):
            print("11")
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
        CtlFB = int(input("Ingrese la opcion a realizar: "))

        if CtlFB == 0:
            Clean()
            Menu()
        elif CtlFB == 1:
            print("1")
            Clean()
        elif CtlFB == 2:
            print("2")
            Clean()
        elif CtlFB == 3:
            print("3")
            Clean()
        elif CtlFB == 4:
            print("4")
            Clean()
        else:
            print("Valor seleccionado no valido")
            input("presiona la tecla Enter para continuar")
            Clean()