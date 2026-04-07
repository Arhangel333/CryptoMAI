import random
import string, sys


def file_size(filename):
    count = 0
    text = ""
    words_from_file = []
    try:
        with open(filename, "r") as f:
            for line in f:
                for char in line:
                    if char.isalpha() or char in " \n":
                        text += char
        words_from_file = text.split()
        count = len(words_from_file)
    except Exception as e:
        print(e)
        exit(0)
    return count





if "--h" in sys.argv or "-h" in sys.argv or "--help" in sys.argv:
        print(f"\nUsage: python3 <prog_name> <file_where_steal_words> <file_we_need_fit_in_by_size | size(int)> [-n|-h|--help|--h]")
        print("-n to see size of file in words")
        print("-h --h --help to see this massage\n\n")
        exit(0)



if len(sys.argv) > 1:
    if sys.argv[1].isdigit():
        print("Нужно ввести название файла(символьно-буквенное)")
        exit(0)
    else:
        file = sys.argv[1]
else:
    file = input("Введите файл: ")

words = []
clear_text = ""
with open(file, "r") as f:
    for line in f:
        for char in line:
            if char.isalpha() or char in " \n":
                clear_text += char
    words = clear_text.split()

#print(clear_text)
#print(set(words))



if len(sys.argv) > 2:
    if sys.argv[2].isdigit():
        n = int(sys.argv[2])
    else:
        file2 = sys.argv[2]
        n = file_size(file2)
    text = ""
    full_text = ""
    for i in range(n):
        text += random.choice(words) + " "

    print(text)

if len(sys.argv) > 3:
    if sys.argv[3] == "-n":
        print(f"\n File {file2} size == {n} == words")

