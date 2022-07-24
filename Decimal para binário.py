def main():
    a = int(input("Digite um número entre 0 e 255: "))

    while 0 > a > 255:
        a = int(input("Digite um número entre 0 e 255: "))

    b = 0
    c = a
    seq = [""]

    cont = 0

    while a != 0:
        b = a % 2
        a = a // 2

        seq.append(b)

    if 64 <= c < 128:
        seq.append(0)
    elif 32 <= c < 64:
        cont = 2
        while cont > 0:
            seq.append(0)
            cont -= 1
    elif 16 <= c < 32:
        cont = 3
        while cont > 0:
            seq.append(0)
            cont -= 1
    elif 8 <= c < 16:
        cont = 4
        while cont > 0:
            seq.append(0)
            cont -= 1
    elif 4 <= c < 8:
        cont = 5
        while cont > 0:
            seq.append(0)
            cont -= 1
    elif 2 <= c < 4:
        cont = 6
        while cont > 0:
            seq.append(0)
            cont -= 1
    elif 1 <= c < 2:
        cont = 7
        while cont > 0:
            seq.append(0)
            cont -= 1
    elif c == 0:
        cont = 8
        while cont > 0:
            seq.append(0)
            cont -= 1

    seq.reverse()

    print("".join(str(x) for x in seq))


main()
