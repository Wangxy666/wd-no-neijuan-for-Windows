#include<bits/stdc++.h>
#include<windows.h>
using namespace std;

int main()
{
    system("taskkill /f /im w-d.exe");
    system("del .\\log\\pid.log");
    cout<<"若无报错或未找到进程，服务器关闭成功"<<endl;
    system("pause");
    return 0;
}
