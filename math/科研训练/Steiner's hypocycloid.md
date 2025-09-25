spectral method 概论：

- 找到一组基
- 用谱方法结合 Galerkin 方法离散为 ode
- 研究 ode 左侧的微分矩阵，如果满足某些性质（比如半可分性，斜对称性）那么可以快速求解 ode
  
目前我的工作

- 查阅别人在 Steiner's hypocycloid 区域上构造的正交多项式系统
- 一般的正交多项式系统的微分矩阵无法保结构（即斜对称性）
- 通过 W-system 处理，利用原标准正交多项式，构造新的标准正交多项式
- 由 W-system 构造的 orthonormal polynomial system 保持微分矩阵的斜对称性
- 用 W-system 处理 Steiner's hypocycloid 区域上的正交多项式系统，得到新的一组标准正交多项式基，满足微分矩阵保持斜对称性
- 进一步计算其微分矩阵，尝试导出半可分性

汇报反馈：这个 Steiner's hypocycloid 区域非常重要，我猜测的原因

- 这个区域本身具有良好的应用性质
- 这是第一个在弯曲边界区域上找到的谱方法应用
