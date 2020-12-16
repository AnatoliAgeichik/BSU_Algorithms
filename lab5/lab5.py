import time
import plotly.express as px
import pandas

def convert_to_binary(numb,bin):
    if numb==0:
        return 1
    dig=numb%2
    bin.append(dig)
    convert_to_binary(numb//2,bin)

numb=int(input())

count=25000
chart_data=[]
for _ in range(10):
    start_time = time.time()
    for i in range(1,count):
        bin=[]
        convert_to_binary(numb,bin)
        bin.reverse()
    res_time=time.time()-start_time
    chart_data.append(dict(size=count, time=res_time))
    count+=15000
fig = px.line(chart_data, x="size", y="time")
fig.show()

# for i in bin:
#     print(i, end='')
# print("--- %s seconds ---" % (time.time() - start_time))
