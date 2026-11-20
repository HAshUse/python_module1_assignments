                            # Lists
subjects = ["PYTHON", "javascript", "SQL"]

print(subjects)

subjects.append("POWERBI")

print(subjects)
subjects.remove("javascript")
print(subjects)

subjects.sort()
print(subjects)

print(len(subjects))
print(subjects)

# Additional method

subjects.pop()
print(subjects)

subjects[1] = "java"
print(subjects)


                            # Tuples

college_location = ("City", "State", 4,6,True)

print(college_location[1])
print(college_location[0])
print(college_location[4])


                            # Dictionary

student = {
    "Name" : "Student1",
    "Age" : 22,
    "College": "GCC",
    "Course" : "WEB DEV"
}     


print(student["Name"])
print(student["Course"])
print(student["Age"])

student["score"]= 90
student["Course"] = "AIML"
student["Age"] = 25
student["Employment_status"] = "Employed"

print(student)


                            # Sets

skills = {"Python", "SQL", "Python", "Excel", "Power BI", "Excel"} 

print(skills)

skills.add("Git")

print(skills)

skills.remove("SQL")

print(skills)

print(len(skills))




print(f"subjects passed {subjects} with score {student['score']} in {student['College']} affialated with OU. These are the student details {student} and he has the following unique skills {skills}")