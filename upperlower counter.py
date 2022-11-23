s = "The Geek King"
l, u = 0, 0
for i in s:
    if (i >= 'a' and i <= 'z'):
        l = l + 1
    if (i >= 'A' and i <= 'Z'):
        u = u + 1
print('Lower case characters: ', l)
print('Upper case characters: ', u)