def lab2():
    n =100
    p=10
    c=5
    T=[4,2,5,2]
    min_time=(n / min(p, c)) * sum(T)
    #достаточное число процессоров
    p0 = min(p, c)
    #минимальное число процессоров
    p1 = n / p0
    print("Минимальное время  "+str(min_time))
    print("достаточное число процессоров   "+str(p0))
    print("минимальное число процессоров    "+str(p1))


lab2()