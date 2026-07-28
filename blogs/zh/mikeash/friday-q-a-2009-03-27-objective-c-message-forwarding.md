---
title: 'Friday Q&A 2009-03-27：Objective-C 消息转发'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-03-27-objective-c-message-forwarding.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:13664c1b4e8f69f3'
translated: true
---

> 原文：[Friday Q&A 2009-03-27: Objective-C Message Forwarding](https://www.mikeash.com/pyblog/friday-qa-2009-03-27-objective-c-message-forwarding.html)　·　mikeash.com Friday Q&A

发表于 2009-03-27 16:50 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2009-04-03：暂停](https://www.mikeash.com/pyblog/friday-qa-2009-04-03-on-hold.html)  
上一篇：[Friday Q&A 2009-03-20：Objective-C 消息传递](https://www.mikeash.com/pyblog/friday-qa-2009-03-20-objective-c-messaging.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2009-03-27：Objective-C 消息转发

作者：[Mike Ash](https://www.mikeash.com/)

本文也有[中文版（neoman 翻译）](https://github.com/0oneo/iOSArchive/wiki/%E7%BF%BB%E8%AF%91-Objective-C-Message-Forwarding)。

**没有这样的方法**  
 [上周](https://www.mikeash.com/pyblog/friday-qa-2009-03-20-objective-c-messaging.html)我讨论了 Objective-C 消息传递的工作原理，并提到当给定选择器找不到方法时会发生一些有趣的事情。正是这些有趣的事情导致了转发。

（如果你对**选择器（selector）** 到底是什么，或者**方法**和**消息**之间的区别不太清楚，你可能想快速读一下那篇文章，或者至少重新读一下其中的「定义」部分。）

什么是消息转发？简单来说，它允许未知消息被捕获并作出反应。换句话说，每当一条未知消息被发送时，它会被打包成一个优美的包裹发送给你的代码，然后你就可以对它做任何想做的事情。

这种机制极其强大，可以实现各种巧妙、聪明的功能。

现在你可能在想，「为什么它叫_转发_？」对未知消息作出任意响应和「转发」之间似乎没有太大联系。其原因是，这种技术主要旨在允许对象让其他对象为它们处理消息，因此称为「转发」。

**发生了什么**  
 当你执行 `[foo bar]` 而 `foo` 没有实现 `bar` 方法时会发生什么？当它_确实_实现了这样一个方法时，过程很直接：它查找相应的方法，然后跳转到它。当找不到这样的方法时，就会发生一系列复杂的事件：

1. **惰性方法决议。** 这是通过向目标类发送 `resolveInstanceMethod:`（类方法则发送 `resolveClassMethod:`）来完成的。如果该方法返回 YES，则假定相应的方法已经被添加，消息发送会重新开始。
2. **快速转发路径。** 这是通过向目标发送 `forwardingTargetForSelector:`（如果它实现了此方法）来完成的。如果它实现了此方法并返回了除 `nil` 或 `self` 之外的值，则整个消息发送过程会以该返回值作为新目标重新开始。
3. **常规转发路径。** 首先运行时将发送 `methodSignatureForSelector:` 来查看参数和返回值类型。如果返回了一个方法签名，运行时就会创建一个描述正在发送消息的 `NSInvocation`，然后向对象发送 `forwardInvocation:`。如果找不到方法签名，运行时就会发送 `doesNotRecognizeSelector:`。

**惰性决议**  
 正如我们上周所学，运行时通过查找方法（即 `IMP`）然后跳转到它来发送消息。有时动态地将 IMP 插入到一个类中，而不是预先全部设置好，会很有用。这样做可以实现非常快速的「转发」，因为方法被决议后，它将作为正常消息发送过程的一部分被调用。当然，缺点是这种方案不够灵活，因为你需要准备好一个 IMP 来插入，而这意味着你需要预先预料到将要到来的参数和返回类型。

这种方法对于 `@dynamic` 属性之类的东西非常适用。方法签名是你应该预先知道的：要么带一个参数并返回 void，要么没有参数并返回一个值。值的类型会变化，但你可以覆盖常见情况。由于 IMP 会收到发送给对象的选择器，它可以使用该选择器获取属性的名称并进行动态查找。通过 `+resolveInstanceMethod:` 将其插入到类中即可。

**快速转发**  
 接下来运行时要做的是检查你是否希望将整个未更改的消息发送给另一个对象。由于这是转发的常见情况，这样可以以最小的开销完成。

出于某种原因，快速转发的文档非常糟糕。除了 `NSObject.h` 中被注释掉的声明外，Apple 唯一提到它的地方是在 [Leopard 发行说明](http://developer.apple.com/ReleaseNotes/Cocoa/Foundation.html)中。（搜索 "New forwarding fast path"）。

这种技术非常适合模拟多重继承。你可以编写一个像这样的小覆盖：

```
    - (id)forwardingTargetForSelector:(SEL)sel { return _otherObject; }
```

这将导致任何未知消息被发送给 `_otherObject`，从而使你的对象从外部看起来就像是将你的对象和这个其他对象合并在了一起。

**常规转发**  
 前两种基本上只是优化，使转发更快。如果你不利用它们，完整的转发机制就会启动。这会创建一个 `NSInvocation` 对象，它完整地封装了正在发送的消息。它持有目标、选择器和所有参数。它还允许对返回值进行完全控制。

在运行时能够构建 `NSInvocation` 之前，它需要一个 `NSMethodSignature`，因此它通过 `-methodSignatureForSelector:` 请求一个。这是 Objective-C 的 C 语言血统所要求的。为了将参数打包到 `NSInvocation` 中，运行时需要知道参数的类型和数量。这些信息通常不会在 C 运行时环境中提供，因此它必须绕开 C 的「字节包」世界观，以另一种方式获取这些类型信息。

一旦构建好调用，运行时就会调用你的 `forwardInvocation:` 方法。从那里开始，你可以对传给你的调用做任何想做的事情。可能性是无限的。

这里有一个快速示例。假设你已经厌倦了编写循环，因此希望能够更直接地操作数组。给 `NSArray` 添加这个小分类（category）：

```
    @implementation NSArray (ForwardingIteration)
    
    - (NSMethodSignature *)methodSignatureForSelector:(SEL)sel
    {
        NSMethodSignature *sig = [super methodSignatureForSelector:sel];
        if(!sig)
        {
            for(id obj in self)
                if((sig = [obj methodSignatureForSelector:sel]))
                    break;
        }
        return sig;
    }
    
    - (void)forwardInvocation:(NSInvocation *)inv
    {
        for(id obj in self)
            [inv invokeWithTarget:obj];
    }
    
    @end
```

然后你可以编写像这样的代码：

```
    [(NSWindow *)windowsArray setHidesOnDeactivate:YES];
```

我不推荐编写这样的代码。问题在于，转发不会捕获 NSArray 已经实现的任何方法，因此你最终只能捕获一部分方法。一个更好的方法是编写一个继承自 `NSProxy` 的 trampoline（中介）类。

`NSProxy` 基本上就是专门设计用于代理的类。它只实现了最小的方法子集，其余所有方法都留待处理。这意味着一个实现了转发的子类基本上可以捕获任何消息。

要使用 `NSProxy` 来做这类事情，你需要编写一个继承自 `NSProxy` 的子类，它可以被初始化以指向一个数组，然后在 `NSArray` 中添加一个返回代理新实例的桩方法，如下所示：

```
    @implementation NSArray (ForwardingIteration)
    - (id)do { return [MyArrayProxy proxyWithArray:self]; }
    @end
```

然后你可以像这样使用它：

```
    [[windowsArray do] setHidesOnDeactivate:YES];
```

编写 trampoline 来捕获消息并让它们执行有趣操作的整个领域已经被充分探索过，并被命名为[高阶消息传递（Higher-Order Messaging）](http://cocoadev.com/index.pl?HigherOrderMessaging)。我不会在这篇文章中深入探讨它的更多细节，但已经有很多很酷的东西了。

**声明**  
 Objective-C 的 C 语言血统的另一个后果是，编译器需要知道你代码中将要发送的每条消息的完整方法签名，即使是纯粹转发的消息。举一个刻意设计的例子，假设编写一个使用转发通过代码来生成整数的类，这样你就可以编写：

```
    int x = [converter convert_42];
```

这显然不是很实用，但你确实可以做到。这种技术有更实用的变体。

问题在于，编译器不知道任何 `convert_42` 方法，因此它不知道它返回什么类型的值。它会给你一个恼人的警告，并假定它返回 `id`。解决方法很简单，只需在某处声明它：

```
    @interface NSObject (Conversion)
    - (int)convert_42;
    - (int)convert_29;
    @end
```

再次说明，这样做显然不太实用，但在你有更实际的转发情况时，这可以帮助你与编译器和平共处。例如，如果你使用转发来模拟多重继承，可以使用分类（category）声明另一个类的所有方法也适用于这个多重继承类。这样编译器就知道它同时拥有两组方法。一组通过转发处理，但这对于编译器来说无关紧要。

**结论**  
 消息转发是一种强大的技术，极大地增强了 Objective-C 的表达能力。Cocoa 在 NSUndoManager、分布式对象等场景中使用了它，它也可以让你在自己的代码中实现许多巧妙的功能。

本周的 Friday Q&A 到此结束。下周请继续收看更多引人入胜的编程故事，并在下方留下你对本期内容的评论。

Friday Q&A 的内容由你的创意驱动。如果你有一个希望在这里讨论的想法，请在评论中发表或[e-mail 直接发送](mailto:mike@mikeash.com)。除非你特别要求，否则我会使用你的名字。

喜欢这篇文章吗？我正销售收录了这些文章的整套书籍！第二卷和第三卷现已出版！提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击此处获取更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-03-27-objective-c-message-forwarding.html)

添加你的想法，发表评论：

垃圾邮件和离题内容将被删除，恕不另行通知。违规者可能会根据我个人的判断被公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
