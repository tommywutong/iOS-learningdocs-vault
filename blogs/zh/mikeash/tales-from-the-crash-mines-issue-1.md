---
title: '崩溃矿场故事集：第 1 期'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/tales-from-the-crash-mines-issue-1.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:74bd6e02e6466465'
translated: true
---

> 原文：[Tales From The Crash Mines: Issue #1](https://www.mikeash.com/pyblog/tales-from-the-crash-mines-issue-1.html)　·　mikeash.com Friday Q&A

发表于 2014-02-06 14:53 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([全文 feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2014-03-14: Sockets API 入门](https://www.mikeash.com/pyblog/friday-qa-2014-03-14-introduction-to-the-sockets-api.html)  
上一篇：[Friday Q&A 2014-01-24: libclang 入门](https://www.mikeash.com/pyblog/friday-qa-2014-01-24-introduction-to-libclang.html)  
标签：[assembly](https://www.mikeash.com/pyblog/?tag=assembly) [crashmines](https://www.mikeash.com/pyblog/?tag=crashmines) [debugging](https://www.mikeash.com/pyblog/?tag=debugging) [guest](https://www.mikeash.com/pyblog/?tag=guest)

崩溃矿场故事集：第 1 期

作者：[Landon Fuller](http://landonf.bikemonkey.org/)

虽然这篇文章可能看起来是为了宣传我们的支持和咨询服务而做的毫不掩饰的尝试，但我向您保证，事实正是如此。

**引言**

在 [PLCrashReporter](https://www.plcrashreporter.org) 的工作中，我们遇到了应用程序和库中各种有趣的崩溃。我们提供的[支持服务](https://www.plcrashreporter.org/support/professional)之一就是帮助应用程序开发者追踪真正隐蔽的 bug；我们常常会对崩溃报告、客户的应用程序代码以及 Apple 的系统框架进行深入的源码和指令级分析。

这是“崩溃矿场故事集”的第一期——我们打算不定期地推出系列文章，介绍我们在 iOS 和 Mac OS X 上追踪到的 _有趣_ 的 bug。对我们来说，有趣的 bug 是指那些以不明显或新颖方式暴露自身，并且开发者很可能在自己的崩溃报告中看到的 bug。我们希望可以就如何在自己的代码库中避免这些问题，以及如何在崩溃报告中识别出类似问题提供一些具体的指导，或许还能让你了解我们分析故障的一些思路。

对于我们的第一个 bug，我们有一个来自 [Unibox](http://www.uniboxapp.com) 朋友的有趣崩溃案例，他们慷慨地允许我们将他们的问题作为本系列的一个例子。Unibox 是一个 Mac OS X 应用程序，但我们的分析同样适用于 iOS——我们会在过程中解释任何细微的差异。

如果你正在寻找一款优秀的电子邮件客户端，一定要试试 [Unibox](http://www.uniboxapp.com)。

女士们先生们：你们即将听到的故事是真实的。只有代码被修改过，以保护 Unibox 的知识产权。你在示例源代码列表、类名和方法名以及崩溃报告中发现的任何问题完全都是 _我们_ 的责任，因为所有示例都是我们编写的。

**一只蝴蝶扇动翅膀**

我相信每个人都熟悉[通俗科学对混沌理论的定义](https://www.youtube.com/watch?feature=player_detailpage&v=n-mpifTiPV4#t=34)——巴西的一只蝴蝶扇动翅膀，却在德克萨斯州引发了一场龙卷风。

这个想法并不是说蝴蝶驱动了龙卷风，而是说，在[确定性非线性系统](http://en.wikipedia.org/wiki/Butterfly_effect)的初始条件中，一个微小的变化可能导致完全不同的宏观结果。

软件执行的复杂度 _远不及_ 天气系统（这对我们来说是件好事！），但基本思想仍然适用；触发故障的 bug 与该故障的实际可见结果之间可能存在巨大差距。更重要的是，实际可见的故障 _类型_（以及故障是否会发生）高度依赖于初始条件——包括哪些线程在运行，它们执行到了什么程度，网络服务器何时响应，以及代码初始化时的初始数据。

Unibox 的 bug 就是这种情况，这也是我觉得它有趣的原因之一。Unibox 的团队根本无法在本地重现这个 bug。它只是半规律性地发生。软件实际崩溃的位置各不相同，而且很少对应到明显的源码行。崩溃的 _类型_ 也各不相同。崩溃报告之间唯一的共同点是：

- 崩溃发生在网络代码的同一区域。
- 尽管使用了 ARC，所有故障都指向了一个对象过度释放（over-release）。

面对一个无法在本地重现的 bug，在不同位置、以不同方式崩溃，甚至可能根本不涉及你自己的代码——你要如何调试它？

这时我们就要回到我们通俗的混沌理论。给定一个观察到的 _结果_（崩溃报告）和一个 _确定性系统_（处理器和执行环境），我们需要找出哪些初始条件可能导致我们所看到的所有故障。

为此，我们在 [Plausible Labs](https://plausible.coop/) 的常用方法是将二进制文件加载到反汇编器中，从崩溃点逆向工作，确定可能导致故障的完整初始条件集合。这是一个简单的排除过程，我们通过证明某些初始条件 _不可能_ 触发崩溃来将其排除。

在大多数情况下，收集到的崩溃报告中存在足够的数据，可以将可能性缩小到能够导致该问题的一组初始条件——从而找到 bug——而无需实际运行代码或重现问题。

如果我们无法缩小到单个 bug，我们会进行更有针对性的数据收集，以帮助消除剩余的任何可能性。我们收集的数据越多，就越能缩小初始条件的数量，直到找到根本原因。

这是我发现的对崩溃报告进行分类的最快方法——有时也是唯一的方法——因为它不需要实际的可重现案例，只需要一份崩溃报告。把它想象成一个用大脑驱动的 `git bisect`，利用你的长期记忆和模式识别能力快速排除可能的初始条件，然后评估剩下的情况。

我还想花一点时间强调以下几点：对于大多数 bug，你 _不需要能够阅读汇编_ 就能进行这种类型的崩溃分析。虽然能够在汇编层面进行静态分析可以更容易、更准确地排除不可能的条件，但通常可以通过在源码层面评估所有内容来得出相同的结论。有时你可能需要多一点数据，但这仍然是我所知道的快速推理故障的最佳方法。

现在，手握着我们通俗的混沌理论，让我们来看看 Unibox 团队提供的一份崩溃报告，并确定哪些可能的初始状态会导致所表现出的行为。前方有一些有趣的曲折和转折。

**崩溃报告——地址 0x0 处的 SIGBUS**

为了本文的目的，我们将逐步分析单个崩溃报告的完整根本原因——在 `SIGBUS` 中触发的 `objc_autorelease()` 信号，故障地址为 `0x0`：

```
    …
    Exception Type:  SIGBUS
    Exception Codes: BUS_ADRERR at 0x0
    …
    Thread 17 Crashed:
    0   libobjc.A.dylib                      0x00007fff896392d2 objc_autorelease + 18
    1   ExampleApp                           0x0000000103fbf0f9 -[EXNetConnection execute:timeout:completionBlock:] (EXNetConnection.m:89)
    2   ExampleApp                           0x0000000103fbeff7 -[EXNetConnection execute:completionBlock:] (EXNetConnection.m:77)
    3   ExampleApp                           0x0000000103fbfba7 -[EXNetConnection selectItem:] (EXNetConnection.m:163)
    …
    Thread 17 crashed with X86-64 Thread State:
        rip: 0x00007fff896392d2    rbp: 0x0000000115846590    rsp: 0x0000000115846568    rax: 0xbadd30ac3ceabead 
        rbx: 0x0000600002a2ef20    rcx: 0x0000000000000001    rdx: 0x0000000115846468    rdi: 0x0000608001c4b0a0 
        rsi: 0x0000000000001a7a     r8: 0x0000000000001fff     r9: 0xffff9fffffb0267f    r10: 0x000000010f8e47a0 
        r11: 0x0000000000000201    r12: 0x00007fff89622080    r13: 0x000060000263d040    r14: 0x0000000000000000 
        r15: 0x0000608002c692c0 rflags: 0x0000000000010246     cs: 0x000000000000002b     fs: 0x0000000000000000 
        gs: 0x0000000011190000
```

**初步假设**

一眼看去，我们可以对调用 `objc_autorelease()` 时进程的初始状态做出以下假设：

- 地址为 0x0 的 SIGBUS _可能_ 意味着我们解引用了一个 NULL 指针（参见[探索 iOS 崩溃报告](https://www.plausible.coop/blog/?p=176)）。
- `id objc_autorelease (id obj)` 函数等同于调用 `[obj autorelease]`，并且像 `-autorelease` 一样，它会忽略 nil 对象值。^[1](#fn-1) 如果我们因为 `objc_autorelease` 中的 NULL 指针而崩溃，那 _可能_ 是因为对象的指针指向了真实内存，但数据实际上不是一个有效的对象。

这给了我们一个可以开始挖掘的地方——一个 `frame 0` 假设。

**检查帧 0：在 objc_autorelease() 中崩溃**

```
    Thread 17 Crashed:
    0   libobjc.A.dylib    0x7fff896392d2 objc_autorelease + 18
    …
```

我们认为我们知道崩溃是什么——`objc_autorelease()` 中的 NULL 解引用——但我们还没有证明任何事情。要实际证明崩溃 _是_ 一个 NULL 解引用，我们需要检查 `objc_autorelease()` 的实现，排除所有不可能的初始状态，直到我们剩下（理想情况下）一个可能有效的状态——比如我们假设的 NULL 解引用。

我们将从检查 Apple 发布的 [objc4-551.1](http://www.opensource.apple.com/source/objc4/objc4-551.1/runtime/NSObject.mm) 运行时源码中 `objc_autorelease()` 的实现开始。在查看下面的源代码时，请注意，在现代 Objective-C 运行时中，Objective-C 对象是作为 C++ 结构体实现的；诸如 `obj->isTaggedPointer()` 之类的语句是 C++ 方法调用，而不是对 C 函数指针的调用：

```
    id objc_autorelease (id obj) {
        if (!obj || obj->isTaggedPointer())
            goto out_slow;

        if (((Class)obj->isa)->hasCustomRR())
            return [obj autorelease];

        return bypass_msgSend_autorelease(obj);

     out_slow:
        return obj;
    }
```

看起来 `objc_autorelease()` 只有在 `obj->isa` 为 NULL 时才会因解引用 NULL 指针而崩溃；如果 `obj` 参数是 NULL，函数会立即终止，而 `obj->isa` 看起来是函数中唯一被解引用的其他指针。

然而，“很可能”还不够好。为了提供证明，我们需要查看实际的 `objc_autorelease()` 实现，特别是实际的崩溃指令，位于 `0x7fff896392d2 objc_autorelease + 18`。

**反汇编帧 0**

`objc_autorelease` 的 x86-64 实现如下；我们将详细地逐步分析汇编列表，所以不必担心你的 x86-64 知识生疏了。^[2](#fn-2)

```
    ; if (!obj || obj->isTaggedPointer())
    ;     goto out_slow;
    0x7fff896392c0    test    rdi, rdi
    0x7fff896392c3    je      loc_out_slow
    0x7fff896392c5    test    dil, 1
    0x7fff896392c9    je      do_autorelease
    ; out_slow:
    ;    return obj;
    0x7fff896392cb loc_out_slow:
    0x7fff896392cb    mov     rax, rdi 
    0x7fff896392ce    ret
    0x7fff896392cf do_autorelease:
    …
```

前两条指令测试 `obj` 参数是否等于 nil，如果是，则跳转到 `loc_out_slow`。^[3](#fn-3)

第二对指令测试 `obj` 参数是否是一个 tagged pointer^[4](#fn-4)。这是 `obj->isTaggedPointer` 的内联实现。如果 `obj` **不是** tagged pointer，我们跳转到下面的 `do_autorelease`。否则，执行继续到下一个指令（恰好是 `loc_out_slow`）。如果你对奇怪的 `dil` 寄存器感到疑惑，在 x86-64 上，`dil` 寄存器只是 `rdi` 寄存器低 8 位的别名。

最后，`loc_out_slow` 将 `obj` 参数（`rdi`）复制到返回地址寄存器（`rax`）中，并将其返回给调用者。如果我们是从 nil 或 tagged pointer 测试到达这里的，原始的 `obj` 参数值将直接返回给调用者，并且 `objc_autorelease()` 将终止。由于我们的崩溃发生在函数稍后的位置，我们已经确认了 `obj` 参数既不是 nil，也不是 tagged pointer。

此时，还没有任何东西解引用过 `obj` 指针，更不用说 `obj` 了，而且我们还没有到达崩溃的指令。让我们继续。

```
    ; if (((Class)obj->isa)->hasCustomRR())
    0x7fff896392cf    mov     rax, [rdi]
    0x7fff896392d2    mov     rax, [rax+32] ; <-- We crashed loading 8 bytes from rax+32
    … [elided remainder of function]
```

这里我们进入了核心部分。第一条 `mov` 指令获取 `obj->isa` 指针^[5](#fn-5)，成功地将值存储在 `rax` 寄存器中。

第二条 `mov` 指令是 `hasCustomRR` 的内联实现，正是在这里我们实际崩溃了，试图从 `rax+32` 加载 8 个字节。

从我们对代码的阅读来看，很明显 `obj` 的 `objc_autorelease()` 参数 _必须_ 指向了已映射、可读的内存；否则，我们永远无法读取 `obj->isa`。实际的崩溃发生在其后一条指令，当在 `isa->data` 解引用 `[rax+32]`（即 `0x7fff896392d2`）时。

鉴于这个已证明的事件顺序，我们现在知道 `obj` 指向的内存 _是_ 已映射且可读的，但在调用 `isa` 时 _并没有_ 包含一个有效的 `objc_autorelease()` 指针——或者它在函数执行期间变得无效——因为崩溃发生在尝试从 `isa->data` 读取 8 个字节时。

因此，我们已经证明了我们假设的 _部分_ 内容：

- 传递给 `objc_autorelease()` 的对象是一个非 NULL 的、指向已映射内存的指针；否则，执行永远不会到达它崩溃的点。
- 在崩溃时，该对象指针 _没有指向有效的 Objective-C 对象_，因为 `objc_autorelease()` 在解引用对象内部一个损坏的 `isa` 指针值时崩溃了。

这让我们从最初的假设中剩下一个未证明的项目：被解引用的 `isa` _是_ NULL，正如崩溃报告中 `Exception Codes: BUS_ADRERR at 0x0` 所暗示的那样。

只有一个问题；再看一下崩溃指令：

```
    0x7fff896392d2    mov     rax, [rax+32] ; <-- We crashed loading 8 bytes from rax+32
```

根据我们的崩溃报告，我们收到了一个 `SIGBUS`，故障内存地址为 `0x0`。故障地址 _绝不可能是_ `0x0`，因为代码 _总是_ 解引用 `rax` 的值，**再加上 32**。更复杂的是，如果我们看看崩溃报告中报告的 `rax` 的值，它 _远非_ `0x0`：

```
    rax: 0xbadd30ac3ceabead
```

怎么回事？崩溃报告器生成了无效的崩溃报告吗？

**无效的崩溃报告？不，只是一个无效的假设**

答案是否定的——崩溃报告没问题。内核报告的 `si_addr` 值 _是_ 0x0，但实际的故障地址 _不是_ 0x0，这一切都有充分理由：[x86-64 规范形式地址](http://en.wikipedia.org/wiki/X86-64#Canonical_form_addresses)。在所有当前的 x86-64 指令集实现中，完整的 64 位地址范围只有 48 位可供使用。此外，AMD64 和 Intel 规范要求地址必须以规范形式表示：地址的第 48-63 位必须是第 47 位的副本。如果第 47 位是 0，那么第 48-63 位也必须是 0，反之亦然。如果你对细节好奇，请参考 [Intel 64 and IA-32 Architectures Software Developer's Manual: Volume 1](http://www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-software-developer-vol-1-manual.pdf) 的第 3.3.7.1 节。

再看一下 `rax` 的值。`0xbadd30ac3ceabead` _不是_ 规范形式。对非规范地址的内存引用会触发通用保护故障，在 x86 上，通用保护故障 _不提供故障地址_。如果你想知道实际的故障地址，你必须检查寄存器状态和机器码，以确定软件试图加载什么——这正是我们刚才手动做的。内核 _可以_ 尝试自动执行此操作以提供有效的 `si_addr`，但它没有，这也是 POSIX [明确允许的](http://pubs.opengroup.org/onlinepubs/009696699/basedefs/signal.h.html)：

> 对于某些实现，si_addr 的值可能不准确。

自动化地执行这类高级指令级启发式分析在 [PLCrashReporter 路线图](https://opensource.plausible.coop/wiki/display/PLCR/Project+Roadmap)上，但与此同时，如果你不熟悉内核级别的 x86-64 故障处理，你如何 _找到_ 像这样的差异的答案呢？

**深入挖掘**  
如果你在你不熟悉的领域发现了令人困惑的事情——比如崩溃报告内容与代码所说之间存在差异——那么就开始挖掘，弄清楚它怎么可能发生。通常一个好主意是从高层向下层工作，首先验证你自己的假设，然后验证你所依赖的实现的假设，依此类推，沿着技术栈向下，直到你找到答案：

1. 查阅系统文档，例如 `signal(3)` 和 `sigaction(2)` 的手册页，以确定系统实际提供了哪些行为保证。你对特定行为的假设可能与实际记录的文档不符。
2. 查阅相关标准，例如 [POSIX 规范](http://pubs.opengroup.org/onlinepubs/9699919799/)，以确定预期的行为保证是什么，并帮助解决系统文档中的任何歧义。
3. 查阅实际实现，以确定这些行为保证是如何实现的。在像这样的情况下，像 Amit Singh 的 [Mac OS X Internals](http://osxbook.com/) 这样的书籍提供了一个很好的起点。Apple 继续在 [http://www.opensource.apple.com/](http://www.opensource.apple.com/) 提供 Mac OS X 内核的源代码，并且 Mac OS X 的实现往往与 iOS 内核匹配。
4. 查阅底层平台（们）的架构参考手册——可从 [ARM](http://www.arm.com/products/processors/instruction-set-architectures/index.php) 和 [Intel](http://www.intel.com/content/www/us/en/processors/architectures-software-developer-manuals.html) 免费获得——以确认你所看到的行为。

在这种情况下，我实际上正是按照上述描述解决了这个问题。我已经熟悉规范地址规则，但我是在逐步检查整个栈并最终到达 Intel 架构手册时才恍然大悟。

最后，如果你深入挖掘却毫无结果，那就 _去问_。真的。像 PLCrashReporter [邮件列表](http://groups.google.com/group/plcrashreporter) 和 [IRC 频道](https://opensource.plausible.coop/wiki/display/PLCR/Project+IRC+Channel) 这样的资源可以提供帮助。

**完善我们的假设**

我们已经证明了我们假设中的前两个陈述，并且我们已经驳斥了第三个——即 isa 是 NULL，触发了 NULL 解引用。这没关系——这对我们的分析并非绝对必要，而且我们现在确定无疑地知道：

- 传递给 `objc_autorelease()` 的对象指针是一个有效的、指向可读内存的指针。
- 在崩溃时，该对象指针没有指向一个有效的 Objective-C 对象。

现在我们知道了 `objc_autorelease()` 故障 _是什么_——它被传递了一个指向已映射内存但 _不是_ 对象的指针——让我们弄清楚 _这是如何发生的_。

**检查帧 1**

```
    Thread 17 Crashed:
    0   libobjc.A.dylib    0x7fff896392d2 objc_autorelease + 18
    1   ExampleApp         0x000103fbf0f9 -[EXNetConnection execute:timeout:completionBlock:] (EXNetConnection.m:89)
    …
```

我们已经确定一个坏的对象指针被传递给了 `objc_autorelease()`。由于我们的回溯显示下一个帧是 `-[EXNetConnection execute:timeout:completionBlock:]`，它 _可能是_ 那个用无效参数调用了 `objc_autorelease()` 的函数。我们有意说“可能”：崩溃报告不是时间机器；它是崩溃发生时进程的快照，回溯是从中重建的。我们不能将任何未经证实的推断视为事实。

现在有些读者可能想到了启用 [`NSZombie`](https://www.mikeash.com/pyblog/friday-qa-2011-05-20-the-inner-life-of-zombies.html) 来运行代码以追踪坏对象；但请记住，没有可靠的可重现案例，而且在 bug 到达我们案头之前很久就尝试过启用 `NSZombie`。

相反，让我们看看 `-[EXNetConnection execute:timeout:completionBlock:]` 的实现，看看是否有任何突出之处：

```
    - (EXResponse *) execute: (NSString *) command timeout: (NSTimeInterval) timeout completionBlock: (EXResponseBlock)
    {
          return [self execute: command timeout: timeout completionBlock: block updateCallback: nil]; // <-- Stack trace claims that we called objc_autorelease() here, at line #89
    }
```

不幸的是，这太模糊了，没什么用——对 `objc_autorelease()` 的调用是由 ARC 插入的，但我们不知道在哪里，甚至不知道 ARC 试图自动释放的是什么对象。我们可以猜测——根据我们对 ARC 的了解，它几乎肯定会为返回值插入自动释放代码。但是，在这种模糊程度下我们无法证明任何事情，而且当我们开始挖掘时，你可能会对我们的发现感到惊讶。让我们看一下 `-[EXNetConnection execute:timeout:completionBlock]` 的实际汇编代码：

```
    0x103fbf0ba -[EXNetConnection execute:timeout:completionBlock:] proc near
    0x103fbf0ba var_20          = qword ptr -20h
    0x103fbf0ba    push    rbp
    0x103fbf0bb    mov     rbp, rsp
    0x103fbf0be    push    r15
    0x103fbf0c0    push    r14
    0x103fbf0c2    push    rbx
    0x103fbf0c3    push    rax
    0x103fbf0c4    mov     r14, rcx
    0x103fbf0c7    movsd   [rbp+var_20], xmm0
    0x103fbf0cc    mov     r15, rdi
    0x103fbf0cf    mov     rdi, rdx
    0x103fbf0d2    call    cs:_objc_retain_ptr
    0x103fbf0d8    mov     rbx, rax
    0x103fbf0db    mov     rsi, cs:selRef_execute_timeout_completionBlock_updateCallback_
    0x103fbf0e2    mov     rdi, r15
    0x103fbf0e5    mov     rdx, rbx
    0x103fbf0e8    movsd   xmm0, [rbp+var_20]
    0x103fbf0ed    mov     rcx, r14
    0x103fbf0f0    xor     r8d, r8d
    ; This is the instruction that supposedly called objc_autorelease(),
    ; but it's actually a call to [self execute:timeout:completionBlock:updateCallback:]
    0x103fbf0f3    call    cs:_objc_msgSend_ptr
    ; The return address in our crash report
    0x103fbf0f9    mov     r14, rax
    0x103fbf0fc    mov     rdi, rbx
    0x103fbf0ff    call    cs:_objc_release_ptr
    0x103fbf105    mov     rdi, r14
    0x103fbf108    call    _objc_retainAutoreleasedReturnValue
    0x103fbf10d    mov     rdi, rax
    0x103fbf110    add     rsp, 8
    0x103fbf114    pop     rbx
    0x103fbf115    pop     r14
    0x103fbf117    pop     r15
    0x103fbf119    pop     rbp
    0x103fbf11a    jmp     _objc_autoreleaseReturnValue
    0x103fbf11a -[NetConnection execute:timeout:completionBlock:] endp
```

在地址 `objc_autorelease()` 或方法中的任何其他地方 _没有_ 对 `0x103fbf0f3` 的调用！相反，崩溃报告中列出的地址对应的是一个对 `[self execute:timeout:completionBlock:updateCallback:]` 的调用（通过 `objc_msgSend`）。这里发生了什么？

为了找到答案，让我们看看实际被调用的方法 `-[NetConnection execute:timeout:completionBlock:updateCallback:]` 的汇编。具体来说，我们想看看 ARC 发出的函数 epilogue：

```
    …[snipped everything but the final two instructions]…
    0x103FBF3A3    pop     rbp
    ; Tail call to objc_autoreleaseReturnValue()
    0x103FBF3A4    jmp     _objc_autoreleaseReturnValue
```

这就是我们的答案。当 `-[NetConnection execute:timeout:completionBlock:updateCallback:]` 返回给它的调用者时，它是通过所谓的对 `objc_autoreleaseReturnValue()` 的 _尾调用_ 来实现的。

[尾调用](http://en.wikipedia.org/wiki/Tail_call)是在函数中作为最终动作执行的函数（或方法）调用；该函数弹出其栈帧（或从不分配栈帧），然后直接分支到另一个函数。进行尾调用的函数的栈帧 _消失了_——崩溃报告器没有什么可以包含在回溯中。这种尾调用的使用是一种优化策略；通过让 `objc_autoreleaseReturnValue` 在完成后直接返回，我们消除了每个返回自动释放值的 ARC 生成函数本应执行的多余栈清理。

通过调查相关的汇编，我们能够确定实际的调用路径：

- `objc_autorelease()` 出现在该位置回溯中的唯一方式是通过 `-[NetConnection execute:timeout:completionBlock:updateCallback:]` 发出的尾调用。
- `-[NetConnection execute:timeout:completionBlock:updateCallback:]` 发出的唯一尾调用是给 `objc_autorelease()`（通过 `objc_autoreleaseReturnValue()`）。
- `-[NetConnection execute:timeout:completionBlock:updateCallback:]` 将其返回值传递给 ``objc_autoreleaseReturnValue()``。

这就是为什么我们无法仅从源代码或崩溃报告中准确推断这个 bug 的原因；在回溯中有两个不可见的中间调用：

```
    Thread 17 Crashed:
    0   libobjc.A.dylib    0x7fff896392d2 objc_autorelease + 18
    *   libobjc.A.dylib    0x7fff896252a9 objc_autoreleaseReturnValue + 47
    *   ExampleApp         0x000103fbf11a -[EXNetConnection execute:timeout:completionBlock:updateCallback:] (NetConnection.m:106)
    1   ExampleApp         0x000103fbf0f9 -[EXNetConnection execute:timeout:completionBlock:] (NetConnection.m:89)
    …
```

掌握了这些信息，我们现在知道是谁调用了 `objc_autorelease()`，以及用了什么值。我们可以将这个项目添加到我们已证明的初始条件列表中：

- **新的**：传递给 `objc_autorelease()` 的无效参数是 `-[NetConnection execute:timeout:completionBlock:updateCallback:]` 的返回值。
- 传递给 `objc_autorelease()` 的参数是一个有效的、指向已映射内存的指针。
- 在崩溃时，传递给 `objc_autorelease()` 的参数没有指向一个有效的 Objective-C 对象。

我们现在快接近尾声了。

**检查帧 1.1**

```
    Thread 17 Crashed:
    0   libobjc.A.dylib    0x7fff896392d2 objc_autorelease + 18
    *   libobjc.A.dylib    0x7fff896252a9 objc_autoreleaseReturnValue + 47
    *   ExampleApp         0x000103fbf11a -[EXNetConnection execute:timeout:completionBlock:updateCallback:] (NetConnection.m:106)
    1   ExampleApp         0x000103fbf0f9 -[EXNetConnection execute:timeout:completionBlock:] (NetConnection.m:89)
    …
```

既然我们知道 `-[EXNetConnection execute:timeout:completionBlock:updateCallback:]` 返回了一个无效的对象，导致了 `objc_autorelease()` 中的崩溃，剩下的唯一事情就是弄清楚 _为什么_ 这个对象是无效的。

让我们尝试看一下 `-[EXNetConnection execute:timeout:completionBlock:updateCallback:]` 的 Objective-C 实现：

```
    - (EXResponse *) execute: (NSString *) command timeout: (NSTimeInterval) timeout completionBlock: (EXResponseBlock) block updateCallback: (EXUpdateBlock) updateCallback
    {
        EXRequest *request = [[EXRequest alloc] initWithCommand: command timeout: timeout completionBlock: block updateCallback: updateCallback];
        EXRequestHandler *requestHandler = [[EXRequestHandler alloc] initWithRequest: request];
        [self.requestExecutor executeRequest: requestHandler]; // Executes synchronously, on a background thread.
        return requestHandler.response;
    }
```

现在我们渐入佳境了。

我们已经知道我们的崩溃是由无效的返回值引起的，而 `-[EXNetConnection execute:timeout:completionBlock:updateCallback:]` 只在方法末尾的一个地方返回：

```
    return requestHandler.response;
```

这段代码获取 `requestHandler.response` 属性值并返回它。

ARC 规则保证 `requestHandler` 实例本身是有效的：我们创建了它，我们持有一个对它的活跃引用，并且它 _应该_ 保持有效。对于这段代码以我们看到的方式失败，存在两种可能的情况：

A) `EXResponse` 返回的 `requestHandler.response` 属性值在访问时是无效的。

B) `EXResponse` 返回的 `requestHandler.response` 值在获取之后、但 ARC 将其传递给 `objc_autoreleaseReturnValue()` 返回之前，以某种方式并发地 _变得_ 无效了。

让我们看看 `-[EXNetConnection execute:timeout:completionBlock:updateCallback:]` 的汇编，并尝试将这个列表缩小到一个。

**反汇编帧 1**

`-[EXNetConnection execute:timeout:completionBlock:updateCallback:]` 的 x86-64 实现如下；我们将再次详细地逐步分析汇编列表。我们还会跳过不相关的指令，只关注 `requestHandler` 和 `requestHandler.response` 实例的相关生命周期：

```
    ; return requestHandler.response
    0x103FBF36D    mov     rsi, cs:selRef_response
    0x103FBF374    mov     rdi, r13 ; requestHandler handler instance
    0x103FBF377    call    r12 ; _objc_msgSend
    0x103FBF37A    mov     r14, rax
    …
    0x103FBF383    mov     rdi, r14
    0x103FBF386    call    _objc_retainAutoreleasedReturnValue
```

前四条指令通过 `requestHandler.response` 获取 `objc_msgSend(requestHandler, @selector(response))` 属性，并将返回的 `EXResponse *` 结果存储在 `r14` 寄存器中。这段代码成功执行的事实意味着 `requestHandler` 在执行时是有效的。

最后两条指令将返回的 `response` 值移动到第一个参数寄存器 (`rdi`) 中，然后发出对 `objc_retainAutoreleasedReturnValue(response)` 的调用。这个调用要么 retain 这个 `response` 值，要么如果 `requestHandler.response` 将其所有权转移到了我们的方法中，则跳过 retain^[6](#fn-6)——确定发生了哪一个可能使我们能够确定 _何时_ EXResponse 值变得无效。

```
    ; return requestHandler.response
    …
    0x103FBF383    mov     rdi, r14 ; response is in r14
    …
    0x103FBF3A4    jmp     _objc_autoreleaseReturnValue
```

`jmp` 指令发生在 `-[EXNetConnection execute:timeout:completionBlock:updateCallback:]` 方法的末尾；这就是崩溃的、对 `objc_autoreleaseReturnValue(response)` 的尾调用。

`response` 属性被获取，传递给 `objc_retainAutoreleasedReturnValue()`，然后最终通过对 `objc_autoreleaseReturnValue()` 的调用返回。

**Response 对象的生命周期**

值得注意的是，对 `objc_retainAutoreleasedReturnValue()` 的调用 _没有崩溃_，但对 `objc_autoreleaseReturnValue` 的后续调用 _却崩溃了_。我们在对 `frame 0` 的分析中确定崩溃是由无效的 `isa` 指针引起的，我们可以利用这些信息来缩小我们当前的假设范围。

如果 `objc_retainAutoreleasedReturnValue()` 访问了 `response` 对象的 `isa` 并且没有崩溃，那么我们知道 `response` 对象是在方法执行期间并发地变得无效的，_在_ 它被传递给 `objc_retainAutoreleasedReturnValue()` _之后_，但 _在_ 它被交给 `objc_autoreleaseReturnValue()` _之前_。如果我们能证明这一点，我们就知道我们 _可能_ 在处理一个与线程相关的竞态条件。

让我们看看 `objc_retainAutoreleasedReturnValue()` 的实现，来自 Apple 发布的 [objc4-551.1](http://www.opensource.apple.com/source/objc4/objc4-551.1/runtime/NSObject.mm) 运行时源码，看看我们能否确定它是否解引用了对象的 `isa`：

```
    id objc_retainAutoreleasedReturnValue (id obj) {
    #if SUPPORT_RETURN_AUTORELEASE
        if (obj == tls_get_direct(AUTORELEASE_POOL_RECLAIM_KEY)) {
            tls_set_direct(AUTORELEASE_POOL_RECLAIM_KEY, 0);
            return obj;
        }
    #endif
        return objc_retain(obj);
    }
```

这段代码很短，但有点棘手。在 x86-64 和 ARM 上，`SUPPORT_RETURN_AUTORELEASE` 被启用，ARC 使用线程局部存储和返回地址的运行时内省来省略对 `objc_retain()` 和 `objc_autorelease()` 的调用，如果 ARC 可以确认被调用者和调用者都支持此行为。这是一种优化策略，允许使用 ARC 编译的代码将对象的所有权直接返回给其调用者，而无需使用自动释放池的开销。

在调用方，线程局部存储用于确定被调用方是否返回了对象的直接所有权。这就是你在 `objc_retainAutoreleasedReturnValue()` 的实现中看到的——如果每线程的 `AUTORELEASE_POOL_RECLAIM_KEY` 值被设置，并且等于返回对象的指针值，那么调用者已经拥有一个引用，并且 `objc_retain()` 不会被调用。

如果 `AUTORELEASE_POOL_RECLAIM_KEY` _没有_ 被 `requestHandler.response` 属性的 getter 设置，我们就知道 `objc_retain(obj)` 被调用了。如果我们检查 `objc_retain()` 的实现，我们可以看到当传递一个非 NULL、非 tagged pointer 时，它 _确实_ 解引用了 `objc->isa`，就像我们的 `response` 值的情况一样：

```
    id objc_retain(id obj) {
        if (!obj || obj->isTaggedPointer()) {
            goto out_slow;
        }
        if (((Class)obj->isa)->hasCustomRR()) {
            …
        }
        …
        return obj;
    }
```

因此，如果我们能证明 `objc_retain()` 被调用了，我们就证明了 `response` 返回值指向的内存在调用时 _是_ 一个有效的对象，否则调用就会崩溃。如果真是这样，那么我们就将我们的两个假设缩小到一个可证明的初始条件：`EXResponse` 返回的 `requestHandler.response` 值在获取之后、但 ARC 将其传递给 `objc_autoreleaseReturnValue()` 返回之前，以某种方式并发地 _变得_ 无效了。

为了证明这一点，我们需要知道 `AUTORELEASE_POOL_RECLAIM_KEY` 是否被 `requestHandler.response` 属性的 getter 设置。如果它 _没有_ 被设置，那么 `objc_retainAutoreleasedReturnValue()` 成功地调用了 `objc_retain()` 对象上的 `response`。确定这一点的最简单方法是查看 `EXRequestHandler.request` 属性 getter 的实现：

```
    0x103FC3DF2 -[EXRequestHandler response] proc
    ; Standard function prologue
    ; Set up the stack frame
    0x103FC3DF2    push    rbp
    0x103FC3DF3    mov     rbp, rsp

    ; Fetch the offset to the response instance variable
    0x103FC3DF6    mov     rax, cs:_OBJC_IVAR_$_EXRequestHandler_response

    ; Load the response instance variable's pointer value
    ; from self+ivaroffset, and place the result
    ; in the return address register.
    0x103FC3DFD    mov     rax, [rdi+rax]

    ; Standard function epilogue
    ; Restore the frame pointer and return
    0x103FC3E01    pop     rbp
    0x103FC3E02    retn
```

没有设置线程局部值的代码，也没有调用任何其他可能设置它的函数——因此，我们确定无疑地知道 `objc_retainAutoreleasedReturnValue()` 成功地调用了 `objc_retain()` 上的 `response`，并且 `response` 值在它被属性 getter 返回 _之后_ 变得无效。

我们还发现了一些非常有趣的事情：`-[EXRequestHandler response]` 直接返回对其后备实例变量的借用引用（borrowed reference）。这是合成的 `non-atomic` 属性的标准行为，事实上，如果我们查看属性声明，这正是我们所发现的：

```
    @property (nonatomic, readonly, strong) EXResponse *response;
```

如果 `response` 属性在另一个线程上被并发设置，那么在调用 `objc_retain()` _之前_，底层的值可能会被释放。虽然我们已经证明在调用 `response->isa` 时 `objc_retain()` 指针指向可读内存，但我们还没有证明该对象实际上还活着；如果我们在一个已释放的对象上调用 `objc_retain()`，行为是未定义的，而 _没有崩溃_ 只是可能的未定义行为之一。

这意味着我们现在有 _两个_ 新项目要添加到我们的已证明初始条件列表中：

- **新的**：`EXResponse` 返回的 `requestHandler.response` 值作为借用引用返回，并且在没有外部锁定的情况下，在获取和设置该值之间存在竞态条件。
- **新的**：`requestHandler.response` 在获取之后、但在被 `-[NetConnection execute:timeout:completionBlock:updateCallback:]` 返回之前 _变得_ 无效了。
- 传递给 `objc_autorelease()` 的无效参数是 `-[NetConnection execute:timeout:completionBlock:updateCallback:]` 的返回值。
- 传递给 `objc_autorelease()` 的参数是一个有效的、指向已映射内存的指针。
- 在崩溃时，传递给 `objc_autorelease()` 的参数没有指向一个有效的 Objective-C 对象。

我们也有了一个新的——可能是最终的——假设：如果在对 `requestHandler.response` 值进行设置时没有进行外部锁定，并且该值在与 `-EXNetConnection execute:timeout:completionBlock:updateCallback:]` 读取的同时被设置，那么 `response` 对象可能会在该方法之下被释放，并最终在 `objc_autorelease()` 中触发崩溃。与我们分析的其他部分相比，证明这最后一点很容易。

对项目文本的快速搜索返回了两个设置 `response` 属性的方法，都没有任何锁定：一个在服务器响应返回时设置该属性，另一个在发生连接错误时设置该属性。当返回有效响应时，`-[NetConnection execute:timeout:completionBlock:updateCallback:]` 中的代码立即尝试读取 `response` 属性。

如果恰好服务器返回了一个有效的响应，然后紧接着发生了连接错误，该属性将连续被设置两次，导致我们假设的竞态条件，`response` 值在 `-EXNetConnection execute:timeout:completionBlock:updateCallback:]` 之下被释放。

修复方法很简单，Unibox 已经在 beta 版本中推出了它。可以通过同步对 `response` 属性的 _更新_ 来防止竞态条件——如果已经设置了一个 response，那么连接错误就不应该修改该属性值，也就没有意外释放的风险。

Objective-C 也支持 `atomic` 属性标志，它提供原子的 get/set 语义：你总是会收到对底层属性的有效引用，即使它正在被另一个线程并发设置。虽然使用 atomic 属性可以防止崩溃，但它也会掩盖底层的 bug——已经收到了有效的服务器响应，连接失败并不重要，不应该覆盖 `response` 属性。

**结论**

这是一次深入的探索，我希望我们已经提供了一些有用的方法，你可以用它们来分析你自己代码中复杂或难以重现的问题。即使你不精通汇编，利用这种演绎方法也能让你将许多复杂且令人困惑的崩溃分解为可处理、可证明的假设。

如果你精通汇编，我希望我们已经证明了在难以重现的问题上可以深入到什么程度。我们是在事后进行所有这些分析的，只有一份崩溃报告，没有可重现的案例——我们甚至从未实际运行过有问题的应用程序。

在未来的几期中，我们将介绍我们在此分析中使用的一些工具，包括 [Hopper](http://www.hopperapp.com/) 和 [IDA Pro](https://www.hex-rays.com/products/ida/)。如果你有一个特定的崩溃相关主题希望我们介绍，请[发送过来](mailto:landonf@plausible.coop)。

如果你正面对某个特别隐蔽的 bug，或者需要对崩溃报告过程有更深入的了解，我们提供[商业支持服务](https://www.plcrashreporter.org/support/professional)，这是我们开源 [PLCrashReporter](https://www.plcrashreporter.org) 项目工作的一部分。作为帮助我们解决崩溃的交换，你资助了持续的开发，使 PLCrashReporter 变得更好！

---

1. `id objc_autorelease (id obj)` 函数是在引入 ARC 时添加的。详情请参考 [clang 文档](http://clang.llvm.org/docs/AutomaticReferenceCounting.html#arc-runtime-objc-autorelease)。[↩](#fnref-1)
2. 要开始进行汇编级分析，我建议阅读 Mike Ash 关于[对象文件工具](https://www.mikeash.com/pyblog/friday-qa-2011-12-02-object-file-inspection-tools.html)和 [Hopper 反汇编器](https://www.mikeash.com/pyblog/friday-qa-2012-01-06-the-hopper-disassembler.html)的文章，以及 Gwynne Raskind 的“反汇编汇编”系列，[第 1 部分](https://www.mikeash.com/pyblog/friday-qa-2011-12-16-disassembling-the-assembly-part-1.html)、[第 2 部分](https://www.mikeash.com/pyblog/friday-qa-2011-12-23-disassembling-the-assembly-part-2.html)和[第 3 部分](https://www.mikeash.com/pyblog/friday-qa-2011-12-30-disassembling-the-assembly-part-3-arm-edition.html)。[↩](#fnref-2)
3. 在 Mac OS X x86-64 上，`rdi` 寄存器用于第一个函数参数。更多细节，请参考 Apple 的 [Mac OS X](https://developer.apple.com/library/mac/documentation/developertools/conceptual/LowLevelABI/000-Introduction/introduction.html) 和 [iOS](https://developer.apple.com/library/ios/documentation/Xcode/Conceptual/iPhoneOSABIReference/Articles/ARMv7FunctionCallingConventions.html) 调用约定文档。[↩](#fnref-3)
4. Tagged pointers 在 Bavarious 的 [Tagged Pointers in Lion](http://objectivistc.tumblr.com/post/7872364181/tagged-pointers-and-fast-pathed-cfnumber-integers-in) 和 Mike Ash 的 [Let's Build Tagged Pointers](https://www.mikeash.com/pyblog/friday-qa-2012-07-27-lets-build-tagged-pointers.html) 中有深入介绍。[↩](#fnref-4)
5. 请参阅 [Objective-C Runtime 入门](https://www.mikeash.com/pyblog/friday-qa-2009-03-13-intro-to-the-objective-c-runtime.html)了解 Objective-C `isa` 指针的解释。[↩](#fnref-5)
6. ARC 对被调用者的指令应用运行时启发式方法，以确定它是否真的需要在返回前自动释放一个值，还是可以直接将当前引用交给调用者。这样做是为了优化，如果你对原因和方式感兴趣，我建议从 Jonathan Rentzsch 的 [ARC's Fast Autorelease](http://rentzsch.tumblr.com/post/75082194868/arcs-fast-autorelease) 和 Mike 关于[自动引用计数](https://www.mikeash.com/pyblog/friday-qa-2011-09-30-automatic-reference-counting.html)的 Friday Q&A 开始。[↩](#fnref-6)

喜欢这篇文章吗？我卖的书里全是这样的内容！第二卷和第三卷现已出版！提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS feed](https://www.mikeash.com/commentsrss.py?page=pyblog/tales-from-the-crash-mines-issue-1.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被立即删除，恕不另行通知。违规者可能会被我酌情公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
