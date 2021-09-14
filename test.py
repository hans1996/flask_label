import pandas as pd    
    
df = pd.read_csv('test2.txt', delimiter = "\t")
print()
df.to_csv("temp.csv")