import pandas as pd
x=pd.read_csv('E:/Sample.csv')
index=0
y=input()
disease=y.rsplit(' ',1)[0]
want=y.rsplit(' ',1)[1]
# print(disease)
# print(want)
# I want to know Covid-19
for i in x.get('Disease'):
    if i==disease:
        break
    else:
        index+=1
print(x.get(want)[index])
