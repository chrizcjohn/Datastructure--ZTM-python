class MyHashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size

    def _hash(self, key):
        hash_value = 0
        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % self.size
        return hash_value

    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = [[key, value]]

        else:
            # self.data.append([ key, value ])
            self.data[address].append([key, value])

    def get(self, key):
        address = self._hash(key)
        if self.data[address]:
            for i in self.data[address]:
                if i[0] == key:
                    return i[1]
        else:
            return None

    def keys(self):
        keyArray = [];
        for i in range(len(self.data)):
            if self.data[i]:
                for j in self.data[i]:
                    keyArray.append(j[0])
        return keyArray

    def values(self):
        valueArray = [];
        for i in range(len(self.data)):
            if self.data[i]:
                for j in self.data[i]:
                    valueArray.append(j[1])
        return valueArray

    def items(self):
        key_value_items = [];
        for i in range(len(self.data)):
            if self.data[i]:
                for j in self.data[i]:
                    pair = (j[0], j[1])
                    key_value_items.append(pair)
        return key_value_items

    def delete(self, key):
        address = self._hash(key)
        if self.data[address]:
            for i, pair in enumerate(self.data[address]):
                if pair[0] == key:
                    del self.data[address][i]


if __name__ == "__main__":
    hash_table_obj = MyHashTable(2)
    hash_table_obj.set("key1", "Iron")
    hash_table_obj.set("key2", "Chocolate")
    hash_table_obj.set("key3", "Lava")
    # hash_table_obj.set("key4", "Copper")
    # hash_table_obj.set("key5", "Earth")
    # hash_table_obj.set("key5", "Earth")

    # print(hash_table_obj.get("key1"))
    # print(hash_table_obj.get("key2"))
    # print(hash_table_obj.get("key3"))
    print(hash_table_obj.keys())
    print(hash_table_obj.values())
    print(hash_table_obj.items())
    hash_table_obj.delete("key1")
    print(hash_table_obj.keys())
