#Profiling

import Main
import cProfile
import HashFacturas
import HashTableV2

def Tabla():
      print("Que Unit Testing quiere hacer?")
      print("1) Main: ModificarCantidad")
      print("2) Main: NuevoElemento")
      print("3) Main: ProcesoCompra")
      print("4) HashTable: QuantityModif (Modificar la cantidad en un nodo)")
      print("5) HashTable: Insert (anadir un nuevo nodo)")
      print("7) HashTable: Retrieve (obtener los datos de un nodo)")
      print("8) TreeFactura: Retrieve")
      print("9) TreeFactura: Insert")  
      Opcion = int(input())
      return Opcion
#def Tabla



def Runner():
      #Ingreso unos valores los hash tables para que pueda funccionar el Unit Testing.
      HashTableV2.hashtable.insert(15, "Fresas", "5", "7", "15")
      HashTableV2.hashtable.insert(3, "Bananos", "4", "7", "20")
      
      HashFacturas.hashfacturas.insert(1, "0315", "Predro", "Bananos", "6", "120")
      HashFacturas.hashfacturas.insert(2, "8943", "Jose", "Fresas", "6", "120")
      
      Opcion = Tabla()

      
      
      if (Opcion == 1):
                  print("")
                  print("Unit Testing del Modificar Cantidad en Main:")
                  #Codigo, nombre, cantidad, preciocompra, precioventa, Utilidad
                  Main.ModificarCantidad(3, "Bananos", "4", "7", "20", 60)
                  
                  print("Success!")
                  Opcion == Tabla
      #if Opcion == 1
      
      
      if (Opcion == 2):
                  print("")
                  print("Unit Testing del Nuevo Elemento en Main:")
                  Main.NuevoElemento(6, 20)
                  print("Success !")
                  Opcion == Tabla
      #if Opcion == 2
      
      
      if (Opcion == 3):
                  print("")
                  print("Unit Testing del Proceso Compra en Main:")
                  Main.ProcesoCompra(15, "Bananos", "4", "7", "20", "Jose", "8943", 2, 70)
                  print("Success !")
                  Opcion == Tabla
      #if Opcion == 3
      
      
      
      if (Opcion == 4):
                  print("")
                  print("Unit Testing del QuantityModif en HashTableV2:")
                  HashTableV2.hashtable.QuantityModif(15, "92")
                  print("Success")
                  Opcion == Tabla
      #if Opcion == 4
      
      
      if (Opcion == 5):
                  print("")
                  print("Unit Testing del Insert en HashTableV2:")
                  HashTableV2.hashtable.insert(5, "Papayas", "7", "5", "8")
                  print("Sucess!")
                  Opcion == Tabla
      #if Opcion == 5
      
      
      if (Opcion == 6):
                  print("")
                  print("Unit Testing del Retrieve en HashTableV2:")
                  HashTableV2.hashtable.retrieve(15)
                  print("Sucess!")
                  Opcion == Tabla
      #if Opcion == 6
      
      
      
      if (Opcion == 7):
                  print("")
                  print("Unit Testing del Retireve en HashFacturas:")
                  HashFacturas.hashfacturas.retrieve(2)
                  print("Sucess!")
                  Opcion == Tabla
      #if Opcion == 7
      
      
      if (Opcion == 8):
                  print("")
                  print("Unit Testing del Insert en HashFacturas:")
                  HashFacturas.hashfacturas.insert(3, "0157", "Juan", "Bananos", "1", "20")
                  print("Sucess!")
                  Opcion == Tabla
      #if Opcion == 8
      
#def Runner

Runner()




















































#fin