import pandas as pd
from matplotlib import pyplot as plt
import statsmodels.formula.api as smf
dat=pd.read_table("cal_sodium.txt",delimiter=' ')
res = smf.ols(formula='Calories ~ Type + Sodium', data=dat).fit()
print(res.params)
print(res.summary())

key=dict(zip(set(dat.Type),['green','blue','red']))
colors=[key[x] for x in dat.Type]
plt.scatter(dat.Sodium,dat.Calories,c=colors)
plt.plot(dat.Sodium,res.params[3]*dat.Sodium+res.params[0])
for i in range(1,3):
    plt.plot(dat.Sodium,res.params[3]*dat.Sodium+res.params[0]+res.params[i])
plt.savefig('Cal_Sodium.png',transparent=True)
plt.show()
