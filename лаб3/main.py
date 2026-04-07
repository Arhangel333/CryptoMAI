""" Сравнить 1) два осмысленных текста на естественном языке, 2) осмысленный текст и текст
из случайных букв, 3) осмысленный текст и текст из случайных слов, 4) два текста из
случайных букв, 5) два текста из случайных слов.
Считать процент совпадения букв в сравниваемых текстах – получить дробное значение от 0
до 1 как результат деления количества совпадений на общее число букв. Расписать подробно
в отчёте алгоритм сравнения и приложить сравниваемые тексты в отчёте хотя бы для одного
запуска по всем пяти случаям. Осознать какие значения получаются в этих пяти случаях.
Привести соображения о том почему так происходит.
Длина сравниваемых текстов должна совпадать. Привести соображения о том какой длины
текста должно быть достаточно для корректного сравнения.
"""
import sys


def sim_count(text):
    arr = {}
    for sim in text:
        if sim.isalpha():
            if sim not in arr:
                arr[sim] = 0
            arr[sim] += 1
    return arr


def read_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def probability(one_arr, two_arr, n):
    arr = {}
    matches = 0
    for sim in one_arr:
        if sim in two_arr:
            arr[sim] = min(one_arr[sim], two_arr[sim])
            matches += arr[sim]
    matches /= n
    return matches

def print_texts(argv, one_text, two_text):
    print("\nFrom file: ", sys.argv[1])
    print("Text 1:", one_text)
    print("\nFrom file: ", sys.argv[2])
    print("Text 2:", two_text)



verbose = 0
if "--verbose" in sys.argv or "-v" in sys.argv:
        verbose = 1


one_text = read_text_from_file(sys.argv[1])
two_text = read_text_from_file(sys.argv[2])

if verbose:
    print_texts(sys.argv, one_text, two_text)


# Обрезаем тексты до одинаковой длины (по количеству символов)
min_len = min(len(one_text), len(two_text))
if len(one_text) != len(two_text):
    if verbose:
        print("Тексты разной длины! Обрезаю до", min_len, "символов")
    one_text = one_text[:min_len]
    two_text = two_text[:min_len]
    if verbose:
        print_texts(sys.argv, one_text, two_text)

one_arr = sim_count(one_text)
two_arr = sim_count(two_text)

# Считаем общее количество букв (а не всех символов подряд)
n = sum(one_arr.values())

res = probability(one_arr, two_arr, n)

if verbose:
    print("\nРезультирующая вероятность:")
print(res)

