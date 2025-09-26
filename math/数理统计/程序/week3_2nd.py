import numpy as np
import sys
import io

# 设置标准输出编码为UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 输出 m 个样本，sigma2 方差情况下，100 次重复实验结果的方差均值
def simulate_variance(m, sigma2, R=100, seed=123):
    """模拟计算样本方差"""
    np.random.seed(seed)
    
    # 循环 100 次实验的方差，存入 s2_values
    s2_values = []
    for i in range(R):
        sample = np.random.normal(0, np.sqrt(sigma2), m)
        s2 = np.var(sample, ddof=1)
        s2_values.append(s2)

    # compute mean of 100 experiments 的方差
    s2_mean = np.mean(s2_values)
    
    return {
        'm': m,
        'sigma2': sigma2,
        'simulated_mean': s2_mean
    }

# 计算两组样本方差的加权平均值
def simulate_weighted_mean(m, n, sigma2):
    """模拟计算加权均值的方差"""
    var_x = simulate_variance(m, sigma2)['simulated_mean']
    var_y = simulate_variance(n, sigma2)['simulated_mean']
    
    weighted_var = ((m-1) * var_x + (n-1) * var_y) / (m + n - 2)
    return weighted_var

# 测试多组参数
parameter_sets = [
    (5, 100, 1), (100, 100, 1), (5, 100, 25), (100, 100, 25)
]

print("不同参数下的样本方差模拟结果：")
print("=" * 70) # create table

# 存储不同参数输出的数组, 并将计算结果与 sigma2 进行比较（这里采用计算误差的方式）
resultsx = []
resultsy = []
resultsw = []
errorsx = []
errorsy = []
errorsw = []
for n, m, sigma2 in parameter_sets:
    resultx = simulate_variance(m, sigma2)
    resulty = simulate_variance(n, sigma2)
    resultw = simulate_weighted_mean(m, n, sigma2)
    errorx = resultx['simulated_mean'] - sigma2
    errory = resulty['simulated_mean'] - sigma2
    errorw = resultw - sigma2
    resultsx.append(resultx)
    resultsy.append(resulty)
    resultsw.append(resultw)
    errorsx.append(errorx)
    errorsy.append(errory)
    errorsw.append(errorw)
    print(f"m = {m:3d}, n = {n:3d}, σ² = {sigma2:3d} | "
        f"模拟均值X: {resultx['simulated_mean']:7.4f} | "
        f"模拟均值Y: {resulty['simulated_mean']:7.4f} | "
        f"模拟均值S_w^2: {resultw:7.4f} | "
        f"误差X: {errorx:7.4f} | "
        f"误差Y: {errory:7.4f} | "
        f"误差S_w^2: {errorw:7.4f}")


print("=" * 70) # end table