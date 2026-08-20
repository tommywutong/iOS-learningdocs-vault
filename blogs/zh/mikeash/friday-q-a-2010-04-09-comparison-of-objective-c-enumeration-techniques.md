---
title: 'Friday Q&A 2010-04-09：Objective-C 枚举技术比较'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-04-09-comparison-of-objective-c-enumeration-techniques.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:295fe50431c6835d'
translated: true
---

> 原文：[Friday Q&A 2010-04-09: Comparison of Objective-C Enumeration Techniques](https://www.mikeash.com/pyblog/friday-qa-2010-04-09-comparison-of-objective-c-enumeration-techniques.html)　·　mikeash.com Friday Q&A

发布于 2010-04-09 11:17 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([全文 feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[一个 Objective-C Continuations 库](https://www.mikeash.com/pyblog/an-objective-c-continuations-library.html)  
上一篇：[Friday Q&A 2010-04-02：OpenCL 基础](https://www.mikeash.com/pyblog/friday-qa-2010-04-02-opencl-basics.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [nsfastenumeration](https://www.mikeash.com/pyblog/?tag=nsfastenumeration) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2010-04-09：Objective-C 枚举技术比较

作者：[Mike Ash](https://www.mikeash.com/)

**基线**  
为了建立比较的基准，让我们看看对 Objective-C 对象的 C 数组进行迭代的情况：

```
    id *array = ...;
    NSUInteger length = ...;
    for(NSUInteger i = 0; i < length; i++)
        // do something with array[i]
```

语法还可以，但不算好。有点冗余，也容易出错。

对于单线程代码，这差不多是对象枚举能达到的最快速度。循环本身的开销很小，几乎是最低限度的了。（如果你真的很激进，可以尝试手动展开循环，但那就有点疯狂了，而且实际上可能反而损害性能。）

当然，在 Cocoa App 中，这种对象枚举通常并不实用。我们很少遇到对象的 C 数组。更常见的是实现了集合（collection）的对象。

**`NSEnumerator`**  
在过去，Cocoa 中枚举集合的标准方式是使用 `NSEnumerator`：

```
    NSEnumerator *enumerator = [collection objectEnumerator];
    id obj;
    while((obj = [enumerator nextObject]))
        // do something with obj
```

这写起来非常冗长且烦人。而且与基线相比，它还有相当可观的开销。首先，它需要分配一个全新的对象来管理枚举。然后，每次迭代都需要向枚举器发送一条消息。这里产生的开销，虽然与循环**内部**可能发生的大多数活动相比相对较小，但仍然比基线大得多。

**`objectAtIndex:`**  
对于喜欢更传统方式，或不喜欢仅仅为了枚举就创建一个新对象的人来说，另一种枚举数组的方式是反复调用 `objectAtIndex:`：

```
    NSUInteger length = [array count];
    for(NSUInteger i = 0; i < length; i++)
    {
        id obj = [array objectAtIndex: i];
        // do something with obj
    }
```

这仍然需要每次迭代发送一条消息，但避免了创建 `NSEnumerator` 对象，因此根据该特定数组中 `objectAtIndex:` 的速度，可能会有一些性能优势。（由于 `NSArray` 的内部实现方式，`objectAtIndex:` 与 `objectEnumerator` 的性能特征并不总是很明显，尤其是在非常大的数组上。）

除了冗长和容易出错之外，一个很大的缺点是它根本无法用于枚举 `NSSet` 或 `NSDictionary`。反过来，一个很大的优点是，通过小心管理循环索引，可以在循环内安全地修改数组，这是其他任何枚举技术都无法做到的（除非你枚举的是副本之类的东西）。

**`NSFastEnumeration`**  
在 10.5 中，Apple 终于解决了这个问题。他们通过引入 `for`/`in` 语法解决了冗长的问题。他们通过将 `for`/`in` 构建在一个名为 `NSFastEnumeration` 的协议（protocol）之上，解决了速度问题。

```
    for(id obj in collection)
        // do something with obj
```

`NSFastEnumeration` 的工作原理是尽可能批量获取对象。编译器生成代码来调用集合，并要求集合返回尽可能多的对象。对于连续存储对象的集合，集合能够直接返回指向这些对象的内部指针。如果数组中的每个对象都是连续的，循环就会变得非常类似于基线，并具有相同的整体性能。如果有多个连续的对象存储区，`NSFastEnumeration` 允许集合一个接一个地返回内部指针，从而在每个存储区上实现快速的循环，并且仅需一条 Objective-C 消息就能获取下一个内部指针。对于没有连续存储的集合，`NSFastEnumeration` 允许集合批量将对象复制到临时存储中，从而获得许多相同的好处。对于这些方案都不适用的集合，`NSFastEnumeration` 仍然允许集合高效地逐个返回对象。

语法友好，性能出色，这是一个伟大的组合。

**基于 block 的枚举**  
在 10.6 中，Apple 将 block 引入 Objective-C，同时也引入了基于 block 的枚举。block 天生适合创建像枚举这样的新控制（control）结构，Apple 也为他们的集合添加了基于 block 的枚举方法：

```
    [array enumerateObjectsUsingBlock: ^(id obj, NSUInteger index, BOOL *stop) {
        // do something with obj
    }];
```

对于简单的枚举，block 语法相比快速枚举和 `for`/`in` 语法并没有什么优势。语法更笨拙一些，迭代速度也稍慢。代码必须为每个对象调用你的 block。这个开销比消息发送（如 `NSEnumerator` 的情况）要小，但比 `NSFastEnumeration` 中简单的 C `for` 循环要大。block 语法在两种情况下很有用。

第一种是你需要的不仅仅是简单的枚举。Apple 提供了两种枚举选项：并发枚举和反向枚举。这两种都不是 `for`/`in` 语法直接支持的。并发枚举用其他方式很难实现，因此如果你的枚举可以利用多线程，这将非常有用。反向枚举可以通过向数组发送 `reverseObjectEnumerator` 然后将其用作 `for`/`in` 的目标来实现，但这仍然有创建 `NSEnumerator` 并通过它进行间接枚举的开销，因此基于 block 的方法可能更胜一筹。

第二种是你正在枚举字典，并且同时需要键和对象。`for`/`in` 语法一次只能给你一个对象。这意味着你必须枚举键，然后作为单独的步骤向字典请求对象：

```
    for(id key in dictionary)
    {
        id obj = [dictionary objectForKey: key];
        // do something with key and obj
    }
```

这不仅比普通的 `for`/`in` 冗长得多，而且速度也慢得多。额外的消息发送和字典查找会破坏 `NSFastEnumeration` 良好的性能特性。

`NSDictionary` 提供了一种基于 block 的枚举方法，它直接将键和对象都传递给 block：

```
    [dictionary enumerateKeysAndObjectsUsingBlock: ^(id key, id obj, BOOL *stop) {
        // do something with key and obj
    }];
```

这写起来稍微好一些，而且可能快得多。字典能够直接在其内部数据结构上迭代键/对象对，跳过了 `for`/`in` 循环所需的额外消息发送和键查找。

**结论**  
对于任何代码，除非你确定存在性能问题，并且可以通过更复杂的方法来解决，否则你都应该优先选择最易于维护和阅读的技术。这对于集合枚举来说尤其如此，因为你在循环内部所做的工作几乎肯定会远远超过循环本身所做的工作。

幸运的是，Apple 的设计使得在大多数情况下我们不必做出任何取舍。在大多数情况下，`for`/`in` 语法既是枚举集合最方便也是最快的代码。对于那些少数它并非最佳选择的情况，10.6 提供了基于 block 的枚举构造来填补空白。除非你必须支持 10.4，否则你几乎永远不需要编写 `NSEnumerator` 循环。如果需要枚举时修改数组，使用 `objectAtIndex:` 手动获取对象会很方便，但除此之外，它相比 `for`/`in` 没有任何优势。

本周就到这里。欢迎下周再来，届时我将讨论如何构建你自己的 `NSFastEnumeration` 协议实现。在那之前，请继续向我发送你想讨论的话题想法。Friday Q&A 由读者提交驱动，所以如果你有想在这里讨论的话题，[请发送给我](mailto:mike@mikeash.com)！下周已经预定，但之后的时间完全开放。

喜欢这篇文章吗？我有一整本书可以卖给你！第二卷和第三卷现已出版！有 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里了解更多](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论 RSS feed](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-04-09-comparison-of-objective-c-enumeration-techniques.html)

发表你的想法，添加评论：

垃圾邮件和离题内容将被删除，恕不另行通知。我可能自行决定公开羞辱违规者。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
