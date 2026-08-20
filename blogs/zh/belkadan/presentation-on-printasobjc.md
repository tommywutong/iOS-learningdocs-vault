---
title: PrintAsObjC 演讲
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2019/09/Presentation-on-PrintAsObjC/'
original_language: en
published: 2019-09-13
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:cae608253ebed792'
translated: true
---

> 原文：[PrintAsObjC 演讲](https://belkadan.com/blog/2019/09/Presentation-on-PrintAsObjC/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [\> 向东走](https://belkadan.com/blog/2019/08/go-east/)

[Queue, Queeu, Quuee](https://belkadan.com/blog/2019/09/Queue-Queeu-Quuee/) »

« [自动引用计数](https://belkadan.com/blog/2011/06/Automatic-Reference-Counting/?tag=objective-c)

[Objective-Rust](https://belkadan.com/blog/2020/08/Objective-Rust/?tag=objective-c) »

« [SIGWINCH](https://belkadan.com/blog/2014/12/SIGWINCH/?tag=humor)

[Queue, Queeu, Quuee](https://belkadan.com/blog/2019/09/Queue-Queeu-Quuee/?tag=humor) »

## [PrintAsObjC 演讲](#)

我正在就 Swift 编译器中一个相当友好的内部组件 PrintAsObjC 做演讲，

!["我们有……导入（Pier 1）！类（在教室里）！协议（通过 C-3PO）！分类（来自数学）！枚举（等等，那只是台 eMac）！以及，函数（即将推出）！"](https://belkadan.com/blog/2019/09/Presentation-on-PrintAsObjC/slide.jpg)

而且，在必须公开讲解之前先把它整理干净，正是做演讲的绝佳动力。

如果你好奇“即将推出”指的是什么：我们已经非常接近了！不过仍需要有人负责讨论和提案，敲定最后几个问题。（还要在非 ObjC 平台上正确实现这些限制。）参见 [https://forums.swift.org/t/best-way-to-call-a-swift-function-from-c/9829/6](https://forums.swift.org/t/best-way-to-call-a-swift-function-from-c/9829/6)。

本演讲还特别感谢 [Pitiphong P.](https://pitiphong.me) 对 availability 支持所做的贡献。:-)

_最初发表于 [Twitter](https://twitter.com/UINT_MIN/status/1172715722838904832)。_

本文发布于 [2019 年 9 月](https://belkadan.com/blog/2019/09) [13 日](https://belkadan.com/blog/2019)，归类于 [技术](https://belkadan.com/blog/technical)。标签：[Objective-C](https://belkadan.com/blog/tags/objective-c)、[幽默](https://belkadan.com/blog/tags/humor)、[社交媒体导入](https://belkadan.com/blog/tags/social-media-import)
