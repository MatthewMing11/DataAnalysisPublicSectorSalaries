import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Citywide_Payroll_Data__Fiscal_Year_.csv")
df["Work Location Borough"]=df["Work Location Borough"].str.capitalize()
#table 1
fiscal=df[["Fiscal Year","Regular Gross Paid"]]
fiscal=fiscal.groupby("Fiscal Year").mean()
plt.style.use('fivethirtyeight')
plt.figure(figsize=(13,8))
plt.xlabel("Year")
plt.ylabel("Regular Gross Paid($)")
plt.plot(fiscal.index,fiscal['Regular Gross Paid'])
plt.savefig("static/graph.png",bbox_inches="tight")
plt.show()
#table 2
plt.style.use('fivethirtyeight')
plt.figure(figsize=(13,8))
plt.xlabel("Borough")
plt.ylabel("Regular Gross Paid($)")
plt.tick_params(axis="x",labelsize=14)
table=pd.pivot_table(df,index=['Work Location Borough','Fiscal Year'], values="Regular Gross Paid",aggfunc=np.mean)
table=table.loc[["Bronx","Brooklyn","Queens","Manhattan","Richmond"]]
splot=sns.barplot(x="Work Location Borough",y="Regular Gross Paid",hue="Fiscal Year",data=table.reset_index())
#this helps move the legend so graph is very readable
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0)
#following functions help correctly display and save the graph
sfig=splot.get_figure()
sfig.savefig("static/graph2.png",bbox_inches="tight")
plt.show()
#table 3
plt.style.use('fivethirtyeight')
plt.figure(figsize=(13,8))
plt.xlabel("Borough")
plt.ylabel("Regular Gross Paid($)")
plt.tick_params(axis="x",labelsize=14)
borough=df[["Work Location Borough","Regular Gross Paid"]]
borough=borough.groupby("Work Location Borough").mean()
borough=borough.loc[["Bronx","Brooklyn","Queens","Manhattan","Richmond"]]
borough=borough.rename(index={"Richmond":"Staten Island"})
plt.bar(borough.index,borough['Regular Gross Paid'])
plt.savefig("static/graph3.png",bbox_inches="tight")
plt.show()

