class MyHashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size
        print(self.data)

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = ( hash + ord(key[i]) * i  ) % self.size
        return hash


    def set(self, key ,value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = [[ key, value ]]

        else:
            # self.data.append([ key, value ])
            self.data[address].append([ key, value ])
        print(self.data)

    def get(self, key):
        address = self._hash(key)
        if self.data[address]:
            for i in self.data[address]:
                if i[0] == key:
                    return i[1]
        else:
            return None



if __name__== "__main__":
    hash_table_obj = MyHashTable(2)
    hash_table_obj.set("key1", "Iron")
    hash_table_obj.set("key2", "Chocolate")
    hash_table_obj.set("key3", "Lava")
    # hash_table_obj.set("key4", "Copper")
    # hash_table_obj.set("key5", "Earth")
    # hash_table_obj.set("key5", "Earth")

    print(hash_table_obj.get("key1"))
    print(hash_table_obj.get("key2"))
    print(hash_table_obj.get("key3"))

