# Analytic Number Theory

## 1. 数论函数

### 1.1 Dirichlet 卷积

concepts

- 卷积

Prop

- 交换律
- 结合律
- 卷积保持可乘性

---

- 数论函数环
- 幺元及其卷积表示（associated with Möbius function）
- Möbius 反演公式

### 1.2 求和公式——Euler Maclaurin

concepts

- Bernoulli polynomials

thm

- Euler-Maclaurin
- Euler

application

- harmonic series
- zeta function
- Dirichlet (求和变短 trick)

### 1.3 Poisson 求和公式

$f:\mathbb{R}^\ell \to \mathbb{R}$ 有任意阶偏导，$\forall (\alpha_1,\cdots,\alpha_\ell), (\beta_1,\cdots,\beta_\ell) \in \mathbb{Z}^{\ell}_{\ge 0}$, and $\sup\limits_{\vec{x} = (x_1,\cdots,x_\ell) \in \mathbb{R}^\ell} \vert x_1 ^{\alpha_1} \cdots x_\ell ^{\alpha ^{\ell}} \frac{\partial ^{\beta_1 + \cdots + \beta_\ell} f}{\partial x_1 ^{\beta_1} \cdots \partial x_\ell ^{\beta_\ell}} (\vec{x}) \vert < \infty.$ 则称 $f$ 是一个 **Schwartz 函数**。所有的 Schwartz 函数的集合称为 **Schwartz 类**，denote as $S(\mathbb{R} ^{\ell}).$

(**Poisson sum Theorem**). Given $f \in S(\mathbb{R})$, then $\sum\limits_{n\in \mathbb{Z}} f(n) = \sum\limits_{n\in \mathbb{Z}} \hat{f}(n).$ Where $\hat{f}(\xi) = \int_{\mathbb{R}} f(x)e(-x \xi)dx,\quad \forall \xi \in \mathbb{R}; \quad e(t) = e ^{2\pi i t}.$

- construct $F(x) = \sum\limits_{n\in \mathbb{Z}} f(x + n)$, then prove that $F$ converges to its Fourier series. 
- calc the Fourier series, and get the thm from the eq.


**example**.

### 1.4 Gamma function

$$\Gamma(s) := \frac{1}{s} \prod\limits_{n=1} ^{N} (1+\frac{s}{n}) ^{-1} (1 + \frac{1}{n}) ^{s}$$

defined on $\mathbb{C}-\mathbb{Z}_{\le 0}$.

**Prop**

$$\Gamma (s + 1) = s\Gamma (s), \quad \forall s\in \mathbb{C}-\mathbb{Z}_{\le 0}.$$

**Corollary**

$$\Gamma (n) = (n - 1)!, \quad \forall n \in \mathbb{Z}_{\ge 1}.$$

**Prop(余元公式)**

$$\Gamma (s) \Gamma (1-s) = \frac{\pi}{sin \pi s}, \quad \forall s \in \mathbb{C}-\mathbb{Z}.$$

**Thm(Stirling)**

Let $s \in \mathbb{C} - \mathbb{Z}$, then 

$$log\Gamma (s) = (s - 2) logs - s + \frac{1}{2}log (2 \pi) + O (\frac{1}{\vert s \vert}).$$

where we choose the branch that $log1 = 0$.

**Corollary**