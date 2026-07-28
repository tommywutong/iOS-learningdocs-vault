---
title: 'Friday Q&A 2009-05-22：Objective-C 类的加载与初始化'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-05-22-objective-c-class-loading-and-initialization.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:995965bbab35039c'
translated: true
---

> 原文：[Friday Q&A 2009-05-22: Objective-C Class Loading and Initialization](https://www.mikeash.com/pyblog/friday-qa-2009-05-22-objective-c-class-loading-and-initialization.html)　·　mikeash.com Friday Q&A

发表于 2009-05-23 00:37 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)
下一篇文章：[Friday Q&A 2009-06-05：Valgrind 入门](https://www.mikeash.com/pyblog/friday-qa-2009-06-05-introduction-to-valgrind.html)
上一篇文章：[使用 NSOperationQueue](https://www.mikeash.com/pyblog/use-nsoperationqueue.html)
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2009-05-22：Objective-C 类的加载与初始化

作者：[Mike Ash](https://www.mikeash.com/)

类在 Objective-C 中到底是如何被加载到内存里的，你作为程序员大多数时候完全不需要操心。它是一大堆复杂的事情，由运行时链接器（linker）处理，在你的代码开始运行之前老早就完成了。

对大部分类来说，知道这些就够了。但有些类需要做更多的事情——真正运行一些代码来完成某种设置。一个类可能需要初始化一个全局表、从用户默认设置中缓存一些值，或者执行任意数量的其他任务。

Objective-C 运行时提供了两个方法来提供这种功能：`+initialize` 和 `+load`。

**+load**
如果类实现了 `+load`，它会在该类实际被加载时被调用。这发生得非常早。如果你在 App 中，或者在 App 所链接的某个框架中实现了 `+load`，`+load` 会在 `main()` 之前运行。如果你是在一个可加载的束（loadable bundle）中实现的 `+load`，那么它会在该束的加载过程中运行。

使用 `+load` 可能很棘手，因为它运行得太早了。显而易见，有些类必须先于其他类被加载，所以你无法确定其他的类是否已经调用过 `+load`。比这更糟的是，你的 App（或框架、插件）中的 C++ 静态初始化器（static initializer）那时也还没有运行，因此如果你运行了任何依赖那些静态初始化器的代码，很可能会崩。好消息是，你所链接的框架保证已经全部加载完毕，所以可以安全地使用框架中的类。你的超类（superclass）也保证已经完全加载，因此也可以安全地使用。请记住，在加载时（通常）没有自动释放池（autorelease pool），所以如果你要调用 Objective-C 的东西，需要把代码包裹在一个自动释放池里。

`+load` 的一个有趣特性是，运行时对它做了特殊处理：在分类（category）以及主类中实现的 `+load` 都会被调用。这意味着，如果你在一个类和它的某个分类里都实现了 `+load`，那么两者都会被调用。这大概会颠覆你对分类运作机制的全部认知，但那是因为 `+load` 不是一个普通的方法。这个特性使得 `+load` 成为一个进行诸如方法调配（method swizzling）之类“邪恶勾当”的上佳场所。

**+initialize**
`+initialize` 方法会在一个更合理的环境中被调用，通常比 `+load` 更适合放置代码。`+initialize` 的有趣之处在于它是惰性调用的，甚至可能根本不会被调用。一个类初次加载时，并不会调用 `+initialize`。当有消息发送给某个类时，运行时会先检查它的 `+initialize` 是否已经被调用过。如果没有，就会在继续发送消息之前先调用它。概念上，你可以把它理解为像这样工作：

```
    id objc_msgSend(id self, SEL _cmd, ...)
    {
        if(!self->class->initialized)
            [self->class initialize];
        ...send the message...
    }
```

当然，由于线程安全和许多其他有趣的事情，实际情况远比这复杂，但基本思想就是这样。`+initialize` 每个类只会发生一次，并且就发生在该类第一次收到消息的时候。和 `+load` 一样，`+initialize` 也一定会先发送给一个类的所有超类，然后才发送给该类本身。

这使得 `+initialize` 使用起来更安全，因为它通常会在一个友好得多的环境中被调用。环境具体怎么样，取决于第一次消息发送的确切时机，但几乎可以肯定，至少是在你调用 `NSApplicationMain()` 之后。

因为 `+initialize` 是惰性运行的，所以它显然不适合用来放置注册一个本来不会被用到的类的代码。例如，`NSValueTransformer` 或 `NSURLProtocol` 的子类就不能用 `+initialize` 来向它们的超类注册自己，因为这会制造一个先有鸡还是先有蛋的局面。

不过，就类加载这个方面而言，对于几乎其他所有事情，它都是一个好地方。它在友好得多的环境中运行，意味着你可以更自在地写代码；它惰性运行，意味着在你的类实际被用到之前，你不会浪费资源去安排它。

关于 `+initialize` 还有一个技巧。在我上面的伪代码里，我写的是运行时执行 `[self->class initialize]`。这意味着正常的 Objective-C 消息分发规则也会适用，如果这个类没有实现它，那么超类的 `+initialize` 就会被运行。实际情况正是如此。因此，你应该始终把你的 `+initialize` 方法写成这个样子：

```
   + (void)initialize
    {
        if(self == [WhateverClass class])
        {
            ...perform initialization...
        }
    }
```

如果没有这个额外的检查，假如你有一个没有实现自己的 `+initialize` 方法的子类，你的初始化代码就可能会运行两次。这绝非空穴来风，即便你自己没有写任何子类也是如此。Apple 的键值观察（Key-Value Observing）就会创建[动态子类](http://www.mikeash.com/?page=pyblog/friday-qa-2009-01-23.html)，而这些子类并不会重写 `+initialize`。

**结论**
Objective-C 提供了两种自动运行类设置代码的方式。`+load` 方法保证会在类一被加载时就非常早地运行，适用于那些也必须非常早运行的代码。这也使得它很危险，因为运行它的环境不太友好。

对于大多数设置任务，`+initialize` 方法要好得多，因为它惰性运行，且处在一个良好的环境中。你几乎可以在这里做任何你想做的事，只要它不需要在某一个外部实体（entity）给你的类发消息之前发生就行。

以上就是本周的 Friday Q&A。下周请再来，迎接又一期激动人心的内容。同往常一样，请把建议[发邮件](mailto:mike@mikeash.com)告诉我，或者留在下方。没有你们用宝贵创意做出的贡献，Friday Q&A 就无法运转，所以今天就请把你的建议发过来吧！

喜欢这篇文章吗？我正在出售整本都是这类文章的书！第二卷和第三卷现已出版！它们提供 ePub、PDF、印刷版，并且在 iBooks 和 Kindle 上均有上架。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-05-22-objective-c-class-loading-and-initialization.html)

添加你的想法，发表评论：

垃圾评论和离题帖子将被删除，恕不另行通知。违规者可能由我单方面决定予以公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
