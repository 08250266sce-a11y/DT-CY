name = str(input("Enter your name: "))
marks1 = float(input("Enter the marks of first subject: "))
marks2 = float(input("Enter the marks of second subject: "))
marks3 = float(input("Enter the marks of third subject: "))
marks4 = float(input("Enter the marks of fourth subject: "))
Attendence = float(input("Enter the attendence: "))
Total = (marks1 + marks2 + marks3 + marks4)
print()
print("Student Name:",name)
print("Attendence:%.2f" %Attendence,"%")
Average = (Total) / 4
print("Averge:%.2f" %Average,"%")
if (100>Average>= 40 and 100>Attendence>=90 and 100>marks1>=40 and 100>marks2>=40 and 100>marks3>=40 and 100>marks4>=40):
    print("Statuts: Pass")
else:
    print("There is an error in entering marks! try again")
    print()
    quit()
if (100>Average>=90 and 100>Attendence>=90):
    print("Grade:A[Excellent]")
elif(100>Average>=80 and 100>Attendence>=90):
    print("Grade:B[v.Good]")
elif(100>Average>=70 and 100>Attendence>=90):
    print("Grade:C[Good]")
elif(100>Average>=60 and 100>Attendence>=90):
    print("GRade:D")
elif(Average>100):
    print("grade error! try again")
if (100>=Average>=90 and 100>=Attendence>=90):
    print("You are Eligible for reward")
else:
    print("you are not Eligible for Reward")