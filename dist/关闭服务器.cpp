#include <bits/stdc++.h>
#include<windows.h>
using namespace std;

int main()
{
	system("del pid.log");
    system("taskkill /f /im w-d.exe");
    cout<<"若无报错或未找到进程，服务器关闭成功"<<endl;
    system("pause");
    return 0;
}
