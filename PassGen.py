from random import choice


characters = ''.join([chr(i) for i in range(ord('a'), ord('z') + 1)])
uppercase_characters = characters.upper()
numbers = '1234567890'
symbols = '!@#$%^&*'

for _ in range(5):
    f = True
    while f:
        password = ''.join([choice(characters + uppercase_characters + numbers + symbols) for _ in range(8)])
        c = 0
        for i in password:
            if i in uppercase_characters:
                c += 1
                break
        for i in password:
            if i in numbers:
                c += 1
                break
        for i in password:
            if i in symbols:
                c += 1
                break
        for i in password:
            if i in characters:
                c += 1
                break
        if c == 4:
            f = False
            print(password)
