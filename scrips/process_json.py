import json
import matplotlib.pyplot as plt
import numpy as np
import os
import csv
import pandas as pd

class process_json:
    def __init__(self) -> None:
        pass
        filenames = []
    
    def get_filenames(self,foldername):
        #need foldername
        files = os.listdir(foldername)
        # filenames = []
        # for file in files:
        #     print(file)
        #     filename, extension = os.path.splitext(file)
        #     # print(filename)
        #     # print(extension)  # 包括了点
        #     fullname = os.path.join(source, filename)
        #     # print(fullname)
        # pass
        # self.filenames = files
        filenames = []
        out = open("./data/filenames.txt", "w")
        for file in files:
            filename, extension = os.path.splitext(file)
            # print(filename)
            # print(extension)  # 包括了点
            fullname = os.path.join(foldername, file)
            # fullname = os.path.join(fullname,extension)
            filenames.append(fullname)
            out.write(fullname+"\n")
        self.filenames = filenames
        return filenames

    def read_all_file(self,filenames,gettime = True):
        #must to extract key informations later,or just read is helpless
        papers = []
        for filename in  filenames:
           self.read_single_file(filename,papers) 
        return papers
        pass
    def load_as_txt(self,papers,txtname = "./data/all_data.txt"):
        file = open(txtname,'w')
        file.write(papers)
        file.close()
        pass
    
    # def load_as_csv(self,papers,csvname = "./data/all_data.csv"):
    #     file = open(csvname,'w')
    #     file.write(papers)
    #     file.close()
    #     pass

    def read_single_file(self,filename,papers = [],gettime = True):
        # papers = []
        i = 0
        try:
            # file = open(filename, 'r', encoding='utf-8')
            with open(filename, 'r', encoding='utf-8') as file:
                # papers = []
                for line in file.readlines():
                    if(len(line)>1):
                        # print("lenth =",len(line))
                        # print(i)
                        dic = json.loads(line)
                        self.appendtime(filename,dic)
                        papers.append(dic)
                        i = i+1
            print("readdone")
        except FileNotFoundError:
            print("FileNotFoundError")
        return papers
    def appendtime(self,filename,dic):
        #1 白天，0黑夜
        if filename>"./201206_tweets/activities_201206100800_201206100810.json" and filename<"./201206_tweets/activities_201206242000_201206242010.json":
            dic.update({"time":1})
        else: 
            dic.update({"time":0})
        pass
    def draw_geo(self,papers):
        geo_coordinate = []
        for line in papers:
            if "geo" in line:
                if line["geo"]!=None:
                    geo_coordinate.append(line["geo"]["coordinates"])
        geo_coordinate = np.array(geo_coordinate)
        # plt.switch_backend('agg')#non-gui backend
        plt.scatter(geo_coordinate[:,0],geo_coordinate[:,1])
        pass

#used for test
if __name__ == "__main__":
    # filename = "./201206_tweets/activities_201206100000_201206100010.json"
    filename = "./201206_tweets/activities_201206241050_201206241100.json"
    foldername = "./201206_tweets/"
    json_processor = process_json()
    papers = json_processor.read_single_file(filename)
    # filenames = json_processor.get_filenames(foldername)
    # json_processor.draw_geo(papers)
    # all_papers = json_processor.read_all_file(filenames)
    if("1a"<"1b"):
        print("1")
    # papers = [[1,2],[3,4]]
    # txtname = "./data/all_data.txt"
    # file = open(txtname,'w')
    # file.write(str(papers))
    # file.close()