import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Citywide_Payroll_Data__Fiscal_Year_.csv")
print(df)
fiscal=df[["Fiscal Year","Regular Gross Paid"]]
print(fiscal)
fiscal=fiscal.groupby("Fiscal Year").mean()
print(fiscal)
plt.style.use('fivethirtyeight')
plt.xlabel("Year")
plt.ylabel("Regular Gross Paid($)")
plt.plot(fiscal.index,fiscal['Regular Gross Paid'])
plt.savefig("graph.png")
plt.show()
table=pd.pivot_table(df,index=['Fiscal Year','Title Description'],values="Regular Gross Paid", aggfunc=np.mean)
print(table)
