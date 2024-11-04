import pandas as pd


table = pd.read_excel('C:\\Users\\Master\\Desktop\\example.xlsx',
                      usecols='A:F')
'''
    открыли файлик экселя, указываем какие столбцы интереснуют
'''
print(table.head()) # выводим в терминал табличку
missing_data = table.isnull().sum() # количество значений None в таблице
print(missing_data)
static_svodka = table.describe()
print(static_svodka)
'''
статистическая сводка каждого столбца, чтобы узнать распределение данных в каждом столбце
'''