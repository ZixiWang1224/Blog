# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, t

# 设置中文字体（可选）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 创建x轴数值范围（从-4到4，包含1000个点）
x = np.linspace(-4, 4, 1000)

# 计算标准正态分布在每个x点的概率密度值
y = norm.pdf(x, 0, 1)  # 均值为0，标准差为1

# compute t-distr
y_t1 = t.pdf(x, df = 1)
y_t3 = t.pdf(x, df = 3)
y_t30 = t.pdf(x, df = 30)
y_t100 = t.pdf(x, df = 100)

# 创建图形？
plt.figure(figsize=(8, 6))

# plot stan normal distr
plt.plot(x, y, 'b-', linewidth=2, label='标准正态分布')

# plot t-distr
plt.plot(x, y_t1, 'c--', linewidth=1, label='t分布（df=1）')
plt.plot(x, y_t3, 'm--', linewidth=1, label='t分布（df=3）')
plt.plot(x, y_t30, 'g--', linewidth=1, label='t分布（df=30）')
plt.plot(x, y_t100, 'r--', linewidth=1, label='t分布（df=100）')

# 添加标题和标签
plt.title('标准正态分布与t分布密度曲线对比', fontsize=16)
plt.xlabel('x值', fontsize=12)
plt.ylabel('概率密度', fontsize=12)

# 添加网格
plt.grid(True, linestyle='--', alpha=0.7)

# 添加图例
plt.legend(fontsize=12)

# 设置x轴和y轴范围
plt.xlim(-4, 4)
plt.ylim(0, 0.45)

# 显示图形
plt.tight_layout()
plt.show()