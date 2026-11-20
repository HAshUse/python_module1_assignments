numbers = [i for i in range(1,11)]
print(numbers)

square = [i * i for i in numbers]
print(square)

even = [i for i in square if i%2 == 0]
print(even)

student_scores = {
    "student1":89,
    "student2":79,
    "student3":87,
    "student4":85,
    "student5":84,
}

for student in student_scores:
    print(student)

for marks in student_scores.values():
    print(marks)

for students,marks in student_scores.items():
    print(f"{students} scored {marks}")



Student_Names = ["akshay", "anirudh", "gayathri", "rohit"]
score = [90, 80, 78, 76]
ratings = [10,9,8,7]


# for name, score in zip(Student_Names, score):
#     print(name, score)


for name, score, ratings in zip(Student_Names, score, ratings):
    print(Student_Names, score, ratings)



square = lambda x : x * x
print(square(5))

cube = lambda x : x * x * x
print(cube(4))

add = lambda a, b : a + b
print(add(4,5))



numbers = [5, 10, 15, 20]

double = list(map(lambda x: 2 * x, numbers))

nums = list(map(lambda x :x + 10, numbers))

print(nums)
print(double)