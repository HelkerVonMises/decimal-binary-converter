a = int(input("Digite um número entre 0 e 255: "))

while 0 > a > 255:
    a = int(input("Digite um número entre 0 e 255: "))

b = 0
c = 0
seq = [""]
d = a
cont = 0

while a != 0:
    c = a % 2
    b = a // 2
    a = a // 2

    seq.append(c)

if 64 <= d < 128:
    seq.append(0)
elif 32 <= d < 64:
    cont = 2
    while cont > 0:
        seq.append(0)
        cont -= 1
elif 16 <= d < 32:
    cont = 3
    while cont > 0:
        seq.append(0)
        cont -= 1
elif 8 <= d < 16:
    cont = 4
    while cont > 0:
        seq.append(0)
        cont -= 1
elif 4 <= d < 8:
    cont = 5
    while cont > 0:
        seq.append(0)
        cont -= 1
elif 2 <= d < 4:
    cont = 6
    while cont > 0:
        seq.append(0)
        cont -= 1
elif 1 <= d < 2:
    cont = 7
    while cont > 0:
        seq.append(0)
        cont -= 1
elif d == 0:
    cont = 8
    while cont > 0:
        seq.append(0)
        cont -= 1


seq.reverse()

print("".join(str(x) for x in seq))
