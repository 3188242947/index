def greet(name):
    """问候函数"""
    return f"你好, {name}!"

def add(a, b):
    """加法函数"""
    return a + b

def calculate_area(width, height=10):
    """计算面积,默认高度为10"""
    return width * height

def factorial(n):
    """计算阶乘"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def find_max(*numbers):
    """找出最大数"""
    return max(numbers) if numbers else None

print(greet("小明"))
print(f"3 + 5 = {add(3, 5)}")
print(f"矩形面积(宽5, 高8): {calculate_area(5, 8)}")
print(f"矩形面积(宽5, 默认高): {calculate_area(5)}")
print(f"5! = {factorial(5)}")
print(f"最大值: {find_max(3, 7, 2, 9, 4)}")