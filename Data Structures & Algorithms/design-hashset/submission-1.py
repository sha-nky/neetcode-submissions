class MyHashSet:

    def __init__(self):
        self.boolean_arr = [False] * 1000001

    def add(self, key: int) -> None:
        self.boolean_arr[key] = True

    def remove(self, key: int) -> None:
        self.boolean_arr[key] = False

    def contains(self, key: int) -> bool:
        return self.boolean_arr[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)