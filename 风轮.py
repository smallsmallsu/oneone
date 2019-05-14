import turtle as t
t.pensize(2)
for i in range(4):
    t.seth(90*i)
    t.fd(100)
    t.right(90)
    t.circle(-100,45)
    t.goto(0,0)


#circle用法得再熟悉，以方向为x轴，逆时针画圆弧
