---
title: 排查程序中的性能问题原因｜Cocoa with Love
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/02/finding-cause-of-simple-performance.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:f4bd5115ccff72f9'
translated: true
---

> 原文：[Finding the cause of performance issues in your programs | Cocoa with Love](https://www.cocoawithlove.com/2010/02/finding-cause-of-simple-performance.html)　·　Cocoa with Love (Matt Gallagher)

本文是对读者提问的回应。有读者问，在我上一篇关于[替换 Core Data 键路径（Key Path）](https://www.cocoawithlove.com/2009/11/performance-tests-replacing-core-data.html)的文章里，我是如何发现最初方案中最大的性能问题是 `NSMutableSet` 的增量重分配。本文将介绍 Mac 上的基本时间分析（time profile）和内存分析（memory profile），并讨论你在尝试解决性能问题时最常需要排查的那些典型场景。

## 概述

在我上一篇博文[《性能测试：替换 Core Data 键路径》](https://www.cocoawithlove.com/2009/11/performance-tests-replacing-core-data.html)中，我介绍了一个简单的分类（category），它能把 Core Data 键路径获取的性能提升 25%–35%（在集合规模较小时，提升幅度其实更大，只是这些场景很少真正构成瓶颈）。这个改进的原理是使用属性访问器（property accessor）直接访问 Core Data 值，而不是按字符串名称查找属性。

然而，为实现这一改进，我最初采用的“朴实”方案所花时间，实则比原始 Core Data 字符串键路径还要多出一倍。

本周，我将介绍我是如何分析这段代码，并找出性能瓶颈所在的。

## 待分析的代码

这段代码的目的是将：

```objc
NSSet *projectNames = [company valueForKeyPath:@"projects.name"];
```

替换为：

```objc
NSSet *projectNames = [company.projects slowObjectValuesForProperty:@selector(name)];
```

但正如方法名中的“slow”所透露的，最初方案的执行速度较慢——大约慢了一倍。

`slowObjectValuesForProperty:` 方法的实现非常简单。我们来看一下：

```objc
- (NSSet *)slowObjectValuesForProperty:(SEL)propertySelector
{
    NSMutableSet *result = [NSMutableSet set];
    for (id object in self)
    {
        id value = [object performSelector:propertySelector];
        if (value)
        {
            [result addObject:value];
        }
    }
    return result;
}
```

这篇推理所采用的测试框架，是[《性能测试：替换 Core Data 键路径》](https://www.cocoawithlove.com/2009/11/performance-tests-replacing-core-data.html)一文附带的 [PropertyAccessors 项目](https://www.cocoawithlove.com/assets/objc-era/PropertyAccessors.zip)，并通过 `ifdef` 只保留“Key Path Accessor”和“slowObjectValuesForProperty: accessor”这两个测试。

## 时间分析器（Time Profiler）

当你的代码运行速度不如预期时，应优先使用基本的时间分析。

在此之前，你应确保测试运行时间足够长，以提供有用的数据。时间分析的工作方式是：定期挂起程序，读取程序当前所处的位置。这相当于在整个时间跨度内做随机采样。但如果时间关键型代码中没有积累到足够多的采样点，这些随机采样就没什么帮助。请增大数据量，或将要检查的代码放入循环中，使其至少运行 2 秒。

在这次测试中，我把 `NumCompanies` 和 `NumProjectsPerCompany` 都设为 100（总数据量为 10,000 个项目名称），并进一步把 `NumTestIterations` 设为 1000（因此该测试共将获取 1000 万个名称）。

这给出了以下测试时长：

```objc
Key Path set iteration test took                4.13078 seconds.
Slow objectValuesForProperty: test took         8.83262 seconds.
```

默认情况下，Time Profiler 每毫秒采样一次。如果你的测试覆盖大量代码，则需要更多采样点——因此要么让测试运行更长时间，要么提高采样频率（Time Profiler 最快可达 20 μs）。

构建项目（但不要直接从 Xcode 运行）。然后选择菜单“Run → Run with Performance Tool → Time Profiler”。你也可以用“Shark”来完成同样的工作，它们运作方式相似，但 Time Profiler 运行在 Instruments 里，界面更美观、更新（不过 Shark 仍能追踪一些 Instruments 尚不具备的底层指标）。

> **iPhone 提示：** Time Profiler 不支持 iPhone 项目。对 iPhone 项目，请从“Run with Performance Tool”菜单中选择“CPU Sampler”。CPU Sampler 开销更高，采样频率和严格程度也较低，但通常也能提供类似的信息。

PropertyAccessors 测试会自动运行，你只需观察即可。对于需要一定交互的其他项目，你需要与程序交互，直到它运行到你想要检查的代码。如果测试持续时间较短或代码量很大，你可能需要点击顶部 Time Profiler Instruments 图标旁边的“i”，更改采样率以获得足够的覆盖率（如果你做了这个更改，需要重新运行测试）。

![](https://www.cocoawithlove.com/assets/objc-era/instruments1.png)

你的窗口应该看起来像这样。如果不是，请确保“Detail”视图可见（你不需要“Extended Detail”视图）。同时确保在“Detail”视图中已选中“Call Tree”视图（即窗口底部看起来像三条略微错开堆放的水平线的图标）。

程序运行完毕后，取消选中左栏中的“Invert call tree”复选框，然后展开“Main Thread → start → `main`”层级，我们将看到 `main()` 函数（本项目中所有测试均在此处运行）里最耗时的步骤。

![](https://www.cocoawithlove.com/assets/objc-era/instruments2.png)

`main()` 函数中的第一项是 `fetchObjectSetForRequest:` 方法，但我们这里不讨论它（这只是 Core Data 加载并预填充整个数据库）。

我们想知道的是，为什么第二项 `slowObjectValuesForProperty:` 所花时间会是第三项 `valueForKeyPath:` 的 2.23 倍。

从 `slowObjectValuesForProperty:` 方法往下展开两层调用树，可以看到 `CFBasicHashAddValue()` 几乎占据了整个方法的时间。

如果再展开 `valueForKeyPath:` 的调用树七层，可以看到同一个 `CFBasicHashAddValue()` 被用来构造这里的 set。但不知为何，这个函数在这里只花了 1402 毫秒，而在 `slowObjectValuesForProperty:` 方法中则花了 5996 毫秒。

同一个函数，处理同样的数据。但一个比另一个慢了约 4 倍。原因何在？

有两种可能的答案：要么慢的情况受困于较差的内存缓存性能，要么它在反复执行，因此因重复而变慢。

## 对象分配

如果你确实认为事件计数（比如缓存未命中和内存带宽）就是问题根源，Shark 可以测量这些——但这里不太可能是。在大多数 Time Profile 无法直接定论的情况下，接下来最值得尝试的就是对象分配（object allocation）分析。

和 Time Profile 一样，我们从 Xcode 的“Run → Run with Performance Tool → Object Allocations”菜单启动 Object Allocations 性能工具。

![](https://www.cocoawithlove.com/assets/objc-era/instruments3.png)

同样，切换到“Call Tree”视图，并确保关闭“Invert Call Tree”和“Separate by Category”。

此外，右键（或 Control-单击）“Detail”视图的表头，确保“Count”和“Bytes”列均已启用。

如果你导航到“Main Thread → start → `main` → `slowObjectValuesForProperty:`”，然后沿着最大的分配项追踪四次，就会看到 `__CFBasicHashRehash` 负责该方法几乎全部的内存分配。

同样，导航到另一项测试的 `valueForKeyPath:`，在七层深处也能看到同一方法分配了其大部分内存。

然而，`__CFBasicHashRehash` 在这两种情形下的内存表现有三个显著差异：

1. `slowObjectValuesForProperty:` 版本执行了 800,000 次分配，而 `valueForKeyPath:` 版本恰好执行了 100,000 次（等于测试次数）。
2. `slowObjectValuesForProperty:` 版本分配了 210.57 MB，而 `valueForKeyPath:` 版本只分配了 97.66 MB。
3. `slowObjectValuesForProperty:` 版本出现在 `CFSetAddValue` 内部，而 `valueForKeyPath:` 版本则出现在 `CFSetCreate` 内部。

从第一点来看，之前“慢版本是因为不必要地自我重复而导致缓慢”的推测看起来是对的——它确实在反复重新分配。

第二点也表明，慢方法浪费了额外的内存（这可能带来了轻微的性能惩罚）。在低内存系统上，后果会更严重。

第三点则揭示了前两点可能的原因：慢方法在添加更多数据时需要重新分配。

## 理解你调用的代码在做什么

所有这些信息都有助于锁定程序的时间都花在了哪里。在此基础上，你大概能想到，一次性分配 `NSMutableSet` 而不是在过程中反复重新分配，是个好办法。

当然，你需要通过实施更改并测试来证实这一点。把这段代码改为只分配一次而不是反复分配，很容易——只需几秒钟。但你需要警惕的是，不要仅凭一时冲动就花太长时间优化代码。代码改动越大，你就越要确信自己确实在修复问题，而不是在检验无关代码或做无益的改动。

正是在这里，深入理解你所摆弄的代码能带来真正帮助。

例如：上面将 `NSMutableSet` 改为单次分配之所以有帮助，其直接原因并非分配本身——因为当继续深挖到底时，`slowObjectValuesForProperty:` 里我们最想优化的时间大头其实花在 `__CFStringEqual` 和 `memcmp` 上，而不是 `malloc`。

事实是，我知道每当 `NSMutableSet` 调整大小，就需要把每一个对象重新哈希（rehash）回新的哈希表。正是这种重新哈希在反复重击 `__CFStringEqual` 和 `memcmp` 函数（因为它们是用于哈希和检测哈希表冲突的函数）。减少重分配能让它变快，但改性能有如此提升的最大原因在于哈希存储的本质：减少重分配，也就减少了对重新哈希的需求。

正如我在原文中报告的，修复这次分配使其只执行一次，这段代码会快上 2.6 倍，但重要的是要理解，重新哈希的需求才是这次改动起效的原因——其他重分配场景未必能获得这么可观的收益。

## 寻找速度提升的最佳候选

不过，一般来说，分配和重分配始终是首要排查点。大量分配在 RAM 中移动开销高昂；数百万次不规则的小分配会造成内存碎片化；而且每次分配通常都要初始化，本身就有一定开销。即便是重分配时无需重新哈希的 `NSArray`，也要把元素从旧数组复制到新数组。虽然性能收益不会那么大，但它仍是一个可以进一步挤压额外性能的地方。

优化时，首先需要寻找的是：

- **内存分配**。它们容易发现，也容易调整。它们未必总能带来最大的性能提升，但它们是很好的第一检查点。
- **在大型数组中迭代以查找元素**。如果需要频繁搜索大型数组，应当改用字典或其他常量时间访问结构来存储。取决于数组大小，这能带来接近翻倍的提速。换句话说，永远不要搜索任何规模超过微不足道的数组。
- **对中型到大型数据集的嵌套循环**。容易发现。尽量消除嵌套。消除嵌套可能很难，因为需要重新思考数据的访问方式，但往往能做一些事情来减轻其影响。如果某个循环内还有一个循环，应尽量把元素较少的循环放在内层，因为内存更适合处理大量小批次的作业。
- **对规模非平凡数据集的任何非多项式操作**。非多项式操作是你可能采用的最慢、最糟糕的做法。偶尔确实不可避免，但如果有可能，请重新设计。什么是非多项式？处理一个集合时，如果涉及的工作包（packet）数量相对于集合大小的增长速度超过多项式级别，那就是非多项式。具体说：记工作包数为 y，集合中对象数为 x，非多项式意味着对于大的 x，工作包数超过 y=x^a（a 为任意常数）。指数增长（y=a^x）或阶乘增长（y=x!）是最常见的非多项式增长形式。如果这些让你困惑，至少请记住最常见场景：通过穷举测试每一个组合来寻找一组对象的顺序或排列，就是非多项式的。

你可能忍不住认为，遍地开花的多线程、OpenCL、SSE 向量化或汇编优化才是解决性能问题的最佳方式，毕竟它们都是“高性能”技术，最快的程序都多少用到了其中几种。然而，实现这些技术比简单的设计改进困难得多，因此它们永远应该排在最后——只有在你确信设计无法再改进之后，才去考虑。

## 结论

优化的第一条规则是：始终基于证据来优化。

如果找不到瓶颈，或者无法用数据制造出一个瓶颈，就不要开始优化。在没有实际瓶颈证据的情况下进行优化（仅仅怀疑将来可能出现瓶颈），被称为“[过早优化（Premature Optimization）](http://c2.com/cgi/wiki$?PrematureOptimization)”，通常被视为浪费时间。

然而，即使你知道瓶颈在哪里，也需要知道是什么导致了它。如果代码规模很小，可以直接动手摆弄看效果，但一般还是需要仔细检查。关于性能问题原因，很容易做出错误猜测，然后白白浪费时间改代码，最终毫无增益——这种情况比你想象的要常见。

希望我已向你展示了如何收集理解简单性能问题所需的信息，以及你需要借助哪些线索来缩小范围，找到代码中可以改进的位置。
