import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics

df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].tolist()
fig=ff.create_distplot([data],["Math_score"],show_hist=False)
fig.show()

mean=statistics.mean(data)
sd=statistics.stdev(data)
print("mean of population:   ",mean)
print("the standard deviation of the population is:   ",sd)