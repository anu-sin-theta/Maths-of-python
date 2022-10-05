year = int(input("Enter the desired year :\n"))
if year % 100 == 0 and year % 4 == 0 :
    print(f"The given year {year} is a leap year.")
elif year % 4 ==0 and year % 100 != 0:
    print(f"The given year {year} is a leap year.")
else :
    print(f"The given year {year} is  not a leap year.")


