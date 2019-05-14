def a(df):    
    for i in range (365):
        if i%7 in [6,0]:
            a=a*(1-0.01)
        else:
            a=a*(1+df)
    return a
b=pow(1.01,365)
df=0.01
while a(df)<b:
    df+=0.001
print("工作日努力的参数是:{:.3f}".format(df))
            
