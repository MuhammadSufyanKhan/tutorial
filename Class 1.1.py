import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
df=pd.read_csv("https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv")
print(df)
df.head()
df.tail()
df.info()
df.describe()
df.columns
df.isnull().sum()
df.dropna(inplace=True)
print(df)
data_types=df.dtypes
print("Data Types:\n",data_types)

df['total_rooms']=df['total_rooms'].astype(int)
print(data_types)
sns.catplot(x="ocean_proximity", y = "population", data = df, kind="box", aspect=2)
plt.title("Boxplot for ocean proximity vs population")
plt.show()
value_column='population'
outliers=df[(df[value_column]<df[value_column].mean()-3*df[value_column].std())|(df[value_column]>df[value_column].mean()+3*df[value_column].std())]
print("Outliers:\n",outliers)
