"""
Программа считает Топ-100 слов для переданного ей текстого файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk

Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""

if __name__ == '__main__':
    pass

import os
import argparse
import nltk
import collections
from nltk.corpus import stopwords

PATTERN = r"\[?(?:[(]'(\w+)', (\d+)[)][,]?\s?)\]?"
RESULT_MESSAGE = 'Топ 100 повторяющихся слов из файла по убыванию:\n'

stop_words = stopwords.words('russian')

parser = argparse.ArgumentParser(description='Подсчет слов в файле')

parser.add_argument('-f', action='store', dest='file_name', required=True)

arguments = parser.parse_args()

file_name = arguments.file_name

file_content = ''
words_from_file = []

if os.path.exists(file_name):
    with open(file_name, encoding='UTF-8') as file:
        file_content = file.read()

    pattern = r'[^\w]'
    cleaned_file_content = re.sub(pattern, ' ', file_content)
    tokenized_words = nltk.word_tokenize(cleaned_file_content)

    for word in tokenized_words:
        if word not in stop_words:
            words_from_file.append(word)

    word_frequency = Counter(words_from_file)

    ordered_word_frequency = str(word_frequency.most_common(100))

    print(RESULT_MESSAGE + re.sub(PATTERN, r'\1: \2,\n', ordered_word_frequency))
else:
    print(f'Файл с именем {file_name} не найден')