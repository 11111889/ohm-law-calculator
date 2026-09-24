def input_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("输入有误，请输入一个数字。")

def calculate_current(u, r):
    if r == 0:
        raise ValueError("电阻不能为 0，否则电流无穷大！")
    return u / r

def calculate_voltage(i, r):
    if r == 0:
        raise ValueError("电阻不能为 0！")
    return i * r

def calculate_resistance(u, i):
    if i == 0:
        raise ValueError("电流不能为 0，否则电阻无穷大！")
    return u / i

def menu():
    print("\n=== 欧姆定律计算器 ===")
    print("1. 计算电流 I")
    print("2. 计算电压 U")
    print("3. 计算电阻 R")
    print("0. 退出")

while True:
    menu()
    choice = input("请选择功能（0-3）： ").strip()

    if choice == "0":
        print("感谢使用，再见！")
        break

    try:
        if choice == "1":
            u = input_float("请输入电压 U（单位：伏特）： ")
            r = input_float("请输入电阻 R（单位：欧姆）： ")
            if r <= 0:
                print("电阻必须大于 0。")
                continue
            i = calculate_current(u, r)
            print(f"电流 I = {i:.4f} 安培")

        elif choice == "2":
            i = input_float("请输入电流 I（单位：安培）： ")
            r = input_float("请输入电阻 R（单位：欧姆）： ")
            if r <= 0:
                print("电阻必须大于 0。")
                continue
            u = calculate_voltage(i, r)
            print(f"电压 U = {u:.4f} 伏特")

        elif choice == "3":
            u = input_float("请输入电压 U（单位：伏特）： ")
            i = input_float("请输入电流 I（单位：安培）： ")
            if i == 0:
                print("电流不能为 0。")
                continue
            r = calculate_resistance(u, i)
            print(f"电阻 R = {r:.4f} 欧姆")

        else:
            print("无效选择，请输入 0、1、2、3 之一。")

        again = input("\n是否继续计算？（y/n）： ").strip().lower()
        if again != "y":
            print("感谢使用，再见！")
            break

    except ValueError as e:
        print(f"错误：{e}")




        
