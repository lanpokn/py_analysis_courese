import json
import matplotlib.pyplot as plt
import numpy as np
import os


class process_json:
    def __init__(self) -> None:
        pass
        filenames = []
    
    def get_filenames(self,dir):
        files = os.listdir(dir)
        # filenames = []
        # for file in files:
        #     print(file)
        #     filename, extension = os.path.splitext(file)
        #     # print(filename)
        #     # print(extension)  # 包括了点
        #     fullname = os.path.join(source, filename)
        #     # print(fullname)
        # pass
        self.filenames = files
        out = open("./data/filenames.txt", "w")
        for file in files:
            filename, extension = os.path.splitext(file)
            # print(filename)
            # print(extension)  # 包括了点
            fullname = os.path.join(dir, filename)
            out.write(fullname+"\n")
        return files

    def read_all_file(self,filenames,gettime = True):
        
        pass

    def read_single_file(self,filename,papers = []):
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
                        papers.append(dic)
                        i = i+1
        except FileNotFoundError:
            print("ERROR")
        return papers
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

if __name__ == "__main__":
    filename = "./201206_tweets/activities_201206100000_201206100010.json"
    foldername = "./201206_tweets"
    json_processor = process_json()
    papers = json_processor.read_single_file(filename)
    filenames = json_processor.get_filenames(foldername)
    json_processor.draw_geo(papers)
    if("1a"<"1b"):
        print("1")