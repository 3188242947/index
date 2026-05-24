score = 85

print(f"成绩: {score}")
print("判断结果:")

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

age = 20
has_ticket = True

print("\n入场检查:")
if age >= 18 and has_ticket:
    print("允许入场")
else:
    print("禁止入场")

user_type = "guest"

match user_type:
    case "admin":
        print("管理员权限")
    case "user":
        print("普通用户权限")
    case "guest":
        print("访客权限")
    case _:
        print("未知用户类型")