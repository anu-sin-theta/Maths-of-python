num = int(input("enter a number:\n"))
s=0
rev = num
while rev > 0:
    digit = rev % 10
    digit=digit**3
    rev //=10
    s=s + digit
print(s)


