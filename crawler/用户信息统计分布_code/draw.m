clear,clc;
dbirth = load('discuss_birth6.txt');
fbirth = load('fan_birth3.txt');
discuss = '�������';
fan = '530�����';
figure(1);
draw_birth(dbirth); title(['����#',discuss,'#�����û�����ֲ�']);
figure(2);
draw_birth(fbirth); title(['����#',fan,'#��˿�û�����ֲ�']);
[ds,dnum] = textread('discuss_isV_gender6.txt','%s%d');
percent = round(dnum(1:3) / sum(dnum(1:3)) * 100, 2);
for i=1:3
    ds{i,1} = [ds{i,1},' ',num2str(percent(i)),'%'];
end
percent = round(dnum(4:5) / sum(dnum(4:5)) * 100, 2);
for i=4:5
    ds{i,1} = [ds{i,1},' ',num2str(percent(i - 3)),'%'];
end
figure(3);
gnum = dnum(1:3); gender = {ds{1,1},ds{2,1},ds{3,1}};
subplot(1,2,1); pie3(gnum, gender); title(['����#',discuss,'#�����û��Ա�ֲ�']);
gnum = dnum(4:5); gender ={ds{4,1},ds{5,1}};
subplot(1,2,2); pie3(gnum, gender); title(['����#',discuss,'#�����û���V�ֲ�']);
[fs,fnum] = textread('fan_isV_gender3.txt','%s%d');
percent = round(fnum(1:3) / sum(fnum(1:3)) * 100, 2);
for i=1:3
    fs{i,1} = [fs{i,1},' ',num2str(percent(i)),'%'];
end
percent = round(fnum(4:5) / sum(fnum(4:5)) * 100, 2);
for i=4:5
    fs{i,1} = [fs{i,1},' ',num2str(percent(i - 3)),'%'];
end
figure(4);
gnum = fnum(1:3); gender = {fs{1,1},fs{2,1},fs{3,1}};
subplot(1,2,1); pie3(gnum, gender); title(['����#',fan,'#��˿�û��Ա�ֲ�']);
gnum = fnum(4:5);gender ={fs{4,1},fs{5,1}};
subplot(1,2,2); pie3(gnum, gender); title(['����#',fan,'#��˿�û���V�ֲ�']);
[fs,fnum] = textread('fan_locate3.txt','%s%d');
[ds,dnum] = textread('discuss_locate6.txt','%s%d');
[fnum,index] = sortrows(fnum);
f = cell(1,length(fnum));
for i = 1:length(fnum)
    f{1,i} = fs{index(i),1};
        if fs{index(i),1} == '#'
        f{1,i} = '����';
    end
end
figure(5);
bar(fnum); colormap(hsv);
set(gca,'xtick',1:length(fnum),'XTickLabel',f,'fontsize',8)
title(['����#',fan,'#��˿�û�����ֲ�']);
[dnum,index] = sortrows(dnum);
f = cell(1,length(dnum));
for i = 1:length(dnum)
    f{1,i} = ds{index(i),1};
    if ds{index(i),1} == '#'
        f{1,i} = '����';
    end
end
figure(6);
ds = ds{index,1}; 
bar(dnum); colormap(hsv);
set(gca,'xtick',1:length(dnum),'XTickLabel',f,'fontsize',8)
title(['����#',discuss,'#�����û�����ֲ�']);
% percent = round(fnum / sum(fnum) * 100,2) ;
% for i=1:length(fnum)
%     fs{i,1} = [fs{i,1},char(13,10)',num2str(percent(i)),'%'];
% end
% percent = round(dnum / sum(dnum)* 100,2);
% for i=1:length(dnum)
%     ds{i,1} = [ds{i,1},char(13,10)',num2str(percent(i)),'%'];
% end
% figure(5);
% pie3(fnum); legend(fs); %title('����#��һ��ͯ��#��˿�û�����ֲ�');
% 
% figure(6);
% pie3(dnum); lengend(ds);%set(gca,'FontSize',5); %title('����#��һ��ͯ��#�����û�����ֲ�');

