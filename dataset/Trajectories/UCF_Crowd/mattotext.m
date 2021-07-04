function [ output_args ] = untitled( fileName )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
load('ucf2.mat');
s = size(labled_tra);
noOfTrack = s(1); 
for i = 1:noOfTrack
    x = labled_tra(1,i).x;
    y = labled_tra(1,i).y;
    t = labled_tra(1,i).t;
    n = size(labled_tra(1,i).x);
    noPts = n(2);
    file_name = [sprintf('%d',i) '.txt'];
    fid = fopen(file_name,'w');
    for k = 1:noPts
        fprintf(fid, '%d\t%d\t%d\n',x(k),y(k),t(k));   
    end
    fclose(fid);
end
end

