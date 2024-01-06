import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv("https://raw.githubusercontent.com/alanjones2/dataviz/master/london2018.csv")
df.plot(x="Month", y="Sun")
df.plot.bar(x="Month", y ="Sun")
df.plot(x="Month", y=["Sun", "Rain", "Tmax","Tmin"])
df.plot.bar(x="Month", y ="Rain", color=["black"])
df.plot.bar(x="Month", y=["Sun","Rain","Tmax","Tmin"], color=["#944737","Blue","Yellow"])
df.plot.scatter(x="Month",y="Sun")
df.plot(x="Month",y=["Sun"],color=["Green"],linestyle=":",linewidth=4,markerfacecolor="black",markersize="15",marker="*")
plt.xlabel("Month of the year 2018 (London City)")
plt.ylabel("Value of the rain")
plt.title("Rain value vs Months of the year 2018")
plt.show()
