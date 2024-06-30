marks={
    "Harry":100,
    "Sheldon":99,
    "Leonard":95,
    "Penny":50
}
print(marks.get("Harry"))
print(marks.pop("Penny"))
print(marks)

print(marks.__contains__("Sheldon"))
print(marks.__contains__("Raj"))

print(marks.items())

print(marks.update({"Leonard":90, "Howard":91,"Raj":91}))
print(marks.values())

print(marks.get("Harry2")) #None
print(marks["Harry2"]) #error