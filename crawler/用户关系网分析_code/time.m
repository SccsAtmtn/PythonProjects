clear all;clc;
data = load('discuss_time6.txt');

isV = load('discuss_isV6.txt');
M = 60;
% isV = isV{1,1};
uid = data(:,1);
time = data(:,2);
len = length(time);
maxtime = max(time);
days = floor(maxtime/M)+1;
fenbu = zeros(1,days);
Vmarker = zeros(1,days);
for k=1:len
    loc = 1+floor(time(k)/M);
    fenbu(loc) = fenbu(loc)+1;
    if(isV(k) == 1)
       Vmarker(loc) = 1;
    end
end


x = 0:days-1;
plot(x,fenbu);
title('����������ʱ��仯���ߣ�ץȡʱ��Ϊ6��2��12:57����*�������ʱ���д�V�������ۣ�');
xlabel('����ʱ���ץȡʱ����');
ylabel('ץȡ��������΢��������'),hold on;
V = Vmarker.*fenbu;
VV = Vmarker.*x;
here = find(VV~=0);
V_here = V(here);
plot(here,V_here,'*');
% bar(Vmarker.*m,0.2);