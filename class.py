class house():
    def __init__(self, nam, num_floor):
        self.name = nam
        self.number_of_floors = num_floor

    def go_to(self, new_flor):
        self.new_floor = new_flor
        if 1 < self.new_floor < self.number_of_floors:
            for i in range(1, self.new_floor + 1):
                print(i)
        else:
            print("Такого этажа не существует")

h1 = house('ЖК Горский', 18)
print(h1.name, h1.number_of_floors)
h1.go_to(5)

h2 = house('Домик в деревне', 2)
print(h2.name, h2.number_of_floors)
h2.go_to(10)
