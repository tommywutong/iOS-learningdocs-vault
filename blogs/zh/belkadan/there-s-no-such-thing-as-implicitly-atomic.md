---
title: '不存在“隐式原子”这种东西'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2023/10/Implicity-Atomic/'
original_language: en
published: 2023-10-04
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ae664df2d890a1dd'
translated: true
---

> 原文：[There's No Such Thing As "Implicitly Atomic"](https://belkadan.com/blog/2023/10/Implicity-Atomic/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [如何在 C 中引用魔数常量](https://belkadan.com/blog/2023/07/Magic-Constants-in-C/)

[数量级的软边界](https://belkadan.com/blog/2023/10/Soft-Orders-of-Magnitude/) »

« [用 Swift 从经典 Mac OS 中抢救文件！](https://belkadan.com/blog/2023/01/Rescuing-Files-with-Swift/?tag=swift)

[GitMounter](https://belkadan.com/blog/2023/11/GitMounter/?tag=swift) »

« [Mac OS 9 上的 Swift](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/?tag=compilers)

[CellLVM](https://belkadan.com/blog/2023/12/CellLVM/?tag=compilers) »

## [不存在“隐式原子”这种东西](#)

> 如果我有一个按机器字大小对齐的变量（Int），并在线程 A 中向它写入，那么我知道线程 B 可能看到旧值而不是新值（因为每个处理器有自己的缓存，或者编译器把一次加载“提升”到了函数中更早的位置）。但在现代处理器上，线程 B 不可能看到新旧值的混合，对吧？只有更宽的值或者未对齐的值，代码才可能以非原子方式更新它们，对吧？

_这个问题改写自 Swift 论坛，不过我没有附上链接，因为它位于一个更长讨论串的中间，而且无论如何，这都是人们可能合理提出的问题。下面是我略作编辑的回答；内容以 Swift 为主，但同样适用于 C、C++ 和 Rust。_

我同意，在这种情况下出现新旧值混合的“撕裂”值非常不可能。据我所知，所有现代处理器都保证：读取或写入按机器字大小对齐的值会作为一个整体发生，也就是不会“撕裂”。不过，你忽略了一种可能：实际发生的事情并不只是“读取内存”和“写入内存”。最简单的例子是，这个机器字大小的值可能是实例变量、全局变量或静态变量；此时 Swift 的[动态独占性检查](https://www.swift.org/blog/swift-5-exclusivity/)会介入，并可能发出错误。

_编辑：连这一点也_没有保证。如果你没有声明“atomic”，编译器可能为了速度或代码大小而决定拆分一次存储！这并非假设，[Greg Parker 在 libobjc 中就遇到过这种情况。](https://discuss.systems/@gparker/111179798868336840)

不过，让我们假设你正通过 UnsafePointer 直接访问；这是 Swift 中最接近发出单条对齐加载或存储指令的做法。这样就能保证你上面描述的行为吗？不能，仍然没有保证。事实上，今天就有一个立即破坏这种假设的办法：启用 [Thread Sanitizer](https://www.swift.org/blog/tsan-support-on-linux/)。^[1](#fn:tsan)（要告诉 Thread Sanitizer 其他线程读取陈旧值没有问题，需要使用[宽松](https://en.cppreference.com/w/cpp/atomic/memory_order#Relaxed_ordering)原子操作。不过，根据你想实现的目标，请注意[即使这样也可能不够](https://www.cl.cam.ac.uk/~pes20/cpp/notes42.html)。^[2](#fn:oota)）

也许你会说，Thread Sanitizer 是人为构造的场景，不能算数？对于可移植、面向未来的代码来说，_这仍然不够。_ 操作系统、硬件或其他任何部分都可以跟踪有关内存的附加信息。事实上，我们知道大多数操作系统确实会逐页做这类事情，以支持权限保护和虚拟内存。因此，理论上它可以为每个程序执行类似 TSan 的操作，把页面或页面子区域标记为“与线程关联”，并出于性能和正确性考虑，捕获任何跨线程访问它们的尝试。默认对每个进程启用这种机制，听起来会带来离谱的工作量和开销；但 [arm64e 确实存在](https://developer.apple.com/documentation/security/preparing_your_app_to_work_with_pointer_authentication)，即使它只用于有限场景。其他以内存安全为重点的 ABI 或架构，例如 [CHERI](https://faultlore.com/blah/fix-rust-pointers/#cheri)，也确实存在。^[3](#fn:cheri) 所以，即使今天主流的^[4](#fn:edit) x86_64 和 arm64 处理器及操作系统没有做类似的事情，我也不会说它不可能发生。

最后，[未定义行为就是未定义](https://blog.regehr.org/archives/213)。我不想把未定义行为说成会故意制造错误答案的_妖魔_，但编译器完全有权说：“我可以证明这次加载与那次存储发生竞争，因此我想加载_任何值都可以_。”（通常，当编译器认为某组条件不可能同时发生时，就会出现这种情况；于是它选择节省代码大小，而不是生成那些“本应”永远不会执行的代码。）

所以，不要在 Swift 中使用单次非原子的机器字加载或存储，在没有任何其他同步机制的情况下跨线程通信。C 和 Rust 也一样。

1. 尴尬的是，这篇博客指向 Apple TSan 页面链接已经失效，因为 Apple 后来重新组织了开发者文档的这一部分。新文档又没有一个方便直接链接的页面。不过，第三方关于在 Xcode 中使用 TSan 的讲解有_很多_，命令行下配合 C 或 C++ 使用 TSan 的资料也很丰富，甚至还有少量 Rust 相关资料。[↩︎](#fnref:tsan)
2. 感谢 [zwarich](https://hachyderm.io/@zwarich/111179409269235025) 指出这一点。原子操作很难，因为 C、Swift 和 Rust 为追求极致速度，暴露了极其微妙的操作。[↩︎](#fnref:oota)
3. 我本可以直接链接到 [CHERI 官方网站](https://www.cl.cam.ac.uk/research/security/ctsrd/cheri/)，但 Gankra 的解释简洁得多，也友好得多。[↩︎](#fnref:cheri)
4. 为了[满足 Gankra](https://toot.cat/@Gankra/111179049210895080)，添加了“主流”一词。（谢谢。）[↩︎](#fnref:edit)

本文发布于 [2023 年 10 月](https://belkadan.com/blog/2023/10) [04 日](https://belkadan.com/blog/2023)，归档于[技术](https://belkadan.com/blog/technical)分类。标签：[Swift](https://belkadan.com/blog/tags/swift)、[编译器](https://belkadan.com/blog/tags/compilers)
