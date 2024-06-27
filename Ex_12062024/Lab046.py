#Programme to determine grade

# score >=90 and score <=100 -> A
# score >=80 and score <=89 -> B
# score >=70 and score <=79 -> C
# score >=60 and score <=69 -> D
# score >=0 and score <=59 -> F

score = float(input("Enter the total marks obtained"))
if 90 <= score <= 100:
    print("Obtained A grade")
elif 80 <= score <= 90:
    print("Obtained B grade")
elif 70 <= score <= 80:
    print("Obtained C grade")
elif 60 <= score <= 70:
    print("Obtained D grade")
elif 50 <= score <= 60:
    print("Obtained F grade")
else:
    print("Obtained Invalid grade")