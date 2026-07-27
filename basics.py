name = "Prasad"
age = 36
salary = 150000.111

print(f"My name is {name}")
print(f"Age = {age}")
print(f"Salary = {salary:.2f}")

for i in range(5):
    print(i)

names = ["Tom", "john", "Sam"]
for name in names:
    print(name)

for id, name in enumerate(names):
    print(id, name)

i = 1
while i < 5:
    print(i)
    i += 1

numbers = [1, 2, 3, 4, 5]
print(5 in numbers)
print(5 not in numbers)

a = [1, 2]
b = a

print(a is b)
print(a is not b)

status = "even" if age % 2 == 0 else "odd"
print(status)
