foods = ["burger", "pizza", "sushi", "taco"]
print(foods)

drinks = ["coke", "pepsi", "juice", "coffee"]
print(drinks)

print(f"can i have {foods[0]} and {drinks[1]}")

foods.append("salad")
print(foods)



foods = ("apple", "banana", "orange", "mango", "strawberry", "grape", "mandarin", "strawberry")
calories = (52, 96, 62, 605, 33, 68, 50, 33)

print(foods)
foods_list=list(foods)
print(foods_list)
print(foods_list[-2])
print(calories[-2])
print(set(foods_list))
dict_foods = {"apple" : 96, "banana" : 96, "orange" : 62, "mango" : 605, "strawberry" : 33, "grape" : 68, "mandarin" : 50, "strawberry" : 33}
print(dict_foods)
dict_foods["tomato"] = 60
print(dict_foods)
dict_foods["grape"] = 50
print(dict_foods)

print(dict_foods["apple"] + dict_foods["banana"])