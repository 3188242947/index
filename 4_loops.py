print("=== for循环 ===")
fruits = ["苹果", "香蕉", "橙子"]

for fruit in fruits:
    print(f"我喜欢吃: {fruit}")

print("\n=== while循环 ===")
count = 0
while count < 5:
    print(f"计数: {count}")
    count += 1

print("\n=== range函数 ===")
for i in range(1, 6):
    print(f"数字: {i}")

print("\n=== 列表推导式 ===")
squares = [x**2 for x in range(1, 6)]
print(f"平方数: {squares}")

print("\n=== 遍历字典 ===")
person = {"name": "小红", "age": 22, "city": "北京"}

for key, value in person.items():
    print(f"{key}: {value}")