#include <iostream>
#include <string>
#include <fstream>
using namespace std;

void main()
{
	ifstream fan("fans_information3.txt", ios::in);
	ifstream discuss("discuss_information6.txt", ios::in);
	ofstream fan1("fan_locate3.txt");
	ofstream fan2("fan_isV_gender3.txt");
	ofstream fan3("fan_birth3.txt");
	ofstream discuss1("discuss_locate6.txt");
	ofstream discuss2("discuss_isV_gender6.txt");
	ofstream discuss3("discuss_birth6.txt");
	ofstream time("discuss_time6.txt");
	string gender[5000];
	int isV[5000];
	string province[5000];
	string birtht[5000];
	string birthtd[5000];
	string uid[5000];
	string location[50];
	string time1[5000];
	int om = 6, od = 2, oh = 12, omm = 57;
	int otime = oh * 60 + omm;
	int h = 0;
	string time2[5000];
	string birthyear[100];
	birthyear[0] = "0000";
	int y_num[100];
	int num[50];
	int i = 0, m = 0;
	int p = 0, flag = 0, j = 0, k = 0;
	string f;
	for (i = 0; i < 100; i++)
		y_num[i] = 0;
	for (i = 0; i < 50; i++)
		num[i] = 0;
	i = 0;
	while (1)
	{
		if (fan.fail())
			break;
		fan >> f;
		if (f == "N")
			isV[i] = 0;
		else
			isV[i] = 1;
		fan >> uid[i]; //id
		fan >> f; //用户名字
		fan >> province[i];
		fan >> f;
		if (f != "男" && f != "女" && f != "#")
		{
			fan >> f;
		}
		gender[i] = f;
		fan >> f;
		if (f != "#" && f.length() >=8 && f[1] >'2')
		{
			for (p = 0; p < 4; p++)
				birtht[i] = birtht[i] + f[p];
		}
		else
			birtht[i] = "0000";
		fan >> f;
		while (f != "]")
			fan >> f;
		for (m = 0; m < i; m++)
			if (uid[m] == uid[i])
			{
				uid[i] = "";
				province[i] = "";
				birtht[i] = "";
				gender[i] = "";
				i--;
			}
		i++;
	}
	int t = i - 1, fan_isv = 0,fan_male = 0,fan_female = 0,fan_notsure = 0;
	j = 0; k = 0;
	for (i = 0; i < t; i++)
	{
		
		fan_isv = fan_isv + isV[i];
		if (gender[i] == "男")
			fan_male++;
		else if (gender[i] == "女")
			fan_female++;
		else
			fan_notsure++;
		for (p = 0; p < k; p++)
		{
			if (birtht[i] == birthyear[p])
			{
				y_num[p]++;
				flag = 1;
			}
		}
		if (flag == 0)
		{
			birthyear[k] = birtht[i];
			y_num[k]++;
			k++;
		}
		else
			flag = 0;
		for (p = 0; p < j; p++)
		{
			if (province[i] == location[p])
			{
				num[p]++;
				flag = 1;
			}
		}
		if (flag == 0)
		{
			location[j] = province[i];
			num[j]++;
			j++;
		}
		else
			flag = 0;
	}
	fan2 << "男 " << fan_male<<endl;
	fan2 << "女 " << fan_female<<endl;
	fan2 << "不确定 " << fan_notsure<<endl;
	fan2 << "大V " << fan_isv<<endl;
	fan2 << "非大V " << fan_male + fan_female + fan_notsure - fan_isv;
	for (i = 0; i < j; i++)
	{
		fan1 << location[i] << "  " << num[i] << endl;
	}
	for (i = 0; i < k; i++)
	{
		fan3 << birthyear[i] << "  " << y_num[i] << endl;
	}
	fan1.close();
	fan2.close();
	fan3.close();
	fan.close();
	i = 0; j = 0; k = 0; p = 0;
	for (i = 0; i < 100; i++)
		y_num[i] = 0;
	for (i = 0; i < 50; i++)
		num[i] = 0;
	i = 0;
	while (1)
	{
		if (discuss.fail())
			break;
		discuss >> time1[i];
		discuss >> f;
		if (f == "]")
			break;
		if (f != "Y"&&f != "N")
		{
			time2[i] = f;
			discuss >> f;
		}
		if (f == "N")
			isV[i] = 0;
		else
			isV[i] = 1;
	
		discuss >> uid[i];
	
		/*
	    discuss >> gender[i];
		discuss >> f;
		discuss >> province[i];
		discuss >> f;
		if (f.length() != 10)
			discuss >> f;
			*/
		discuss >> f; //用户名字
		discuss >> province[i];
		discuss >> f;
		if (f != "男" && f != "女" && f != "#")
		{
			discuss >> f;
		}
		gender[i] = f;
		discuss >> f;
		if (f != "#" && f.length() >= 8 && f[1] >'2')
		{
			for (p = 0; p < 4; p++)
				birthtd[i] = birthtd[i] + f[p];
		}
		else
			birthtd[i] = "0000";
		discuss >> f;
		while (f != "]")
			discuss >> f;
		if (gender[i] == "#")
			gender[i] == "#";
		for (m = 0; m < i; m++)
			if (uid[m] == uid[i])
			{
				uid[i] = "";
				province[i] = "";
				birthtd[i] = "";
				gender[i] = "";
				time1[i] = "";
				time2[i] = "";
				i--;
			}		
		i++;
	}
	t = i - 1;

	int discuss_isv = 0, discuss_male = 0, discuss_female = 0, discuss_notsure = 0;
	j = 0; k = 0;
	for (i = 0; i < t; i++)
	{
		if (time1[i] == "\\u4eca\\u5929")
		{
			h = atoi(time2[i].substr(0, time2[i].find(":")).c_str()) * 60 + atoi(time2[i].substr(time2[i].find(":") + 1, time2[i].length()).c_str());
			h = otime - h;
		}
		else if (time1[i] == "\\u6628\\u5929")
			h = (24 - atoi(time2[i].substr(0, time2[i].find(":")).c_str())) * 60 + otime + 60 - atoi(time2[i].substr(time2[i].find(":") + 1, time2[i].length()).c_str());
		else if (time1[i].find("\\u5206\\u949f\\u524d") != time1[i].npos)
		{
			h = atoi(time1[i].substr(0, time1[i].find("\\u5206\\u949f\\u524d")).c_str());
		}
		else
		{
			if (od < atoi(time1[i].substr(time1[i].find("-") + 1, time1[i].length()).c_str()))
			{
				h = (od + 31 - atoi(time1[i].substr(time1[i].find("-") + 1, time1[i].length()).c_str()) - 1) * 24 * 60 + (24 - atoi(time2[i].substr(0, time2[i].find(":")).c_str()) - 1) * 60 + otime + 60 - atoi(time2[i].substr(time2[i].find(":") + 1, time2[i].length()).c_str());
			}
			else
				h = (od - atoi(time1[i].substr(time1[i].find("-") + 1, time1[i].length()).c_str()) - 1) * 24 * 60 + (24 - atoi(time2[i].substr(0, time2[i].find(":")).c_str()) - 1) * 60 + otime + 60 - atoi(time2[i].substr(time2[i].find(":") + 1, time2[i].length()).c_str());
		}
		time << uid[i] << "  " << h << endl;
		discuss_isv = discuss_isv + isV[i];
		if (gender[i] == "男")
			discuss_male++;
		else if (gender[i] == "女")
			discuss_female++;
		else
			discuss_notsure++;
		for (p = 0; p < k; p++)
		{
			if (birthtd[i] == birthyear[p])
			{
				y_num[p]++;
				flag = 1;
			}
		}
		if (flag == 0)
		{
			birthyear[k] = birthtd[i];
			y_num[k]++;
			k++;
		}
		else
			flag = 0;
		for (p = 0; p < j; p++)
		{
			if (province[i] == location[p])
			{
				num[p]++;
				flag = 1;
			}
		}
		if (flag == 0)
		{
			location[j] = province[i];
			num[j]++;
			j++;
		}
		else
			flag = 0;
	}
	discuss2 << "男 " << discuss_male << endl;
	discuss2 << "女 " << discuss_female << endl;
	discuss2 << "不确定 " << discuss_notsure << endl;
	discuss2 << "大V " << discuss_isv<<endl;
	discuss2 << "非大V " << discuss_male + discuss_female + discuss_notsure - discuss_isv;
	for (i = 0; i < j; i++)
	{
		discuss1 << location[i] << "  " << num[i] << endl;
	}
	for (i = 0; i < k; i++)
	{
		discuss3 << birthyear[i] << "  " << y_num[i] << endl;
	}
	discuss1.close();
	discuss2.close();
	discuss3.close();
	discuss.close();
}