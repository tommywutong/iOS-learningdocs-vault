---
title: Autorelease 很快
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/autorelease-is-fast.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ceb09e86f3f56091'
translated: true
---

> 原文：[Autorelease is Fast](https://www.mikeash.com/pyblog/autorelease-is-fast.html)　·　mikeash.com Friday Q&A

发布于 2006-06-07 00:00 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Using Evil for Good](https://www.mikeash.com/pyblog/using-evil-for-good.html)  
上一篇：[Making Xcode Better](https://www.mikeash.com/pyblog/making-xcode-better.html)  
标签：[autorelease](https://www.mikeash.com/pyblog/?tag=autorelease) [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [performance](https://www.mikeash.com/pyblog/?tag=performance)

Autorelease 很快

作者：[Mike Ash](https://www.mikeash.com/)

我写了一个快速测试程序，分配一百万个 NSObject 并记录所花费的时间。程序每次将使用的自动释放池（autorelease pool）数量增加十倍。第一次测试在整个运行过程中只使用一个池，第二次测试使用十个，以此类推。最后，它为每个对象使用一个池。

你可以[在此](http://mikeash.com/tmp/autorelease_test.m)获取测试程序的源代码。

以下是结果，使用 gcc4 和 -Os 编译，在我相对空闲的 PowerBook G4/1.5（10.4.6）上运行：

| 对象数 | 每个池的对象数 | 运行时间（秒） |
|---|---|---|
| 1000000 | 1000000 | 1.65 |
| 1000000 | 100000 | 1.59 |
| 1000000 | 10000 | 1.48 |
| 1000000 | 1000 | 1.46 |
| 1000000 | 100 | 1.43 |
| 1000000 | 10 | 1.64 |
| 1000000 | 1 | 2.91 |

有趣的是，在运行的前半部分，随着创建的自动释放池数量增加，运行时间实际上在下降。这可能是因为更频繁地创建池意味着程序的内存占用空间（memory footprint）更小，从而花在页表等操作上的时间更少。

在末尾，运行时间急剧上升。但请注意，最差运行时间只是最佳运行时间的大约两倍，这是有道理的，因为最后我们分配的对象数量几乎是原来的两倍。最后一次运行创建并销毁了两百万个对象（一百万个 NSObject，一百万个 NSAutoreleasePool），而最佳运行只略多于一百万个。

那么结论是什么？创建和销毁一个 NSAutoreleasePool 的成本与创建并自动释放一个 NSObject 大致相当。这真的是极其廉价。你甚至可以在循环的每次迭代中都创建一个新的池。唯一需要在池上做文章，让它每 N 次迭代才被销毁并重新创建的情况是，每次循环只创建少量对象，即便如此，最佳情况下节省的开销也只有 50%，而这还是假设你在循环中只创建一个对象并且不做任何其他事。而且，你何必要让它超级无敌快呢？

过早优化是万恶之源。许多在其他方面同意这一说法的人，仍然会说出「你可能想每 10 次迭代释放池一次」这样的话。下次你看到有人说类似的话时，温和地纠正他们，并让他们来看看这篇文章。

---

你喜欢这篇文章吗？我卖的整本书里全是这类文章！第二卷和第三卷现已发售！它们提供 ePub、PDF 和印刷版，并在 iBooks 和 Kindle 上架。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/autorelease-is-fast.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会被我单方面公开羞辱。
