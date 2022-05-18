#Version 2 de la implementacion de un Hash Table para un inventario
#Creador: Paul Bauer
#Carnet: 20210060


class HashTable(object):
      
      
      def __init__(self, size):
            self.size = size
            self.slots = [None] * self.size
            self.nombre = [None] * self.size
            self.cantidad = [None] * self.size
            self.preciocompra = [None] * self.size
            self.precioventa = [None] * self.size
            
      #def __init__
      
      
      
      
      def insert(self, key, nombre, cantidad, preciocompra, precioventa):
            
            hashvalue = self.hashfunction(key, len(self.slots))
            
            #Si el slot es vacio:
            if self.slots[hashvalue] == None:
                  self.slots[hashvalue] = key
                  self.nombre[hashvalue] = nombre
                  self.cantidad[hashvalue] = cantidad
                  self.preciocompra[hashvalue] = preciocompra
                  self.precioventa[hashvalue] = precioventa
            #if self.slot == None
            
            else:
                  
                  # si el key ya existe, remplazar el valor
                  if self.slots[hashvalue] == key:
                        self.nombre[hashvalue] = nombre
                        self.cantidad[hashvalue] = cantidad
                        self.preciocompra[hashvalue] = preciocompra
                        self.precioventa[hashvalue] = precioventa
                  #if self.slots
                  
                  #sino, buscar un slot disponible
                  else:
                        
                        nextslot = self.rehash(hashvalue, len(self.slots))
                        
                        #ir a proximo slot
                        while self.slots[nextslot] != None and self.slots[nextslot] != key:
                              nextslot = self.rehash(nextslot,len(self.slots))
                        #while
                        
                        # if None, poner un nuevo key
                        if self.slots[nextslot] == None:
                              self.slots[nextslot] = key
                              self.nombre[nextslot] = nombre
                              self.cantidad[hashvalue] = cantidad
                              self.preciocompra[hashvalue] = preciocompra
                              self.precioventa[hashvalue] = precioventa
                        #if self.slots == None
                        
                        #sino, remplazar el valor
                        else:
                              self.nombre[nextslot] = nombre
                              self.cantidad[hashvalue] = cantidad
                              self.preciocompra[hashvalue] = preciocompra
                              self.precioventa[hashvalue] = precioventa
                        #else
                        
                  #else
              
            #else
            
      #def Insert
      
      
      
      def hashfunction(self, key, size):
            return key % size
      #def hashfuntion
      
      def rehash(self, oldhash, size):
            return (oldhash + 1) % size
      #def rehash
      
      
      
      def retrieve(self, key):
            
            startslot = self.hashfunction(key, len(self.slots))
            nombre = None
            cantidad = None
            preciocompra = None
            precioventa = None
            stop = False
            found = False
            position = startslot
            
            #while no esta encontrado o que no este vacio
            while self.slots[position] != None and not found and not stop:
                  
                  #if found
                  if self.slots[position] == key:
                        found = True
                        nombre = self.nombre[position]
                        cantidad = self.cantidad[position]
                        preciocompra = self.preciocompra[position]
                        precioventa = self.precioventa[position]
                        
                        return nombre, cantidad, preciocompra, precioventa
                  #if self.slots == key
                  
                  else:
                        position=self.rehash(position,len(self.slots))
                        if position == startslot:
                              stop = True
                        #if position == startslot
                  #else
                  """
                  # si fue encontrado
                  if nombre is not None:
                     return nombre, cantidad, preciocompra, precioventa
                     """
                  
            #while
            
            
            return None, None, None, None
 
      #def Retrieve
      
      
#Class Hash Table






global hashtable
hashtable = HashTable(10000)
#No se podra crear mas de 90 elementos.
#Sino crashea


from time import perf_counter



for Loop in range(10000):
      hashtable.insert(Loop, "1", "1", "1", "1")
#for Loop in range

for Loop in range(10000):
   
   TimeStart = perf_counter() 
   Nombre, Cantidad, PrecioCompra, PrecioVenta = hashtable.retrieve(Loop)
   TimeFinish = perf_counter()

   TotalTime = (TimeFinish - TimeStart) * (10**6)
   print(TotalTime)
#for Loop in range







































#fin.