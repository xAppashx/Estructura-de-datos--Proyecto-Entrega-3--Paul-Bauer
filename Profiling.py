#Profiling

import Main
import cProfile
import HashFacturas
import HashTableV2

def Tabla():
      print("Que profiling quiere hacer?")
      print("1) Main: Runner (todo el codigo)")
      print("2) Main: ModificarCantidad")
      print("3) Main: NuevoElemento")
      print("4) Main: ProcesoCompra")
      print("5) HashTable: QuantityModif (Modificar la cantidad en un nodo)")
      print("6) HashTable: Insert (anadir un nuevo nodo)")
      print("7) HashTable: Retrieve (obtener los datos de un nodo)")
      print("8) TreeFactura: Retrieve")
      print("9) TreeFactura: Insert")  
      Opcion = int(input())
      return Opcion
#def Tabla



def Runner():
      #Ingreso unos valores los hash tables para que pueda funccionar el profiling.
      HashTableV2.hashtable.insert(15, "Fresas", "5", "7", "15")
      HashTableV2.hashtable.insert(3, "Bananos", "4", "7", "20")
      
      HashFacturas.hashfacturas.insert(1, "0315", "Predro", "Bananos", "6", "120")
      HashFacturas.hashfacturas.insert(2, "8943", "Jose", "Fresas", "6", "120")
      
      Opcion = Tabla()
      
      if (Opcion == 1):
                  print("")
                  #print("Profiling completo:")
                  cProfile.run('Main.Runner()')
                  #Opcion == Tabla
      #if Opcion == 1
      
      
      if (Opcion == 2):
                  print("")
                  print("Profiling del Modificar Cantidad en Main:")
                  #Codigo, nombre, cantidad, preciocompra, precioventa, Utilidad
                  cProfile.run('Main.ModificarCantidad(3, "Bananos", "4", "7", "20", 60)')
                  Opcion == Tabla
      #if Opcion == 2
      
      
      if (Opcion == 3):
                  print("")
                  print("Profiling del Nuevo Elemento en Main:")
                  cProfile.run('Main.NuevoElemento(6, 20)')
                  Opcion == Tabla
      #if Opcion == 3
      
      
      if (Opcion == 4):
                  print("")
                  print("Profiling del Proceso Compra en Main:")
                  cProfile.run('Main.ProcesoCompra(15, "Bananos", "4", "7", "20", "Jose", "8943", 2, 70)')
                  Opcion == Tabla
      #if Opcion == 4
      
      
      
      if (Opcion == 5):
                  print("")
                  print("Profiling del QuantityModif en HashTableV2:")
                  cProfile.run('HashTableV2.hashtable.QuantityModif(15, "92")')
                  Opcion == Tabla
      #if Opcion == 5
      
      
      if (Opcion == 6):
                  print("")
                  print("Profiling del Insert en HashTableV2:")
                  cProfile.run('HashTableV2.hashtable.insert(5, "Papayas", "7", "5", "8")')
                  Opcion == Tabla
      #if Opcion == 6
      
      
      if (Opcion == 7):
                  print("")
                  print("Profiling del Retrieve en HashTableV2:")
                  cProfile.run('HashTableV2.hashtable.retrieve(15)')
                  Opcion == Tabla
      #if Opcion == 7
      
      
      
      if (Opcion == 8):
                  print("")
                  print("Profiling del Retireve en HashFacturas:")
                  cProfile.run('HashFacturas.hashfacturas.retrieve(2)')
                  Opcion == Tabla
      #if Opcion == 8
      
      
      if (Opcion == 9):
                  print("")
                  print("Profiling del Insert en HashFacturas:")
                  cProfile.run('HashFacturas.hashfacturas.insert(3, "0157", "Juan", "Bananos", "1", "20")')
                  Opcion == Tabla
      #if Opcion == 9
      
#def Runner

Runner()




















































#fin