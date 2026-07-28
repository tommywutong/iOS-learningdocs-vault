---
title: 'Friday Q&A 2017-09-22：Swift 4 弱引用'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2017-09-22-swift-4-weak-references.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:35fd443bc426dd0d'
translated: true
---

> 原文：[Friday Q&A 2017-09-22：Swift 4 弱引用](https://www.mikeash.com/pyblog/friday-qa-2017-09-22-swift-4-weak-references.html)　·　mikeash.com Friday Q&A

发布于 2017-09-23 00:57 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2017-10-06：类型安全的 User Defaults](https://www.mikeash.com/pyblog/friday-qa-2017-10-06-type-safe-user-defaults.html)  
上一篇：[Swift 4 中最好的新特性](https://www.mikeash.com/pyblog/the-best-new-features-in-swift-4.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2017-09-22：Swift 4 弱引用

作者：[Mike Ash](https://www.mikeash.com/)

本文亦提供[中文版（邓翔翻译）](https://ddddxxx.github.io/2017/09/27/swift-4-weak-references/)。

**旧实现**  
对于已经忘记旧实现且不想阅读上一篇文章的各位，我们简要回顾一下它的工作原理。

在旧实现中，Swift 对象有两个引用计数：强引用计数和弱引用计数。当强引用计数降为零而弱引用计数仍非零时，对象会被销毁，但其内存不会被释放。这会在内存中留下一种僵尸对象，剩余的弱引用会指向它。

当加载弱引用时，运行时会检查该对象是否为僵尸。如果是，它会将弱引用置零并递减弱引用计数。一旦弱引用计数降为零，对象的内存就会被释放。这意味着，一旦所有指向僵尸对象的弱引用都被访问，僵尸对象最终会被清除。

我非常喜欢这种实现的简洁性，但它有一些缺陷。一个缺陷是僵尸对象可能会在内存中停留很长时间。对于具有大型实例的类（因为它们包含大量属性，或使用 `ManagedBuffer` 等内联分配额外内存），这可能会造成严重的浪费。

另一个问题是我在撰写旧文章后[发现的](https://bugs.swift.org/browse/SR-192)，即该实现在并发读取时不是线程安全的。哎呀！这个问题后来被修补了，但围绕它的讨论表明，实现者无论如何都想要一个更好的弱引用实现，一个对此类问题更有弹性的实现。

**对象数据**  
在 Swift 中，构成“一个对象”的数据有很多。

首先，也是最明显的，是源代码中声明的所有存储属性。这些属性可由程序员直接访问。

其次，是对象的类。它用于动态派发和 `type(of:)` 内建函数。这部分基本是隐藏的，尽管动态派发和 `type(of:)` 暗示了它的存在。

第三，是各种引用计数。除非你做了像读取对象原始内存或说服编译器让你调用 `CFGetRetainCount` 这样的不当之事，否则这些是完全隐藏的。

第四，是由 Objective-C 运行时存储的辅助信息，比如 Objective-C 弱引用列表（Objective-C 的弱引用实现会单独跟踪每个弱引用）和关联对象。

你把所有这些信息都存储在哪里？

在 Objective-C 中，类和存储属性（即实例变量）内联存储在对象的内存中。类占据第一个指针大小的块，实例变量紧随其后。辅助信息存储在外部表中。当你操作关联对象时，运行时会在一个以对象地址为键的大型哈希表中查找它。这有点慢，并且需要加锁以防止多线程访问失败。引用计数有时存储在对象的内存中，有时存储在外部表中，具体取决于你运行的 OS 版本和 CPU 架构。

在 Swift 的旧实现中，类、引用计数和存储属性都是内联存储的。辅助信息仍然存储在单独的表中。

暂且不谈这些语言实际是如何做到的，我们来问一个问题：它们*应该*怎么做？

每种方式都有权衡。存储在对象内存中的数据访问速度快，但总是占用空间。存储在外部表中的数据访问速度较慢，但对于不需要它的对象来说，占用空间为零。

这至少是 Objective-C 传统上不将引用计数存储在对象本身中的部分原因。Objective-C 引用计数是在计算机远不如现在强大、内存极其有限的时代创建的。典型的 Objective-C 程序中，大多数对象只有一个所有者，因此引用计数为 1。为存储这个始终为 `1` 的值而预留对象内存的四个字节会很浪费。通过使用外部表，常见的 `1` 值可以用条目的缺失来表示，从而减少内存使用。

每个对象都有一个类，并且会频繁访问。每个动态方法调用都需要它。这应该直接放在对象的内存中。将其存储在外部没有任何节省。

存储属性被期望是快速的。对象是否拥有它们是在编译时确定的。没有存储属性的对象即使在对象内存中存储，也可以为零分配空间，所以它们应该放在那里。

每个对象都有引用计数。并非每个对象的引用计数都不是 `1`，但这仍然相当常见，而且现在的内存也大多了。这应该放在对象的内存中。

大多数对象没有任何弱引用或关联对象。在对象的内存中为这些内容预留空间会很浪费。这些应该存储在外部。

这是正确的权衡，但很烦人。对于有弱引用和关联对象的对象来说，它们相当慢。我们该如何解决？

**旁表（side table）**  
Swift 新的弱引用实现引入了*旁表*的概念。

旁表是一块独立的内存，用于存储对象的额外信息。它是*可选*的，意味着一个对象可能有旁表，也可能没有。需要旁表功能的对象可以承担额外开销，而不需要的对象则无需付出代价。

每个对象都有一个指向其旁表的指针，而旁表也有一个指回对象的指针。然后旁表可以存储其他信息，比如关联对象数据。

为了避免为旁表预留八个字节，Swift 做了一个巧妙的优化。最初，对象的第一个字是类，下一个字存储引用计数。当一个对象需要旁表时，第二个字被重新用作旁表指针。由于对象仍然需要引用计数，引用计数被存储在旁表中。这两种情况通过在此字段中设置一个位来区分，该位指示它持有的是引用计数还是指向旁表的指针。

旁表使 Swift 能够保持旧弱引用系统的基本形式，同时修复其缺陷。弱引用现在不再像以前那样指向对象，而是直接指向旁表。

因为已知旁表很小，所以不存在为大型对象的弱引用浪费大量内存的问题，因此这个问题就消失了。这也为线程安全问题提供了一个简单的解决方案：不要抢先地将弱引用置零。由于已知旁表很小，指向它的弱引用可以保持不变，直到这些引用本身被覆盖或销毁。

我应该指出，当前的旁表实现只持有引用计数和一个指向原始对象的指针。像关联对象这样的额外用途目前还是假设性的。Swift 没有内置的关联对象功能，Objective-C API 仍然使用全局表。

这项技术潜力巨大，我们很可能在不久的将来看到类似关联对象的东西使用它。我希望这能为扩展（extension）中的存储属性（针对类类型）以及其他很棒的特性打开大门。

**代码**  
由于 Swift 是开源的，所有这些功能的代码都是可访问的。

大多数旁表相关代码可以在 [stdlib/public/SwiftShims/RefCount.h](https://github.com/apple/swift/blob/c262440e70896299118a0a050c8a834e1270b606/stdlib/public/SwiftShims/RefCount.h) 中找到。

高级别的弱引用 API，以及关于该系统的详尽注释，可以在 [swift/stdlib/public/runtime/WeakReference.h](https://github.com/apple/swift/blob/c262440e70896299118a0a050c8a834e1270b606/stdlib/public/runtime/WeakReference.h) 中找到。

关于堆分配对象如何工作的更多实现和注释，可以在 [stdlib/public/runtime/HeapObject.cpp](https://github.com/apple/swift/blob/c262440e70896299118a0a050c8a834e1270b606/stdlib/public/runtime/HeapObject.cpp) 中找到。

我链接到了这些文件的特定提交，以便来自遥远未来的读者仍然能看到我所谈论的内容。如果你想看到最新的内容，请务必在点击链接后切换到 `master` 分支或任何与你兴趣相关的分支。

**结论**  
弱引用是一项重要的语言特性。Swift 的原始实现非常巧妙并具有一些不错的属性，但也存在一些问题。通过添加一个可选的旁表，Swift 工程师得以解决这些问题，同时保留了原始实现的巧妙属性。旁表实现也为未来伟大的新功能开辟了许多可能性。

今天就到这里。欢迎再次回来聆听更多疯狂的编程相关鬼故事。在此之前，如果你有希望在这里看到的话题，请[发送过来](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我出售包含这些内容的整套书籍！第二卷和第三卷现已出版！有 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击此处获取更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2017-09-22-swift-4-weak-references.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。
