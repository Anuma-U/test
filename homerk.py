def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if (root_word in str(word).lower()) or (str(word).lower() in root_word):
            same_words.append(word)
    return same_words

root_word = input("Введите ключевое слово: ").lower() # <- здесь автоматом слово принимает нижний регистр
other_words = list(input("Введите список слов через пробел: ").split())

print("Однокоренные слова: ", single_root_words(root_word, *other_words))