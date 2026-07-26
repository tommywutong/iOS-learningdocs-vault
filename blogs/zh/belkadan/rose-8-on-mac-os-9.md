---
title: ROSE-8 跑在 Mac OS 9 上
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/'
original_language: en
published: 2020-05-24
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6045ba216066f83a'
translated: true
---

> 原文：[ROSE-8 on Mac OS 9](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Shallow Git Repositories](https://belkadan.com/blog/2020/04/Shallow-Git-Repositories/)

[Suffusion: Playing with Filesystems](https://belkadan.com/blog/2020/07/Suffusion/) »

« [Swift on Mac OS 9](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/?tag=swift)

[Suffusion: Playing with Filesystems](https://belkadan.com/blog/2020/07/Suffusion/?tag=swift) »

« [Swift on Mac OS 9](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/?tag=mac-os-classic)

[Rescuing Files From Classic Mac OS...with Swift!](https://belkadan.com/blog/2023/01/Rescuing-Files-with-Swift/?tag=mac-os-classic) »

« [Introducing the Game 'by Color](https://belkadan.com/blog/2020/02/ROSE-8-Game-by-Color/?tag=rose-8)

## [ROSE-8 跑在 Mac OS 9 上](#)

[![](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/meme.png)](https://knowyourmeme.com/memes/ah-shit-here-we-go-again)

距离我今年的愚人节项目（不是整蛊！）——成功[让一个 Swift 程序跑在 Mac OS 9 上](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/)——已经快两个月了。我至今依然为那次技术上的成果_以及_那篇博客文章感到自豪。但当我做完那件事之后……我并不想就此_停下。_

有几件事是我一直想做的。首先，这里面有一小部分确实是有用的工作：为了做到我那个最小可行的、能和 C 互操作的产品，我把 Swift 标准库砍掉了相当大一部分。这对那些想在受限环境（比如嵌入式代码）里写 Swift 的人来说依然有用，也有人鼓励我把这方面的发现写出来。（我也打算这么做。）但更重要的是，虽然 [BitPaint](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/#whats-the-goal) 是个很棒的概念验证，它其实并没怎么用到 Swift。它说到底_就是_ C 互操作而已。那么，我能做点什么才能真正有点_ Swift_ 项目的味道呢？

那不如试试我今年的_另一个_没什么用的项目，[ROSE-8](https://belkadan.com/blog/2020/01/ROSE-8/) 和 [Game 'by Color](https://belkadan.com/blog/2020/02/ROSE-8-Game-by-Color/)？一个我自己设计的虚构游戏系统，跑在我学编程时用的操作系统上？_完美。_

结果这变成了，呃，相当大的工作量。

### 运行时需求

ROSE-8 其实并没有用到太多复杂的 Swift 特性……但它当然还是依赖标准库，具体来说是 Swift 那种平平无奇、可变长、写时复制的 Array。要处理好 Array，就得妥善处理

- 类的分配与保留计数
- 泛型类型
- 没有被完全优化掉的泛型实现

这一切都需要真正的_运行时_支持。^[1](#fn:runtime) 在正常的 Swift 里，运行时是用 C++ 写的，链接进标准库。虽然我已经[让 Clang 能为 Mac OS 9 生成代码](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/#modern-compiler-classic-linker)，但 C++ 有它_自己_的标准库，而我并不想去折腾让_那个_跑在 Mac OS 9 上。（当然，Mac OS 9 提供的 C++ 标准库也太老了，撑不起 Swift 运行时需要的很多特性。）所以不管怎样，我都得从头实现一部分东西，而不能像标准库那样直接照搬真正的版本。

但等等，Swift 运行时为什么要用 C++ 实现？为什么不直接用 Swift 写？

1. 运行时在 Swift 早期的搭建阶段就已经需要了，所以它最早的那部分不可能是用 Swift 写的。不过这个理由在这里不适用。
2. 运行时通常需要能访问平台功能，但 Swift 有「覆盖层」（overlay）库，会在你写 `import Darwin`（或者在这里是 `import MacTypes`）这样的代码时，为通常的平台功能做增强。这样一来，运行时（通常和标准库链接在一起）和平台覆盖层之间就会有循环依赖。_不过，_如果我打算全程使用静态链接，链接器是能处理这些循环依赖的。^[2](#fn:circular)
3. C++ 依然能做一些 Swift 做不到的事，其中最重要的是用特定名字声明全局变量，以及声明带编译期常量值的复杂全局变量。Swift 编译器期望能直接引用某些东西，比如基础整数类型的类型元数据。这一点对我来说依然是个问题，但也许我可以把 C++ 的使用限制在这上面。

我之前一直避免依赖运行时，但也许这对我来说会是个不错的学习机会。哪怕是我在苹果做 Swift 的那段时间，我大部分时间也只是在做_编译器_面向用户的那部分，只是短暂地涉猎过运行时和标准库。所以我决定放手一搏，（主要）用 Swift 写一个运行时。它可能不是最快的，也不是最漂亮的，而且肯定支持不了真正运行时能做的一切，但我能让它跑起来。对吧？

### 拆解问题

和[上次](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/#modern-compiler-classic-linker)一样，我决定先定一个更容易的目标：让运行时的功能足以支持一个 ‑Onone 构建的 BitPaint。就像我上面说的，从 Swift 的角度看 BitPaint 其实并不复杂，基本上就是在搬运整数和指针。开了优化之后，它需要的一切都会被内联，甚至都不需要链接构建好的标准库。但是，Swift 里相当多的整数和指针操作都是以泛型方式实现的，依赖编译器把它们优化成机器原生的操作！所以一上来我就得处理一大堆泛型模型的东西。

题外话：这篇文章不会去讨论 Swift 运行时本身——不管是真正的那个，_还是_我做的这个迷你版。有人鼓励我以后专门写一篇讲这个的文章，但眼下我还是专注讲讲我是怎么让 Mac OS 9 上的 Game 'by Color App 跑起来的。

我的做法基本上是「用 ‑Onone 编译 BitPaint，试着链接，看看缺了哪些运行时功能」。一开始缺的还真不少！^[3](#fn:unresolved)

```
#  Unresolved external references:
#    $sBi16_WV
#    $sBi32_WV
#    $sBi64_WV
#    $sBi8_WV
#    $sytN
#    $sytWV
#    $syXlN
#    $syycWV
#    .swift_allocateGenericValueMetadata
#    .swift_allocObject
#    .swift_checkMetadataState
#    .swift_deallocObject
#    .swift_getAssociatedConformanceWitness
#    .swift_getAssociatedTypeWitness
#    .swift_getForeignTypeMetadata
#    .swift_getGenericMetadata
#    .swift_getTupleTypeLayout2
#    .swift_getTupleTypeMetadata
#    .swift_getTupleTypeMetadata2
#    .swift_getTupleTypeMetadata3
#    .swift_getWitnessTable
#    .swift_initEnumMetadataSinglePayload
#    .swift_initStructMetadata
#    .swift_release
#    .swift_retain
#    .swift_slowAlloc
#    .swift_slowDealloc
#    .truncf
#    .__divdi3
#    .__fixdfdi
#    .__fixsfdi
#    .__fixunsdfdi
#    .__fixunssfdi
#    .__floatdidf
#    .__floatdisf
#    .__moddi3
#    .__mulodi4
#    .__udivdi3
#    .__umoddi3
```

这些大致可以分成四类：

1. 我前面提到的那些全局对象（以 `$s` 开头的那些）
2. 元数据、布局，以及关联类型相关的工具函数
3. 对象分配与引用计数
4. 一些当年的 PowerPC 上没有实现的底层数值运算

而这四类，我最终各自用了不同的办法来处理：

1. 这是我从真正的运行时里搬过来最多的一块。它_确实_是用 C++ 实现的，但凡是复杂一点的代码，我都会回调进 Swift。
2. 这是工作量最大的一部分。运行时做的很多事情都是管理泛型元数据——如果某次使用没法被优化掉，就得为每一组泛型参数分配并填好元数据。这个也很容易出错。
3. 如果你不支持 unowned 和 weak 引用的话，对象分配其实相当简单！但等等，BitPaint 明明只处理数字和指针，我为什么还需要它？原来 Swift 在幕后会用对象来实现既存类型（existential）和闭包捕获的存储，再说了，反正我后面也需要用它来实现 Array 的存储。（另外，[这样一来我的 Swift 代码就能用 ARC 来管理 CF 对象了](https://twitter.com/UINT_MIN/status/1248154940318482432)。）
4. 这些数值运算里带下划线的那些大多来自 LLVM 本身。LLVM 知道并不是每个平台都实现了这些运算，所以它提供了 [compiler-rt](https://compiler-rt.llvm.org) 项目，用软件的方式实现它们。没费太大力气，我就搞定了为 PPC32 构建所需要的 compiler-rt「内建函数」。

  `truncf` 是唯一的例外，因为它通常是 C 标准库的一部分，但 Mac OS 9 实际上并没有提供它。为什么？大概是因为反正 C 语言里 `float` 和 `double` 之间的转换本来就存在，而绕道 `double` 的往返转换结果也是一样的。但 LLVM 就是想要这个函数存在，而想办法_骗_它去调用双精度版的 `trunc` 又行不通，所以到最后我干脆绕了个弯，[自己实现了它](https://belkadan.com/source/ppc-swift-project/blob/refs/heads/dev:/stdlib/_Runtime/Truncf.swift)，顺带复习了一下 IEEE 754 格式。

### 调试

……是个挑战。没有真正的字符串格式化功能，我用上了一个我发过推特的小 `dump` 工具：

> ```
> withUnsafePointer(to: v) {
>   let p = UnsafeRawPointer($0)
>   var i = 0
>   while i < MemoryLayout.size(ofValue: v) {
>     let nextByte = (p + i).load(as: UInt8.self)
>     putchar(hexToASCII(nextByte >> 4))
>     putchar(hexToASCII(nextByte & 0xF))
>     putchar(0x20)
>     i += 1
>   }
> }
> ```
> 
> — Jordan Rose (@UINT_MIN) [2020 年 5 月 13 日](https://twitter.com/UINT_MIN/status/1260696630677757953?ref_src=twsrc%5Etfw)

但这也就只能帮到这个程度。当某个指针指向了错误的东西，或者某块内存没有初始化，又或者整个数据相对正确地址偏移了 4 个字节时，它就没什么用了。我用过的调试手段五花八门：插入占位调用 `puts`（「跑到这里了没？」）、试着编译出仍然会以同样方式崩溃的最小程序（我管这叫「playground」App）、提前退出，甚至故意破坏一些东西看它还会不会崩溃。这些都是相当标准的调试手段，但最有力的那些恰恰缺席了：直接查看内存、单步执行指令直到找到崩溃或异常行为。在 Mac OS 9 上既没有回溯栈（backtrace），也没有实时调试，至少在没有我手头没有的更专业工具的情况下是这样！^[4](#fn:MacsBug)

最神秘的一个问题是：BitPaint _看起来_能正常工作，但用户操作几秒钟之后就会崩溃。到底是怎么回事？想猜猜看吗？

.

.

.

.

.

.

.

我花了_好几天_才想到会不会是内存耗尽了；更糟的是，这个想法其实是我在跟一个朋友交换想法的时候，_已经_被对方提出来之后才想到的。（你知道吗，在 Mac OS 9 上，一个 App 得预先声明它最多会用多少内存。）平心而论，出问题的那段代码_本不该分配任何内存，_运行时里唯一会分配元数据的地方，只有在一个新的泛型类型被实例化的时候。那为什么缓存没有起作用？

结果这其实是个_编译器_ bug，好在这个 bug 从没有出现在任何一个已发布的 Swift 版本里。^[5](#fn:master-next) 症状是：带常量初始值的全局变量被认为永远不会变化，因此泛型元数据的缓存每次调用都会从零开始重新分配，空空如也。修复办法最后是拉取编译器的最新更新，再重新合并一次我的改动。就这样。

_第二_神秘的 bug 是我同样发过推特的另一个：

> 这几天调试的收获：  
> `a != a`  
> → 两个 Optional 之间的 == 用了一个元组 [https://bugs.swift.org/browse/SR-12829](https://bugs.swift.org/browse/SR-12829)  
> → 运行时以为元组只有该有大小的一半  
> → 所有元组都在用同一份元数据  
> → 缓存的 key 是一个 CFData  
> → 所有缓存 key 长度都是 0  
> → 忘了调用 [https://developer.apple.com/documentation/corefoundation/1542375-cfdatasetlength](https://developer.apple.com/documentation/corefoundation/1542375-cfdatasetlength)
> 
> — Jordan Rose (@UINT_MIN) [2020 年 5 月 19 日](https://twitter.com/UINT_MIN/status/1262609197411098624?ref_src=twsrc%5Etfw)

总之，经过大量的试错、「[灵异调试](https://devblogs.microsoft.com/oldnewthing/?s=psychic+debugging&submit=%EE%9C%A1)」，以及反复重读那些我_猜测_是问题所在的代码，我最终得到了一个能配合未优化版 BitPaint 工作的运行时。没过多久，Array 也跑通了，接着是 Game 'by Color。

### 收获与计划

总的来说，做最初那个项目花了我[大约一个月](https://twitter.com/UINT_MIN/status/1253740850049191936)，而这一部分大概花了一个半月。事后想想，我本该料到这一点：最初的项目基本上只是把能用的部件接起来、把不能用的砍掉，而这一次则是要在没有测试也没有调试器的情况下，移植一个中等复杂项目（Swift 运行时）里相当大的一块。但我确实从中收获了一些东西：

- [一个能跑在 Mac OS 9 上的 Game 'by Color 版本](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/GameByColor.hqx)。（这是我一直在用来测试的[游戏](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/super-maze.gbyc)。）
- （部分）Swift 运行时的一份实现，以及更多能跑在 Mac OS 9 上的标准库内容。你可以在 [ppc-swift-project 仓库](https://belkadan.com/source/ppc-swift-project/)里查看这些内容。（Game 'by Color 的源码也在那里。）
- 一份用特性开关（feature flag）保护起来的 Swift 标准库版本，我打算在真正的 Swift 论坛上讨论这个，看看嵌入式开发者是否感兴趣。
- 对 Swift 运行时更深的理解，我希望能在以后的博客文章里写出来。

最后用一张照片收尾：Game 'by Color 跑在一台真正的 PowerPC Mac 上，同样要感谢我朋友 Nadine：

[![Mac OS 9.2.2 跑在一台 Power Mac G4 上，运行着 Game 'by Color，正在跑 super-maze](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/running.jpg)](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/running.jpg)

1. 「运行时」（runtime）这个词现在说起来挺有意思的。它原本大概只是指「程序运行的那个时刻」，但如今它也可以指「一个库，为那些不只是被编译成普通机器码的特性提供支持」。这方面最简单的例子就是 Swift 类所使用的自动引用计数：编译器不会直接操作每个对象里的引用计数数据，而是发出对 `swift_retain` 和 `swift_release` 函数的调用。为了把这两种含义区分清楚，我倾向于用「run-time」表示「程序运行的时候」这个泛泛的形容词含义，而用「runtime」表示那个支持库，或者跟它相关的东西。 [↩︎](#fnref:runtime)
2. 循环依赖通常不只是链接层面的问题，更是概念层面的问题：如果某样东西变了，什么该被重新构建？是不是所有东西都要重新构建？_是不是所有东西都会导致所有东西被重新构建，从而永远循环构建下去？_

  *咳*

  总之，在这个例子里，就算我们_真的_对所有东西都使用动态链接，只要把接口和实现分开，其实也并不存在真正的循环依赖：

    1. 构建 Swift.swiftmodule（无依赖）
    2. 构建 MacTypes.swiftmodule（依赖 Swift.swiftmodule）
    3. 构建 _Runtime.dylib（依赖 Swift.swiftmodule 和 MacTypes.swiftmodule）
    4. 构建 Swift.dylib（依赖 Runtime.dylib）
    5. 构建 MacTypes.dylib（依赖 Swift.dylib 和 Runtime.dylib）

  这套逻辑之所以成立，是因为运行时本身是经过优化的，在链接期对标准库或覆盖层本身没有任何依赖。如果没有这一点，这套流程依然行得通，只是不会那么_干净利落。_实际上，运行时总是被静态链接进标准库，哪怕标准库本身是个 dylib，所以唯一必须被优化掉的，只有对覆盖层的使用。

  这是不是意味着值得为真正的运行时也这么做一遍？大概不值得，至少不是马上。真正的运行时复杂得多，用到了不少 C++ 特性，而且它有一大块逻辑是和调试器共享的。想让逻辑同时在 C++ 和 Swift 之间共享会很痛苦，所以想直接用 Swift 写_新_代码也会很难办。理清构建依赖关系同样会很麻烦。但也许有朝一日，把这一切都转换过去还是值得的。 [↩︎](#fnref:circular)
3. 这甚至还不是全部，因为我用 `#if` 排除了标准库里一些我发现有运行时依赖、而我又用不上的东西。 [↩︎](#fnref:unresolved)
4. 苹果发行过一个叫 [MacsBug](https://en.wikipedia.org/wiki/MacsBug) 的标准调试器，但我没能让它在我的模拟器里跑起来。 [↩︎](#fnref:MacsBug)
5. 我用的是 `master-next` 分支，因为我需要 IBM 关于 AIX 最新的工作成果；等下一次 LLVM 重新分支之后，我会把这个项目锁定到 Swift 5.3 或 5.4 之类的某个版本，然后就不再动它了。 [↩︎](#fnref:master-next)

This entry was posted on [May](https://belkadan.com/blog/2020/05) 24, [2020](https://belkadan.com/blog/2020) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Mac OS Classic](https://belkadan.com/blog/tags/mac-os-classic), [ROSE-8](https://belkadan.com/blog/tags/rose-8)
