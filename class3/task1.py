while True: 
    age = int(input("Enter the age: "))
    if age < 13:
        print("Sorry your not allowed to pas")
    elif age >=13 and age < 18:
        print("Please call your legal guardian")
    elif age >= 18:
        print("Welcome")


