import pandas as pd
import json
file = pd.read_csv('data/dataset.csv')
cols = file.columns
dic = {}
for row in range(file.shape[0]):
    doc = {}
    for col in range(file.shape[1]):
        if(cols[col]=="olvlRes" or cols[col]=="alvlRes"):

            lst =str(file.iloc[row,col]).split(", ")
            resDic = {}
            for res in lst:
                resDic[res[1]] = res[0]
            doc[str(cols[col])] = resDic
        else:
            doc[str(cols[col])] =str(file.iloc[row,col])

    dic[str(file.iloc[row,0])] = doc


json_object = json.dumps(dic, indent = 4)
  
# Writing to sample.json
with open("data/dataset.json", "w") as outfile:
    outfile.write(json_object)
# with open("data/dataset.json", "w") as outfile:
#     json.dump(dict(dic), outfile)