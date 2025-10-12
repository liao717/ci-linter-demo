# 这是一个故意违反PEP8规范的Python文件示例
# 包含了多余空格、过长行、不规范命名等问题


def  calculate_average(  numbers  ):   # 函数定义有多余空格，函数名不符合蛇形命名法
    sum =0  # 缺少空格，变量名使用了关键字
    count =  0  # 多余空格
    
    # 这是一个很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长的注释，明显超过了PEP8建议的72个字符长度
    for  num  in  numbers:  # 循环语句有多余空格
        if num % 2 == 0 :  # 条件判断有多余空格
            sum += num   # 赋值语句有多余空格
            count +=1  # 缺少空格
        else:
            pass  # 无意义的空语句
    
    # 下面这行代码非常非常非常非常非常非常非常非常非常非常非常非常非常非常非常非常非常非常长，远超88个字符的建议长度
    average = sum / count if count != 0 else 0; print("计算的平均值是:", average)  # 一行多语句
    
    return average   # 多余空格


# 变量名使用驼峰式而非蛇形
userName = "Alice"
user_age =  30  # 多余空格


# 字典定义格式混乱
user_info = {
'name': userName, 
    'age': user_age,
'height': 175.5 ,  # 多余逗号和空格
'address': '这是一个很长很长很长很长很长很长很长很长很长很长很长的地址字符串，用来演示过长行问题'
}


# 导入语句顺序混乱
import sys
from math import *  # 不推荐的通配符导入
import os


def main():
    # 列表定义有多余空格
    nums = [ 1,2,3,4,5,6,7,8,9,10 ]
    
    # 函数调用有多余空格
    result = calculate_average( nums )
    
    # 打印语句格式不规范
    print( "用户名:", userName, "年龄:", user_age )  # 多余空格
    print("用户信息:", user_info)
    
    # 条件语句格式错误
    if user_age > 18 :  # 多余空格
        print(userName + "是成年人")  # 字符串拼接而非f-string
    else:
        print(userName + "是未成年人")


if __name__ == "__main__" :  # 多余空格
    main()  # 函数调用后无空行
