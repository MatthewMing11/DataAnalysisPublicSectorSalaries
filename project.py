"""
Name:  Matthew Ming
Email: matthew.ming11@myhunter.cuny.edu
URL: https://public-salary-analysis-ny.herokuapp.com
Title: Data Analysis of Public Sector Salaries Over Time
Resources:  Used https://data.cityofnewyork.us/City-Government/Citywide-Payroll-Data-Fiscal-Year-/k397-673e to get data for NYC salaries,
            used https://pandas.pydata.org/docs/ to help process data,
            and used https://html5-templates.com/ to create website.
"""
#import all libraries as aliases
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#process dataset into pandas dataframe
df=pd.read_csv("Citywide_Payroll_Data__Fiscal_Year_.csv")
#capitalize work location for styling of graph later on
df["Work Location Borough"]=df["Work Location Borough"].str.capitalize()
#table 1
#extract relevant columns from dataframe and find grouped mean
fiscal=df[["Fiscal Year","Regular Gross Paid"]]
fiscal=fiscal.groupby("Fiscal Year").mean()
#apply fivethirtyeight style
plt.style.use('fivethirtyeight')
#set figure size so graph looks good on website
plt.figure(figsize=(13,8))
#set labels of graph
plt.xlabel("Year")
plt.ylabel("Regular Gross Paid($)")
#plot points onto graph and save it. Display is shown when running program to ensure figure saved is as envisioned
plt.plot(fiscal.index,fiscal['Regular Gross Paid'])
plt.savefig("static/graph.png",bbox_inches="tight")
plt.show()
#table 2
#apply fivethirtyeight style to next graph and set figure size and labels
plt.style.use('fivethirtyeight')
plt.figure(figsize=(13,8))
plt.xlabel("Borough")
plt.ylabel("Regular Gross Paid($)")
#Set label size so x axis is readable
plt.tick_params(axis="x",labelsize=14)
#generate pivot table using the necessary columns
table=pd.pivot_table(df,index=['Work Location Borough','Fiscal Year'], values="Regular Gross Paid",aggfunc=np.mean)
#filter boroughs as they best represent NYC public sectors
table=table.loc[["Bronx","Brooklyn","Queens","Manhattan","Richmond"]]
#rename Richmond to Staten Island since thats the borough's name
table=table.rename(index={"Richmond":"Staten Island"})
#plot using seaborn to generate grouped bar chart to display data
splot=sns.barplot(x="Work Location Borough",y="Regular Gross Paid",hue="Fiscal Year",data=table.reset_index())
#this helps move the legend so graph is very readable
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0)
#following functions help correctly display and save the graph
sfig=splot.get_figure()
sfig.savefig("static/graph2.png",bbox_inches="tight")
plt.show()
#table 3
#apply fivethirtyeight to new graph and set figure size and labels
plt.style.use('fivethirtyeight')
plt.figure(figsize=(13,8))
plt.xlabel("Borough")
plt.ylabel("Regular Gross Paid($)")
#set label size on graph so it is readable
plt.tick_params(axis="x",labelsize=14)
#extract relevant columns from dataframe and find grouped mean
borough=df[["Work Location Borough","Regular Gross Paid"]]
borough=borough.groupby("Work Location Borough").mean()
#filter boroughs as they best represent NYC public sectors
borough=borough.loc[["Bronx","Brooklyn","Queens","Manhattan","Richmond"]]
#rename Richmond to Staten Island since thats the borough's name
borough=borough.rename(index={"Richmond":"Staten Island"})
#plot using matplotlib to generate graph
plt.bar(borough.index,borough['Regular Gross Paid'])
#save generated graph and show to make sure graph is as envisioned
plt.savefig("static/graph3.png",bbox_inches="tight")
plt.show()

