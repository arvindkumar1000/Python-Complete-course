Year = int(input("Enter your year: "))
print(Year)

if (Year % 400 == 0) or (Year % 4 == 0 and Year % 100 != 0):
    print("leap year")
else:
    print("Not a leap year")