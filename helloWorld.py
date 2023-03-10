# input for user

while True:
    try:
        name = input('please enter your name: ')
        age = int(input("enter your age: "))
        break
    except Exception:
        print("please enter correct input: ")

# printing out input for user
print(f"my name is {name} and im {age} years old")