# 这是一个符合PEP8规范的Python文件示例
# 修复了多余空格、过长行、不规范命名等问题

import os
import sys
from math import sqrt  # 只导入需要的函数


def calculate_average(numbers):
    """计算列表中偶数的平均值"""
    total = 0  # 变量名修改，避免使用关键字
    count = 0

    # 注释长度控制在72个字符以内，过长时换行
    # 这是一个说明循环逻辑的注释，用于演示适当的注释长度
    for num in numbers:
        if num % 2 == 0:
            total += num
            count += 1
        else:
            pass  # 保留此逻辑但明确其用途

    average = total / count if count != 0 else 0
    print("计算的平均值是:", average)  # 拆分为单行语句

    return average


# 变量名使用蛇形命名法
user_name = "Alice"
user_age = 30  # 去除多余空格


# 字典定义格式统一，键值对对齐
user_info = {
    'name': user_name,
    'age': user_age,
    'height': 175.5,  # 去除多余逗号和空格
    'address': (
        '这是一个很长很长很长很长很长很长很长很长很长很长很长的'
        '地址字符串，用来演示过长行的正确拆分方式'
    )
}


def main():
    # 列表定义格式规范
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 函数调用格式规范，这里使用返回值但不做额外操作，若有需要可进一步利用
    calculate_average(nums)

    # 使用f-string使打印语句更清晰
    print(f"用户名: {user_name} 年龄: {user_age}")
    print(f"用户信息: {user_info}")

    # 条件语句格式规范
    if user_age > 18:
        print(f"{user_name}是成年人")
    else:
        print(f"{user_name}是未成年人")


if __name__ == "__main__":
    main()