years = int(input("Enter number of years: "))
unit = input("""Select your choice:  
1 - days
2 - weeks
3- hours
""")

if unit == "1":
    print(years*365)
elif unit == "2":
    print(years*365)
elif unit == "3":
    print(years*365*24)
else:
    print("pink the right choice")