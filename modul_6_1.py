
class Plant:
    edible = False
    def __init__(self, name):
        self.name = name

    def Food(self):
        food = self.edible
        return food

class Flower(Plant):
    edible = False

class Fruit(Plant):
    edible = True

class Animal:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.alive = True

    def eat(self, food):
        if food.edible == True:
            self.fed = True
            print(f"{self.name} съел {food.name}")
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)