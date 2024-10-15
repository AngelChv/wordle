#for i, c in enumerate("string"):
#    print(i, c)

seed = "words"
guess = "froms"

for i, c in enumerate(guess):
    position = seed.find(c)
    if position == -1:
        print(c, "gris")
    elif position == i:
        print(c, "verde")
    else: print(c, "naranja")


for i, c in enumerate(guess):
    if c in seed:
        if seed.find(c) == i:
            print(c, "verde")
        else: print(c, "naranja")
    else: print(c, "gris")

numeros = [1, 3, 4]

for i, n in enumerate(numeros):
    print(i, n)


print(*"asd")
characters: list[str] = list("abcd")
print(characters)

p1 = "angela"
p2 = "angela"

for i1, c1 in enumerate(p1):
    find = [i2 for i2, c2 in enumerate(p2) if c2 == c1]
    if find:
        if i1 in find: print(c1, "verde")
        else: print(c1, "naranja")
    else: print(c1, "gris")
