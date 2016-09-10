#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

int main()
{
	ifstream discuss("discuss_information6_new.txt", ios::in);
	
	ofstream discuss1("discuss_isV6.txt");

	string s,isV[900];
	int i=0;
	while(1)
	{
		discuss>>s;
		if(s == "]")//这表明文件已经读完
			break;
		while(s != "Y" && s != "N")
		{
			discuss>>s;
		}
		isV[i] = s;
		if(s == "Y")
			discuss1<<1<<endl;
		else
			discuss1<<0<<endl;

		//discuss1<<s<<endl;
		cout<<s<<endl;
		while(s != "]")
		{
			discuss>>s;
		}
		i++;
	}

}