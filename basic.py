# ========================================
# Python 基础知识完全学习指南
# 循序渐进，从入门到精通
# ========================================

print("=" * 50)
print("1. 变量与基本数据类型")
print("=" * 50)

# 变量赋值 - Python中不需要声明类型
name = "Python"
version = 3.12
is_popular = True
nothing = None

print(f"变量名: {name}")
print(f"版本号: {version}")
print(f"是否流行: {is_popular}")
print(f"空值: {nothing}")

# 数据类型检查
print(f"name的类型: {type(name)}")
print(f"version的类型: {type(version)}")
print(f"is_popular的类型: {type(is_popular)}")

print("\n" + "=" * 50)
print("2. 基本数据类型详解")
print("=" * 50)

# 整数 (int)
age = 25
print(f"整数: {age}, 类型: {type(age)}")

# 浮点数 (float)
height = 1.75
print(f"浮点数: {height}, 类型: {type(height)}")

# 字符串 (str)
message = "Hello Python"
print(f"字符串: {message}, 类型: {type(message)}")

# 布尔值 (bool) - 只有 True 和 False
is_learning = True
print(f"布尔值: {is_learning}, 类型: {type(is_learning)}")

print("\n" + "=" * 50)
print("3. 字符串操作")
print("=" * 50)

# 字符串拼接
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"拼接: {full_name}")

# 字符串格式化 - f字符串 (推荐)
age = 30
print(f"我是{first_name}，今年{age}岁")

# 字符串方法
text = "python programming"
print(f"大写: {text.upper()}")
print(f"首字母大写: {text.capitalize()}")
print(f"替换: {text.replace('python', 'Python')}")

# 字符串切片
print(f"前5个字符: {text[:5]}")
print(f"倒数3个字符: {text[-3:]}")
print(f"第3到8个字符: {text[2:8]}")

print("\n" + "=" * 50)
print("4. 数学运算符")
print("=" * 50)

a = 10
b = 3

print(f"{a} + {b} = {a + b}")      # 加法
print(f"{a} - {b} = {a - b}")      # 减法
print(f"{a} * {b} = {a * b}")      # 乘法
print(f"{a} / {b} = {a / b}")      # 除法 (返回浮点数)
print(f"{a} // {b} = {a // b}")    # 整除 (返回整数)
print(f"{a} % {b} = {a % b}")      # 取模 (求余)
print(f"{a} ** {b} = {a ** b}")    # 幂运算

print("\n" + "=" * 50)
print("5. 比较运算符和逻辑运算符")
print("=" * 50)

x = 5
y = 8

# 比较运算符
print(f"{x} == {y}: {x == y}")     # 等于
print(f"{x} != {y}: {x != y}")     # 不等于
print(f"{x} > {y}: {x > y}")       # 大于
print(f"{x} < {y}: {x < y}")       # 小于
print(f"{x} >= {y}: {x >= y}")     # 大于等于
print(f"{x} <= {y}: {x <= y}")     # 小于等于

# 逻辑运算符
print(f"\nTrue and False: {True and False}")   # 逻辑与
print(f"True or False: {True or False}")      # 逻辑或
print(f"not True: {not True}")                # 逻辑非

print("\n" + "=" * 50)
print("6. 条件语句 (if/elif/else)")
print("=" * 50)

score = 85

if score >= 90:
    print("等级: A (优秀)")
elif score >= 80:
    print("等级: B (良好)")
elif score >= 70:
    print("等级: C (中等)")
else:
    print("等级: D (需要改进)")

# 三元表达式 (简洁的条件表达式)
age = 25
status = "成年人" if age >= 18 else "未成年人"
print(f"年龄{age}: {status}")

print("\n" + "=" * 50)
print("7. 列表 (List) - 可变、有序、重复")
print("=" * 50)

# 创建列表
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print(f"列表: {fruits}")
print(f"列表长度: {len(fruits)}")

# 访问列表元素 (索引从0开始)
print(f"第一个水果: {fruits[0]}")
print(f"最后一个水果: {fruits[-1]}")

# 切片
print(f"前两个: {fruits[:2]}")

# 修改列表
fruits[0] = "西瓜"
print(f"修改后: {fruits}")

# 添加元素
fruits.append("菠萝")
print(f"添加后: {fruits}")

# 删除元素
fruits.pop()  # 删除最后一个
print(f"删除后: {fruits}")

# 列表中查找
print(f"香蕉在列表中: {'香蕉' in fruits}")

print("\n" + "=" * 50)
print("8. 元组 (Tuple) - 不可变、有序")
print("=" * 50)

colors = ("红", "绿", "蓝")
print(f"元组: {colors}")
print(f"第一个颜色: {colors[0]}")
# colors[0] = "黄"  # 这会报错，因为元组不可变

# 元组拆包
r, g, b = colors
print(f"拆包结果: r={r}, g={g}, b={b}")

print("\n" + "=" * 50)
print("9. 字典 (Dictionary) - 键值对")
print("=" * 50)

# 创建字典
person = {
    "name": "张三",
    "age": 28,
    "city": "北京",
    "job": "工程师"
}

print(f"字典: {person}")

# 访问字典值
print(f"名字: {person['name']}")
print(f"年龄: {person.get('age')}")

# 修改字典
person["age"] = 29
person["hobby"] = "编程"  # 添加新键值对
print(f"修改后: {person}")

# 删除键值对
del person["hobby"]
print(f"删除后: {person}")

# 遍历字典
print("字典所有键值对:")
for key, value in person.items():
    print(f"  {key}: {value}")

print("\n" + "=" * 50)
print("10. 循环语句 (for和while)")
print("=" * 50)

# for 循环
print("for循环 - 打印1到5:")
for i in range(1, 6):  # range(1, 6) 生成1到5的数字
    print(f"  {i}", end=" ")
print()

# for 循环遍历列表
print("\nfor循环 - 遍历列表:")
numbers = [10, 20, 30, 40]
for num in numbers:
    print(f"  {num}", end=" ")
print()

# while 循环
print("\nwhile循环 - 计数器:")
count = 0
while count < 3:
    print(f"  计数: {count}")
    count += 1  # 等同于 count = count + 1

# break 和 continue
print("\nbreak和continue示例:")
for i in range(1, 6):
    if i == 2:
        continue  # 跳过当前迭代
    if i == 4:
        break     # 退出循环
    print(f"  {i}", end=" ")
print()

print("\n" + "=" * 50)
print("11. 函数 (Function)")
print("=" * 50)

# 简单函数
def greet(name):
    """向用户问好的函数"""
    return f"你好，{name}！"

result = greet("张三")
print(result)

# 多参数函数
def add(a, b):
    """两个数相加"""
    return a + b

print(f"5 + 3 = {add(5, 3)}")

# 默认参数
def introduce(name, age=25, city="北京"):
    """介绍一个人"""
    return f"{name}今年{age}岁，来自{city}"

print(introduce("李四"))
print(introduce("王五", 30, "上海"))

# 返回多个值
def get_min_max(numbers):
    """返回最小值和最大值"""
    return min(numbers), max(numbers)

nums = [3, 1, 4, 1, 5, 9]
minimum, maximum = get_min_max(nums)
print(f"最小值: {minimum}, 最大值: {maximum}")

# 可变长度参数
def sum_all(*numbers):
    """求任意个数的和"""
    total = 0
    for num in numbers:
        total += num
    return total

print(f"1+2+3+4+5 = {sum_all(1, 2, 3, 4, 5)}")

print("\n" + "=" * 50)
print("12. 列表推导式 (List Comprehension)")
print("=" * 50)

# 简单列表推导式
squares = [x**2 for x in range(1, 6)]
print(f"1到5的平方: {squares}")

# 带条件的列表推导式
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(f"1到10的偶数: {even_numbers}")

# 嵌套列表推导式
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"矩阵:\n{matrix}")

print("\n" + "=" * 50)
print("13. 异常处理 (Try/Except)")
print("=" * 50)

# 基础异常处理
try:
    result = 10 / 0  # 这会抛出错误
except ZeroDivisionError:
    print("错误: 不能除以0")

# 处理多种异常
try:
    numbers = [1, 2, 3]
    print(numbers[5])  # 索引超出范围
except IndexError:
    print("错误: 列表索引超出范围")
except ValueError:
    print("错误: 数值错误")

# else 和 finally
try:
    value = int("123")
    print(f"成功转换: {value}")
except ValueError:
    print("错误: 不能转换为整数")
else:
    print("没有发生异常")
finally:
    print("无论如何都会执行这行代码")

print("\n" + "=" * 50)
print("14. 类和对象 (Classes and Objects)")
print("=" * 50)

class Student:
    """学生类"""
    
    # 构造函数 (初始化对象)
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    
    # 实例方法
    def study(self):
        return f"{self.name}正在学习Python"
    
    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        else:
            return "C"
    
    # 特殊方法 - 字符串表示
    def __str__(self):
        return f"{self.name} ({self.age}岁, 分数:{self.score})"

# 创建对象
student1 = Student("张三", 20, 95)
student2 = Student("李四", 21, 85)

print(student1)
print(student2)
print(student1.study())
print(f"{student1.name}的等级: {student1.get_grade()}")

print("\n" + "=" * 50)
print("15. 模块导入和常用方法")
print("=" * 50)

import math
import random
from datetime import datetime

# math模块
print(f"圆周率 π: {math.pi}")
print(f"√16 = {math.sqrt(16)}")
print(f"sin(π/2) = {math.sin(math.pi/2)}")

# random模块
random_num = random.randint(1, 10)
print(f"随机数(1-10): {random_num}")

shuffled = [1, 2, 3, 4, 5]
random.shuffle(shuffled)
print(f"打乱后的列表: {shuffled}")

# datetime模块
now = datetime.now()
print(f"当前时间: {now.strftime('%Y年%m月%d日 %H:%M:%S')}")

print("\n" + "=" * 50)
print("16. 文件操作")
print("=" * 50)

# 写入文件
file_path = "test.txt"
with open(file_path, "w", encoding="utf-8") as f:
    f.write("这是第一行\n")
    f.write("这是第二行\n")
    f.write("这是第三行\n")
print(f"已写入文件: {file_path}")

# 读取文件
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()
print(f"文件内容:\n{content}")

# 按行读取
with open(file_path, "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, 1):
        print(f"第{line_num}行: {line.strip()}")

print("\n" + "=" * 50)
print("17. 综合示例 - 学生成绩管理系统")
print("=" * 50)

class GradeManager:
    """学生成绩管理系统"""
    
    def __init__(self):
        self.students = {}
    
    def add_student(self, name, score):
        """添加学生"""
        self.students[name] = score
    
    def get_average(self):
        """计算平均成绩"""
        if not self.students:
            return 0
        return sum(self.students.values()) / len(self.students)
    
    def get_top_student(self):
        """获取成绩最高的学生"""
        if not self.students:
            return None
        return max(self.students, key=self.students.get)
    
    def display_all(self):
        """显示所有学生成绩"""
        print("学生成绩列表:")
        for name, score in self.students.items():
            print(f"  {name}: {score}")

# 使用成绩管理系统
manager = GradeManager()
manager.add_student("张三", 95)
manager.add_student("李四", 88)
manager.add_student("王五", 92)
manager.add_student("赵六", 85)

manager.display_all()
print(f"平均成绩: {manager.get_average():.2f}")
print(f"成绩最高的学生: {manager.get_top_student()}")

print("\n" + "=" * 50)
print("学习完成！🎉")
print("=" * 50)
print("""
接下来学习建议:
1. 练习基本语法 - 编写更多小程序
2. 学习内置函数 - map, filter, zip 等
3. 学习包和模块 - 使用第三方库
4. 面向对象编程 - 继承、多态等
5. 函数式编程 - lambda, 装饰器等
6. 异步编程 - async/await
7. Web开发 - Django/Flask
8. 数据分析 - pandas/numpy
""")
