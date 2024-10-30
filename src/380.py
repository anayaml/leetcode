class RandomizedSet:

    def __init__(self):
        self.index_dict = {}
        self.values_list = []

    def insert(self, val: int) -> bool:
        if val in self.index_dict:
            return False
        self.index_dict[val] = len(self.values_list)
        self.values_list.append(val)

    def remove(self, val: int) -> bool:
        if val not in self.index_dict:
            return False
        index_to_del = self.index_dict[val]
        l_element = self.values_list[-1]
        self.values_list[index_to_del] = l_element
        self.index_dict[l_element] = index_to_del
        self.values_list.pop()
        del self.index_dict[val]
        return True

    def getRandom(self) -> int:
        return choice(self.values_list)