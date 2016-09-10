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
title('讨论数量随时间变化曲线（抓取时间为6月2日12:57）（*代表这个时间有大V加入讨论）');
xlabel('讨论时间距抓取时间数');
ylabel('抓取到的讨论微博的数量'),hold on;
V = Vmarker.*fenbu;
VV = Vmarker.*x;
here = find(VV~=0);
V_here = V(here);
plot(here,V_here,'*');
% bar(Vmarker.*m,0.2);