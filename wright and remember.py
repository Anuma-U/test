def custom_write(file_name, strings):
    file = open(file_name, "w", encoding="utf-8")
    cnt_strok = 0
    dictionary = {}
    for stroka in strings:
        now = file.tell()
        cnt_strok += 1
        file.write(stroka + "\n")
        dictionary[(cnt_strok, now)] = stroka
    return dictionary

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('file.txt', info)
for elem in result.items():
  print(elem)