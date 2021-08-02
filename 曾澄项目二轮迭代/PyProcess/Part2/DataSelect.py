import pandas as pd
import numpy as np

batch_size = 100
reader = pd.read_csv("全体词频矩阵结果.csv",dtype=np.int8,chunksize=batch_size,iterator=False)
temp = pd.DataFrame(reader.get_chunk(batch_size))
# print(temp.head())
print(temp.columns)

index = open("列标签.txt","w+")
for i in temp.columns:
    index.write(i+"\n")