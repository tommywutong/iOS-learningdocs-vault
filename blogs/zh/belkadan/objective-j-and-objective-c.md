---
title: Objective-J 与 Objective-C
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2008/09/Objective-J-and-Objective-C/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:fe25d93028c7fc8d'
translated: true
---

> 原文：[Objective-J and Objective-C](https://belkadan.com/blog/2008/09/Objective-J-and-Objective-C/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [HTTPS and Name-based Virtual Hosting](https://belkadan.com/blog/2008/08/HTTPS-and-Name-based-Virtual-Hosting/)

[JavaScript Tetris](https://belkadan.com/blog/2009/03/JavaScript-Tetris/) »

[Const Correctness](https://belkadan.com/blog/2009/03/Const-Correctness/?tag=programming-languages) »

[Categories and +load](https://belkadan.com/blog/2009/03/Categories-and-load/?tag=objective-c) »

## [Objective-J 与 Objective-C](#)

就在一周多前，Chris Lattner [向 Clang 邮件列表宣布](http://lists.cs.uiuc.edu/pipermail/cfe-dev/2008-August/002670.html)，Apple 正在向 C 语言添加一种名为“block”的东西。这些 block 基本上就是闭包（closure），与任何计算机科学学生在 Lisp 中使用它们的含义相同，只是加入了一些内存管理方面的额外复杂性。（具体而言，如果你想要修改 block 外部声明的变量，必须使用一个新的存储限定符 `__block`。）

今天，用于构建令人印象深刻的 [280 Slides 网络应用](http://280slides.com/) 的备受期待的“Objective-J”框架，以及一个受 Cocoa 启发（几乎是 Cocoa 的克隆）的名为 Cappuccino 的框架，[发布了](http://cappuccino.org/discuss/2008/09/04/announcing-cappuccino/)。在某些情况下，它似乎过于相似，比如包含像 `-[CPWindowController initWithWindowCibName:]` 这样的方法，其中“cib”当然代表 Cappuccino Interface Builder。（我不确定这个工具是否已经存在；我在网站上找不到任何提及。）但鉴于 GNUStep 仍然存在，而 OpenStep（我认为）仍然开放，我认为在技术上并没有发生任何版权侵权。我也想玩玩 Cappuccino，但我手头事已经够多了。

不管怎样，我觉得 block 很酷，并且希望开始使用它们，只是我试图保持向后兼容性。（不过想想警告表单（alert sheet）的回调！）Objective-J 非常酷，但我想看到一些性能指标（尽管我相信它比过度使用 AJAX 的网站要快）。

不过，我觉得有趣的是 [Objective-J 教程](http://cappuccino.org/learn/tutorials/objective-j-tutorial.php) 方法章节中的这段片段（snippet）：

> 你可能会疑惑方法的具体名称为什么重要。在 Objective-J 和 Cappuccino 中，你会遇到的一种模式是将方法作为参数传递给另一个方法。这常用于委托和事件系统中。由于方法并不像 JavaScript 那样是一等对象，我们使用一种特殊的符号来引用它们，即 `@selector`。如果我想将前面的方法作为参数传递给另一个方法，我会使用以下代码：
> 
> ```
> [fooObject setCallbackSelector: @selector(setJobTitle:company:)];
> ```
> 
> 如你所见，方法名称连同其冒号和参数标签被传递给 `@selector`。

与此同时，Objective-C（以及纯 C 语言）则获得了 block 的使用：

```
// 类似这样
[fooObject setCallback:^(NSString *title, NSString *company) {
    // do stuff
}];
```

……虽然这对绑定（bindings）没有帮助，甚至可能无法替代 target-action，但它非常适合回调。

具有讽刺意味的是，这两种语言似乎在大雾中彼此擦肩而过。就我个人而言，我终于被 block 说服了，因为它们似乎完全没有搞乱 C 语言（不像我见过的其他一些闭包语法，只在高级环境中工作）。而尽管并非总是需要将 JavaScript 函数作为一等实体使用，但实现起来似乎并不困难。也许问题仅仅是过于严格地复制了语法。*grin*

这篇文章发表于 [2008 年](https://belkadan.com/blog/2008) [9 月](https://belkadan.com/blog/2008/09) 4 日，归类于 [技术](https://belkadan.com/blog/technical)。标签：[编程语言](https://belkadan.com/blog/tags/programming-languages)、[Objective-C](https://belkadan.com/blog/tags/objective-c)
