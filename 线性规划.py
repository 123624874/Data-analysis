import pulp
# "LPProbDemo1"是用户定义的问题名（用于输出信息）。
# 参数 sense 用来指定求最小值/最大值问题，可选参数值：LpMinimize、LpMaximize 。
MyProbLP = pulp.LpProblem("LPProbDemo1", sense=pulp.LpMaximize)
# 初始化数据，定义上下限，相当于0 < x < 7;
# 参数 cat 用来设定变量类型，可选参数值：
# ‘Continuous’ 表示连续变量（默认值）、’ Integer ’ 表示离散变量（用于整数规划问题）、’ Binary ’ 表示0/1变量（用于0/1规划问题）。
x = pulp.LpVariable('x', lowBound=0, upBound=7, cat='Continuous')
y = pulp.LpVariable('y', lowBound=0, upBound=7, cat='Continuous')
# 设置目标函数
MyProbLP += 2*x + 3*y
# 不等式约束
MyProbLP += (2*x - 5*y >= 10)
# 不等式约束
MyProbLP += (x + 3*y <= 12)
# 等式约束
MyProbLP += (x + y == 7)
# 进行求解
MyProbLP.solve()
# 输出求解状态，是否有问题
print("Status:", pulp.LpStatus[MyProbLP.status])
for v in MyProbLP.variables():
    # 输出每个变量的最优值，x,y在最优解的值
    print(v.name, "=", v.varValue)
#输出最优解的目标函数值
print("F(x) = ", pulp.value(MyProbLP.objective))

