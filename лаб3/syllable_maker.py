import random
import string, sys


def file_size(filename):
    count = 0
    try:
        with open(filename, "r") as f:
            for line in f:
                for sim in line:
                    if sim.isalpha():
                        count += 1
    except Exception as e:
        print(e)
        exit(0)
    return count









if len(sys.argv) > 1:
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        n = file_size(sys.argv[1])
else:
    n = int(input("Введите длину текста: "))

# Случайные буквы (русские + английские)
#alphabet = string.ascii_lowercase + "абвгдежзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz"
alphabet = string.ascii_lowercase + "абвгдежзийклмнопрстуфхцчшщъыьэюя"

vowels = "аеиоуыэюя"
consonants = "бвгджзйклмнпрстфхцчшщ"


text = ""
full_text = ""
for i in range(n // 2):
    text = random.choice(consonants) + random.choice(vowels)
    full_text += text + " "
print(full_text)

if len(sys.argv) > 2:
    if sys.argv[2] == "-n":
        print(f"\n File size == {n} == simbols, == {n // 2} syllables")
