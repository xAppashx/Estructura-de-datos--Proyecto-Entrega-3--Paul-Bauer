#Version 1 de la implementacion de un Hash Table para un inventario
#Creador: Paul Bauer
#Carnet: 20210060


class HashTable(object):
      
      
      def __init__(self, size):
            self.size = size
            self.slots = [None] * self.size
            self.data = [None] * self.size
      #def __init__
      
      
      
      
      def insert(self, key, data):
            
            hashvalue = self.hashfunction(key, len(self.slots))
            
            #Si el slot es vacio:
            if self.slots[hashvalue] == None:
                  self.slots[hashvalue] = key
                  self.data[hashvalue] = data
            #if self.slot == None
            
            else:
                  
                  # si el key ya existe, remplazar el valor
                  if self.slots[hashvalue] == key:
                        self.data[hashvalue] = data
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
                              self.data[nextslot] = data
                        #if self.slots == None
                        
                        #sino, remplazar el valor
                        else:
                              self.data[nextslot] = data
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
            data = None
            stop = False
            found = False
            position = startslot
            
            #while no esta encontrado o que no este vacio
            while self.slots[position] != None and not found and not stop:
                  
                  #if found
                  if self.slots[position] == key:
                        found = True
                        data = self.data[position]
                  #if self.slots == key
                  
                  else:
                        position=self.rehash(position,len(self.slots))
                        if position == startslot:
                              stop = True
                        #if position == startslot
                  #else
                  
                  return data
                  
            #while
 
      #def Retrieve
      
      
      
      # Special Methods for use with Python indexing
      def __getitem__(self, key):
            return self.get(key)
      #def __getitem__
 
      def __setitem__(self, key, data):
            self.put(key,data)
      #def __setitem__
      
      
#Class Hash Table







h = HashTable(5)









h.insert(1, "one")
h.insert(3, "Three")
h.insert(2, "Two")




returned = h.retrieve(1)
print(returned)


returned = h.retrieve(5)
print(returned)

returned = h.retrieve(3)
print(returned)















































#fin.