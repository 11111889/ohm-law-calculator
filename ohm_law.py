# 欧姆定律计算器

U = float(input("请输入电压 U (单位: 伏特): "))
R = float(input("请输入电阻 R (单位: 欧姆): "))

if R == 0:
    print("电阻不能为0，否则电流无穷大！")
else:
    I = U / R
    print(f"电流 I = {I} 安培")
