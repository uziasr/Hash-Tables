# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def __str__(self):
        return (f"{self.key}, {self.value}")

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity        


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.
        
        '''
        index = self._hash_mod(key) # index = number within storage range
        none_count = self.storage.count(None)
        # if (1 - none_count/self.capacity) > .7:
        #     self.resize()
        # if key =="key-3":
            # print('this is the index ',index)    
        if None not in self.storage:
            self.resize()

        #if not self.storage[index] 
        if self.storage[index] is not None:
            # print('Theres a collision')
            # make sure .next is None
            current_node = self.storage[index]
            while current_node:
                if current_node.key == key:
                    current_node.value = value
                    break
                elif current_node.next == None:
                    if key == "key-6":
                        print("\nthis is secure in\n",index)
                    current_node.next =  LinkedPair(key,value)
                    break
                current_node = current_node.next  
                # self.storage[index].next = LinkedPair(key,value)

        else:
            # self.storage[index] = value
            self.storage[index] = LinkedPair(key,value)




            # self.storage[self._hash_mod(key)] = value
        # if self.storage[index] is not None:
        #     print("Error: key is in use")
        # else:
        #     self.storage[index] = value

        # pass



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        
        # if self.storage[index] is not None:
        #     self.storage[index] = None
        # else:
        #     print('Warning: Key not found')


        
        # index = self._hash_mod(key)

        if self.storage[index] == None:
            print('Warning: Key not found')
        else:
            previous_node = None
            current_node = self.storage[index]
            while current_node:
                # print('this is the current_node', current_node.key, key)
                # print("this is the next node ",current_node.next)
                if current_node.key == key:
                    print(current_node.key, key, current_node.key == key)
                    if previous_node and current_node.next:
                        # print("im in the middle")
                        # print(f"hfdsahfakjsh previous_node {previous_node} current_node {current_node}")
                        previous_node.next = current_node.next
                        current_node = None
                        break
                    elif current_node.next:
                        # print("does this ever print? ",key,index, current_node.key)
                        self.storage[index] = current_node.next
                        current_node = None
                        break
                    elif previous_node:
                         current_node = None
                         break
                    else:
                        self.storage[index] = None
                        break
                previous_node = current_node
                current_node = current_node.next
        print('Warning: Key not found')

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # print("this is the index ", index)

        if self.storage[index] == None:
            return None
        else:
            current_node = self.storage[index]
            while current_node:
                # print('this is the current_node', current_node.key, key)
                # print("this is the next node ",current_node.next)
                if current_node.key == key:
                    return current_node.value
                current_node = current_node.next

        # return self.storage[index]


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        #spread out with new_capacity
        #if link list gets too long, resize
        #resize at 70%
        #go through every node and insert
        self.capacity *= 2
        newHT = HashTable(self.capacity)
        # print("this is the storage ",self.storage) 
        for lp in self.storage:
            if lp:
                newHT.insert(lp.key, lp.value)
                current_node = lp
                while current_node.next is not None:
                    newHT.insert(current_node.next.key, current_node.next.value)
                    current_node = current_node.next
        self.storage = newHT.storage



# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("I want to see this print", ht.storage )

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     print("")
ht = HashTable(8)

ht.insert("key-0", "val-0")
ht.insert("key-1", "val-1")
ht.insert("key-2", "val-2")
ht.insert("key-3", "val-3")
ht.insert("key-4", "val-4")
ht.insert("key-5", "val-5")
ht.insert("key-6", "val-6")
ht.insert("key-7", "val-7")
ht.insert("key-8", "val-8")
print(ht.remove("key-0"))
print(ht.remove("key-1"))
print(ht.remove("key-2"))
print(ht.remove("key-3"))
print('hello!!',ht.retrieve("key-3"))
print(ht.remove("key-4"))
print(ht.remove("key-5"))
print(ht.remove("key-6"))
print(ht.remove("key-7"))
print(ht.remove("key-8"))
print(ht.storage)
print((ht.storage).count(None))
# print(ht.retrieve("key-3"))