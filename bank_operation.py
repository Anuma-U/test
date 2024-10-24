from threading import Thread, Lock
from random import randint
from time import sleep

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for num_tran in range(100):
            rand = randint(50, 500)
            self.balance += rand
            if (self.balance >= 500) and (self.lock.locked()):
                self.lock.release()
            print(f"Пополнение: {rand}. Баланс: {self.balance}")
            sleep(0.01)

    def take(self):
        for num_tran in range(100):
            col_denyak = randint(50, 500)
            print(f"Запрос на {col_denyak}")
            if col_denyak <= self.balance:
                print(f"Снятие: {col_denyak}. Баланс: {self.balance}")
                self.balance -= col_denyak
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            sleep(0.01)

bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')