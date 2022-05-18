""" 
      Proyecto Estructura de Datos
      Paul Bauer 
      20210060

      Entrega 3

"""

import HashTableV2
import HashFacturas



def Runner():
      
      
      TtlFacturas = 0
      
      Corriendo = Tabla()
      
      AllCodigos = [None] * 90
      TtlCodigos = 0
      
      Utilidad = 0
      
      while (Corriendo != 6):
            
         # Creando / anadiendo un producto
         if (Corriendo == 1):
               
               print("Ingrese el codigo del articulo:")
               Codigo = int(input())
               
               nombre, cantidad, preciocompra, precioventa = HashTableV2.hashtable.retrieve(Codigo)
               
               if nombre is not None:
                     Utilidad = ModificarCantidad(Codigo, nombre, cantidad, preciocompra, precioventa, Utilidad)
               #if nombre is not None
               
               else:
                     AllCodigos[TtlCodigos] = Codigo
                     TtlCodigos = TtlCodigos + 1
                     
                     Utilidad = NuevoElemento(Codigo, Utilidad)
               #else
               
               
               Corriendo = Tabla()
         #if Corriendo == 1
         
         
         
         
         if (Corriendo == 2):
               print("Cual es el nombre del cliente ?")
               ClienteNombre = input()
               
               print("Cual es su nit ?")
               ClienteNit = input()
               
               print("Cual es el codigo del articulo que desea comprar el cliente ?")
               Codigo = int(input())
               
               nombre, cantidad, preciocompra, precioventa = HashTableV2.hashtable.retrieve(Codigo)
               
               
               if (nombre is None):
                     print("No se encontro el producto. Proceso abortado.")
               #if nombre is None
               
               
               
               if (nombre is not None):
                     
                     TtlFacturas, Utilidad = ProcesoCompra(Codigo, nombre, cantidad, preciocompra, precioventa, ClienteNombre, ClienteNit, TtlFacturas, Utilidad)
               #if Nombre is not none
               
               Corriendo = Tabla()
         #if Corriendo == 2
         
         
         
         if (Corriendo == 3):
               print("La utilidad de la empresa es:", Utilidad)
               Corriendo = Tabla()
         #if Corriendo == 3
         
         
         
         if (Corriendo == 4):
         
               for Loop in range(TtlCodigos):
               
                     if AllCodigos[Loop] != None:
                           nombre, cantidad, preciocompra, precioventa = HashTableV2.hashtable.retrieve(AllCodigos[Loop])
                           print()
                           print("Codigo:", AllCodigos[Loop])
                           print("Nombre:", nombre)
                           print("Cantidad disponible:", cantidad)
                           print("Precio de compra:", preciocompra)
                           print("Precio de venta:", precioventa)
                     #if
               #For loop in range
               
               Corriendo = Tabla()
         #if Corriendo == 4
         
         
         
         
         if (Corriendo == 5):
         
               for Loop in range(TtlFacturas):
                     nit, nombre, articulo, cantidad, pagototal = HashFacturas.hashfacturas.retrieve(Loop)
                     print()
                     print("Nit:", nit)
                     print("Nombre:", nombre)
                     print("Articulo:", articulo)
                     print("Cantidad comprada:", cantidad)
                     print("Total pagado:", pagototal)
               #for Loop in range
               
               Corriendo = Tabla()
         #if Corriendo == 5
         
         
         #        Entrada invalilda
         if (Corriendo < 1 or Corriendo > 6):
            print("Entrada invalida.")
            Corriendo = Tabla()
         #If Corriendo < 1 or Corriendo > 6


      #While Corriendo != 6
      
      if (Corriendo == 6):
            print("Ok, adios!")
      #if Corriendo == 6
      
#def Runner





def Tabla():
   print(" ")
   print("Que es lo que quiere hacer?")
   print("1) Entrada de articulos.")
   print("2) Salida / Venta de articulos.")
   print("3) Calculo de la utilidad total de la empresa.")
   print("4) Mostrar todo el inventario.")
   print("5) Mostrar todas las ventas.")
   print("6) Salir.")
   
   Seleccionado = int(input())
   
   return(Seleccionado)
# def Tabla







# Funcciones utiles para la opcion 1 de la tabla.

def ModificarCantidad(Codigo, nombre, cantidad, preciocompra, precioventa, Utilidad):

      print("Usted se refiere al producto:", nombre)
      print("Ingrese la cantidad ingresante en el inventario:")
      CantidadIngresante = int(input())
      IntCantidad = int(cantidad)
      
      TotalCantidad = CantidadIngresante + IntCantidad
      StringCantidad = str(TotalCantidad)
      
      HashTableV2.hashtable.QuantityModif(Codigo, StringCantidad)
      print("Se anado la cantidad exitosamente !")
      
      intPrecio = int(preciocompra)
      Utilidad = Utilidad - (CantidadIngresante * intPrecio)
      
      return Utilidad
      
#def ModificarCantidad


def NuevoElemento(Codigo, Utilidad):
      
      print("Esta creando un nuevo articulo !")
      
      print("Cual es el nombre del producto?")
      Nombre = input()
                  
      print("Cual es su cantidad ?")
      Cantidad = input()
                  
      print("Cual es el precio de compra ?")
      PrecioCompra = input()
                  
      print("Cual es el precio de venta ?")
      PrecioVenta = input()
      
      HashTableV2.hashtable.insert(Codigo, Nombre, Cantidad, PrecioCompra, PrecioVenta)
      print("Se anadio el articulo correctamente!")
      
      intPrecio = int(PrecioCompra)
      intCantidad = int(Cantidad)
      
      Utilidad = Utilidad - (intCantidad * intPrecio)
      
      return Utilidad
      
#def NuevoElemento







#Funccion util para la opcion 2 de la tabla.

def ProcesoCompra(Codigo, nombre, cantidad, preciocompra, precioventa, clientenombre, clientenit, TtlFacturas, Utilidad):
      
      
      print("El cliente desea comprar", nombre)
      print("Hay un total de", cantidad, "disponible en el inventario")
      print("Cuanto desea comprar el cliente?")
      print("La unidad cuesta", precioventa)
      
      
      ClienteCompra = 0
      CantidadRestante = -1
      while (CantidadRestante < 0):
            ClienteCompra = int(input())
            IntCantidad = int(cantidad)
            CantidadRestante = IntCantidad - ClienteCompra
            
            if (CantidadRestante < 0):
                  print("No puede comprar esa cantidad el cliente")
                  print("No hay sufisamiente en el inventario")
                  print("Que desea hacer?")
                  print("1) Volver a ingresar una cantidad")
                  print("2) Abortar proceso")
                  Opcion = int(input())
                  
                  if Opcion == 1:
                        print("Vuelve a ingresar la cantidad que desea comprar el cliente:")
                  #if opcion == 1
                  
                  if Opcion == 2:
                        print("Proceso abortado.")
                        break
                  #if opcion == 2
                  
            #if Cantidad restante < 0
            
      #While CantidadRestante < 0
         
         
      if (CantidadRestante >= 0):
         
               
               
               StringClienteCompra = str(ClienteCompra)
               StringCantidad = str(CantidadRestante)
               HashTableV2.hashtable.QuantityModif(Codigo, StringCantidad)
               
               
               IntPrecioVenta = int(precioventa)
               ClienteDebePagar = IntPrecioVenta * ClienteCompra
               StringClienteDebePagar = str(ClienteDebePagar)
               
               HashFacturas.hashfacturas.insert(TtlFacturas, clientenit, clientenombre, nombre, StringClienteCompra, StringClienteDebePagar )
               print("Se genero la factura exitosamente!")
               
               TtlFacturas = TtlFacturas + 1
               
               Utilidad = Utilidad + ClienteDebePagar
               
         #if Cantidad Restante >= 0
      
      return TtlFacturas, Utilidad
#def Proceso Compra
































































#fin.
