# ming1016/study —— 仅保留 Markdown

原仓库：https://github.com/ming1016/study

## 为什么只留文本

这个仓库完整 clone 是 **576 MB**，其中 markdown 只有 3.7 MB，其余 572 MB 是
博客配图（`StarmingBlog/source/uploads/` 一个目录就 513 MB）和无关项目源码
（QuickJS 引擎 40 MB）。

而 `ming1016.github.io` 在 2026 暑假学习计划里**只被引用 1 次**，占掉一半的
`oss/` 预算不成比例。所以这里**只保留 Markdown 与配置文本**，其余按需回原仓库取。

准确地说，删掉的 2,436 个文件里除了图片（864 个 png、587 个 jpg、171 个 jpeg），
还包括仓库夹带的无关项目源码：330 个 `.java`、100 个 `.py`、47 个 `.h`
（QuickJS 引擎、LispToC、OCInterpreter 等），这些与 iOS 底层学习无关。

## 需要配图或源码时

文章里的图片路径形如 `/uploads/<文章 slug>/<序号>.png`，对应原仓库的
`StarmingBlog/source/uploads/<文章 slug>/`。直接访问：

```
https://github.com/ming1016/study/tree/main/StarmingBlog/source/uploads/<文章 slug>
```

或者整目录取：

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/ming1016/study.git
cd study && git sparse-checkout set "StarmingBlog/source/uploads/<文章 slug>"
```

## 同类处理

`oss/` 下其余中文笔记仓库（`analyze`、`Perspective`、`iOS-Weekly`、
`iOS-Source-Probe`）保留了图片，只对超过 300 KB 的做了压缩——它们体积小得多，
且 `draveness/analyze` 在学习计划里被引用 5 次，配图价值更高。
