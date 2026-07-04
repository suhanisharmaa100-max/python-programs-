#Take a student's marks as input and print their grade using an elif chain:90+ -> "A+", 75-89 -> "A",60-74 ->"B", below 60 -> "Fail".
marks = float(input("Enter the student's marks: "))

if marks >= 90:
    print("A+")
elif marks >= 75:
    print("A")
elif marks >= 60:
    print("B")
else:
    print("Fail")