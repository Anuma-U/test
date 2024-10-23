import time
from threading import Thread

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        enemy = 100
        col_day = 0
        print(f"{self.name}, на нас напали!")
        while enemy > 0:
            time.sleep(1)
            col_day += 1
            enemy -= self.power
            print(f"{self.name} сражается {col_day} день(дня)..., осталось {enemy} воинов.")
        print(f"{self.name} одержал победу спустя {col_day} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")
