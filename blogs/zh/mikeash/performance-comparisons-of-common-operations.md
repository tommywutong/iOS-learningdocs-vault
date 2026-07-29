---
title: 常见操作的性能比较
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/performance-comparisons-of-common-operations.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:3384a32f64fd5ce7'
translated: true
---

> 原文：[Performance Comparisons of Common Operations](https://www.mikeash.com/pyblog/performance-comparisons-of-common-operations.html)　·　mikeash.com Friday Q&A

发布于 2007-08-25 00:00 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Don't use strnstr](https://www.mikeash.com/pyblog/dont-use-strnstr.html)  
上一篇：[Subtle Bugs](https://www.mikeash.com/pyblog/subtle-bugs.html)  
标签：[cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [performance](https://www.mikeash.com/pyblog/?tag=performance)

常见操作的性能比较

作者：[Mike Ash](https://www.mikeash.com/)

我编写了一个 Cocoa 程序来计算大量不同操作的耗时。你可以[在此处](http://www.mikeash.com/perf.mm)下载该程序。

我在一台配备 2.66GHz Mac Pro、3GB RAM 和原装硬盘的机器上运行了该程序。我懒得关闭其他 App，因为我比较懒，而且有大量空闲 CPU。磁盘计时可能受到了后台活动的影响。程序产生了以下表格：

| 名称 | 迭代次数 | 总时间（秒） | 每次耗时（纳秒） |
|---|---|---|---|
| IMP 缓存消息发送 | 1000000000 | 0.9 | 0.9 |
| C++ 虚方法调用 | 1000000000 | 1.4 | 1.4 |
| 整数除法 | 1000000000 | 2.3 | 2.3 |
| Objective-C 消息发送 | 1000000000 | 5.0 | 5.0 |
| 浮点数除法带整数转换 | 100000000 | 0.9 | 9.2 |
| 浮点数除法 | 100000000 | 0.9 | 9.3 |
| 16 字节 memcpy | 100000000 | 2.9 | 29.5 |
| 16 字节 malloc/free | 100000000 | 5.2 | 52.5 |
| NSInvocation 消息发送 | 10000000 | 1.6 | 160.7 |
| NSObject alloc/init/release | 10000000 | 1.9 | 186.6 |
| NSAutoreleasePool alloc/init/release | 10000000 | 3.0 | 300.0 |
| NSButtonCell 创建 | 1000000 | 5.2 | 5219.2 |
| 16MB malloc/free | 100000 | 1.0 | 10211.3 |
| 读取 16 字节文件 | 100000 | 2.0 | 19905.4 |
| 零秒延迟 perform | 100000 | 3.0 | 30374.1 |
| NSButtonCell draw | 100000 | 7.6 | 76167.0 |
| pthread create/join | 10000 | 1.1 | 114887.3 |
| 1MB memcpy | 10000 | 1.2 | 124217.6 |
| 写入 16 字节文件 | 10000 | 5.0 | 503798.5 |
| 写入 16 字节文件（原子操作） | 10000 | 9.9 | 989662.0 |
| NSTask 进程派生 | 1000 | 5.5 | 5504646.1 |
| 读取 16MB 文件 | 100 | 2.9 | 29116230.5 |
| 写入 16MB 文件 | 30 | 10.0 | 334185067.2 |
| 写入 16MB 文件（原子操作） | 30 | 10.0 | 334293782.2 |

所有文件操作均使用 NSData。其余部分使用的 API 应该一目了然。

大体上，这些结果鲜有意外。不过，其中一些仍然具有启发性。

IMP 缓存消息发送是最快的。这并不令人惊讶：它只是通过一个 C 函数指针进行调用。C++ 虚分派紧随其后，慢约 50%，这也在意料之中，因为它只比调用 C 函数指针多一次数组查找。

Objective-C 消息发送如人们所料较慢，但仍非常合理。每次 5 纳秒，平均每条消息发送仅需略多于 13 个周期，这快得惊人。

Malloc/free 正如预期那样昂贵得多。这里有大量的簿记工作。不过，每次分配 53 纳秒，还不至于需要拼命避免。

NSInvocation 慢得离谱，但这同样不足为奇。它需要做更多工作，并且其提供的额外间接调用是有代价的，即比直接消息发送慢大约 30 倍。

NSObject 的创建和销毁比 malloc/free 昂贵得多，但从大局来看仍是小菜一碟。NSAutoreleasePool 的创建和销毁耗时稍多一点，但[你已经知道这一点了](http://www.mikeash.com/blog/pivot/entry.php?id=19)。

分配大块内存比分配小块内存昂贵得多。这是因为一旦超过某个阈值，每次分配都会直接进入内核，你将以系统调用开销的形式为此付出代价。10 微秒仍然相当快，但如果你在紧密循环中大量使用大块内存，或许可以考虑缓存它们。

不出所料，任何涉及到磁盘的操作都极其缓慢。最快的操作是读取 16 字节文件，在整个测试期间，这个文件无疑完全驻留在 RAM 缓存中，每次读取平均仍需要 20 微秒。

延迟 perform（Delayed perform）出乎意料地昂贵，达到了 30 微秒。即便如此，这仍能支持每秒大约 30,000 次，希望你的程序用不了那么多。

创建线程很慢，超过 100 微秒。这就是[线程池](http://en.wikipedia.org/wiki/Thread_pool_pattern)存在的原因。

大块 memcpy 的速度约为 8GB/秒。我相信 Mac Pro 的理论最大内存带宽约为 20GB/秒，但 memcpy 会在总线上双向传输数据，因此我认为这是一个极其出色的性能表现。

表格底部填充了剩余的所有文件操作。我们可以看到使用 NSData 写入的“atomic”标志的成本；由于 16 字节文件的数据量微不足道，写入可视为单次操作，而原子交换增加了一次操作，从而使写入所需的时间翻倍。正如预期，对于大文件，“atomic”的成本基本上可以忽略不计。大文件写入测试的速度为 48.7MB/秒，相当可观。大文件读取测试的速度为 550MB/秒，这显然是操作系统缓存的结果。

表格末尾附近一个令人惊讶的条目是进程派生测试。每次派生超过 5 毫秒，这是一个非常昂贵的操作。绝对不适合在紧密循环中使用。

需要记住的要点：

- 不要害怕 ObjC 消息，它们非常快。
- 不要害怕创建 ObjC 对象，即使在相当紧密的循环中，它也很迅速。
- 尽量避免在紧密循环中连续分配大块内存。
- 如果需要高速，不要执行同步磁盘操作。
- 创建新线程相当慢，如果你打算每秒进行上千次这样的操作，那么创建线程池可能是值得的。
- Intel Mac 拥有惊人的内存带宽。
- 一如既往，首先要为正确性和清晰度编码，然后在必要时进行性能分析（profile），并且只有在确定了关键瓶颈后才应进行优化。

喜欢这篇文章吗？我正出售包含全部文章的整套书籍！第二卷和第三卷现已推出！提供 ePub、PDF、印刷版以及 iBooks 和 Kindle 版本。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/performance-comparisons-of-common-operations.html)

发表你的想法，添加评论：

垃圾信息和离题帖子将被删除，恕不另行通知。违规者可能由我自行决定公开羞辱。
