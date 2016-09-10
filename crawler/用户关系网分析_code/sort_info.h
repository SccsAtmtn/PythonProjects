#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <fstream>
#include <sstream>
#include <ctime>
#include <sys/timeb.h>
using namespace  std;
void str2int(int &int_temp,const string &string_temp);
class info
{
public:
	int time;
	//string month;
	//string day;
	//string isV;
	vector<int> guid;
	int uid;
};

vector<vector<int>> get_graph(vector<info> &user,int G_size,string filename,int start,int end,vector<vector<int>> G)

{
	int i,j;
	int vec_len;
	bool flag;
	struct timeb startTime , endTime;
	int guanzhu,id;
	for (i=start;i<end;i++)
	{
		ftime(&startTime);
		vec_len = user[i].guid.size();
		for (j=0;j<G_size;j++)
		{
			id = user[j].uid;
			flag = 0;
			for (int k=0;k<vec_len;k++)
			{
				guanzhu = user[i].guid[k];
				if(id == guanzhu)
				{
					G[i][j]=1;
					flag = 1;
					break;
				}
			}
		}
		ftime(&endTime);
		cout<<"第"<<i<<"个人的关注列表已统计，耗时"<<(endTime.time-startTime.time)*1000 + (endTime.millitm - startTime.millitm) << "毫秒"<<endl;
	}

	ofstream f(filename);

	for (i=0;i<G_size;i++)
	{
		for (j=0;j<G_size;j++)
		{
			f<<G[i][j]<<'\t';
			//cout<<G[i][j]<<'\t';
		}
		f<<endl;
		//cout<<endl;
	}
	return G;
}

vector<info> ini_data(string filename1,string filename2)
{
	struct timeb startTime , endTime;
	vector<info> user;
	ifstream f1(filename1, ios::in);
	ifstream f2(filename2, ios::in);
	string s;
	info temp;
	int count,temp_int;
	count = 0;
	while(1)//存入数据，初始化
	{
		ftime(&startTime);
		f1>>s;
		if(s == "]")//这表明文件已经读完
			break;
		f2>>s;f2>>s;
		str2int(temp_int,s);
		temp.time = temp_int;
		while(s!="N" && s!="Y")
		{
			f1>>s;
		}
		//temp.isV = s;
		f1>>s;
		str2int(temp_int,s);
		temp.uid = temp_int;
		while(s!="[")
		{
			f1>>s;
		}
		f1>>s;
		while(s!="]")
		{	
			str2int(temp_int,s);
			temp.guid.push_back(temp_int);
			f1>>s;
		}
		user.push_back(temp);
		ftime(&endTime);
		cout<<"第"<<count<<"个用户信息输入完毕,耗时"<<(endTime.time-startTime.time)*1000 + (endTime.millitm - startTime.millitm) << "毫秒"<<endl;
		count++;
		if(count == 28)
		{
			cout<<"hahaha"<<endl;
		}
	}
	return user;
}

void str2int(int &int_temp,const string &string_temp)  
{  
    stringstream stream(string_temp);  
    stream>>int_temp;  
}

void int2str(int &int_temp,string &string_temp)  
{  
    stringstream stream;  
    stream<<int_temp;
	string_temp = stream.str();
}