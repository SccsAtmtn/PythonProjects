clear all;clc;
N = 12;
for i=0:N
    filename = strcat(num2str(i),'discuss_information6_new.txt');
%     filename = 'fan3_graph.txt';
    G = load(filename);
    loc = strfind(filename,'.');
    filename = filename(1:loc-1);
    ug = G+G';
    G_size = size(G);
    G = digraph(G);
    indeg = indegree(G);
    
    h = figure;hist(indeg),title('���ͳ��ͼ'),xlabel('���'),ylabel('����');
    saveas(h,strcat('���_',filename),'jpg');
    % figure,bar(1:G_size,indeg),title('���ͳ��ͼ');
   
    outdeg = outdegree(G);
    h = figure;hist(outdeg),title('����ͳ��ͼ'),xlabel('����'),ylabel('����');
    saveas(h,strcat('����_',filename),'jpg');
    % figure,bar(1:G_size,outdeg),title('����ͳ��ͼ');
    
    ug(ug == 2) = 1;
    G = graph(ug);
    bin = conncomp(G);
    %figure,plot(G,'Layout','layered'),title('����ͼ');
    [island_num,~] = max(bin);
    island_size = zeros(1,island_num);
    for k = 1:island_num
        island_size(k) = length(find(bin == k));
    end
    
    h = figure;hist(island_size),title('�µ���Сͳ��ͼ'),xlabel('�µ���С'),ylabel('����');
    saveas(h,strcat('�µ�_',filename),'jpg');
end

