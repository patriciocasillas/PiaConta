import os
import sys

from Menu import Menu
from Menu import Financial_Budget
from Menu import Operation_Budget

from Presupuesto_Operacion import Sales_Budget
from Presupuesto_Operacion import DCBI
from Presupuesto_Operacion import Production_Budget
from Presupuesto_Operacion import Materials_Requirement_Budget
from Presupuesto_Operacion import Materials_Purchase_Budget
from Presupuesto_Operacion import DBSO
from Presupuesto_Operacion import Direct_Labor_Budget
from Presupuesto_Operacion import IMEB
from Presupuesto_Operacion import Operating_Expenses_Budget
from Presupuesto_Operacion import DUCFP
from Presupuesto_Operacion import Final_Inventory_Valuation

from Presupuesto_Financiero import SCPS
from Presupuesto_Financiero import Statement_Income
from Presupuesto_Financiero import Cash_Flow_Statement
from Presupuesto_Financiero import Balance_Sheet

##Variables
mtzArticulos = []
mtzPVenta = []
lstValArticulo = []
lstTotalVS = []
dicArticulos = dict(CodArticulo="", NomArticulos= "")
dicPVenta = dict(CodArticulo = "", UnAVender = 0, Pventa = 0, Semestre = 0, ImporteVenta = 0)

dicArticulos["CodArticulo"] = "1"
dicArticulos["NomArticulo"] = "CL"
mtzArticulos.append(dicArticulos.copy())

dicArticulos["CodArticulo"] = "2"
dicArticulos["NomArticulo"] = "CE"
mtzArticulos.append(dicArticulos.copy())

dicArticulos["CodArticulo"] = "3"
dicArticulos["NomArticulo"] = "CR"
mtzArticulos.append(dicArticulos.copy())

##Determinación del saldo de Clientes y Flujo de Entradas

Clean = lambda: os.system('cls')
