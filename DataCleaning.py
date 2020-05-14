import pandas as pd
import glob
import matplotlib.pyplot as plt
import seaborn as sns

df=[]
veriler=glob.glob('data*.csv')
for veri in veriler:
    df.append(pd.read_csv(veri))   
df=pd.concat(df)    

print(df.isna().sum())
df.dropna(inplace=True)
print(df.isna().sum())
df.drop(columns=['Unnamed: 0'],inplace=True)
print(df.duplicated().count())
df.drop_duplicates(inplace=True)

df=pd.melt(frame=df,
           id_vars=['State','TotalPop','Income','GenderPop'],
           value_vars=['Hispanic','White','Black','Native','Asian','Pacific'],
           var_name='Peoples',
           value_name='Values')
genderpop=df.GenderPop.str.split('_')
m=genderpop.str.get(0)
f=genderpop.str.get(1)
f=f.str[:-1]
m=m.str[:-1]
f=pd.to_numeric(f)
m=pd.to_numeric(m)
df['Female']=f
df['Male']=m
df=pd.melt(frame=df,id_vars=['State','TotalPop','Income','GenderPop','Peoples','Values'],
           value_vars=['Male','Female'],
           var_name='Gender',
           value_name='Number')
df.drop(columns=['GenderPop'],inplace=True)

replace=df['Income'].replace('[\$,]', '', regex=True)
replace=pd.to_numeric(replace)
df['Income ($)']=replace
df.drop(columns=['Income'],inplace=True)
values=df['Values']
values=df['Values'].replace('[\%,]', '', regex=True)
values=pd.to_numeric(values)
df['Values']=values


white=df[df['Peoples'].isin(['White'])]
pacific=df[df['Peoples'].isin(['Pacific'])]
black=df[df['Peoples'].isin(['Black'])]
native=df[df['Peoples'].isin(['Native'])]
asian=df[df['Peoples'].isin(['Asian'])]
hispanic=df[df['Peoples'].isin(['Hispanic'])]

sns.barplot(data=df,x='Peoples',y='Income ($)')
plt.show()
sns.barplot(data=df,x='Peoples',y='Income ($)',hue='Gender')











