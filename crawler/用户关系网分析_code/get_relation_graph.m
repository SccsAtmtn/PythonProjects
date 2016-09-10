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
    
    h = figure;hist(indeg),title('入度统计图'),xlabel('入度'),ylabel('个数');
    saveas(h,strcat('入度_',filename),'jpg');
    % figure,bar(1:G_size,indeg),title('入度统计图');
   
    outdeg = outdegree(G);
    h = figure;hist(outdeg),title('出度统计图'),xlabel('出度'),ylabel('个数');
    saveas(h,strcat('出度_',filename),'jpg');
    % figure,bar(1:G_size,outdeg),title('出度统计图');
    
    ug(ug == 2) = 1;
    G = graph(ug);
    bin = conncomp(G);
    %figure,plot(G,'Layout','layered'),title('有向图');
    [island_num,~] = max(bin);
    island_size = zeros(1,island_num);
    for k = 1:island_num
        island_size(k) = length(find(bin == k));
    end
    
    h = figure;hist(island_size),title('孤岛大小统计图'),xlabel('孤岛大小'),ylabel('个数');
    saveas(h,strcat('孤岛_',filename),'jpg');
end

