---
title: 分类与 +load
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2009/03/Categories-and-load/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:360a450f63695bbe'
translated: true
---

> 原文：[Categories and +load](https://belkadan.com/blog/2009/03/Categories-and-load/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Subversion Checksum Problems](https://belkadan.com/blog/2009/03/Subversion-Checksum-Problems/)

[Const Correctness](https://belkadan.com/blog/2009/03/Const-Correctness/) »

« [Alerts Without Apps (or nibs)](https://belkadan.com/blog/2008/03/Alerts-Without-Apps/?tag=cocoa)

[Safer Plugin Categories](https://belkadan.com/blog/2009/04/Safer-Plugin-Categories/?tag=cocoa) »

« [Objective-J and Objective-C](https://belkadan.com/blog/2008/09/Objective-J-and-Objective-C/?tag=objective-c)

[Safer Plugin Categories](https://belkadan.com/blog/2009/04/Safer-Plugin-Categories/?tag=objective-c) »

## [分类与 +load](#)

如果你写过 Cocoa 插件，不管是不是官方认可的那种，大概都琢磨过分类（category）。琢磨过怎么靠它给现有的类变魔术般地加方法……如果够小心，甚至能替换掉现有的方法。但有几个限制：你没法调用原来的实现，而且如果别人也在对同一个方法做同样的事，最后只有一边能生效。所以往好里说，这也就算是个下下策。

好吧，今天我心不在焉地翻着 GCC 对 C 语言的扩展，读到了[这么一段](http://gcc.gnu.org/onlinedocs/gcc-4.3.3/gcc/Executing-code-before-main.html)：

> `+load` 是一个不会被分类覆盖的方法。如果一个类和它的某个分类都实现了 `+load`，两个方法都会被调用。这样就能在分类里额外做一些初始化工作。

哇！分类居然有自己的 `+load` 方法？这不就跟每个类都有自己的 `+initialize`一样嘛！有了这个,你就能安全地用分类给现有方法加功能了：

1. 起一个不太可能撞车的前缀，新建一个方法：`-(id)ComBelkadan_valueForKey:(NSString *)key`。
2. 让这个方法在本该调用原始方法的地方，改为调用它自己。
3. 在 `+load` 里，把这两个方法的实现互换（用类似 [JRSwizzle](http://rentzsch.com/trac/wiki/JRSwizzle) 的手段）。

这样一来,如果之后又有别人做了同样的事,这些方法就会依次串联起来,最终按预期调用到原始实现。之前有人用过这一招吗,还是根本没人知道?(还有,另一个编译器 [Clang/LLVM](http://clang.llvm.org/) 会不会提供同样的功能?)

记住,在 `+load` 里[能做的事非常有限](http://gcc.gnu.org/onlinedocs/gcc-4.3.3/gcc/What-you-can-and-what-you-cannot-do-in-_002bload.html#What-you-can-and-what-you-cannot-do-in-_002bload)。但上面说的这点事还是能做到的。(而且既然我们说的是插件里的分类,那多半可以假定应用其余部分和各个框架反正都已经加载完了。)

GCC 的语言扩展里还有不少有意思的东西。就算你最终用不上,翻一翻也挺好玩的。

本文发布于 [2009](https://belkadan.com/blog/2009) 年 [3](https://belkadan.com/blog/2009/03) 月 19 日，归类于 [技术](https://belkadan.com/blog/technical)。标签：[Cocoa](https://belkadan.com/blog/tags/cocoa)、[Objective-C](https://belkadan.com/blog/tags/objective-c)
</content>
