score=int(input("Enter your score : "))
print(score)
# score = 85
if score>=101:
    print("Please verify again your score")
    exit()
elif score>=90 :
    grade = "A"
elif score>=80:
    garde= "B"
elif score >=70:
    grade= "C"
elif score >=60:
    grade = "D"
else:
    grade = "F"
    print("Grade is  Here: ",grade)