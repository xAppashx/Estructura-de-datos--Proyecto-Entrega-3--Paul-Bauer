#Version 1 de la implementacion de un Hash Table para almacenar facturas
#Creador: Paul Bauer
#Carnet: 20210060


class HashFacturas(object):
      
      
      def __init__(self, size):
            self.size = size
            self.slots = [None] * self.size
            self.nit = [None] * self.size
            self.nombre = [None] * self.size
            self.articulo = [None] * self.size
            self.cantidad = [None] * self.size
            self.pagototal = [None] * self.size
            
      #def __init__
      
      
      
      
      def insert(self, key, nit, nombre, articulo, cantidad, pagototal):
            
            hashvalue = self.hashfunction(key, len(self.slots))
            
            #Si el slot es vacio:
            if self.slots[hashvalue] == None:
                  self.slots[hashvalue] = key
                  self.nit[hashvalue] = nit
                  self.nombre[hashvalue] = nombre
                  self.articulo[hashvalue] = articulo
                  self.cantidad[hashvalue] = cantidad
                  self.pagototal[hashvalue] = pagototal
            #if self.slot == None
            
            else:
                  
                  # si el key ya existe, remplazar el valor
                  if self.slots[hashvalue] == key:
                        self.nit[hashvalue] = nit
                        self.nombre[hashvalue] = nombre
                        self.articulo[hashvalue] = articulo
                        self.cantidad[hashvalue] = cantidad
                        self.pagototal[hashvalue] = pagototal
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
                              self.nit[nextslot] = nit
                              self.nombre[nextslot] = nombre
                              self.articulo[nextslot] = articulo
                              self.cantidad[hashvalue] = cantidad
                              self.pagototal[nextslot] = pagototal
                        #if self.slots == None
                        
                        #sino, remplazar el valor
                        else:
                              self.nit[nextslot] = nit
                              self.nombre[nextslot] = nombre
                              self.articulo[nextslot] = articulo
                              self.cantidad[hashvalue] = cantidad
                              self.pagototal[nextslot] = pagototal
                        #else
                        
                  #else
              
            #else
            
      #def Insert
      
      
      
      def hashfunction(self, key, size):
            return (key % size)
      #def hashfuntion
      
      def rehash(self, oldhash, size):
            return ( (oldhash + 1) % size)
      #def rehash
      
      
      
      def retrieve(self, key):
            
            startslot = self.hashfunction(key, len(self.slots))
            nit = None
            nombre = None
            articulo = None
            cantidad = None
            stop = False
            found = False
            position = startslot
            
            #while no esta encontrado o que no este vacio
            while self.slots[position] != None and not found and not stop:
                  
                  #if found
                  if self.slots[position] == key:
                        found = True
                        nit = self.nit[position]
                        nombre = self.nombre[position]
                        articulo = self.articulo[position]
                        cantidad = self.cantidad[position]
                        pagototal = self.pagototal[position]
                        
                        return nit, nombre, articulo, cantidad, pagototal
                  #if self.slots == key
                  
                  else:
                        position=self.rehash(position,len(self.slots))
                        if position == startslot:
                              stop = True
                        #if position == startslot
                  #else
                  

            #while
            
            
            return None, None, None, None, None
 
      #def Retrieve
      

      
#Class Hash Table






global hashfacturas
hashfacturas = HashFacturas(180)
#No se podra crear mas de 90 elementos.
#Sino crashea

