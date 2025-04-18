from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda fir, sec: fir == sec, first, second)))

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, "w", encoding="utf-8") as f:
            for string in data_set:
                if isinstance(string, str) == False:
                    string = str(string)
                f.write(string + "\n")

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self, *args, **kwargs):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())