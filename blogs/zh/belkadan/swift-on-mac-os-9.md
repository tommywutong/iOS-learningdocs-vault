---
title: Swift 跑在 Mac OS 9 上
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/'
original_language: en
published: 2020-04-01
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:bf67af605884dd51'
translated: true
---

> 原文：[Swift on Mac OS 9](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Flexible Identities in git](https://belkadan.com/blog/2020/02/Flexible-Identities-in-git/)

[Shallow Git Repositories](https://belkadan.com/blog/2020/04/Shallow-Git-Repositories/) »

« [Leaving Apple](https://belkadan.com/blog/2019/11/Leaving-Apple/?tag=swift)

[ROSE-8 on Mac OS 9](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/?tag=swift) »

« [Color Palette #8](https://belkadan.com/blog/2018/01/Color-Palette-8/?tag=mac-os-classic)

[ROSE-8 on Mac OS 9](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/?tag=mac-os-classic) »

« [So You Want to Be a (Compiler) Wizard](https://belkadan.com/blog/2016/05/So-You-Want-To-Be-A-Compiler-Wizard/?tag=compilers)

[There's No Such Thing As "Implicitly Atomic"](https://belkadan.com/blog/2023/10/Implicity-Atomic/?tag=compilers) »

[SICPelago](https://belkadan.com/blog/2025/04/SICPelago/?tag=april-fools) »

## [Swift 跑在 Mac OS 9 上](#)

今天是 4 月 1 日，这意味着它既是[愚人节](https://en.wikipedia.org/wiki/April_Fools'_Day)，也是[苹果公司成立的周年纪念日](https://en.wikipedia.org/wiki/History_of_Apple_Inc.)。虽然由于[当下的时局](https://staythefuckhome.com)，今年的气氛比较沉重，但我想很多人依然感激大家创作和分享的东西，能给彼此打打气——不管是音乐、艺术，还是……不切实际的编程项目。虽然愚人节的_整蛊_好像越来越没意思了^[1](#fn:harder)，但那种不拿任何人开涮的、纯粹的玩笑和奇思妙想，我依然相信它的价值……如果这东西还真能跑起来，那就更好了。

去年我实现了[世界上最好的代码可视化工具](https://forums.swift.org/t/new-code-visualizer-for-swift-source-is-view/22454)。今年我决定认真挑战一件以前就想过的事：让一个 [Swift](https://swift.org) 程序在 Mac OS 9 上跑起来。

### 什么是 Mac OS 9？

![](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/macos9.png)

二十（！）年前，在我们今天所知的 macOS^[2](#fn:names-osx) 之前，还有一个叫「Mac OS」的操作系统^[3](#fn:names-classic)。它是最早采用图形界面的操作系统之一，这在今天几乎已经是理所当然的事。它还来自那个一次只能跑一个程序的年代；正因如此，即便是它的最新版本，也依然使用_协作式多任务处理_来运行多个程序——也就是说，一个程序得主动让出时间片，别的程序才能运行。^[4](#fn:MultiFinder) 如果某个程序崩溃了，或者覆写了它不该碰的内存，你很有可能得重启整台机器。

Mac OS 9 跑在 [PowerPC](https://en.wikipedia.org/wiki/PowerPC) 处理器上，这款处理器同样也用在 GameCube、PS3，_还有_ Xbox 360 里；这个操作系统更早的版本则是从 Motorola 的 [68k](https://en.wikipedia.org/wiki/Motorola_68000_series) 系列 CPU 起步的。它的继任者 Mac OS X^[5](#fn:ten) 刚发布时同样跑在 PowerPC 上；直到 10.4 苹果才开始转向 Intel 处理器，到 10.6 PowerPC 才被彻底放弃。

Mac OS X 在很多方面都比 Mac OS 9 前进了一大步，其中就包括_抢占式多任务处理_，让你能_真正_同时运行多个任务。但苹果不想就这么抛下 OS 9 的程序，于是他们做了两件事：

- _[Classic 环境](https://en.wikipedia.org/wiki/List_of_macOS_components#Classic)_ 搭建了一个足够像 Mac OS 9 的沙盒，让经典 Mac OS 程序能直接在 Mac OS X 里运行。因为 Classic 环境本身就是一个 App，所以在它里面运行的所有程序都不会干扰到 Mac OS X 的其他程序，反过来也一样。它其实效果相当好，甚至比直接启动进 Mac OS 9（那个系统始终没有支持更新的 PowerPC 处理器）活得还久。但它的生命随着 Mac 转向 Intel 芯片而终结——Classic 的实现方式是直接运行原始 App 里的指令，只需要为库提供兼容垫片。可以把它想象成 [Wine](https://www.winehq.org) / [CrossOver](https://www.codeweavers.com)，而不是 [VirtualBox](https://www.virtualbox.org) / [Parallels](https://www.parallels.com/products/desktop/)。^[6](#fn:Rosetta)
- _[Carbon](https://en.wikipedia.org/wiki/Carbon_(API))_ 把旧版 Mac OS 的 _Toolbox_ API 打包成了一整套，让你能按老办法写 Mac OS X App。你基本上只需要重新编译一遍你的 App，再加一个标注说明它已经「Carbon 化」了。（[是不是很耳熟？](https://developer.apple.com/mac-catalyst/) ^[7](#fn:catalyst)）顺带一提：这（大概）就是 [Core Foundation](https://developer.apple.com/documentation/corefoundation) 存在的原因之一——[为 Carbon 和 Cocoa 提供一个公共接口](https://youtu.be/NTGJm2BdqSU)。（感谢 [Marshall Elfstrand](https://twitter.com/llahsram/status/1246118151118450690) 提供的这段视频链接。）

Classic 随着 2000 年代 Mac 转向 Intel 处理器而终结，但 Carbon 一路撑到了去年的 macOS Mojave。苹果从未发布过 64 位版本的 Carbon，大概是为了鼓励开发者转向 Cocoa，而到了去年的 macOS Catalina，对 32 位 App 的支持~~被彻底~~在极少数例外之外被砍掉了。^[8](#fn:32-bit)

### 目标是什么？

因为我是在经典 Mac OS 上学的编程，多年后又把职业生涯里相当大一块时间花在了 [Swift](https://swift.org) 上，我一直有个挥之不去的念头：**用 Swift 写一个程序，让它跑在 Mac OS 9 上。** 也就是说：

- 我写调用 Carbon / Toolbox API 的 Swift 源代码。
- 我用（某个版本的）Swift 编译器把它编译成 PowerPC 代码。
- 我按 Mac OS 9 的要求把它打包起来。
- 大功告成！

这有用吗？没用！完全没用！但 [ROSE-8](https://belkadan.com/blog/2020/01/ROSE-8/) 也一样没用，可我做那个项目还是学到了很多东西。

你大概已经猜到了，我确实做成了，不然我也不会在这写这篇博客。所以，废话不多说，先上一张 Swift Toolbox App 跑在 Mac OS 9.2 上的照片，机器是我朋友 Nadine 的 Power Mac G4。（瞧瞧那飞快的 400MHz 处理器！）

[![你能看到 BitPaint 正在中间运行，Classic 版的 Apple System Profiler 也显示这确实是 Mac OS 9.2。](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/running.jpg)](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/running.jpg)

我猜看到这的不少人都想知道该怎么做到这一点！

- **如果你想自己构建一个支持 PPC 的 Swift 编译器**，去看看下面这些仓库：

  ```
  git clone https://belkadan.com/source/ppc-swift-project
  cd ppc-swift-project
  git clone -b ppc-swift https://belkadan.com/source/swift
  git clone -b ppc-swift https://belkadan.com/source/llvm-project
  git clone https://github.com/apple/swift-cmark cmark
  make  # quick start to build swiftc and the stripped-down stdlib
  ```

  留意这些子仓库的目录名和分支名，也留意它们都应该嵌套在 ppc-swift-project 仓库里面。**你还需要 [`mpw`](https://github.com/ksherlock/mpw) 模拟器，以及一份 [Macintosh Programmer's Workshop](https://en.wikipedia.org/wiki/Macintosh_Programmer%27s_Workshop) 工具集^[9](#fn:mpw-img)**，才能在现代 macOS 上构建出一个真正的 App。
- **如果你想要一份预先构建好的支持 PPC 的 Swift 工具链**，这里有一份：[ppc-swift-toolchain](https://www.dropbox.com/s/g3c6tnsg08z6zgv/ppc-swift-toolchain.zip?dl=1)。注意虽然我在这个工具链里放了一份构建好的 Swift.o，但你大概只有在优化过、且已经不再链接标准库任何部分的代码上（也就是所有东西都被内联掉了）才能成功。**你还需要 [`mpw`](https://github.com/ksherlock/mpw) 模拟器，以及一份 [Macintosh Programmer's Workshop](https://en.wikipedia.org/wiki/Macintosh_Programmer%27s_Workshop) 工具集。^[9](#fn:mpw-img)**

  你可能还是想去看看 [ppc-swift-project](https://belkadan.com/source/ppc-swift-project) 仓库里的示例。`swiftc`、`PPCLink` 和 `Rez` 所需的参数可能会有点挑剔。（另外注意 `SIZE` 和 `carb` 资源是任何 Carbon App 都必需的，所以如果你真想让 App 跑起来，就不能跳过 Rez 这一步。）

  _**更新：**这个工具链的[最新版本](https://www.dropbox.com/s/89zw69j5rw0wli7/ppc-swift-toolchain-2023.zip?dl=1)（2 月 23 日）*确实*支持链接标准库和使用未优化的代码了。不过你还是应该照着项目仓库里（现在已经不止一个了）的示例来搭建你自己的环境。_
- **如果你只是想试试构建好的 BitPaint**，这里有一份：[BitPaint-swift.hqx](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/BitPaint-swift.hqx)。

  [![（".hqx，好久没听过这个扩展名了。"）](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/obi-wan.jpg)](https://en.wikipedia.org/wiki/BinHex)

我很想听听大家用这些工具做出了什么东西！与此同时，如果你想知道我是怎么把这事做成的，请继续往下看。

### 收集素材

我上一次构建经典 Mac OS App 还是用 [CodeWarrior](https://www.macintoshrepository.org/577-codewarrior-pro-6) 的时候。其实说那是「构建经典 Mac OS App」都有点勉强；我当时是在学 C 语言，用 CodeWarrior 的终端 I/O 库凑出一个经典 Mac OS 本来没有的 stdin/stdout 接口。（记住，那会儿没有命令行！）我本可以想办法把某个版本的 CodeWarrior 重新跑起来，但那看起来不是最省事的办法。我也不觉得自己能把 Swift _编译器_ 本身跑在 Classic 上，所以无论如何我都得在两个操作系统之间来回搬运目标文件才能把事情做完。

好在我不是唯一一个对在现代 macOS 上构建 Classic App 感兴趣的人。我在某个时刻发现了 [`mpw`](https://github.com/ksherlock/mpw) 项目：一个专门用来运行苹果 [Macintosh Programmer's Workshop](https://en.wikipedia.org/wiki/Macintosh_Programmer%27s_Workshop) 工具集的模拟器。而且我知道这肯定能行，因为 Steve Troughton-Smith——在苹果社区里以发掘苹果各操作系统里未公开和预发布功能而（臭）名昭著——已经[写下了他的经验](https://www.highcaffeinecontent.com/blog/20150124-MPW,-Carbon-and-building-Classic-Mac-OS-apps-in-OS-X)：只需用合适的编译器、链接合适的库，就能用 `mpw` 构建出一个从 System 1 到现代 Mac OS X 都能运行的 App。

如果你对这些感兴趣，我强烈推荐去看看他的[博客文章](https://www.highcaffeinecontent.com/blog/20150124-MPW,-Carbon-and-building-Classic-Mac-OS-apps-in-OS-X)。这不仅是我入门时用的参考资料，上面那张照片里运行的 App，BitPaint，正是 Troughton-Smith 的测试 App，被我移植成了 Swift。（我事先确实问过他，用他的 App 做业余项目是否可以。）资深 Mac 开发者 Gwynne Raskind 几年前也在 Mike Ash 的博客上分两部分对 Toolbox API 做了一次高层次的导览（[第一部分](https://mikeash.com/pyblog/friday-qa-2012-01-13-the-mac-toolbox.html) | [第二部分](https://mikeash.com/pyblog/the-mac-toolbox-followup.html)）；好在即便在 Mac OS 9 上，Carbon 也替我们处理了相当一部分工作。

那么好。MPW 给了我们什么？

- 一个 PowerPC 编译器
- 一个 PowerPC 汇编器
- 一个 PowerPC 链接器
- 经典 Mac OS 的头文件
- 用于链接的经典 Mac OS 库桩（stub）
- 一堆目标文件和二进制检查工具，成品用不上，但我在[调试神秘的异常行为](#a-week-of-mysterious-failures)时没少用它们

这已经相当不错了；正如 Troughton-Smith 的博客文章所展示的，光靠这些就足以构建出一整个能在 Classic 上运行的 App。而我的想法是拿现代编译器产出的目标文件去喂给 PowerPC 链接器，这就意味着我还额外需要：

- 一个经过修改、支持生成 MPW 兼容目标文件的 Swift 编译器版本
- 某种精简版的 Swift 标准库和运行时（至少要能读入并对接 Carbon 头文件）
- 一台真正跑着 Mac OS 9 的机器。我确实_有_一台，但没有它的充电器，所以大部分测试我都是用 [SheepShaver](https://sheepshaver.cebix.net) 做的。等东西能跑起来之后，我朋友 Nadine 又在真机上做了一些测试。

嗯，这样应该就齐了！那么，开始吧。

### 现代编译器，经典链接器

为了让事情更好把控，我设了一个中间目标：先用 _Clang_——Xcode 自带的那个现代 C 编译器——构建出一个 App。Clang 和 Swift 编译器用的是同一套 [LLVM](http://llvm.org) 基础设施，所以我盘算着可以先在 Clang 里把目标文件格式和工作流程的问题都解决掉，再去处理 Swift 特有的部分。

我做的第一件事，是搞清楚 PowerPC 目标文件用的是什么文件格式。结果发现是一种叫 XCOFF 的格式；搜索这方面的现代文档，找到了一份 [IBM 的参考文档](https://www.ibm.com/support/knowledgecenter/ssw_aix_71/filesreference/XCOFF.html)。几乎没别人用这个格式，这可不是个鼓舞人心的信号。我第一次琢磨这个项目的时候，还担心自己得让编译器输出汇编代码，再把_那份_代码送进 MPW 的 PowerPC 汇编器——而且还得先修一修，弥合 LLVM 和 MPW 打印 PowerPC 汇编代码方式上的差异。

不过，当我去查 LLVM 是否支持 XCOFF 时，运气不错。原来 IBM 就在去年才开始为 LLVM 添加 XCOFF 支持，作为[给他们的 AIX 系统添加支持](https://lists.llvm.org/pipermail/llvm-dev/2019-February/130175.html)工作的一部分——_而 AIX 就跑在 PowerPC 上。_ 所以我可以让 Clang 为 AIX 生成 XCOFF 文件，这样一来，让它为经典 Mac OS 生成 XCOFF 文件应该只是一小步的事。

这时我想起了一则冷知识：[苹果和 IBM 曾经有过密切的合作关系，Motorola 也在其中。](https://en.wikipedia.org/wiki/AIM_alliance)他们甚至制定过一些跨平台、跨 CPU 通用的标准，虽然影响力可能不如他们当初希望的那么大。那么，AIX 和经典 Mac OS 会不会刚好用了相同的过程调用约定，从而不需要额外的工作就能互操作？

我很幸运：答案（几乎）是肯定的。[AIX 的寄存器约定](https://www.ibm.com/support/knowledgecenter/en/ssw_aix_72/assembler/idalangref_reg_use_conv.html)和[栈约定](https://www.ibm.com/support/knowledgecenter/en/ssw_aix_72/assembler/idalangref_runtime_process.html)和 [Mac OS Runtime Architectures](https://developer.apple.com/library/archive/documentation/mac/pdf/MacOS_RT_Architectures.pdf) 指南里的约定是对得上的。这意味着我可以把 Clang 产出的目标文件直接喂给 MPW 的 `PPCLink`，得到一个能用的经典 Mac OS 二进制文件。

我第一次看到这个跑起来的时候，我很确定自己的下巴都掉下来了。

```
% clang -c test.c \
    -target powerpc-ibm-aix-xcoff \
    -isystem ${MPW}/Interfaces/CIncludes \
    -integrated-as \
    -fpascal-strings
% mpw PPCLink test.o ${PPC_LIBRARIES} -o Test
```

只用最新主干版本的 LLVM/Clang（配上一份很简单的 test.c）应该就能跑通。虽然到最后我确实还是得对 LLVM 做了几处修改，但改动其实相当小，非常感谢 IBM 那边的人替我把最难的部分做完了！

### 接下来轮到 Swift

能编译一个简单的测试程序是个不错的里程碑，但要让 swiftc 编译出一整个 BitPaint，我还得再做不少工作。这里挑几个重点：

- **让 Swift 认识 PPC/AIX 目标平台。** 这主要涉及在 Swift 编译器各处的 switch 语句里加上 `ppc` 和 `AIX` 这两个 case，也涉及为 Clang 拼一份 Swift 调用约定的简单描述（我是从 32 位 ARM 的实现里抄来的），然后让 PPC/AIX 后端相信这是一个可以使用的调用约定。这方面我算是走了运，因为 Swift 已经支持 32 位 ARM、小端序的 64 位 PowerPC（跑在 Linux 上时），以及大端序的 64 位 s390x（另一款 IBM 架构）；所有的零件其实都已经就位了。
- **添加对 Pascal 字符串的支持。** Mac 最早的高级编程语言是 Pascal，不是 C！因此，Toolbox API 里字符串的默认格式是 _Pascal 字符串_（一个长度字节后面跟着字符串数据），而不是 _C 字符串_（字符串数据后面跟着一个空字节）。借助 `-fpascal-strings` 这个命令行开关，Clang 支持用 `"\pHello World"` 这样的语法写静态 Pascal 字符串。`\p` 会被替换成字符串的长度（不能超过 255 字节），这样你就不用自己去数了。[我把这个也黑进了 Swift 里](https://belkadan.com/source/swift/commitdiff/293d4b39ab9bbfd3f0762b6883da860e3601d373)，虽然我的实现大概还有些问题^[10](#fn:utf-8)，但足够让简单的东西跑起来了。
- **关掉反射支持，以及几乎所有的运行时元数据。** Swift 的运行时非常强大，但我不想为这个项目写太多运行时，毕竟这个项目主要就是在调用一堆 C 函数。除此之外，Swift 元数据的默认格式还大量用到了_相对寻址_（主要是为了缩短启动时间，[这里可以了解更多](https://youtu.be/G3bpj-4tWVU)），以及指向某个全局变量内部的符号，而 LLVM 的 XCOFF 实现（目前）两者都不支持。所以为了先做出一个能跑的概念验证，我把 IRGen 里用到这两种特性的部分都粗暴地注释掉了。我以后想把部分静态元数据加回来，但反射这块我完全不感兴趣。大概吧。
- **弄一个小小的标准库。** 完整的 Swift 标准库里有_很多_东西我用不上，还有一些我甚至不知道该_怎么_实现。（在一个不能假设 Unicode 存在的世界里，String 该是什么样？）但所有跟 C 代码对接的逻辑，都是建立在标准库里一些基础类型（比如 Int16 和 UnsafeMutablePointer）之上的。我最终的做法是拿标准库源码的一个子集，再添加一些额外文件、注释掉一些东西，直到它能跑。

  ……哈，然并卵，就算这样也还不够好。我早期的尝试倒是编译通过了，但一旦我想写个测试程序，它们就会让 PPCLink 崩溃，大概是因为标准库里符号_实在太多_了。所以我把范围砍得更_小_，最终（总算）跑通了。当然，我是在修改编译器、争取做出能跑的概念验证的同时干这件事的，所以我觉得自己最终砍得比实际需要的还要多。（有一堆符号只是给运行时元数据用的。）如上所述，非优化构建的、非平凡的程序目前还跑不起来，所以我也不知道自己是不是已经踩进了危险区，但我可能会试着把一些东西加回来。

  我没有去改动实际的 Swift 仓库，而是把我精简过的标准库单独放着，你可以在 [ppc-swift-project](https://belkadan.com/source/ppc-swift-project) 仓库里找到它。**对于想找一份兼容 C、不带运行时的 Swift 子集的人来说，这可能是个不错的参考**，比如做嵌入式或其他资源受限的环境。
- **禁用跳转表。** 当 LLVM 觉得有助于性能和/或代码体积时，会把 switch 语句优化成_[跳转表](https://en.wikipedia.org/wiki/Branch_table)_，但它默认的跳转表实现同样不受 LLVM 的 XCOFF 实现支持。我猜 AIX 那边的人迟早会把这个实现出来，但眼下我干脆整个禁用了跳转表，强迫编译器把 switch 语句改成一串 `if` 来发出。

如果你好奇的话，可以去 [swift](https://belkadan.com/source/swift/shortlog/refs/heads/ppc-swift) 和 [llvm-project](https://belkadan.com/source/llvm-project/shortlog/refs/heads/ppc-swift) 这两个仓库看看全部改动。其中能提交回上游各自项目的改动很少，但我会试着找机会把那些确实合适的改动提交上去。

### 神秘故障的一周

做完上面所有改动之后，我有了一个能跑的 App！还是用 Swift 写的！

……可它只是偶尔能跑。我随便改点什么，事件就突然不再触发了。情况严重到我不得不加了个计数器：任意十个事件之后就退出 App。不这么做的话，我会被卡住，甚至没法退出，只能重启（虚拟）机器。哪怕是在一个看起来能正常工作的版本里，我朋友 Nadine 也报告说，尝试使用 Reset 命令会导致 App 崩溃。到底是怎么回事？

我觉得我必须搞清楚早些时候看到的一件怪事的根源：就连 _Clang_ 版本的程序，在我打开优化选项之后也跑不对了。有可能这是 IBM 新加的 AIX 支持里的一个 bug，也可能是 32 位 PowerPC 支持的问题（毕竟它不算什么常见平台），甚至可能是 LLVM 优化本身的问题。也有可能 AIX 和经典 Mac OS 其实并没有我想象的那么相似，所以我的代码在某些约定上跟系统代码对不上。还有可能是优化后的代码用到了某条 SheepShaver 不支持的指令，尽管这好像也对不上症状。

而症状很古怪。有些局部变量被破坏了，有些却没有。于是我开始一项项排查：

- 栈是不是对齐正确？
- 栈指针是不是没有正确恢复？
- 跨库调用的胶水代码是不是把别的数据给覆写了？^[11](#fn:indirect)（见 [Mac OS Runtime Architectures](https://developer.apple.com/library/archive/documentation/mac/pdf/MacOS_RT_Architectures.pdf) 指南）
- 是不是有什么东西导致 Code Fragment Manager（动态链接器）在跨库调用时填入了错误的地址？

在没法依赖日志输出的情况下，我做了一个我能想到的最简单的文本调试输出方式：修改某个菜单的标题。（后来才发现，在 Mac OS 9 上写 stdout 会自动创建一个文件，我本可以用这个办法。）我写了一些 C 函数来追踪当前的栈指针，确保它被正确恢复；我没少用 MPW 自带的 `DumpXCOFF` 和 `DumpPEF` 工具；我了解了 PEF 的「pidata」（「模式初始化数据」）是怎么工作的，还试着手动逐步执行 CFM 的重定位（还是参见 [Mac OS Runtime Architectures](https://developer.apple.com/library/archive/documentation/mac/pdf/MacOS_RT_Architectures.pdf) 指南）。我甚至开始尝试反编译一些实际的系统库，看它们是不是在搞什么鬼，尽管实际的 Mac OS 9 里存在 bug 这件事本身看起来极不可能。这一路查下去，我甚至了解到了「toolbox ROM」——它其实根本不是 ROM：它是一段启动脚本，加上一堆压缩过的系统库。（之所以叫这个名字，是因为它的内容_曾经_确实是放在 ROM 里的。）好在 [SheepShaver 本来就知道怎么加载它](https://github.com/cebix/macemu/blob/2e302d60a337daa252c6992335e6365a9beac83f/SheepShaver/src/rom_patches.cpp#L148)，这意味着我可以照猫画虎地做同样的解压，然后手动把各个库拆分出来。

是的，我扯得有点远了。不过我确实学到了不少东西！

最后，我看了反编译后优化过的代码——是 C 版本的，不是 Swift 版本的。我发现被破坏的那个变量在通用寄存器 13 里。按理说，在经典 Mac OS（以及 32 位 AIX、32 位 Mac OS X）里，这是个可以放数据的安全位置，但我决定不再相信这一点，尤其是因为这个寄存器在 64 位 AIX 里曾被用来追踪线程本地存储。于是我把 r13 标记为保留寄存器……

……然后问题就消失了。优化的、非优化的，甚至开着 [`-fstack-protector-all`](https://clang.llvm.org/docs/ClangCommandLineReference.html#cmdoption-clang-fstack-protector) 也一样。Swift 版本同样如此。

（调试这个问题花了大概一周时间，很不幸，这也导致这个项目最终没能做到我原本设想的那么有野心。）

### 「未来的方向」

我还有哪些没做到的？其实还挺多的。

- 完全没有运行时，也就是说没有动态分配（以及其他一系列后果）。
- 没有类型元数据，也就是说没有泛型（除非它被优化掉了）。
- 没有字段元数据，也就是说没有键路径（除非它被优化掉了）。
- 没有 Unicode 支持，所以没有 String。我大概可以做一个没有 Character 的 String，或者一个以 [MacRoman](https://en.wikipedia.org/wiki/Mac_OS_Roman) 作为原生编码的 String，但那未必会长得像今天的 Swift.String。
- 还有一大堆其他标准库的东西缺失，一部分是因为我只想先让概念验证跑起来，另一部分是因为 `PPCLink` 在处理大的目标文件时会出问题。如果我真的让更多标准库的东西跑起来了，大概会想办法把它从「Swift」模块里拆出来。
- 为了让 LLVM 的 XCOFF 后端满意，我不得不在好几处摆弄[链接方式（linkage）](https://en.wikipedia.org/wiki/Linkage_(software))，所以我不确定多文件构建能不能跑。我甚至都没测试过。
- 我用的是 Carbon，理论上说我的程序_应该_也能在更老版本的 Mac OS X 上跑，但我朋友 Nadine 试过，没跑通，而这也不是当务之急，就没去深究。
- 我本想在 Toolbox API 之上做一些漂亮的封装。
- 我本想再做一些更复杂的示例 App！

也许我以后会继续跟进其中一些方向，但我为了赶在 4 月 1 日之前完成这个项目已经投入了大量精力，所以现在大概该回去处理一些之前为了这个项目而搁置的事情了。

### 小结

这个项目花了不少时间，即便我（1）对编译器懂得不少，而且（2）是靠一路野路子黑出来的，而不是小心翼翼地遵循规范的软件开发实践。但我学到了很多，也完成了一个在我心里放了很久的目标。

如果你一路读到了文章的最后，这里有个小奖励：BitPaint 在 Mac OS X 10.2 的 Classic 下运行的样子（同样由 Nadine 提供）。

[![你能看到 BitPaint 正在中间运行，Classic 版的 Apple System Profiler……但同时还能看到 Mac OS X 的"关于本机"窗口显示的是 10.2.8。](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/classic.jpg)](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/classic.jpg)

大家注意安全，力所能及地照顾好身边的人。另外，如果有谁用这个项目做出了什么东西，我很想听听！

1. [「刻薄很容易，年轻人。幽默才难。」——Annalee Flower Horne](https://twitter.com/LeeFlower/status/1109450357778853890) [↩︎](#fnref:harder)
2. 曾用名 OS X，再往前曾用名 _Mac_ OS X。 [↩︎](#fnref:names-osx)
3. 曾用名「System」，就像「System 7」里那样。这个操作系统直到 Mac OS 7.6 才有了这个品牌名。 [↩︎](#fnref:names-classic)
4. 如果你想多了解一点这方面的内容，可以去看看维基百科上的 [MultiFinder](https://en.wikipedia.org/wiki/MultiFinder) 词条。 [↩︎](#fnref:MultiFinder)
5. [永远读作「ten」，绝不读作「ex」。](https://twitter.com/UINT_MIN/status/790977467842301952) [↩︎](#fnref:ten)
6. 苹果在转向 Intel 芯片的时候_确实_也做了一个给 PowerPC App 用的模拟器，叫 [Rosetta](https://en.wikipedia.org/wiki/Rosetta_(software))。从某种意义上说，这在技术上甚至比 Classic 更了不起，但为什么他们不能让 Classic 通过 Rosetta 运行呢？维基百科上的说法是，因为 Classic 需要更底层的系统钩子，而他们不想在 Rosetta 里提供这些；我也可以想象这是因为层数太多、难以保证性能，又或者只是苹果想甩掉维护一款使用量逐年减少的软件的负担。 [↩︎](#fnref:Rosetta)
7. 虽然我实在忍不住想拿它跟 Catalyst 做个_技术上_的类比，但我不觉得这两种情况真的有那么像。对当年的 Mac 程序员来说，Carbon/Toolbox 曾是那个熟悉的 API，但对今天的 Mac 程序员来说，AppKit 才是熟悉的 API，UIKit 反倒是新引入的东西。 [↩︎](#fnref:catalyst)
8. 「[这惹恼了不少人，并被普遍认为是个糟糕的举动。](https://www.goodreads.com/quotes/1-the-story-so-far-in-the-beginning-the-universe-was)」这里的问题不只是开发者需要把现有 App 移植到 64 位（或者，如果他们还在用 Carbon 而它早就停止更新了的话，移植到 Cocoa）；更让人担心的是那些开发者已经没有计划再更新的老 App。人们尤其担心游戏，因为它没法用一个处理相同数据的类似 App 来「替代」。另一方面，操作系统里有_大量_苹果不再需要维护的旧代码，这意味着更少的安全漏洞、更少的 bug、更快的开发速度。至少理论上是这样。与此同时，人们不得不诉诸一些奇怪的办法，比如[在虚拟机里跑 macOS Mojave](https://appletoolbox.com/need-to-run-32-bit-apps-on-macos-catalina-use-a-mojave-virtual-machine/)，很遗憾地告诉你，这么做基本上真的行得通。 [↩︎](#fnref:32-bit)
9. 如今想搞到 MPW 已经越来越难了。我自己不太方便托管它，而维基百科页面底部链接的、目前仍可用的托管资源，是以 [HFS](https://en.wikipedia.org/wiki/Hierarchical_File_System) 磁盘镜像的形式提供这些工具的——这是苹果在 [HFS+](https://en.wikipedia.org/wiki/HFS_Plus)（它本身又已经被 [APFS](https://en.wikipedia.org/wiki/Apple_File_System) 取代）_之前_使用的磁盘格式。macOS 10.15 Catalina 已经不再支持 HFS 磁盘镜像了，所以为了提取这个磁盘镜像，我最终用上了自己的 Mac OS 9 装机，外加一份匆忙搞到的 [Disk Copy](https://support.apple.com/kb/DL1262)（不知为何苹果至今还托管着它）。如果你手头有台 Catalina 之前的机器，那大概会容易得多。 [↩︎](#fnref:mpw-img) [↩︎^2](#fnref:mpw-img:1)
10. Swift 字符串按理说必须是合法的 UTF-8，我也不确定编译器的某些部分会不会因为不合法而崩溃。但如果我哪天用到一个超过 127 字节的字符串字面量，那个长度字节就会出现在某个多字节 UTF-8 序列的内部，而不是作为一个单独的 Unicode 标量出现。好在到目前为止我所有的测试字符串都很短。

  （反正经典 Mac OS 上的字符串默认是用 [MacRoman](https://en.wikipedia.org/wiki/Mac_OS_Roman) 编码的，所以如果我真想在静态字符串里放一个 MacRoman 的省略号字符，同样也会碰到这个问题。） [↩︎](#fnref:utf-8)
11. 顺带一提，跨库调用（「具名间接调用」）的代码，看起来本该能和通过函数指针调用共享逻辑。这样做能减小代码体积，代价是多一次跳转，但也许这一次额外的跳转对性能的影响还挺大的。^[12](#fn:footnote) [↩︎](#fnref:indirect)
12. 这篇文章创下了「我写过的文章里脚注数量」的记录（还没算上这一条）。有人建议我用一条脚注来纪念这件事。 [↩︎](#fnref:footnote)

This entry was posted on [April](https://belkadan.com/blog/2020/04) 01, [2020](https://belkadan.com/blog/2020) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Mac OS Classic](https://belkadan.com/blog/tags/mac-os-classic), [Compilers](https://belkadan.com/blog/tags/compilers), [April Fools](https://belkadan.com/blog/tags/april-fools)
