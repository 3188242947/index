students = []

def add_student(name, score):
    """添加学生"""
    students.append({"name": name, "score": score})
    return f"添加学生: {name}"

def find_student(name):
    """查找学生"""
    for student in students:
        if student["name"] == name:
            return student
    return None

def calculate_average():
    """计算平均分"""
    if not students:
        return 0
    total = sum(s["score"] for s in students)
    return total / len(students)

def get_top_student():
    """获取最高分学生"""
    if not students:
        return None
    return max(students, key=lambda s: s["score"])

add_student("张三", 85)
add_student("李四", 92)
add_student("王五", 78)
add_student("赵六", 95)

print("所有学生:")
for student in students:
    print(f"  {student['name']}: {student['score']}分")

print(f"\n平均分: {calculate_average():.2f}")
print(f"最高分学生: {get_top_student()['name']} ({get_top_student()['score']}分)")

result = find_student("李四")
print(f"查找李四: {result}")