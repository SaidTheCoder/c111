import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].tolist()

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)

mean=statistics.mean(mean_list)
sd=statistics.stdev(mean_list)
print("mean of sampling population:   ",mean)
print("the standard deviation of the sampling population is:   ",sd)

first_sd_start,first_sd_end=mean-sd,mean
second_sd_start,  second_sd_end=mean-(2*  sd),mean+(2*  sd)
third_sd_start,  third_sd_end=mean-(3*  sd),mean+(3*  sd)

df=pd.read_csv("data1.csv")
data=df["Math_score"].tolist()

mean_sample1=statistics.mean(data)
print("mean of sample one ==> ",mean_sample1)
fig=ff.create_distplot([mean_list],["Math_score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_sample1,mean_sample1],y=[0,0.17],mode="lines",name="MEAN OF SAMPLE 1"))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1 END"))
fig.show()

# df=pd.read_csv("data2.csv")
# data=df["Math_score"].tolist()

# mean_sample2=statistics.mean(data)
# print("mean of sample two ==> ",mean_sample2)
# fig=ff.create_distplot([mean_list],["Math_score"],show_hist=False)
# fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
# fig.add_trace(go.Scatter(x=[mean_sample2,mean_sample2],y=[0,0.17],mode="lines",name="MEAN OF SAMPLE 2"))
# fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1 END"))
# fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2 END"))
# fig.show()

# df=pd.read_csv("data3.csv")
# data=df["Math_score"].tolist()

# mean_sample3=statistics.mean(data)
# print("mean of sample three ==> ",mean_sample3)
# fig=ff.create_distplot([mean_list],["Math_score"],show_hist=False)
# fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
# fig.add_trace(go.Scatter(x=[mean_sample3,mean_sample3],y=[0,0.17],mode="lines",name="MEAN OF SAMPLE 3"))
# fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1 END"))
# fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2 END"))
# fig.add_trace(go.Scatter(x=[third_sd_end,third_sd_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 3 END"))
# fig.show()

# z_score=(mean-mean_sample3)/sd
# print("the z score is ==>",z_score)
# z_score=(mean-mean_sample2)/sd
# print("the z score is ==>",z_score)
z_score=(mean-mean_sample1)/sd
print("the z score is ==>",z_score)