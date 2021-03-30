
import numpy as  np
import math
import  random
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D  # 空间三维画图



data = np.array([])

# 生成横轴数据
x = [ i for i in np.arange(-10, 10, 1)]
x = np.array(x)
y = 2* x
z= 2 *y








# 绘制散点图

pyplot.scatter(x, y, c='r')
pyplot.show()


# 绘制折线图


pyplot.plot(x, y, c='b')
pyplot.show()




# 二维动图
pyplot.ion()
for i in range(10):
    y = x *i

    if i % 5 ==0:
        pyplot.cla() # 清除屏幕
    pyplot.plot(x, y, c='b')
    pyplot.pause(0.1)

pyplot.show()






# 绘制3D的散点图


from mpl_toolkits.mplot3d import Axes3D

fig = pyplot.figure()
ax = fig.gca(projection='3d')



surf = ax.scatter(x, y, z)
pyplot.show()






# 绘制 动态 3D的散点图

pyplot.ion()

from mpl_toolkits.mplot3d import Axes3D



for i in range(10):
    y = x *i

    if i % 5 ==0:
        pyplot.cla() # 清除屏幕




    pyplot.clf()  # 清除之前画的图
    fig = pyplot.gcf()  # 获取当前图
    ax = fig.gca(projection='3d')  # 获取当前轴

    ax.scatter(x, y,z)
    z = x *y * np.random.randint(0, 10)
    pyplot.pause(0.1) # 暂停一段时间，不然画的太快会卡住显示不出来

pyplot.show()







# 绘制3D的曲面图


from mpl_toolkits.mplot3d import Axes3D

fig = pyplot.figure()
ax = fig.gca(projection='3d')

# 先把x y 自由排列组合 绘制底
x,y = np.meshgrid(x, y)

# 设置高
z =x + y

X = x.reshape(100,-1)
Y = y.reshape(100,-1)
Z = z.reshape(100,-1)


surf = ax.plot_wireframe(X, Y, Z)
pyplot.show()






# 绘制 动态 3D的曲面图

pyplot.ion()

from mpl_toolkits.mplot3d import Axes3D



for i in range(20):
    y = x *i

    if i % 5 ==0:
        pyplot.cla() # 清除屏幕




    pyplot.clf()  # 清除之前画的图
    fig = pyplot.gcf()  # 获取当前图
    ax = fig.gca(projection='3d')  # 获取当前轴

    # 先把x y 自由排列组合 绘制底
    x1,y1 = np.meshgrid(x, y)

    # 设置高
    z =y1 * np.random.uniform(0,0.1)

    X = x1.reshape(10,-1)
    Y = y1.reshape(10,-1)
    Z = z.reshape(10,-1)


    surf = ax.plot_wireframe(X, Y, Z)
    
    pyplot.pause(0.1) # 暂停一段时间，不然画的太快会卡住显示不出来

pyplot.show()




