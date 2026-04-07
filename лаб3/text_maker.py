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







if "--h" in sys.argv or "-h" in sys.argv or "--help" in sys.argv:
        print(f"\nUsage: python3 <prog_name> <file_we_need_fit_in_by_size | size_of_text(int)> [-n|-h|--help|--h]")
        print("-n to see size of file")
        print("-h --h --help to see this massage\n\n")
        exit(0)




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
text = ""
for i in range(n):
    text += random.choice(alphabet)

print(text)

if len(sys.argv) > 2:
    if sys.argv[2] == "-n":
        print(f"\n File size == {n} == simbols")
