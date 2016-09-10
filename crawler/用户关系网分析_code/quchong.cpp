#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

int search(string* uid,string s,int len)
{
	for(int i=0;i<len;i++)
	{
		if(uid[i].compare(s) == 0)
		{
			return 0;
		}
	}
	return 1;
}
int main()
{
	ifstream discuss("discuss_information6.txt", ios::in);
	
	ofstream discuss1("discuss_information6_new.txt");

	string s;
	string temp[3],uid[900];
	int count,flag,i;
	i = 0;
	while(!discuss.eof())
	{
		count = 0;
		discuss>>s;//date
		temp[count] = s;
		count++;
		if(s == "]")//这表明文件已经读完
			break;
		while(1)
		{
			discuss>>s;
			temp[count] = s;
			count++;
			if(s == "Y" || s == "N")
			{
				//discuss3 << s << endl;
				break;
			}
		}
		discuss>>s;//uid
		uid[i] = s;
		flag = search(uid,s,i);
		if(flag == 1)
		{
			for(int j=0;j<count;j++)
			{
				discuss1<<temp[j]<<'\t';
			}
			discuss1<<s<<'\t';
		}
		while(s != "]")
		{
			discuss>>s;
			if(flag == 1)
			{
				discuss1<<s<<"\t";
			}
		}
		i++;
		if(flag == 1)
		{
			discuss1<<endl;
		}
	}
	return 0;
}