function draw_birth(birth)
birth = sortrows(birth,1); 
y = birth(:,1); x = birth(:,2); flag = zeros(1,length(y));

cnt = zeros(1,6);
for i = 1:5
    cnt(i) = sum(x(y >= 1950 + i * 10 & y < 1960 + i * 10));
    flag(y >= 1950 + i * 10 & y < 1960 + i * 10) = 1;
end
cnt(6) = sum(x(flag == 0));
cnt = round(cnt/sum(cnt) * 100, 2);
year = {'60后','70后','80后','90后','00后','不详'};
for i = 1 : 6
    year{1,i} = [year{1,i},':',num2str(cnt(i)),'%'];
end

pie3(cnt,year);

