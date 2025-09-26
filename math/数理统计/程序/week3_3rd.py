import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.special import gammaln  # 使用伽马函数的对数
import sys
import io

# 设置标准输出编码为UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# 绘图中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 比较不同样本量下，样本均值的密度函数与其渐近分布的密度函数图像

k = 1
true_mean = 4 * k
true_var = 8 * k  # variance of X_i

n_values = [5, 10, 50, 100]
x_plot = np.linspace(0.01, 8, 1000)


# 使用对数空间计算的样本均值密度函数
def sample_mean_pdf(x, n, k):
    degree1 = 2 * n * k
    degree2 = 1 / 2
    
    # 在对数空间计算，避免数值溢出
    log_term1 = degree1 * np.log(degree2) - gammaln(degree1)
    log_term2 = (degree1 - 1) * np.log(n * x)
    log_term3 = -n * x * degree2
    log_result = log_term1 + log_term2 + log_term3 + np.log(n)
    
    return np.exp(log_result)

# 样本均值的渐近正态分布密度函数
def asymptotic_normal_pdf(x, n, k):
    return norm.pdf(x, 4 * k, np.sqrt(8 * k / n))

# 创建图形
fig, axes = plt.subplots(2, 2, figsize=(8, 6))
axes = axes.flatten()

# 为每个n值绘制图像
for i, n in enumerate(n_values):
    # 计算精确密度
    exact_density = sample_mean_pdf(x_plot, n, k)
    
    # 计算渐近正态密度
    asymptotic_density = asymptotic_normal_pdf(x_plot, n, k)
    
    # 绘制图像
    ax = axes[i]
    ax.plot(x_plot, exact_density, 'b-', linewidth=2, label='精确分布')
    ax.plot(x_plot, asymptotic_density, 'r--', linewidth=2, label='渐近正态')
    
    # 设置标题和标签
    ax.set_title(f'n = {n}')
    ax.set_xlabel('x')
    ax.set_ylabel('密度')
    ax.legend()
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
