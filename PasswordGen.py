import random
import string

minl = 16
maxl = 16


def passGen():
    return "".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(random.randint(minl,maxl)))


print("\n\n")

for i in range(9):
    print(str(i) + ":  " + passGen())

print("\n\n")