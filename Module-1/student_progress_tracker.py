
students = ["Akshay", "Priya", "Rahul", "Sneha", "Aman"]

for index, name in enumerate(students):
    print(f'{index + 1}. {name}')


for i in range(2,20,2):
    print(i)


score = 89

if score >= 90 and score <= 100:
    print("A grade")
elif score >= 70 and score < 90:
    print("B grade")
elif score >= 50 and score <= 69:
    print("C grade")
elif score < 50:
    print("Needs improvement")



attendence = ["Present", "Present", "Absent", "Present", "Absent"]

for i in attendence:
    if i == "Absent":
        continue
    print(i)




attempt = 1

while attempt <= 5:
    print(attempt)    
    attempt += 1
    if attempt == 5:
        print("Maximum Attempts Reached")
        break



print(f'Summary: {index + 1}. {name}')
for i in range(2,20,2):
    print(f"student role numbers {i}")

