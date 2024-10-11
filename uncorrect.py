class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, vin, number):
        self.model = model
        self.__vin = self.__is_valid_vin(vin)
        self.__number = self.__is_valid_numbers(number)


    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int) == False:
            raise IncorrectVinNumber("Некорректный тип vin номер")
        if ((1000000 <= vin_number) and (vin_number <= 9999999)) == False:
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        return True

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str) == False:
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        if len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")
        return True

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')