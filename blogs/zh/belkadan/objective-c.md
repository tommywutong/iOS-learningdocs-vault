---
title: Objective-C
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/tags/objective-c'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a5bd7cfad743ba5e'
translated: true
---

> 原文：[Objective-C](https://belkadan.com/blog/tags/objective-c)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

## [ARM64 反汇编中的相对引用](https://belkadan.com/blog/2022/05/ARM64-Relative-References/?tag=objective-c)

2022 年 5 月 14 日

视角：你是一个面向 arm64^[1](#fn:arm64) 的编译器，想让某段代码引用同一库中的这个全局变量。传统做法是发出一条指令来加载“X 的地址”，该地址由[动态加载器在运行时确定](https://belkadan.com/blog/2022/02/Dynamic-Linking-and-Static-Linking/)。但这并不是特别高效！首先，地址长度为 64 位，而指令只有 32 位，因此你要么将其拆分为多条指令，要么从某个*其他*位置加载地址。但更重要的是，这个全局变量*位于同一库中*。动态加载器不会把它与这段代码分开^[2](#fn:ios)，如果我们知道*它有多远*，就可以用那种方式来引用它。

这就是 `adrp` 指令的作用。

[（继续阅读…）](https://belkadan.com/blog/2022/05/ARM64-Relative-References/?tag=objective-c)

发布于 [技术](https://belkadan.com/blog/technical)。标签：[汇编](https://belkadan.com/blog/tags/assembly)、[调试](https://belkadan.com/blog/tags/debugging)、[Objective-C](https://belkadan.com/blog/tags/objective-c)

## [Objective-Rust](https://belkadan.com/blog/2020/08/Objective-Rust/?tag=objective-c)

2020 年 8 月 26 日

这又是一篇这样的文章：我做了一些荒谬的事情，然后向你展示我是如何做到的。所以我们直接开始吧。

[（继续阅读…）](https://belkadan.com/blog/2020/08/Objective-Rust/?tag=objective-c)

发布于 [技术](https://belkadan.com/blog/technical)。标签：[Objective-C](https://belkadan.com/blog/tags/objective-c)、[Rust](https://belkadan.com/blog/tags/rust)、[Swift](https://belkadan.com/blog/tags/swift)

## [关于 PrintAsObjC 的演讲](https://belkadan.com/blog/2019/09/Presentation-on-PrintAsObjC/?tag=objective-c)

2019 年 9 月 13 日

为 Swift 编译器中一个相当友好的部分——PrintAsObjC 制作一个内部演示，以及

!["我们有……导入（Pier 1）！类（在教室中）！协议（借助 C-3PO）！分类（来自数学）！枚举（等等那只是一台 eMac）！还有函数（即将推出）！"](https://belkadan.com/blog/2019/09/Presentation-on-PrintAsObjC/slide.jpg)

[（继续阅读…）](https://belkadan.com/blog/2019/09/Presentation-on-PrintAsObjC/?tag=objective-c)

发布于 [技术](https://belkadan.com/blog/technical)。标签：[Objective-C](https://belkadan.com/blog/tags/objective-c)、[幽默](https://belkadan.com/blog/tags/humor)、[社交媒体导入](https://belkadan.com/blog/tags/social-media-import)

## 历史文章

1. 2011-06-20[自动引用计数（Automatic Reference Counting）](https://belkadan.com/blog/2011/06/Automatic-Reference-Counting/?tag=objective-c)
2. 2009-04-16[更安全的插件分类（Safer Plugin Categories）](https://belkadan.com/blog/2009/04/Safer-Plugin-Categories/?tag=objective-c)
3. 2009-03-19[分类与 +load](https://belkadan.com/blog/2009/03/Categories-and-load/?tag=objective-c)
4. 2008-09-04[Objective-J 与 Objective-C](https://belkadan.com/blog/2008/09/Objective-J-and-Objective-C/?tag=objective-c)

### 可能相关的标签

- [汇编](https://belkadan.com/blog/tags/assembly)
- [Cocoa](https://belkadan.com/blog/tags/cocoa)
- [编译器](https://belkadan.com/blog/tags/compilers)
- [调试](https://belkadan.com/blog/tags/debugging)
- [幽默](https://belkadan.com/blog/tags/humor)
- [LLVM](https://belkadan.com/blog/tags/llvm)
- [编程语言](https://belkadan.com/blog/tags/programming-languages)
- [Rust](https://belkadan.com/blog/tags/rust)
- [社交媒体导入](https://belkadan.com/blog/tags/social-media-import)
- [Swift](https://belkadan.com/blog/tags/swift)
