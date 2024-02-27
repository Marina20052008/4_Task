a = int(input("Перше  число: "))
b = int(input("Друге  число: "))
c = int(input("Третє число: "))

max = (a + b + abs(a - b)) // 2
max = (max+ c + abs(max - c)) // 2

min = (a + b - abs(a - b)) // 2
min= (min + c - abs(min - c)) // 2

remainder= a + b + c - max - min

print(max)
print(min)
print(remainder)
