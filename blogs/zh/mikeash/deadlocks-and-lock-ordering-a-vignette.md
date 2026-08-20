---
title: '死锁与锁顺序：一段小记'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/deadlocks-and-lock-ordering-a-vignette.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7ea9d4eb35fa3e1d'
translated: true
---

> 原文：[Deadlocks and Lock Ordering: a Vignette](https://www.mikeash.com/pyblog/deadlocks-and-lock-ordering-a-vignette.html)　·　mikeash.com Friday Q&A

发表于 2012-02-13 04:26 | [RSS 源](https://www.mikeash.com/pyblog/rss.py) ([全文源](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2012-02-17: Ring Buffers and Mirrored Memory: Part II](https://www.mikeash.com/pyblog/friday-qa-2012-02-17-ring-buffers-and-mirrored-memory-part-ii.html)  
上一篇：[Friday Q&A 2012-02-03: Ring Buffers and Mirrored Memory: Part I](https://www.mikeash.com/pyblog/friday-qa-2012-02-03-ring-buffers-and-mirrored-memory-part-i.html)  
标签：[evil](https://www.mikeash.com/pyblog/?tag=evil) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [threading](https://www.mikeash.com/pyblog/?tag=threading)

死锁与锁顺序：一段小记

作者：[Mike Ash](https://www.mikeash.com/)

这个难题的解决方案是强制规定锁顺序（lock ordering）。有时存在一种自然的顺序，比如父与子。但有时你只有两把锁，并且需要同时获取它们。像这样的代码可能很危险：

```
    @synchronized(a)
    {
        @synchronized(b)
        {
            // 做些事情
        }
    }
```

如果两个线程对 `a` 和 `b` 的认知相反，这就有发生死锁的潜在风险。需要找到某种方法来确保每个线程先锁定同一个对象。在没有其他方法时，可以通过比较这些对象的地址来给它们施加一种顺序。如果我们始终先锁定地址较小的那个，那么即使多个线程从不同的来源获取对象且彼此不通信，也永远不会发生死锁。

幸运的是，这种比较很容易，因为 C 语言允许对同一类型的指针使用比较运算符：

```
    id min, max;
    if(a < b)
        min = a, max = b;
    else
        min = b, max = a;

    @synchronized(min)
    {
        @synchronized(max)
        {
            // 安全地做些事情
        }
    }
```

这消除了死锁的风险。太棒了！

你可能注意到，寻找地址较小对象的代码看起来有点像你为两个不同的 `int` 变量寻找较小整数而编写的代码。实际上，它**完全**等同于整数版本的代码。唯一的区别是类型。

所以重点来了：Cocoa 的 `MIN` 和 `MAX` 变量，由于是以完全类型通用的方式编写的，对对象指针的适用性跟对整数和浮点数一样好。它们可以用来更优雅地解决这个问题：

```
    @synchronized(MIN(a, b))
    {
        @synchronized(MAX(a, b))
        {
            // 安全地做些事情
        }
    }
```

这段代码与上面等价，但更简洁，且没有牺牲任何可读性或安全性。除了在指针上使用 `MIN` 和 `MAX` 这一点，你可能会认为这牺牲了可读性。这取决于个人品味。

这对其他锁结构也同样适用。例如：

```
    NSLock *aLock = [[NSLock alloc] init];
    NSLock *bLock = [[NSLock alloc] init];

    ...

    [MIN(aLock, bLock) lock];
    [MAX(aLock, bLock) lock];
    // 安全地做些事情
    [MAX(aLock, bLock) unlock];
    [MIN(aLock, bLock) unlock];
```

看到一个 `MIN` 宏作为 Objective-C 消息发送表达式中的目标，有点疯狂，但它完全可行。甚至 pthread 互斥锁和自旋锁也能使用这种技巧，只要将其应用于它们的指针，而不是值本身。

如果你发现自己需要同时获取两把锁，首先，仔细想想是否可以避免这样做。但如果必须，`MIN` 和 `MAX` 宏提供了一种简单的方法，可以确保在所有不同线程间保持一致且无死锁的锁顺序。

你喜欢这篇文章吗？我正在销售包含全部此类文章的完整书籍！第二卷和第三卷现已出版！提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 源](https://www.mikeash.com/commentsrss.py?page=pyblog/deadlocks-and-lock-ordering-a-vignette.html)

发表你的想法，添加评论：

垃圾邮件和跑题帖子将被删除，恕不另行通知。违规者可能由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
