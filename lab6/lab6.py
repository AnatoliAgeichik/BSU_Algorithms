import  random
import time
import plotly.express as px
import pandas

def bose_nelson(data):
    m = 1
    while m < len(data):
        j = 0
        while j + m < len(data):
            bose_nelson_merge(j, m, m,data)
            j = j + m + m
        m = m + m
    return data

def bose_nelson_merge(j, r, m,data):
    if j + r < len(data):
        if m == 1:
            if data[j] > data[j + r]:
                data[j], data[j + r] = data[j + r], data[j]
        else:
            m = m // 2
            bose_nelson_merge(j, r, m,data)
            if j + r + m < len(data):
                bose_nelson_merge(j + m, r, m,data)
            bose_nelson_merge(j + m, r - m, m,data)
    return data


def buble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1]=arr[j+1],arr[j]

def get_arr(n):
    arr=[random.randint(0,n) for _ in range(n)]
    return arr
                

#arr=[5,2,6,25,96,12,15,32,17,82,3,16,27,41,2]
#res=bose_nelson(arr)
#print(arr)
count=500
chart_data=[]
for i in range(5):
    arr=get_arr(count)
    start_time = time.time()
    bose_nelson(arr)
    res_time=time.time()-start_time
    chart_data.append(dict(size=count, time=res_time))
    count += 500
fig = px.line(chart_data, x="size", y="time")
fig.show()

count=500
chart_data=[]
for i in range(15):
    arr=get_arr(count)
    start_time = time.time()
    buble_sort(arr)
    res_time=time.time()-start_time
    chart_data.append(dict(size=count, time=res_time))
    count += 500
fig = px.line(chart_data, x="size", y="time")
fig.show()
print(arr)


