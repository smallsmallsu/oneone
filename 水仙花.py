a=""
for i in range(100,1000):
    b=str(i)
    if pow(eval(b[0]),3)+pow(eval(b[1]),3)+pow(eval(b[2]),3)==i:
        a+="{},".format(i)
print(a[ :-1])
