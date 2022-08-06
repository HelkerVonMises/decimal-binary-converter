def main():
    a = int(input("Type an integer number: "))

    c = a
    cont = 0
    seq = [""]

    while a != 0:
        b = a % 2
        a = a // 2

        seq.append(b)

    if 64 <= c < 128:
        cont = 1
    elif 32 <= c < 64:
        cont = 2
    elif 16 <= c < 32:
        cont = 3
    elif 8 <= c < 16:
        cont = 4
    elif 4 <= c < 8:
        cont = 5
    elif 2 <= c < 4:
        cont = 6
    elif 1 <= c < 2:
        cont = 7
    elif c == 0:
        cont = 8

    while cont > 0:
        seq.append(0)
        cont -= 1

    seq.reverse()

    print("".join(str(x) for x in seq))


main()
