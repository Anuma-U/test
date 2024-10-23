from threading import Thread
from time import sleep
from datetime import datetime

time_start = datetime.now()
def write_words(word_count, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for num in range(word_count):
            file.write(f"Какое-то слово № {num + 1}" + "\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


one = write_words(200, "example3.txt")
two = write_words(100, "example4.txt")
tree = write_words(30, "example2.txt")
four = write_words(10, "example1.txt")
time_end_1 = datetime.now()
res_1 = time_end_1 - time_start
print(res_1)

time_start_2 = datetime.now()
first_th = Thread(target=write_words, args=(10, "example5.txt"))
second_th = Thread(target=write_words, args=(30, "example6.txt"))
third_th = Thread(target=write_words, args=(100, "example7.txt"))
fourth_th = Thread(target=write_words, args=(200, "example8.txt"))

first_th.start()
second_th.start()
third_th.start()
fourth_th.start()

first_th.join()
second_th.join()
third_th.join()
fourth_th.join()

time_end_2 = datetime.now()
res_2 = time_end_2 - time_start_2

print(res_2)