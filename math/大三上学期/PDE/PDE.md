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