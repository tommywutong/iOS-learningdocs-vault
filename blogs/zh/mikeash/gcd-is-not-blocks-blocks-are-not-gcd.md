---
title: GCD 不是 Blocks，Blocks 不是 GCD
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/gcd-is-not-blocks-blocks-are-not-gcd.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6271459d90b7cd54'
translated: true
---

> 原文：[GCD Is Not Blocks, Blocks Are Not GCD](https://www.mikeash.com/pyblog/gcd-is-not-blocks-blocks-are-not-gcd.html)　·　mikeash.com Friday Q&A

发布于 2009-09-11 21:27 | [RSS feed](https://www.mikeash.com/pyblog/rss.py)（[全文 feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[iPhone 开发故事：一年之后](https://www.mikeash.com/pyblog/the-iphone-development-story-one-year-later.html)  
上一篇文章：[Friday Q&A 2009-09-11：Grand Central Dispatch 入门，第三部分：Dispatch Sources](https://www.mikeash.com/pyblog/friday-qa-2009-09-11-intro-to-grand-central-dispatch-part-iii-dispatch-sources.html)  
标签：[gcd](https://www.mikeash.com/pyblog/?tag=gcd) [吐槽](https://www.mikeash.com/pyblog/?tag=rant)

GCD 不是 Blocks，Blocks 不是 GCD

作者：[Mike Ash](https://www.mikeash.com/)

**Blocks**  
 Blocks 是 Apple 设计并开发的一种新的 C/C++/Objective-C 语言特性。它们最早作为 [clang 项目](http://clang.llvm.org/)的一部分向公众发布。今年夏天，以 [PLBlocks](http://code.google.com/p/plblocks/) 的形式出现了一个打包好的、支持 blocks 的编译器，而 blocks 本身在 10.6 中获得了 Apple 的官方支持。

Blocks 就是其他语言通常所说的 lambda 或闭包（closure）。它们是能够捕获封闭作用域的匿名内嵌函数，并且可以超出该封闭作用域的生命周期。本质上，它们允许编写可以传递给其他函数或模块的内联代码，而不是立即执行。

Apple 在 10.6 及以上版本中官方支持 blocks。针对 10.5 的程序如果使用 PLBlocks 也可以使用 blocks。为其他平台编写的程序如果使用 clang 编译可能也能使用 blocks，但我不确定这方面的工作状态。

**Grand Central Dispatch**  
 GCD（也称 libdispatch）是 10.6 中新增的 Mac OS X 多处理框架。其主要特性是一个高效且感知系统状态的线程池实现。“感知系统状态”意味着它会根据系统负载、计算机 CPU 核心的数量以及当前在线程池中执行的线程状态，自动动态调整池中线程的数量。GCD 还提供了其他多处理特性，例如事件系统和信号量（semaphore）。

从本周起，GCD [已经开源](http://libdispatch.macosforge.org/)。GCD 的感知系统状态功能需要内核集成，这可能使其移植到其他平台更加困难，目前 GCD 仍然是一个纯粹的 Mac OS X 10.6 库。

**为什么会混淆？**  
 阅读以上内容，我想任何人都能看出这两者是截然不同的。它们确实毫无共同之处。那么为什么大家对它们是什么会有这么多混淆呢？

答案很简单：GCD 是围绕回调构建的。你可以为事件触发、执行工作单元、取消处理程序或其他很多场景传递回调。

C 语言中的回调一直很笨拙。Blocks 让回调变得更容易使用。由于 GCD 如此重度依赖回调，解决方案很简单：给 GCD 添加基于 blocks 的 API。因此，你在外面看到的大多数 GCD 示例都包含了 blocks，就像 `dispatch_async` man 页面中的这个例子：

```
     dispatch_async(my_queue, ^{
             // critical section
     });
```

这种混淆是可以理解的，但理解两者之间的区别非常重要。你可以在没有 GCD 的情况下使用 blocks，事实上 10.6 中许多新的基于 blocks 的 Cocoa API 正是如此。你也可以通过每个接受 block 的 GCD 函数提供的 `_f` 变体，在没有 blocks 的情况下使用 GCD。它们配合得很好，但实际上是完全不同的技术。

现在你知道了故事的其他部分。

你喜欢这篇文章吗？我正出售整本收录了它们的书！第二卷和第三卷已经上市了！提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页面的评论 RSS feed](https://www.mikeash.com/commentsrss.py?page=pyblog/gcd-is-not-blocks-blocks-are-not-gcd.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会被我单方面公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
