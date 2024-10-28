import threading
from threading import Thread
from time import sleep
from random import randint
from queue import Queue



class Table:
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *args):
        self.queue = Queue()
        self.tables = args

    def guest_arrival(self, *guests):
        for guestss in guests:
            for table in self.tables:
                if table.guest == None:
                    table.guest = guestss.name
                    potok1 = Thread(target=Guest.run, args=(table.guest, ))
                    print(f"{table.guest} за стол номер {table.number}")
                    potok1.start()
                    break
            else:
                self.queue.put(item=guestss.name)
                print(f"{guestss.name} в очереди")


    def discuss_guests(self):
        while not(self.queue.empty()):
            if threading.current_thread().is_alive():
                print(f"{threading.current_thread()} покушал(-а) и ушёл(ушла)")
                sleep(10)




# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
