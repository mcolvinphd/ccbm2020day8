import pandas as pd
import statsmodels.formula.api as smf
dat=pd.read_table("diamond.txt",delimiter=' ')
mod=smf.ols(formula='cost~carat+color+clarity',data=dat)
res=mod.fit()
print(res.summary())
print(res.params)
