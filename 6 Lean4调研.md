# Lean4 调研

## 问题

MyQuestions:

- Lean4 可以做什么事情？
- 形式化是否就是指用把自然语言与 Lean4 这门编程语言进行对应？
- 形式化是如何对 LLM、ML、强化学习的发展进行推进的？
- Lean4 语言的历史，它是如何发展起来的？哪些人或者组织在推动它？
- 如何快速学习 Lean4 的使用方法？
- Lean4 领域相关的研究是否有论文发表？主要有哪些高水平高质量的论文？
- Lean4 是否推动了 deepmind 的发展？
- 如何改进 Lean4 的工具箱？（比如 tactics like `apply?`）
- 如何改进 Lean4 的定理搜索功能？

DouBao's Questions:

- Lean4 与其他定理证明器（如 Coq、Isabelle、Agda 等）相比，核心优势和劣势分别是什么？在不同应用场景下如何选择？
- Lean4 在工业界有哪些实际的落地案例？例如在软件验证、数学定理证明、硬件设计验证等领域的具体应用。
- Lean4 的类型系统有哪些独特之处？其类型理论基础（如依赖类型）在实际使用中如何影响开发效率和证明可靠性？
- Lean4 的社区生态现状如何？是否有活跃的开源项目、插件库或社区支持资源（如论坛、教程、工具链）？
- Lean4 对并行计算或分布式证明验证是否支持？在处理大规模定理证明任务时的性能表现如何？
- Lean4 的语法设计理念是什么？对于初学者来说，其语法学习曲线与其他编程语言或定理证明器相比有何特点？
- Lean4 在教育领域的应用情况如何？是否被用于高校的数学、计算机科学等专业的教学，以帮助学生理解形式化推理？
- Lean4 的未来发展 roadmap 是怎样的？核心开发团队有哪些明确的功能迭代计划或技术突破方向？
- 如何利用 Lean4 进行程序合成（Program Synthesis）？它在自动生成正确程序方面有哪些潜力和局限？
- Lean4 与自然语言处理（NLP）技术结合的可能性？例如是否有研究尝试将自然语言数学证明自动转换为 Lean4 形式化证明？

## 初步搜索

### Keywords

- 定理证明器
- 依赖类型论（dependent type theory）
- ICLR 的论文
- Lean, Isabelle, miniF2F, ProofNet, autoformal 
- [LeanAgent](https://openreview.net/pdf?id=Uo4EHT4ZZ8)
- [ImProver](https://openreview.net/pdf?id=dWsdJAXjQD)
- [Herald](https://openreview.net/pdf?id=Se6MgCtRhz)
- Haskell
- OCaml 
- 依赖语言
- Idris
- 神经网络
- Benchmark
- 通用函数式编程语言
- 交互式定理证明器（Interactive Theorem Prover, ITP）
- 元编程
- 词向量
- prompting
- CoT (Chain of Thought)
- 蒸馏

### 参考

[写给一般CS人的 Lean4 安利](https://zhuanlan.zhihu.com/p/669124637#:~:text=Lean4%20%E5%8F%AF%E4%BB%A5%E7%94%A8%E6%9D%A5%E8%A1%A8%E8%BE%BE,.org%2Ftheorem_proving_in_lean4%2F.)
>Lean4 可以用来表达和证明数学命题, 这是 Lean 的初衷, 即, 用来**严格地验证数学定理**. 它拥有一个庞大的数学定理库 Mathlib, 并已在数学界发挥了作用. 

[西湖大学课程简介](https://its.westlake.edu.cn/info/1017/1942.htm)
>最初由Leonardo de Moura等人于2013年在微软研究院推出。

>2018年，Kevin Buzzard等人曾在Liquid tensor experiment中使用Lean验证菲尔兹奖得主Peter Scholze关于凝聚态数学的一系列定理。

[数学小站](https://www.lookeng.cn/2024/10/15/lean/iclr2024-formal-proof-lean/)
>由于数学形式化能用于消除模型幻觉，在当下格外受到关注。

本站还收录了2025年与形式化有关的20+篇论文链接。

[陶哲轩最新采访：AI将颠覆数学界！用Lean规模化，成百上千条定理一次秒杀](https://hub.baai.ac.cn/view/37908)
>在形式化项目中，我们注意到，你可以与那些不理解整个项目但理解其中一部分的人合作。

>现在，在数学合作中，每个人都必须知道几乎所有的数学知识，正如Scholze提到的，这是一个绊脚石。

>如果你想证明一个尚未解决的猜想，首先要做的一件事就是把它分解成更小的部分，每个部分都有更大的机会被证明。但你往往会把一个问题分解成更难的问题。**将一个问题转化为更难的问题比转化为更简单的问题要容易得多**。在这方面，人工智能并没有表现出比人类更好的能力。

>人们只发表成功的故事，但真正珍贵的数据来自于尝试。可能起初不太成功，但解决的过程更有价值。然而，大家只公布成功的研究结果，不公布研究的过程。

## 更多问题

- LLM在形式化数学中的挑战和局限？
  - 数据稀缺
  - 自然语言与形式语言的翻译
  - 形式系统的复杂性

## 后记

目前受限于 Lean4 本身发展的有限性，导致网络上关于 Lean4 的成熟的介绍很少，所以能搜索到的内容不多。加上其本身不属于一个社科类的主题，和之前提出的调研方法范围适配性不是非常好，所以很多问题现在无法回答（我猜想甚至专业的研究人员也未必能回答）