#include <iostream>
using namespace std;

int main() {
    double U, R, I;
    cout << "请输入电压 U (单位: 伏特): ";
    cin >> U;
    cout << "请输入电阻 R (单位: 欧姆): ";
    cin >> R;

    if (R == 0) {
        cout << "电阻不能为0，否则电流无穷大！" << endl;
    } else {
        I = U / R;
        cout << "电流 I = " << I << " 安培" << endl;
    }

    return 0;
}