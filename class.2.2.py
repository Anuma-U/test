class house():

    houses_history = []
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, nam, num_floor):
        self.name = nam
        self.number_of_floors = num_floor
        self.houses_history.append(self.name)

    def go_to(self, new_flor):
        self.new_floor = new_flor
        if 1 < self.new_floor < self.number_of_floors:
            for i in range(1, self.new_floor + 1):
                print(i)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, other):
        if isinstance(other, house):
            self.number_of_floors += other.number_of_floors
        elif isinstance(other, int):
            self.number_of_floors += other
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")



h1 = house('ЖК Горский', 18)
print(house.houses_history)
h2 = house('Домик в деревне', 2)
print(house.houses_history)
h3 = house('ЖК Матрёшки', 20)
print(house.houses_history)

del h2
del h3
print(house.houses_history)