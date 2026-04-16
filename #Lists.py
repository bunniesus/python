#Lists

people = ["Sarah", "Rhea", "Sarang", "Taylor", "Taylor"]
rolls = [23, 33, 41, 13, 67]

people.sort()
print(people)
people.extend(rolls)
print(people)

people.append("Neeraj")
print(people)

print(people.index("Sarah"))

people.pop() # Pops out last value
print(people)

people.remove("Sarang")
print(people)

# #people.sort()
# print(people)

print(people.count("Taylor"))
people.clear()
print(people)

rolls.sort()
print(rolls)