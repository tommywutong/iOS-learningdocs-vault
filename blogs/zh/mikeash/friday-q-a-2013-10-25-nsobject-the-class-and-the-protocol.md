---
title: 'Friday Q&A 2013-10-25：NSObject：类与协议'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-10-25-nsobject-the-class-and-the-protocol.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c88a245fdf68551b'
translated: true
---

> 原文：[Friday Q&A 2013-10-25: NSObject: the Class and the Protocol](https://www.mikeash.com/pyblog/friday-qa-2013-10-25-nsobject-the-class-and-the-protocol.html)　·　mikeash.com Friday Q&A

发表于 2013-10-25 13:27 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[VoodooPad 收购案](https://www.mikeash.com/pyblog/voodoopad-acquisition.html)  
上一篇：[Friday Q&A 2013-10-11：为什么寄存器快而 RAM 慢](https://www.mikeash.com/pyblog/friday-qa-2013-10-11-why-registers-are-fast-and-ram-is-slow.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2013-10-25：NSObject：类与协议

作者：[Mike Ash](https://www.mikeash.com/)

本文另有[中文版（neoman 译）](https://github.com/0oneo/iOSArchive/wiki/%E7%BF%BB%E8%AF%91-NSObject%EF%BC%9Athe-Class-and-the-Protocol)。

**命名空间**  
首先来看看这两个同名的实体是_如何_共存的。Objective-C 中的类和协议处于完全独立的命名空间（namespace）里。一个类和一个协议在语言层面毫无关联，却可以有相同的名字。`NSObject` 就是这种情况。

从语言本身来看，不存在可以不加区分地使用类名或协议名的位置。类名可以用作消息发送的目标、用在 `@interface` 声明里，或用作类型名。协议能用在其中一些相同的位置上，但方式总是不同。因此，两者同名并不会带来歧义。

**根类**  
作为类的 `NSObject` 是一个根类（root class）。根类是类层次结构最顶端的类，也就是说它没有超类。与 Java 这类语言不同，Objective-C 中可以存在不止一个根类。

Java 只有一个根类 `java.lang.Object`，其他所有类都直接或间接继承自它。正因如此，Java 代码可以确信遇到的任何对象都实现了 `java.lang.Object` 中的基本方法。

Cocoa 有多个根类。除了 `NSObject`，还有 `NSProxy` 以及其他一些形形色色的根类。这正是 `NSObject` 协议存在的部分原因。`NSObject` 协议定义了一组基本方法，所有根类都应该实现它们。这样，代码就可以确信这些方法一定在那里。

`NSObject` 类遵循（conform to）`NSObject` 协议，这意味着 `NSObject` 类实现了这些基本方法：

```
    @interface NSObject <NSObject>
```

`NSProxy` 同样遵循 `NSObject` 协议：

```
    @interface NSProxy <NSObject>
```

`NSObject` 协议包含 `hash`、`isEqual:`、`description` 等方法。`NSProxy` 遵循 `NSObject` 这一点意味着，你仍然可以确信 `NSProxy` 的实例会实现这些基本的 `NSObject` 方法。

**关于代理的题外话**  
顺便问一句，究竟为什么会有一个 `NSProxy` 根类呢？

某些情况下，拥有一个不实现太多方法的类会很有用。顾名思义，代理（proxy）对象就是典型的适用场景。`NSObject` 类在 `NSObject` 协议之外还实现了很多东西，比如键值编码（key-value coding），而这些东西你未必想要。

构建代理对象时，目标通常是让大多数方法保持未实现，以便能用 `forwardInvocation:` 这样的方法把它们成批转发出去。派生 `NSObject` 的子类会带进一堆碍事的包袱。`NSProxy` 为你提供了一个没有那么臃肿的更简单的超类，帮助你避开这个问题。

**协议**  
`NSObject` 协议对根类有用这一点，对大多数 Objective-C 编程来说并不算多有意思，因为我们并不经常使用其他根类。不过，在你编写自己的协议时，它就变得真正好用了。假设你有这样一个协议：

```
    @protocol MyProtocol

    - (void)foo;

    @end
```

现在你有一个指向遵循该协议的对象的指针：

```
    id<MyProtocol> obj;
```

你可以让这个对象执行 foo：

```
    [obj foo];
```

但是，你不能向这个对象索要它的 `description`：

```
    [obj description]; // 协议中没有这个方法
```

也不能对它做相等性检查：

```
    [obj isEqual: obj2]; // 协议中没有这个方法
```

总之，普通对象能做的那些事，你都无法要求它去做。有时这无关紧要，但有时你确实希望能做这些事。

这正是 `NSObject` 协议发挥作用的地方。协议可以从其他协议继承。你可以让 `MyProtocol` 继承 `NSObject` 协议：

```
    @protocol MyProtocol <NSObject>

    - (void)foo;

    @end
```

这表明遵循 `MyProtocol` 的对象不仅能响应 `-foo`，还能响应 `NSObject` 协议里那些常见的消息。由于你 App 中的每个对象通常都继承自 `NSObject` 类，而该类又遵循 `NSObject` 协议，这对实现 `MyProtocol` 的人不会强加任何额外要求，同时又让你能在实例上使用这些常见方法。

**结论**  
存在两个不同的 `NSObjects` 是框架里一个古怪的角落，但深究起来是有道理的。`NSObject` 协议让多个根类都能拥有相同的基本方法，也让声明一个包含任何对象都应具备的基本功能的协议变得容易。`NSObject` 类遵循 `NSObject` 协议，把一切联系在了一起。

今天就到这里。Friday Q&A 一如既往由读者的建议驱动，如果你有希望在未来一期中看到的主题，请[发给我](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我正在销售收录这些文章的整套书！第二卷和第三卷现已出版，提供 ePub、PDF、印刷版、iBooks 和 Kindle 版本。[点击这里了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2013-10-25-nsobject-the-class-and-the-protocol.html)

分享你的想法，发表评论：

垃圾评论和离题内容将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。

代码语法高亮由 [Pygments](http://pygments.org/) 提供。
