Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
City = input("Enter your City: ")
College_Name = input("Enter your college name: ")
Favorite_Programming_Language = input("Enter your favourite programming language: ")
Height = float(input("Enter your Height (In Meters): "))


print(f"My name is {Name} and I am {Age} years old and I am {Height} meters tall, I stay in {City}")
print(f"I am currently persuing my graduation in {College_Name} and my favourite progrmming language is {Favorite_Programming_Language}.")


print(type(Name))
print(type(Age))
print(type(City))
print(type(College_Name))
print(type(Favorite_Programming_Language))
print(type(Height))


print(f"Age after 5 years is {Age + 5}")