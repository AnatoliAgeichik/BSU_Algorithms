import random
from decorator_time import time_work_func
import plotly.express as px
import pandas
import time


def get_matrix(n):
    #random.randint(5,10000)
    print(n)
    matrix=[[random.randint(5,10000) for y in range(n)] for x in range(n)]
    # for i in range(0,n):
    #     print(matrix[i])
    return matrix


def product_diog(matrix):
    n=len(matrix)
    for _ in range(0,1000):
        i=0
        j=n-1
        product=1

        while j>-1:
            product*=matrix[i][j]
            i+=1
            j-=1
        #print(product)

chart_data=[]
count=1500
for _ in range(5):
    start_time = time.time()
    matrix=get_matrix(count)
    res_time=time.time() - start_time
    chart_data.append(dict(size=count, time=res_time))
    count+=500
fig = px.line(chart_data, x="size", y="time")
fig.show()

