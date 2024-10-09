class WordsFinder:
    def __init__(self, *name_files):
        self.file_names = name_files

    def get_all_words(self):
        all_word = {}
        for file in self.file_names:
            with open(file, encoding="utf-8") as file:
                s = ""
                for line in file:
                    s += str(line)
                list_with_words = (s.lower().split())
                for elem in range(len(list_with_words)):
                    if list_with_words[elem][-1] in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        list_with_words[elem] = list_with_words[elem][:-1]
                all_word[file.name] = list_with_words
        return all_word

    def find(self, word):
        word = word.lower()
        new_dic = {}
        for name, words in self.get_all_words().items():
            for ww in range(len(words)):
                if word == words[ww]:
                    new_dic[name] = ww + 1
                    return new_dic

    def count(self, word):
        word = word.lower()
        new_dict = {}
        for name, words in self.get_all_words().items():
            if word in words:
                cnt = words.count(word)
                new_dict[name] = cnt
        return new_dict

finder2 = WordsFinder('file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего