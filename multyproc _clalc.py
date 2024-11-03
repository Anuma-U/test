from asyncio import timeout
from multiprocessing import Process, Pool
from datetime import datetime


def read_info(name):
    all_data = []
    with open(f"{name}", "r") as file:
        stroka = file.readline()
        while stroka != "":
            all_data.append(stroka)
            stroka = file.readline()

filenames = [f'file {number}.txt' for number in range(1, 5)]

start1 = datetime.now()
list(map(read_info, filenames))
end1 = datetime.now()
print(end1 - start1, "линейное")

if __name__ == '__main__':
    start2 = datetime.now()
    # start 4 worker processes
    with Pool(processes=1) as pool:
        for file in filenames:
            res = pool.apply_async(read_info, (file,))
            res.get()
    end2 = datetime.now()

    print(end2 - start2, "мультипроцессорное")
