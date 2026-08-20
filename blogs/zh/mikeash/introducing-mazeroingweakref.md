---
title: 介绍 MAZeroingWeakRef
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/introducing-mazeroingweakref.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:3c8e0157fd738d5f'
translated: true
---

> 原文：[Introducing MAZeroingWeakRef](https://www.mikeash.com/pyblog/introducing-mazeroingweakref.html)　·　mikeash.com Friday Q&A

发表于 2010-07-16 20:19 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)
下一篇：[Friday Q&A 2010-07-30：CoreFoundation 对象的零值弱引用](https://www.mikeash.com/pyblog/friday-qa-2010-07-30-zeroing-weak-references-to-corefoundation-objects.html)
上一篇：[Friday Q&A 2010-07-16：Objective-C 中的零值弱引用](https://www.mikeash.com/pyblog/friday-qa-2010-07-16-zeroing-weak-references-in-objective-c.html)
标签：[code](https://www.mikeash.com/pyblog/?tag=code) [hack](https://www.mikeash.com/pyblog/?tag=hack) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [sourcecode](https://www.mikeash.com/pyblog/?tag=sourcecode)

介绍 MAZeroingWeakRef

作者：[Mike Ash](https://www.mikeash.com/)

零值弱引用（zeroing weak reference）是一种指向对象的引用：它不会阻止对象销毁（换句话说，不会 retain 对象），并会在对象销毁后自动变为 `nil`。要使用 `MAZeroingWeakRef`，只需通过 `-initWithTarget:` 创建一个实例：

```
    MAZeroingWeakRef *ref = [[MAZeroingWeakRef alloc] initWithTarget: object];
```

你可以随时通过 `-target` 方法访问该对象：

```
    NSLog(@"Target is %@", [ref target]);
```

只要对象仍然存在，`-target` 就会返回它。对象销毁后，`-target` 会返回 `nil`。`-target` 返回的是经过 retain 和 autorelease 的引用，从而确保你使用返回对象时它仍然有效，即使另一个线程在此期间释放了指向它的最后一个强引用。

你可以从我的公共 Subversion 仓库获取 `MAZeroingWeakRef`：

```
    svn co http://mikeash.com/svn/ZeroingWeakRef
```

它以 BSD 许可证发布，因此只要注明来源，就可以用于商业应用。

`MAZeroingWeakRef` 应该能在任何支持“现代”runtime API 的操作系统上编译和运行，基本上就是 10.5 及以上版本和所有 iOS 版本。只有清理 block 功能（允许在引用销毁时运行任意代码）需要 block 支持；其他功能在没有 block 的情况下也能工作。

如果在 iOS 上使用 `MAZeroingWeakRef`，可能需要在 `MAZeroingWeakRef.m` 中将 `COREFOUNDATION_HACK_LEVEL` 设为 `0`。这会使 `MAZeroingWeakRef` 无法指向 CoreFoundation 桥接对象，但也能避免使用 Apple 有时会严格限制的私有 API。这并不是很大的缺点，因为对 CF 对象使用弱引用极其少见。

希望这个库能对你有所帮助！

喜欢这篇文章吗？我正在销售收录这些文章的整套书！第二卷和第三卷现已出版，提供 ePub、PDF、印刷版、iBooks 和 Kindle 版本。[点击这里了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/introducing-mazeroingweakref.html)

分享你的想法，发表评论：

垃圾评论和离题内容将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。

代码语法高亮由 [Pygments](http://pygments.org/) 提供。
