def welcome():
    print("Welcome to the Student Function Manager")


def student_details(name, course):
    print(f"Name: {name} \ncourse: {course}")

student_details("Bhaskar", "Python programming")
student_details("Student1", "java")
student_details("Student2", "java script")


def greet_student(city="Hyd"): 
    print("I stay in", city)

greet_student()
greet_student("Mumbai")
greet_student("Delhi")



def introduce(name, age, city):
    print(name, age, city)

introduce(city="Hyderabad", age=20, name="Ravi")


def calculate_total(marks1, marks2, marks3):
    total_marks = marks1 + marks2 + marks3 
    return total_marks

Total = calculate_total(90,78,87)
print(f"Total Marks Obtained: {Total}")
percentage = (Total/300) * 100
print(f"Percentage: {percentage}")



def find_average(*marks):
    sum = 0
    for i in marks:
        sum += i

    return sum/len(marks)

print(find_average(98,84,95,76,77))


def student_profile(**details):
    for key,value in details.items():
        print(f"{key} : {value}")

student_profile(name="Bhaskar", Age = 22, Course = "AI", College = "GCC")



college = "Government Degree College"

def test():
    college = "GCC"
    print(college)

print(college)

test()