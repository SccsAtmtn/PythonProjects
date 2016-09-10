#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <fstream>
#include "sort_info.h"
using namespace  std;
static int cmp_times = 0;
bool cmp(info a,info b)
{
	cmp_times++;
	cout<<"成功进行第"<<cmp_times<<"次比较"<<endl;
	return a.time>b.time;
}
int main()
{
	string filename,filename1,filename2,s;
	int max_len,count,pre_count,graph_num,t,begin,flag,interval;

	filename1 = "discuss_information6_new.txt";
	filename2 = "discuss_time6.txt";
	
	vector<info> user;
	
	user = ini_data(filename1,filename2);
	cout<<"成功进行数据初始化"<<endl;
	sort(user.begin(),user.end(),cmp);
	cout<<"成功进行数据排序"<<endl;
	max_len = user.size();

	count = 0;
	pre_count = 0;
	flag = 0;
	interval = 60;//每h画一张图
	graph_num = 0;
	vector<vector<int>> G(max_len,vector<int>(max_len,0));
	while(count<max_len)
	{
		t = user[count].time;
		if(flag == 0)//刚画完图或者开始
		{
			begin = t;
			flag = 1;
		}
		else if(begin-t<interval)
		{
			flag = 1;
		}
		else
		{
			int2str(graph_num,s);
			filename = s+filename1;
			G = get_graph(user,max_len,filename,pre_count,count,G);
			cout<<"成功做出了第"<<graph_num<<"张图"<<endl;
			flag = 0;
			pre_count = count;
			graph_num++;
		}
		count++;
	}
	int2str(graph_num,s);
	filename = s+filename1;
	get_graph(user,max_len,filename,pre_count,count,G);
	cout<<"成功做出了第"<<graph_num<<"张图"<<endl;
	return 0;
}