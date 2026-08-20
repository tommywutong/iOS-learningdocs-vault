---
title: Objective-C 中可供枚举集合的多种选项
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'http://www.mikeash.com/pyblog/friday-qa-2010-04-09-comparison-of-objective-c-enumeration-techniques.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:295fe50431c6835d'
translated: true
---

> 原文：[the various options available in Objective-C for enumerating over a collection](http://www.mikeash.com/pyblog/friday-qa-2010-04-09-comparison-of-objective-c-enumeration-techniques.html)　·　mikeash.com Friday Q&A

发布于 2010-04-09 11:17 | [RSS 源](http://www.mikeash.com/pyblog/rss.py) ([全文源](http://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](http://www.mikeash.com/pyblog/)  
下一篇文章：[一个 Objective-C Continuations 库](http://www.mikeash.com/pyblog/an-objective-c-continuations-library.html)  
上一篇文章：[Friday Q&A 2010-04-02：OpenCL 基础](http://www.mikeash.com/pyblog/friday-qa-2010-04-02-opencl-basics.html)  
标签：[fridayqna](http://www.mikeash.com/pyblog/?tag=fridayqna) [nsfastenumeration](http://www.mikeash.com/pyblog/?tag=nsfastenumeration) [objectivec](http://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2010-04-09：Objective-C 枚举技术比较

作者 [Mike Ash](http://www.mikeash.com/)

**基线**  
为了建立比较的基线，先考虑遍历一个 Objective-C 对象的 C 数组：

```
    id *array = ...;
    NSUInteger length = ...;
    for(NSUInteger i = 0; i < length; i++)
        // do something with array[i]
```

语法还算过得去，但不算好。有些冗余且容易出错。

对于单线程代码，这差不多是进行对象枚举能获得的最快速度。循环本身的开销很小，基本上已经做到了最小。（如果你真想极端一些，可以尝试手动展开循环，但那会变得非常疯狂，甚至可能损害性能。）

当然，这种对象枚举方式在 Cocoa App 中通常不太实用。我们很少会碰到一个对象的 C 数组。更常见的是一个实现了集合（collection）的对象。

**`NSEnumerator`**  
在过去，Cocoa 中枚举集合的标准方式是使用 `NSEnumerator`：

```
    NSEnumerator *enumerator = [collection objectEnumerator];
    id obj;
    while((obj = [enumerator nextObject]))
        // do something with obj
```

这种方法写起来极其冗长且烦人。相比基线，它也有相当大的开销。首先，它需要分配一个全新的对象来管理枚举。然后，每次迭代都需要向这个 enumerator 发送一条消息。这里的开销虽然与循环 *内部* 大多数活动相比相对较小，但比基线要大得多。

**`objectAtIndex:`**  
对于那些更喜欢传统方式，或者不喜欢仅仅为了枚举就创建一个全新对象的人来说，另一种枚举数组的方法是重复调用它的 `objectAtIndex:`：

```
    NSUInteger length = [array count];
    for(NSUInteger i = 0; i < length; i++)
    {
        id obj = [array objectAtIndex: i];
        // do something with obj
    }
```

这仍然需要每次迭代发送一条消息，但避免了创建 `NSEnumerator` 对象，因此可能是一个小胜，具体取决于该数组 `objectAtIndex:` 的速度。（由于 `NSArray` 的内部实现方式，`objectAtIndex:` 与 `objectEnumerator` 的性能特征并不总是完全明显，尤其是在非常大的数组上。）

除了冗长且容易出错之外，一个很大的缺点是它根本无法用于枚举 `NSSet` 或 `NSDictionary`。相反，一个很大的优点是，通过仔细管理循环索引，在循环内部修改数组是安全的，这是其他任何枚举技术都不具备的（除非你改为枚举一个副本，或者采取类似做法）。

**`NSFastEnumeration`**  
在 10.5 中，Apple 终于解决了这个问题。他们通过引入 `for`/`in` 语法解决了冗长问题。并且通过在一个名为 `NSFastEnumeration` 的协议之上构建 `for`/`in` 解决了速度问题。

```
    for(id obj in collection)
        // do something with obj
```

`NSFastEnumeration` 的工作方式是尽可能批量获取对象。编译器生成代码，该代码会调用集合并要求集合返回尽可能多的对象。对于连续存储对象的集合，集合能够直接返回指向这些对象的内部指针。如果数组中的每个对象都是连续的，那么循环就会变得非常类似于基线，并具有相同的整体性能。如果存在多个连续的对象存储区域，`NSFastEnumeration` 允许集合一个接一个地返回内部指针，从而为每个存储区域实现快速的循环，并且只需要在获取下一个内部指针时发送一个 Objective-C 消息。对于没有连续存储的集合，`NSFastEnumeration` 允许集合批量将对象复制到临时存储中，从而获得许多相同的好处。对于这些方法都不适用的集合，`NSFastEnumeration` 仍然允许集合高效地逐个返回对象。

语法简洁，性能出色，这是一个很好的组合。

**基于 block 的枚举**  
在 10.6 中，Apple 将 block 引入了 Objective-C，同时也引入了基于 block 的枚举。Block 非常适合创建像枚举这样的新控制结构，Apple 也为他们的集合添加了基于 block 的枚举方法：

```
    [array enumerateObjectsUsingBlock: ^(id obj, NSUInteger index, BOOL *stop) {
        // do something with obj
    }];
```

对于简单的枚举，block 语法相比快速枚举和 `for`/`in` 语法并没有提供任何优势。语法有点笨拙，迭代速度也稍慢一些。代码必须为每个对象调用你的 block。这个开销小于像 `NSEnumerator` 那种发送消息的开销，但大于 `NSFastEnumeration` 那种简单的 C `for` 循环。block 语法在两种情况下是有用的。

第一种是当你需要的不仅仅是简单的枚举时。Apple 提供了两种枚举选项：并发枚举和反向枚举。`for`/`in` 语法都不能直接支持。并发枚举很难用其他方式实现，所以如果你的枚举可以利用多线程，这将非常有用。反向枚举可以通过向数组发送 `reverseObjectEnumerator` 然后将其作为 `for`/`in` 的目标来完成，但这仍然有创建 `NSEnumerator` 并通过它进行间接枚举的开销，因此基于 block 的方法可能更优。

第二种是当你枚举一个字典且同时需要键和对象时。`for`/`in` 语法一次只能给你一个对象。这意味着你必须先枚举键，然后作为单独的步骤向字典询问对象：

```
    for(id key in dictionary)
    {
        id obj = [dictionary objectForKey: key];
        // do something with key and obj
    }
```

这不仅比普通的 `for`/`in` 冗长得多，而且速度也慢得多。额外的消息发送和字典查找会破坏 `NSFastEnumeration` 的良好性能特性。

`NSDictionary` 提供了一种基于 block 的枚举方法，它直接将键和对象同时传递给 block：

```
    [dictionary enumerateKeysAndObjectsUsingBlock: ^(id key, id obj, BOOL *stop) {
        // do something with key and obj
    }];
```

这种写法更优雅一些，而且可能会快得多。字典能够直接遍历其内部数据结构中的键/值对，跳过了 `for`/`in` 循环所需的额外消息发送和键查找。

**结论**  
对于任何代码，除非你确切知道存在速度问题，并且更困难的方法能带来好处，否则应始终优先选择最易于维护和阅读的技术。对于集合枚举尤其如此，因为你在循环内部所做的工作几乎肯定比循环本身所做的工作要大得多。

幸运的是，Apple 已经让我们在大多数情况下无需进行任何权衡。在大多数情况下，`for`/`in` 语法同时是枚举集合最优雅和最快的代码。对于少数它不是最佳选择的情况，10.6 提供了基于 block 的枚举结构来填补空缺。除非你必须支持 10.4，否则你几乎不应该再编写 `NSEnumerator` 循环。如果你需要在枚举时修改数组，使用 `objectAtIndex:` 手动获取对象会很方便，但除此之外，它相比 `for`/`in` 没有任何优势。

本周就到这里。下周我将讨论如何构建你自己的 `NSFastEnumeration` 协议实现。在此之前，请继续向我发送你想讨论的话题。Friday Q&A 由读者提交的内容驱动，所以如果你有想在这里讨论的话题，[请发过来](mailto:mike@mikeash.com)！下周已经被预约了，但之后的时间是开放的。

你喜欢这篇文章吗？我卖整本的书！卷 II 和卷 III 现已上市！提供 ePub、PDF、印刷版，以及在 iBooks 和 Kindle 上阅读。[点击此处获取更多信息](http://www.mikeash.com/book.html)。

---

评论：

---

[本页评论 RSS 源](http://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-04-09-comparison-of-objective-c-enumeration-techniques.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。

代码语法高亮由 [Pygments](http://pygments.org/) 提供。
