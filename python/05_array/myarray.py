class myArrary(object):
    def __init__(self, capacity=10):
        self._data = []
        self._capacity = capacity

    def __len__(self):
        return len(self._data)
    
    def __getitem__(self, position):
        return self._data[position]

    def __setitem__(self, position, value):
        self._data[position] = value
    
    def __iter__(self):
        for item in self._data:
            yield item
    
    def __str__(self):
        print(self._data)

    def delete(self, index: int):
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    def insert(self, index, value):
        if len(self) >= self._capacity:
            return False
        else:
            self._data.insert(index, value)

    def __add__(self, other):
        self._data += other._data
        return self

if __name__== "__main__":
    a = myArrary()
    b = myArrary()
    for i in range(13):
        a.insert(i, i)
        b.insert(i, i)
    a = a + b
    print(a)