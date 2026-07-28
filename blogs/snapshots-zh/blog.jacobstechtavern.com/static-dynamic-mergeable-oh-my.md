---
title: 静态、动态、可合并，天哪！
source_url: 'https://blog.jacobstechtavern.com/p/static-dynamic-mergeable-oh-my'
source_domain: blog.jacobstechtavern.com
source_group: single-site
original_language: en
published: 2024-11-18
archived_at: 2026-07-27
content_hash: 'sha256:70e19aa0537d35e4'
plan_ref: 第七周：编译、链接、Mach-O、dyld 与 App 启动 / Day 4｜在 Mach-O 基础上学习 dyld（对应 W1-08）
plan_week: 第七周：编译、链接、Mach-O、dyld 与 App 启动
plan_day: Day 4｜在 Mach-O 基础上学习 dyld（对应 W1-08）
container: //article
container_source: guess
translated: true
---

> 原文：[Static, Dynamic, Mergeable, oh, my!](https://blog.jacobstechtavern.com/p/static-dynamic-mergeable-oh-my)

# 静态、动态、可合并，天哪！

### 库（Library）、框架（Framework）与链接（Linking）的理论指南

[![Jacob Bartlett 的头像](../../../attachments/snapshots/blog.jacobstechtavern.com/4c8fdc0cbdec/82b57dbce3824ce60df3.jpg)](https://substack.com/@jacobbartlett)

[Jacob Bartlett](https://substack.com/@jacobbartlett)

2024 年 11 月 18 日

![](../../../attachments/snapshots/blog.jacobstechtavern.com/4c8fdc0cbdec/a921e75e0955488404e8.jpg)

如果你想难倒一位资深 iOS 工程师，那就让他解释动态框架（Dynamic Framework）和静态库（Static Library）的区别。

这些概念极其重要，但多年来，它们一直被我装在大脑里一个名为“总有一天我会搞懂，但在那之前，我只能继续带着冒名顶替综合征”的盒子里。

除非你正在努力减少 App 体积、简化依赖图、优化启动性能或加快构建时间，否则你无法将这些知识付诸实践。

> _订阅 Jacob's Tech Tavern（免费），每周在收件箱中获取关于 iOS、Swift、技术和独立项目的深入文章。_
>
> _完整订阅者可以解锁 **Quick Hacks**（我的高级技巧系列），并享受我长文的独家抢先阅读权限。_

让我们通过一份关于**库**、**框架**和**链接**的入门指南来改变这一点，然后理解**静态**和**动态**的含义。最后，我们将学习 Xcode 中新增的**可合并**库。

### 库与框架

如果你以全新的视角来看待，库和框架实际上是非常直接的概念。

> _它们让人感到困惑的主要原因，通常是解释得非常糟糕。_

#### 库

**库（Library）** 是纯粹的代码。它们可以被导入到你的项目中，以提供可复用的类和函数。库可以是静态的（`.a`）或动态的（`.dylib`）。我们将在后面的“链接”部分探讨静态库和动态库之间的区别。

#### 框架

**框架（Framework）** 是包含一个库的文件夹。这个库可以是静态的或动态的，文件夹会继承这个属性——如果它包含一个静态库，就成为静态框架；如果包含一个 dylib，就成为动态框架。

除了库之外，框架文件夹还包含额外的资源和元数据，包括：

- 素材目录
- 字符串、nib 文件、Objective-C 头文件和元数据
- 代码签名
- 文档

这是一个真实的（动态）`.framework` 文件夹的样子：

![](../../../attachments/snapshots/blog.jacobstechtavern.com/4c8fdc0cbdec/a25c0f8a809654317c44.jpg)

<sub>包含素材、代码签名、Info.plist 和 Unix 可执行文件的动态框架文件夹</sub>

你可以看到素材、代码签名和 `Info.plist` 元数据。代码本身被打包成一个二进制文件（Unix Executable File）。这个文件已经编译完成，并准备好链接到 App。

#### 库素材与 Bundle

库本身不包含素材，但你可以通过一个资源 **bundle**（在 Swift Package 中默认名为 _Media_）来创建它们。这些资源作为 `.bundle` 文件的一部分包含在 App 中。

这个示例 App 包含一个 `TavernUI` 库，其中包含一个[设计系统](https://blog.jacobstechtavern.com/p/enums-and-design-systems)和素材。`TavernUI` 库中的代码直接链接到主可执行文件 `TavernTools` 中。包含素材的 `TavernUI.bundle` 文件被单独打包在主要的 `.app` bundle 内。

![](../../../attachments/snapshots/blog.jacobstechtavern.com/4c8fdc0cbdec/1525030d55efe7d6d210.jpg)

<sub>在 .app bundle 内可见的来自库的资源 bundle</sub>

### 什么是链接？

在计算机科学中，**链接器（linker）** 将编译后的目标文件组合成一个单一的可执行实体。

如果你在一家拥有庞大复杂 App 的公司工作，你的 App 可能由一个主 target（加上扩展）、几个功能模块、用于核心工具的其他层以及第三方依赖项组成。

这些模块由 Swift 编译器处理，然后链接器……嗯，_链接_ 这些编译后的模块。它们最终被合并成一个操作系统可以运行的单一程序：你的 App。

这个链接何时发生？**视情况而定。**

### 静态链接

**静态链接（Static Linking）** 是 Swift 编译器的最后一个阶段。在 Swift 经过 [SIL](https://blog.jacobstechtavern.com/p/swift-intermediate-language)、优化和 [LLVM IR](https://blog.jacobstechtavern.com/p/cow2llvm-the-isknownuniquelyreferenced) 处理之后，最终成为目标文件（`.o`）中的机器码（即 ARM 汇编），看起来像这样：

```
mov x0, #0x0   ; Move 0 into register x0
bl  _printf    ; Branch to the printf function
ret            ; Return from the function
```

这段汇编代码在目标文件中表示为 `TEXT`。除了这些高度优化的机器码，目标文件还包含：

- 符号表，将函数和变量映射到你正在运行的程序中的内存地址。
- 全局变量和静态变量，在文件中表示为 `DATA`。
- 调试信息，也称为 `DWARF`。

#### 静态复制

如果你的库或框架是静态的，那么在静态链接期间，其编译后的目标文件会被复制到主 Unix 可执行文件中。

理解这种复制至关重要：**静态链接与动态链接的性能特征，都是这种编译时复制的下游结果**。

如果你有大型库，将它们全部复制到二进制文件中需要很长时间。更糟糕的是，如果你的 App 有复杂的依赖图，导入了许多相互依赖的库，即使对于增量构建，这种复制也会重复发生。**对开发者而言，这表现为更长的构建时间**。

静态链接完成后，我们会得到一个单一的 Mach-O 可执行文件，它由主 App 中的编译后目标文件，与依赖图中所有静态库和框架的目标文件链接而成。

这个单一的静态链接可执行文件由操作系统加载以运行你的 App。由于它只是一个单一文件，启动速度非常快。

这使得静态链接对于最终用户来说非常棒。这种用户体验的优势就是为什么非系统模块默认会被静态链接到你的 App 中。

#### 静态膨胀

如果你的 App 很大或很复杂，你可能包含扩展 target，例如小组件或通知分享扩展。

如果不小心，你可能会遇到静态链接最大的缺点：静态库和框架——连同它们关联的资源 bundle——会被复制到**每个 target** 中。

这会急剧增加你的 App 体积。

![](../../../attachments/snapshots/blog.jacobstechtavern.com/4c8fdc0cbdec/534edd50751d267317ee.jpg)

<sub>TavernUI 资源 bundle 被复制到一个 App 和每个扩展 target 中</sub>

### **动态链接**

**动态链接**的库和框架是在**运行时**由名为 dyld 的系统进行链接的。

在动态链接期间，动态库或框架被加载到 App 进程的虚拟内存地址空间中。它的函数被映射到内存中，就像主可执行文件中的函数一样。

在编译时，动态库和框架大体上经历了与任何 Swift 代码完全相同的编译步骤。然而，在链接阶段，不是将整个可执行文件复制到主可执行文件中，而是只复制动态链接模块的**文件夹位置**。这使得它们的增量构建时间几乎可以忽略不计。

> _我需要快速澄清一个非常常见的误解：动态库和框架 **不是**按需链接的。_
>
> _它们在启动时，在 pre-`main()` 阶段（也就是你的任何代码执行之前），就被映射到进程内存地址空间中。因此，如果过度使用动态框架，可能会对启动时间产生负面影响。_

#### 性能特征

现在我们了解了动态链接的机制，就很容易理解我们观察到的与静态链接相比的性能特征了。

- **动态链接的构建时间更快**，因为可执行文件中只嵌入了一个文件夹引用，而不是复制整个模块。
- **动态链接的启动时间更慢**，因为 dyld 需要在 App 启动的 pre-`main()` 阶段将代码映射到 App 进程中。
- **动态链接减少了重复**，因为相同的动态框架或库可以在运行时被链接到每个需要它的 target。

这种对启动时间的负面影响有多显著？你可以使用 App Launch instrument 自行分析。

![](../../../attachments/snapshots/blog.jacobstechtavern.com/4c8fdc0cbdec/aa5de86f14e771ee0e0f.jpg)

你将能够测量并识别每个动态框架的 pre-`main()` 启动时间。根据我的经验，每个框架的时间变化很大，从几百纳秒到几十毫秒不等。由于 [dyld 缓存优化](https://developer.apple.com/documentation/xcode/reducing-your-app-s-launch-time)，首次启动通常比冷启动慢。

![](../../../attachments/snapshots/blog.jacobstechtavern.com/4c8fdc0cbdec/489bba2a3fcec2581a4d.jpg)

#### 动态链接与优化

还有另一个鲜为人知的因素需要考虑：动态链接的框架和库可能**优化程度较低**。

由于动态链接的模块是与 App 的其他模块独立编译的，它们不会进行[死代码剥离](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/CodeFootprint/Articles/CompilerOptions.html)，因为 Swift 编译器在编译时无法知道哪些函数需要被映射到 App 进程中。

因此，即使你将它们导入到多个 target 中，动态框架和库也不能保证比静态链接模块更节省空间。这可能导致出乎意料的结果，与标准教条相悖。

我最近遇到一个情况，一个小的依赖项 [Factory](https://github.com/hmlongco/Factory) 由于这种天真的体积优化方法，被作为动态框架导入到多个 target。然而，这个优化较少的框架，连同其所有元数据，总计达到了 **200kB**。

当它被作为静态库链接时，只占用了微小的 **15kB**，这意味着我可以略微改善启动时间性能，**并**节省 bundle 空间。

这里的教训是：**分析你自己的 App**！

#### 系统框架

Apple 系统框架，如 Foundation、SwiftUI 和 CoreGraphics，是动态链接到 App 的。这允许它们位于操作系统的一个地方，而不是捆绑到每个已安装的应用程序中。

> _像 Foundation 这样的系统框架在内部实际上是高度模块化的，“Foundation”是包裹它们的伞框架（Umbrella Framework）的名称。_

这些动态系统框架由 dyld 在 pre-`main()` 启动步骤中链接到你的 App 进程，但 Apple 使用 _[dyld 共享库缓存](https://www.nowsecure.com/blog/2024/09/11/reversing-ios-system-libraries-using-radare2-a-deep-dive-into-dyld-cache-part-1/)_ 极大地优化了这种链接。该缓存是所有主要系统库的预链接集合，被映射到你的 App 进程的地址空间中。

### 可合并库

可合并库（Mergeable Library）是 Xcode 15 中引入的一种热门的新链接策略方法。由于我们现在理解了它们试图解决的问题，它们实际上非常直接。

可合并库被设计为在 **Debug** 构建中**动态**链接，在 **Release** 构建中**静态**链接。

这表面上给了它们两全其美的特性：

- 动态链接的编译时优势，改善开发者体验和迭代速度。
- 面向生产用户的静态链接的启动时优势。

![](../../../attachments/snapshots/blog.jacobstechtavern.com/4c8fdc0cbdec/59b6ce5696fd326107b9.jpg)

<sub>来自 WWDC Notes；[认识可合并库](https://wwdcnotes.com/documentation/wwdcnotes/wwdc23-10268-meet-mergeable-libraries/)</sub>

任何动态框架或库都可以通过设置 Xcode 构建设置中的 `MERGED_BINARY_TYPE` 来构建为可合并。这会指示静态链接器在 `.dylib` 旁边生成元数据，使其能够在 Release 构建中被静态链接。

这个元数据大致会使库的体积翻倍，这促使一位 HackerNews 用户[认为该模块只是将静态库和动态库捆绑在一起](https://news.ycombinator.com/item?id=36232861)。

我个人诚实的评估是：可合并库被设计为那些理解依赖图和优化构建系统不是高优先级的工程团队的**一个良好默认选择**。公平地说，这可能是大多数 iOS 团队（以及独立开发者）的情况。

[Tuist 团队](https://docs.tuist.io/en/guides/develop/projects/cost-of-convenience)对可合并库有更细致的看法：

> 动态框架虽然更灵活、更易用，但会对 App 的启动时间产生负面影响。另一方面，静态库启动更快，但会影响编译时间，并且稍微难处理一些，尤其是在复杂的依赖图场景中。如果能根据配置在不同方案间切换，岂不是很棒？这一定是苹果在决定开发可合并库时的想法。但再次地，他们将更多的构建时推断转移到了构建时。如果说推理依赖图已经很困难了，那么想象一下，当 target 的静态或动态属性将在构建时根据某些 target 中的某些构建设置来决定时，情况会怎样。祝你在确保 SwiftUI 预览等功能不崩溃的前提下，让它能可靠地工作。
>

虽然可合并库的好处显而易见，但它们没有考虑到影响静态和动态链接选择的另一个重大权衡：**target 之间模块的重复**。这通常是决定依赖项或库是否为动态的主要因素，但这一点被完全忽略了。

我个人非常希望看到资源捆绑系统的彻底改革。要将共享资源捆绑到框架中，我们需要[痛苦且不直观的变通方法](https://www.emergetools.com/blog/posts/make-your-ios-app-smaller-with-dynamic-frameworks)。目前，框架默认会将其资源通过 `.bundle` 重复复制到每个 target 中。

### 结论

我希望你学到了很多，并且当下次有人问为什么你的模块是动态的时候，你可以在你的团队面前显得非常聪明。

一旦你扎实掌握了链接器的工作原理，你就解锁了让你在任何工程团队中都成为宝贵资源的技能：

- App 体积优化
- 依赖图简化
- 启动速度提升
- 构建时间缩短

如果我能给出任何真正的建议，那就是那句老话：**分析你的 App！** 不要盲目听信网上的某些人。找出最适合你情况的方法。

我已经给了你工具，_现在去应用它们吧！_

> _喜欢 Jacob's Tech Tavern？分享给他人！推荐一位朋友作为免费订阅者，以解锁一个月的免费完整订阅。_

[推荐给朋友](https://blog.jacobstechtavern.com/leaderboard?&utm_source=post)
