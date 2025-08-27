# 序

GitHub 是一个十分强大的云存储网站。这里会记录一些比较常用的使用方法便于查阅。

目前记录得比较零散，后面有时间可以整理一份教程。

## git clone

在网页端创建 GitHub 仓库是十分容易的，在其中添加或删除文件也十分直观。但是网页端没有像 VSCode 等一样方便好用的渲染器，所以我们常常会把 GitHub 上的文件复制下来，再进行修改。如果希望这份复制下来的文件在修改后重新提交到 GitHub 云端，那么我们在复制的时候就应该采用 `git clone` 的方式。具体步骤如下：

- 找一个用来存储即将被 clone 的仓库的地方（稍后这个 repo 会以一个 folder 的形式被 clone 下来）
- 在这个地方打开 git bash
- 输入 `git clone https://github.com/你的用户名/仓库名.git`，回车

这样就顺利地 clone 了一个 repo！

## 将本地仓库推送到 GitHub

假设现在已经有了一个本地仓库，那么应该如何推送到 GitHub 云端呢？

- 打开 GitHub 网页，创建一个 repo （注意如果本地仓库没有 README 文件，此时创建的时候不要勾选创建 README 选项）
- 返回本地文件夹，打开
- 打开 git bash
- 输入 
```bash
git init
git add .
git commit -m "初始提交"
git branch -M main
git remote add origin https://github.com/你的用户名/仓库名.git
git push -u origin main
```

## Awesome list

## Hello Github
