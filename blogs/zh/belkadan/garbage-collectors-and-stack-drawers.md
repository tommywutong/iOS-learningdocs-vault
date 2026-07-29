---
title: 垃圾收集器与叠放抽屉
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2009/06/Garbage-Collectors-and-Stack-Drawers/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f07b5260f507027d'
translated: true
---

> 原文：[Garbage Collectors and Stack Drawers](https://belkadan.com/blog/2009/06/Garbage-Collectors-and-Stack-Drawers/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Z shell](https://belkadan.com/blog/2009/06/Z-shell/)

[What Happened to Dockyard?](https://belkadan.com/blog/2009/07/What-Happened-to-Dockyard/) »

« [C++ Templates are Turing-Complete](https://belkadan.com/blog/2009/05/C-plus-plus-Templates-are-Turing-Complete/?tag=programming-languages)

[Dealing with "Sandwich Code"](https://belkadan.com/blog/2011/06/Sandwich-Code/?tag=programming-languages) »

[User-Side Troubleshooting](https://belkadan.com/blog/2011/05/User-Side-Troubleshooting/?tag=mac-os-x) »

## [垃圾收集器与叠放抽屉](#)

本周的帖子包含两个简短且不相关的主题，一个有趣，一个实用。

一段时间以来，我一直在随意关注 [Parrot 虚拟机](http://www.parrot.org/)的诞生。Parrot 的目标是成为动态语言的通用虚拟机，尤其是 Perl 6，其次是 Python。（有点类似于微软的[通用语言基础设施（Common Language Infrastructure）](http://en.wikipedia.org/wiki/Common_Language_Infrastructure)，但更具动态性且开源。）作为一个对高级语言设计感兴趣的人，这里有很多很酷的东西……前提是我要懂足够的 Perl 来编写自己的前端。（你也可以用其他语言来做，包括经典的 lex-yacc/flex-bison，但会失去一些他们已为你完成的工作。）

总之，今天 Parrot 博客上有一篇关于（主要是）无锁[并发垃圾收集](http://wknight8111.blogspot.com/2009/06/concurrent-garbage-collection.html)的文章。这个想法不仅让我觉得相当惊艳，而且随着并行性变得越来越重要，它也变得越来越适用。原始技术也早在 1998 年就已发表。（背景信息是，如今 Java 和 Cocoa 中的垃圾收集器已经在单独的线程上运行，而即将推出的 Mac OS X Snow Leopard 的两个“特性”是 [Grand Central Dispatch](http://www.apple.com/macosx/technology/#grandcentral) 和 [OpenCL](http://www.apple.com/macosx/technology/#opencl)。并行性是未来的趋势。）我还没有阅读那篇文章链接的技术论文，但那里有一个非常清晰的总结，其简洁性令人惊叹。（也就是说，我大概可以在不阅读论文的情况下自己去实现最简单的那个。）

这类事情之所以酷，有两个原因：一是能实现如此巧妙的 hack，二是如果我将 Parrot 作为后端，它会帮我处理这些事情。

Parrot 的部分就此打住。总有一天我会有机会真正去摆弄它。

接下来是另一个小技巧！如果你使用 Leopard 的“叠放（Stacks）”功能，你可能会对你 Dock 中叠放的不整洁外观感到沮丧……尤其是当你的叠放全是文件夹时！幸运的是，一个解决方案已经存在好几年了：由 Yasushi Chida 制作的精美的[抽屉图标](http://www.geocities.jp/chy065/)。这些图标实际上附加在旧的 resource fork 文本剪贴片（你拖拽文本到访达时得到的内容）上。它们被巧妙（？）地命名，带有“.app”扩展名，以阻止 QuickLook 显示。

安装这些精美的抽屉图标很容易：只需将你喜欢的图标拖到你的叠放上。它们的名称已经以空格开头，因此如果按名称排序，它们会跳到叠放的最前面；并且它们的时间戳设置在将来，以处理创建日期或修改日期。（添加日期稍微复杂一些；我将在下周的帖子末尾总结我的解决方案。我这并非偷懒；它在另一台电脑上。）问题在于，当你意外（？）点击抽屉图标时，你会收到消息：“无法启动应用程序‘ System ’。”

为了解决这个问题，我改装了一个 AppleScript 应用程序，一个合法的 Mac OS X bundle 应用程序，并放入了一个简单的脚本，用于打开其所在的文件夹（本质上是模拟列表*末尾*的“在访达中显示”选项）。对于图标，我使用了 [Iconverter](http://www.versiontracker.com/dyn/moreinfo/macosx/16468)（VersionTracker 链接，开发者的网站似乎已经消失）将图标提取为 Mac OS X .icns 文件，然后将其放入模拟应用程序的 resources 目录中。（预览（Preview）可以从剪贴板拉取图标，但不能保存为 .icns。开发者应用 Icon Composer 不能从剪贴板拉取图标——我准备就此提交一个 bug。）以下是可执行脚本的核心源代码；你也可以下载[整个设置](http://belkadan.com/blog/upload/Drawer.zip)并自行修改。

```
#!/bin/bash

container=`dirname "$0"`
open "$container/../../.."
```

现在一切运行良好；没有涉及资源或过时的格式，而且如果你点击抽屉图标，它会执行合理的操作。我不怎么使用叠放，就算用，也几乎总是网格视图。但这让它们更容易区分——而且在美学上也更令人愉悦。现在，如果能在网格视图中也去掉图标就好了……

本文发布于 [2009 年](https://belkadan.com/blog/2009) [6 月](https://belkadan.com/blog/2009/06) 26 日，归类于 [技术](https://belkadan.com/blog/technical)。标签：[编程语言](https://belkadan.com/blog/tags/programming-languages)，[Mac OS X](https://belkadan.com/blog/tags/mac-os-x)
