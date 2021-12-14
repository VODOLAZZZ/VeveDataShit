cocks = []
q = input()
while q:
    cocks.append(q)
    q = input()
for i in range(len(cocks)):
    print(f'{i + 1}) аккаунт\nveve={cocks[i]}')