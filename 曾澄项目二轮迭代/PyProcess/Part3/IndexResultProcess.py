import pandas as pd
import numpy as np

allPCAData = pd.read_csv("pca降维处理.csv")
sample = pd.read_csv("0708-5000样本.csv")

sample.drop("sentence", axis=1, inplace=True)
result = pd.DataFrame(columns=sample.columns)

row = sample["Unnamed: 0"].to_list()
ind = sample["index"].to_list()
dataIndex = zip(row, ind)

for i in dataIndex:
    temp = allPCAData[allPCAData["Unnamed: 0"] == i[0]]
    temp["index"] = ""
    temp["index"] = i[1]
    result = result.append(temp)
print(result.shape)
print(result.head())
result.drop("Unnamed: 0",axis=1,inplace=True)
result.to_csv("处理完的打标签数据.csv")
