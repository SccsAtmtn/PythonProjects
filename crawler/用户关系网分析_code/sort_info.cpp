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
	cout<<"�ɹ����е�"<<cmp_times<<"�αȽ�"<<endl;
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
	cout<<"�ɹ��������ݳ�ʼ��"<<endl;
	sort(user.begin(),user.end(),cmp);
	cout<<"�ɹ�������������"<<endl;
	max_len = user.size();

	count = 0;
	pre_count = 0;
	flag = 0;
	interval = 60;//ÿh��һ��ͼ
	graph_num = 0;
	vector<vector<int>> G(max_len,vector<int>(max_len,0));
	while(count<max_len)
	{
		t = user[count].time;
		if(flag == 0)//�ջ���ͼ���߿�ʼ
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
			cout<<"�ɹ������˵�"<<graph_num<<"��ͼ"<<endl;
			flag = 0;
			pre_count = count;
			graph_num++;
		}
		count++;
	}
	int2str(graph_num,s);
	filename = s+filename1;
	get_graph(user,max_len,filename,pre_count,count,G);
	cout<<"�ɹ������˵�"<<graph_num<<"��ͼ"<<endl;
	return 0;
}