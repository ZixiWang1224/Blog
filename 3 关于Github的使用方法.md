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

## 设置代理

有时在 clone GitHub repo 时会遇到速度过慢甚至失败的情况，而这些往往是因为没有设置网络代理。

- 打开 VSCode 的 terminal
- 输入

```bash
git config --global http.proxy http://x.x.x.x:xxxx 
# 相应代理地址
git config --global https.proxy https://x.x.x.x:xxxx
```

但是之前在一个项目的实习中，有学长提到 Windows 环境下直接在 GitHub 中设置网络代理似乎是不行的，但是我也没有尝试过。如果遇到这种情况，可以直接在相应的本地仓库打开 git bash 然后输入以上代码进行设置。

## 协作项目要建立审查

[和傻子一起写代码](https://www.bilibili.com/video/BV1udEuzrEa7?spm_id_from=333.788.videopod.sections&vd_source=511a91ef2f7b2b1dbc28ac62a47dadae)

## API

## token

## Github大文件上传与管理