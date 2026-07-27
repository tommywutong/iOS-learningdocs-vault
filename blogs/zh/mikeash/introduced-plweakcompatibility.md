---
title: 推出 PLWeakCompatibility
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/introducing-plweakcompatibility.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c9f845c848d73125'
translated: true
---

> 原文：[introduced PLWeakCompatibility](https://www.mikeash.com/pyblog/introducing-plweakcompatibility.html)　·　mikeash.com Friday Q&A

发布于 2012-03-31 03:09 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2012-04-13: Nib Memory Management](https://www.mikeash.com/pyblog/friday-qa-2012-04-13-nib-memory-management.html)  
上一篇：[Friday Q&A 2012-03-16: Let's Build NSMutableDictionary](https://www.mikeash.com/pyblog/friday-qa-2012-03-16-lets-build-nsmutabledictionary.html)  
标签：[arc](https://www.mikeash.com/pyblog/?tag=arc) [code](https://www.mikeash.com/pyblog/?tag=code) [hack](https://www.mikeash.com/pyblog/?tag=hack) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [sourcecode](https://www.mikeash.com/pyblog/?tag=sourcecode)

推出 PLWeakCompatibility

作者：[Mike Ash](https://www.mikeash.com/)

使用 PLWeakCompatibility 很简单。把一个文件加进你的 Xcode 项目，再加两个编译器标志，就可以直接上手了。如果你的 App 里已经有 [MAZeroingWeakRef](https://github.com/mikeash/MAZeroingWeakRef)，PLWeakCompatibility 会用它来在较旧的操作系统上处理弱引用。如果没有，它就会用自己的实现——这个实现简单得多，但速度略慢一些。当你的 App 运行在内置弱引用支持的较新操作系统上时，PLWeakCompatibility 会把所有调用都直接传递给原生支持。

从前缀你大概能猜到，PLWeakCompatibility 来自我的雇主 [Plausible Labs](http://plausible.coop/)。这是我参与写的，但不是我一个人完成的！现在你可以在任何能部署 ARC 的操作系统上使用 `__weak` 了，赶紧去 [GitHub 上获取 PLWeakCompatibility](https://github.com/plausiblelabs/PLWeakCompatibility) 吧！

喜欢这篇文章吗？我还卖有满满几本这样的合集！第二卷和第三卷现已出版！提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点此查看详情](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论的 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/introducing-plweakcompatibility.html)

发表你的想法，发一条评论：

垃圾内容和离题帖子将被无通知删除。视情节严重程度，发帖者可能会被公开批评。
