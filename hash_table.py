class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [[] for item in range(self.max)]

    def __get_hash(self, key):
        hsh = 0
        for char in key:
            hsh += ord(char)
        return hsh % 100

    def __setitem__(self, key, val):
        hsh = self.__get_hash(key)
        print('hsh is ', hsh)
        found = False
        for idx, item in enumerate(self.arr[hsh]):
            if len(item) == 2 and item[0] == key:
                self.arr[hsh][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[hsh].append((key, val))

    def __getitem__(self, key):
        hsh = self.__get_hash(key)
        for item in self.arr[hsh]:
            if item[0] == key:
                return item[1]
        return None

    def __delitem__(self, key):
        hsh = self.__get_hash(key)
        self.arr[hsh] = None


ht = HashTable()
ht['I'] = 'first value'
ht['marh 17'] = 'modified first value'
ht['march 18'] = 'second value'

print(ht['marh 17'])
print(ht['march 17'])
print(ht['march 18'])
