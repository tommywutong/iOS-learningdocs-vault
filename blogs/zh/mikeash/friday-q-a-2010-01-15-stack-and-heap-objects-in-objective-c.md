---
title: 'Friday Q&A 2010-01-15：Objective-C 中的栈对象与堆对象'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-01-15-stack-and-heap-objects-in-objective-c.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ee74357400dd0d2c'
translated: true
---

> 原文：[Friday Q&A 2010-01-15：Objective-C 中的栈对象与堆对象](https://www.mikeash.com/pyblog/friday-qa-2010-01-15-stack-and-heap-objects-in-objective-c.html)　·　mikeash.com Friday Q&A

发布于 2010-01-15 21:58 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Friday Q&A 2010-01-22：Toll Free Bridging 内部原理](https://www.mikeash.com/pyblog/friday-qa-2010-01-22-toll-free-bridging-internals.html)  
上一篇文章：[Friday Q&A 2010-01-08：NSNotificationQueue](https://www.mikeash.com/pyblog/friday-qa-2010-01-08-nsnotificationqueue.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [堆](https://www.mikeash.com/pyblog/?tag=heap) [内存](https://www.mikeash.com/pyblog/?tag=memory) [栈](https://www.mikeash.com/pyblog/?tag=stack)

Friday Q&A 2010-01-15：Objective-C 中的栈对象与堆对象

作者：[Mike Ash](https://www.mikeash.com/)

在深入探讨之前，我们先定义一下术语。

**栈（Stack）**  
栈是一块内存区域，用于存储局部变量以及内部的临时值和管理信息。在现代系统中，每个执行线程（thread）都有一个栈。当函数被调用时，会向栈上压入一个_栈帧（stack frame）_，函数局部数据就存储在其中。当函数返回时，其栈帧被销毁。这一切都是自动发生的，程序员除了调用函数外无需采取任何显式操作。

**堆（Heap）**  
堆，本质上就是内存中的其他所有区域。（是的，除了栈和堆之外还有其他东西，但这里我们先忽略它们。）内存可以在堆上随时分配和销毁。你必须显式地请求从堆上分配内存，并且如果没有使用垃圾回收（garbage collection），还需要显式地释放它。堆用于存储那些需要比当前函数调用存活更久的数据。当你调用 `malloc` 和 `free` 时，访问的就是堆。

**栈对象与堆对象**  
基于以上定义，什么是栈对象，什么是堆对象？

首先，我们必须理解对象在一般情况下是什么。在 Objective-C（以及许多其他语言）中，对象就是一个具有特定布局（layout）的连续内存块。（如果你对它包含什么以及如何布局感兴趣，可以看看我的 [Objective-C 运行时入门](https://www.mikeash.com/pyblog/friday-qa-2009-03-13-intro-to-the-objective-c-runtime.html)。）

这块内存的具体位置并不那么重要。只要你在某处有满足正确内容的内存，它就是一个可用的 Objective-C 对象。在 Objective-C 中，对象通常创建在堆上：

```
    NSObject *obj = [[NSObject alloc] init];
```

变量 `obj` 自身的存储位于栈上，但它指向的对象在堆上。`[NSObject alloc]` 调用会分配一块堆内存，并将其填充成 `NSObject` 所需的布局。

栈对象就是其内存分配在栈上的对象。Objective-C 本身不直接支持这一点，但你可以手动构造一个，并不麻烦：

```
    struct {
        Class isa;
    } fakeNSObject;
    fakeNSObject.isa = [NSObject class];
    
    NSObject *obj = (NSObject *)&fakeNSObject;
    NSLog(@"%@", [obj description]);
```

这段代码可以正常工作，但你不应该依赖它，因为它依赖于复制该类的内部布局。

**栈对象的优势**  
从一般意义上说，栈对象显然是可能的。除了上面这种 hack，像 C++ 这样的真实语言在语言层面就支持栈对象。在 C++ 中，你可以在栈或堆上创建对象：

```
    std::string stackString;
    std::string *heapString = new std::string;
```

为什么两者都允许？

栈对象有两个显著的优势：

1. **速度：** 在栈上分配内存非常快。所有簿记工作都在编译程序时由编译器完成。在运行时，函数序言（prolog）只需为所有局部变量划出所需的空间，代码知道什么内容放在哪里，因为这一切都是预先计算好的。栈分配基本上是零成本的，而堆分配则可能相当昂贵。
2. **简单性：** 栈对象具有明确的生存期。你永远不会泄漏它，因为它总是在其声明的作用域结束时被销毁。

**栈对象的劣势**  
栈对象严格定义的生存期也是一个劣势，而且是主要劣势。在 Objective-C（以及 C++ 和许多其他语言）中，对象在创建后是无法移动的。原因是可能有许多指针指向该对象，而这些指针并没有被跟踪。要移动对象，就需要更新所有这些指针，但这是无法做到的。

（注：这并非绝对不可能，许多语言确实会移动对象，通常作为垃圾回收方案的一部分。但这需要比 Objective-C 更强的运行时智能和更严格的类型系统。）

在 Cocoa 中，Objective-C 使用引用计数（reference counting）系统进行内存管理。这个系统的优势在于，单个对象可以有多个“所有者”，并且系统不会允许对象在所有所有者都放弃所有权（ownership）之前被销毁。

栈分配的对象本质上只有一个所有者，即创建它的函数。如果 Objective-C 有栈对象，当把它传递给其他代码，而那段代码又试图通过 `retain` 来保留它时，会发生什么？当创建它的函数返回时，没有办法防止对象被销毁，因此 `retain` 无法生效。试图保留该对象的代码会失败，最终得到一个悬垂引用（dangling reference），然后崩溃。

另一个问题是栈对象不够灵活。在 Objective-C 中，实现一个销毁原对象并返回新对象的初始化方法并不少见。用栈对象要怎么做到这一点？实际上做不到。Objective-C 的许多运行时灵活性都依赖于堆对象。

**Objective-C 中真正的栈对象**  
事实证明，自 10.6 起，Objective-C 确实有真正官方的栈对象！

不过别太激动。它只支持一种对象：block。当你使用 `^{}` 语法在函数内编写一个 block 时，该表达式的结果就是一个栈对象！

但是，我之前讨论的那些问题呢？

运行时动态性的问题对 block 来说并不存在。Block 具有由语言固定的布局，更改它会破坏二进制兼容性。Block 对象的大小在编译时就能计算出来，实际上整个对象都是由编译器生成的代码构建的，因此编写一个做复杂事情的初始化方法的可能性根本不存在。

对象生存期的问题_确实_存在于 block 中，但没那么严重。原因很简单：block 是一种全新的、语言里之前从未有过的对象，任何处理 block 的代码都知道如果需要保留引用，它需要 `copy` 该 block（如果它不在堆上，就在堆上创建一份副本并返回指向它的指针），而不是 `retain` 它。

Block 的栈本质确实会带来一些陷阱。例如，这段代码是有问题的：

```
    void (^block)();
    if(x)
    {
        block = ^{ printf("x\n"); };
    }
    else
    {
        block = ^{ printf("not x\n"); };
    }
    block();
```

Block 栈对象在其封闭作用域的生存期内才有效，而在这里，它们所在的封闭作用域在最后调用 `block()` 之前就已经不存在了。当你将 block 传递给不知道它们是 block 的代码时，还会出现其他陷阱：

```
    [dictionary setObject: ^{ printf("hey hey\n"); } forKey: key];
```

字典会 `retain` 该 block 对象而不是 `copy` 它，导致悬垂引用。

栈对象的速度和简单性对 block 来说是一个巨大的恩惠，但也为粗心的程序员带来了一类全新的 bug。

**结论**  
本周的内容就到这里。七天后再回来，期待另一篇精彩的文章。在那之前，请[继续提出你的建议](mailto:mike@mikeash.com)。我的素材来自用户的想法，所以如果你有希望在这里讨论的话题，欢迎发送过来！

喜欢这篇文章吗？我正在出售整本合集！第二卷和第三卷现已上市！提供 ePub、PDF、印刷版以及 iBooks 和 Kindle 版本。[点击这里了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-01-15-stack-and-heap-objects-in-objective-c.html)

发表你的想法，提交评论：

垃圾邮件和无关帖子将被删除，恕不另行通知。违规者可能会被我单方面公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
