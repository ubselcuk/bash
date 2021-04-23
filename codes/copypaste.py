z = 0
x = 0
print('\n')
with open('copypaste.txt') as f:
    while True:
        c = f.read(1)
        if not c:
            print('\n\nchar = ', end = '')
            print(z)
            break

        if x < 1999:

            print(c, end='')
            if x == 1998:
                print('\n\n')
                x = 0

        z = z + 1
        x = x + 1
