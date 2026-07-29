---
title: 常见操作性能比较，Leopard 版
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/performance-comparisons-of-common-operations-leopard-edition.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7709d4b7f9f8a713'
translated: true
---

> 原文：[Performance Comparisons of Common Operations, Leopard Edition](https://www.mikeash.com/pyblog/performance-comparisons-of-common-operations-leopard-edition.html)　·　mikeash.com Friday Q&A

发表于 2008-01-12 21:01 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([全文 feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[A Tool for Editing Version-Controlled Bundles](https://www.mikeash.com/pyblog/a-tool-for-editing-version-controlled-bundles.html)  
上一篇文章：[The Cults of Programming](https://www.mikeash.com/pyblog/the-cults-of-programming.html)  
标签：[cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [leopard](https://www.mikeash.com/pyblog/?tag=leopard) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [performance](https://www.mikeash.com/pyblog/?tag=performance)

常见操作性能比较，Leopard 版

作者：[Mike Ash](https://www.mikeash.com/)

你可以[在此](https://www.mikeash.com/pyblog/performance-comparisons-of-common-operations.html)查看原始文章。我使用了与之前完全相同的程序，你可以[在此](http://www.mikeash.com/perf.mm)获取。硬件有一处变化，即计算机现在有 7GB 内存而不是 3GB。我认为这不会对结果产生太大影响。它仍然有 2.66GHz 的 CPU 和标准的 250GB 硬盘。以下是新的图表：

| 名称 | 迭代次数 | 总时间（秒） | 每次时间（纳秒） |
|---|---|---|---|
| IMP 缓存的消息发送 | 1000000000 | 0.7 | 0.7 |
| C++ 虚方法调用 | 1000000000 | 1.1 | 1.1 |
| 整数除法 | 1000000000 | 2.4 | 2.4 |
| Objective-C 消息发送 | 1000000000 | 4.9 | 4.9 |
| 浮点除法与整数转换 | 100000000 | 0.9 | 9.0 |
| 浮点除法 | 100000000 | 0.9 | 9.2 |
| 16 字节 memcpy | 100000000 | 2.9 | 28.9 |
| 16 字节 malloc/free | 100000000 | 5.6 | 56.0 |
| NSInvocation 消息发送 | 10000000 | 0.8 | 77.3 |
| NSObject alloc/init/release | 10000000 | 2.9 | 290.5 |
| NSAutoreleasePool alloc/init/release | 10000000 | 3.6 | 357.7 |
| 16MB malloc/free | 100000 | 0.4 | 4485.2 |
| NSButtonCell 创建 | 1000000 | 6.6 | 6640.5 |
| 读取 16 字节文件 | 100000 | 2.1 | 21219.3 |
| 零秒延迟 perform | 100000 | 4.2 | 42211.8 |
| pthread create/join | 10000 | 0.6 | 56633.2 |
| NSButtonCell 绘制 | 100000 | 6.9 | 69400.5 |
| 1MB memcpy | 10000 | 1.2 | 123001.8 |
| 写入 16 字节文件 | 10000 | 4.9 | 492040.5 |
| 写入 16 字节文件（原子操作） | 10000 | 8.7 | 867380.7 |
| NSTask 进程创建 | 1000 | 6.1 | 6096478.5 |
| 读取 16MB 文件 | 100 | 2.9 | 28619582.6 |
| 写入 16MB 文件（原子操作） | 30 | 10.7 | 356168718.8 |
| 写入 16MB 文件 | 30 | 10.9 | 361767086.5 |

正如你所预期的，不涉及操作系统的底层操作基本没有变化，任何差异都在误差范围之内。像 Objective-C 消息发送这类操作，已经很难再快多少了，所以没有变化。不过，与 Tiger 的数据相比，还是有些有趣的变化。

在 Tiger 上，使用 NSInvocation 发送消息大约需要 160ns 每条消息，而在 Leopard 上只需要 77ns。速度快了两倍多。虽然它仍然比直接消息发送慢 10 倍以上，但已经好多了。

Objective-C 对象的分配和销毁明显变慢了。`[[[NSObject alloc] init] release]` 在 Tiger 上只需要不到 190ns，但在 Leopard 上需要 290ns。在大多数情况下，这仍然可以忽略不计，但耗时增加了 50% 并不是好事。我不确定是什么改动导致了变慢。小尺寸的 malloc/free 测试基本没有影响，所以这显然是 Objective-C 特有的问题。

16MB malloc/free 测试在 Leopard 上的耗时不到之前的一半。在这个尺寸下，malloc/free 会直接触及内核，因此很可能是某些系统调用或内核内存管理优化在起作用。

延迟 perform 在 Leopard 上稍微变差了，从每次 30µs 变成了 42µs。

NSButtonCell 绘制稍微快了一些，尽管不显著。Leopard 可能包含各种绘制优化，因为这是操作系统经常要做的事情。

Pthread 创建在 Leopard 上快了大约两倍。虽然它仍然慢得令人烦恼，但现在你每秒可以创建大约 20,000 次，而不是 10,000 次。

最后，原子操作的 16 字节文件写入速度快了 10% 多一点。这可能是因为文件系统优化影响了它所使用的原子交换过程。

**更新：** 以上是按照 32 位编译的，有人指出展示 64 位数据可能更好：

| 名称 | 迭代次数 | 总时间（秒） | 每次时间（纳秒） |
|---|---|---|---|
| IMP 缓存的消息发送 | 1000000000 | 0.8 | 0.8 |
| C++ 虚方法调用 | 1000000000 | 1.1 | 1.1 |
| 整数除法 | 1000000000 | 2.4 | 2.4 |
| Objective-C 消息发送 | 1000000000 | 8.6 | 8.6 |
| 浮点除法与整数转换 | 100000000 | 0.9 | 9.0 |
| 浮点除法 | 100000000 | 0.9 | 9.0 |
| 16 字节 memcpy | 100000000 | 2.9 | 29.3 |
| 16 字节 malloc/free | 100000000 | 5.3 | 52.7 |
| NSInvocation 消息发送 | 10000000 | 0.8 | 81.6 |
| NSAutoreleasePool alloc/init/release | 10000000 | 1.7 | 169.5 |
| NSObject alloc/init/release | 10000000 | 1.9 | 192.6 |
| 16MB malloc/free | 100000 | 0.3 | 2924.6 |
| NSButtonCell 创建 | 1000000 | 6.1 | 6069.9 |
| 读取 16 字节文件 | 100000 | 1.7 | 17382.1 |
| 零秒延迟 perform | 100000 | 3.4 | 33858.4 |
| pthread create/join | 10000 | 0.6 | 56279.8 |
| NSButtonCell 绘制 | 100000 | 6.5 | 64812.5 |
| 1MB memcpy | 10000 | 1.2 | 122725.0 |
| 写入 16 字节文件 | 10000 | 4.9 | 486454.7 |
| 写入 16 字节文件（原子操作） | 10000 | 8.6 | 859274.8 |
| NSTask 进程创建 | 1000 | 5.6 | 5551589.2 |
| 读取 16MB 文件 | 100 | 2.8 | 27785650.2 |
| 写入 16MB 文件 | 30 | 9.2 | 305342338.2 |
| 写入 16MB 文件（原子操作） | 30 | 9.2 | 306369990.9 |

这里确实有一些有趣的差异。Objective-C 对象分配又回到了 Tiger 的数据。我甚至更不清楚为什么它只在 Leopard 32 位中更慢，而在 64 位中不慢。16MB malloc/free 在 64 位下甚至更快，延迟 perform 也显著更快。其他所有项目看起来基本一致，有一些误差。

你觉得这篇文章有趣吗？我正在销售整本书籍！第 II 卷和第 III 卷现已出版！它们提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS feed](https://www.mikeash.com/commentsrss.py?page=pyblog/performance-comparisons-of-common-operations-leopard-edition.html)

发表你的想法，发表评论：

垃圾邮件和偏离主题的帖子将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。
