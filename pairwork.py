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
if (Average >= 50 and Attendence >=90):
    print("Statuts: Pass")
else:
    print("Status: Fail")
if (Average>=90 and Attendence>=90):
    print("Grade:A[Excellent]")
elif(Average>=80 and Attendence>=90):
    print("Grade:B[v.Good]")
elif(Average>=70 and Attendence>=90):
    print("Grade:C[Good]")
elif(Average>=60 and Attendence>=90):
    print("GRade:D")
if (Average>=90 and Attendence>=90):
    print("You are Eligible for reward")
else:
    print("No Reward")