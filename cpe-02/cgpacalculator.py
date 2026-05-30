totalPoints = 0
totalCredits = 0
gradePoint = 0
cgpa = 0
creditUnits = 0

print("--Student CGPA Calculator--")
courseNum = int(input("Total number of courses: "))

for i in range(courseNum):
    print("\nCourses", i + 1)
    
    creditUnits = int(input("Input course units: "))
    grade = input("Enter grade: ")
   
    if grade == "A":
        gradePoint = 5
        
    elif grade == "B":
        gradePoint = 4
        
    elif grade == "C":
        gradePoint = 3
        
    elif grade == "D":
        gradePoint = 2
        
    elif grade == "E":
        gradePoint = 1
        
    elif grade == "F":
        gradePoint = 0
        
totalCredits += creditUnits
totalPoints = creditUnits * gradePoint
if totalCredits != 0:
    cgpa = totalPoints / totalCredits
    
    print("\nYour CGPA is ", round(cgpa, 2))
       
else:
    print("No course entered.")
