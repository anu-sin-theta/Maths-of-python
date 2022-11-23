str = "AnuBhaV"
x=""
upperalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
loweralphabets="abcdefghijklmnopqrstuvwxyz"
for i in str:
    if i in upperalphabets:
        x+=loweralphabets[upperalphabets.index(i)]#x= x+lowealphabets[0]
    else:
        x+=upperalphabets[loweralphabets.index(i)]
print(x)