# PDE

P.D.E Fritz John

ref：

- Evans
- 数学物理方程. 姜尚礼

lds: 0.2 + 0.8; 考勤+作业+回答问题; 数学楼213; 周五晚 7:30-9:00

## Lec 1

concepts

- order
- linear
- quasilinear
- $\nabla$ operator
- Laplace operator($\Delta$ or $\nabla^2$)
- harmonic function
- gradient($\nabla$)
- divergence($\nabla \cdot$)
- curl($\nabla \times$)

---

prop

- 散度、梯度和拉普拉斯算子
- curl、div、grad、Laplace

---

examples

- heat equation
- wave equation
- Maxwell's eq(in vacumn)
- Elastic waves
- Schrödinger's wave eq
- minimal surface eq(分部积分公式)
- Navier-Stokes eq

## 第一章：一阶 PDE

### 最困难的部分：一般的一阶二元 PDE 的求解

思路：用一个 ode system 构造一个曲面，验证这个曲面满足原 PDE. 

关键点：由于在构造过程中，涉及到一些参数的相容性问题，所以除了验证原 PDE，还需要验证相容性问题。

障眼法：FJ 中进行了相当篇幅的对 ode system 建立过程的推导，但是仔细观察就会发现，一些想法和方程的建立「感觉上」是凭空出现的，并非经过严谨的逻辑推导。这是因为此方法其实是一个构造性方法，FJ 的书中只是尝试在解释这个构造的思想来源。（以上为本人看法）

比较：经典的方程求解方法。

假设存在一个解，通过寻找必要条件逐渐确定这个解，最后验证找到的「必要解」也是一个「充分解」。但是这里的逻辑更像是「瞪眼法」：观察到某个结果可能是解，再代入验证。

这个方法也被称为特征线法。对比经典的方法，一个自然的问题是：

>这样的解是否唯一？

>tips（与上一个问题无关，因为我记得上课的时候好像说这个求的是局部解来着，但是具体是因为哪个限制我忘了（ode 和数分忘干净了😭），先挖个坑）: 观察 ode system 的求解条件以及一些定理的使用条件，找到这个解的一些限制。

<!-- some complaints: 我看了半天 + 问 ai 才发现这是个构造解，紫砂😭FJ 大师写的书文学性太高看不懂😭😭😭 -->

## 第二章：二阶 PDE

### 2.1 判断曲线的类型以及特征性

对于 Cauchy 问题，会给出未知函数在一条初始曲线上的值。通过行列式的计算，可以确定这条初始曲线对于这个方程是否是特征曲线。如果不是特征曲线，则可以求解未知函数的各阶导数；如果是特征曲线，则可以进一步分类，根据判别式的正负，可以分成 

- hyperbolic
- parabolic
- elliptic

这三类。

### 2.2 特征曲线上 singularity 的传播

下面只考虑 $\gamma$ 为特征曲线的情况。考虑这样的解，在定义域上 $C^1$，但在被 $\gamma$ 分割的两片区域上分别 $C^2$，然后考虑这个解在 $\gamma$ 上的 jump.

通过研究这个 jump function 的性质，可以发现，如果存在 $\gamma$ 上一个点处的 jump 为 0，则未知函数在整个 $\gamma$ 上的 jump 均为 0.