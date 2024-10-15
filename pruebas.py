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