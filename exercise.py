list = []
N = int(input('Enter the number of students :\n'))
for x in range(0,N):
    students = float(input('Enter height of student :\n'))
    list.append(students)
print(list)
sum = 0
for y in list:
    sum += y
avg = round(sum/N)
print('The average height of given',N,'students is',avg,"meters")


