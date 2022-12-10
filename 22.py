'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''
#%%
import pandas as pd
import string

alpha=dict(zip(string.ascii_lowercase, range(1,27)))

df = pd.read_csv(r'Additional Resources\p022_names.txt', sep=",", header=None,quotechar='"',index_col=False)
df = pd.DataFrame.transpose(df)
df.columns=["Names"]
df.loc[len(df.index)] = ["NA"]
df=df.sort_values(by="Names")
df.insert(1,"nameValue",0)
df.insert(2,"weightedValue",1)
df.reset_index(drop=True, inplace=True)
df.drop(df.tail(1).index,inplace=True)

def nameValue(name):
    value = 0
    name=str(name)
    name=name.lower()
    for i in name:
            value+=alpha[i]
    return(value)

for i in range(len(df)):
    df.iat[i,1]=nameValue(df.loc[i][0])
    df.iat[i,2]=df.iat[i,1]*(i+1)

print(sum(df["weightedValue"]))
#%%