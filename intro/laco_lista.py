

lst = list(range(1, 20, 2))
print(lst)

for elemento in lst:
    print(elemento * 2)

print('######### While ruim')
i = 0
while i < len(lst):
    print(i, lst[i])
    i += 1

print('Melhor que o while')

for i in range(len(lst)):
    print(i, lst[i])

print('Melhor forma com enumerate')

for i, x in enumerate('ABCD', start=1):
    print(i, x)

print('acabou')
