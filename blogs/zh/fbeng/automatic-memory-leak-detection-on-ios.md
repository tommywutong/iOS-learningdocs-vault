---
title: iOS 上的自动内存泄漏检测
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2016/04/13/ios/automatic-memory-leak-detection-on-ios/'
original_language: en
published: 2016-04-13
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c9da9163749a5d36'
translated: true
---

> 原文：[Automatic memory leak detection on iOS](https://engineering.fb.com/2016/04/13/ios/automatic-memory-leak-detection-on-ios/)　·　Meta Engineering — iOS

移动设备上的内存是一种共享资源。管理不当的 App 会耗尽内存、崩溃，并导致性能大幅下降。

Facebook for iOS 有许多功能，它们共享同一块内存空间。如果某个特定功能开始消耗过多内存，就可能影响整个 App。例如，一个功能意外引入了内存泄漏，就会发生这种情况。

当我们把内存的某一部分分配给一组对象，但在使用完毕后忘记释放时，就会发生内存泄漏。这意味着系统永远无法回收这部分内存用于其他用途，最终会导致可用内存耗尽。

在 Facebook，许多工程师在我们代码库的不同部分工作。内存泄漏难免会发生，一旦发生，我们需要快速找到并修复它们。

已有一些工具可以用来查找泄漏，但它们需要大量的人工干预：

1. 打开 Xcode，为性能分析构建。
2. 启动 Instruments。
3. 使用 App，尽量重现尽可能多的场景和行为。
4. 观察泄漏/内存峰值。
5. 追查内存泄漏的源头。
6. 修复问题。

这意味着每次都要重复大量的手动工作。正因如此，我们可能无法在开发周期的早期发现并修复内存泄漏。

将这个过程自动化，可以让我们在无需太多开发者介入的情况下更快地发现内存泄漏。为了解决这个问题，我们构建了一套工具来实现自动化，并修复了我们自己代码库中的许多问题。今天，我们激动地宣布，我们将开源这些工具：[FBRetainCycleDetector](https://github.com/facebook/FBRetainCycleDetector)、[FBAllocationTracker](https://github.com/facebook/FBAllocationTracker) 和 [FBMemoryProfiler](https://github.com/facebook/FBMemoryProfiler)。

## 保留环（Retain Cycle）

Objective-C 使用引用计数（Reference Counting）来管理内存和释放不再使用的对象。内存中的任何对象都可以“retain（保留）”另一个对象，只要第一个对象需要，就能将另一个对象保留在内存中。一种理解方式就是对象“拥有（own）”其他对象。

这种情况在大多数时候运行良好，但当两个对象最终互相“拥有”时——直接地，或者更常见地，通过连接它们的对象间接地——我们就会陷入僵局。这种拥有引用的循环称为保留环（retain cycle）。

![](https://engineering.fb.com/wp-content/uploads/2016/04/GOhLxgDdpE-xixYEAL7PWUwAAAAAbj0JAAAB.jpg)

保留环可能引发一系列问题。最好的情况，如果对象无限期占用 RAM 空间，只会浪费少量内存。如果泄漏的对象正在积极执行一些非琐碎的任务，那么 App 其他部分可用的内存就会减少。最坏的情况，如果泄漏导致 App 使用的内存超过可用内存，App 可能会崩溃。

在手动的性能分析过程中，我们发现我们经常遇到不少保留环。它们很容易被引入，但之后却很难被发现。Retain Cycle Detector 让发现它们变得容易。

## 运行时保留环检测

在 Objective-C 中查找保留环，类似于在有向无环图中查找环——其中节点是对象，边是对象之间的引用（因此，如果对象 A 保留了对象 B，就存在从 A 到 B 的引用）。我们的 Objective-C 对象已经在图里了；我们只需要使用深度优先搜索来遍历它。

这是一个非常简单的抽象，效果却很好。我们必须确保能够将对象作为节点来使用，并且对于每个对象，能够获取它引用的所有对象。这些引用可能是弱引用（weak）或强引用（strong）。保留环只由强引用引起。因此，对于每个对象，我们需要弄清楚如何只找到那些强引用。

幸运的是，Objective-C 提供了一个强大的、内省（introspective）的运行时库，可以为我们提供足够的数据来深入分析这个图。

图中的节点可以是对象，也可以是 block。让我们分别讨论如何遍历它们。

### 对象

运行时提供了很多工具，让我们可以探查对象并了解它们的大量信息。

首先，我们可以获取对象所有实例变量（instance variable）的布局（即“ivar layout”）。

```
    const char *class_getIvarLayout(Class cls);
    const char *class_getWeakIvarLayout(Class cls);
```

对于给定的对象，ivar layout 描述了我们应该在哪里寻找它引用的其他对象。它会提供一个“索引（index）”，表示我们需要加到对象地址上的偏移量，以获取它引用的对象的地址。运行时还允许我们获取“weak ivar layout”，即该对象所有弱实例变量的布局。我们可以假设这两个布局的差异就是强引用（strong）的布局。

此外，对于 Objective-C++ 也有部分支持。在 Objective-C++ 中，我们可以在结构体（struct）中定义对象，而这些对象不会被包含在 ivar layout 中。运行时提供了“类型编码（type encoding）”来处理这种情况。对于每个实例变量，类型编码描述了变量的结构方式。如果它是一个结构体，它会描述它包含的字段和类型。我们解析类型编码来找出哪些实例变量是 Objective-C 对象。我们对它们计算偏移量，如同在布局中一样，获取它们所指向对象的地址。

还有一些边界情况我们不会深入探讨。这些主要是集合（collection），它们的行为不同，我们必须实际枚举它们才能获取它们保留的对象，这可能会产生一些副作用。

### Block

Block 与对象略有不同。运行时不允许我们轻易查看它们的布局，但我们仍然可以玩一个“猜谜游戏”。

在处理 block 时，我们使用了 Mike Ash 在他的项目 [Circle](https://github.com/mikeash/Circle) 中提出的思路——该项目正是 FBRetainCycleDetector 最初的灵感来源。

我们可以利用 [block 的应用程序二进制接口](http://clang.llvm.org/docs/Block-ABI-Apple.html)（ABI）。它描述了 block 在内存中的布局。如果我们知道正在处理的是一个 block，我们可以将它转换为一个模拟 block 的伪结构体。在将 block 转换为 C 结构体后，我们就知道 block 保留的对象保存在哪里。不幸的是，我们无法知道这些引用是强引用还是弱引用。

为此，我们使用了一种黑盒技术。我们创建一个对象，假装成我们想要调查的 block。因为我们知道 block 的接口，我们知道在哪里可以找到这个 block 持有的引用。在这些引用的位置上，我们的假对象将放置“释放探测器（release detector）”。释放探测器是一些小对象，用于观察发送给它们的 release（释放）消息。当所有者想要放弃所有权时，会向强引用发送这些消息。当我们的假对象被释放时，我们可以检查哪些探测器收到了这样的消息。知道了这些探测器的索引位置，我们就能找到原始 block 所拥有的实际对象。

![](https://engineering.fb.com/wp-content/uploads/2016/04/GNNLxgApnIqZ_IEDABvZygYAAAAAbj0JAAAB.jpg)

## 自动化

当该工具在员工的内部构建版本上持续自动运行时，才真正大放异彩。

客户端部分的自动化很简单。我们通过一个定时器安装 Retain Cycle Detector，并定期扫描部分内存以发现保留环。不过，这也并非一帆风顺。第一次运行检测器时，我们发现它无法足够快地遍历整个内存空间。我们需要为它提供一组候选对象，让它从这些对象开始检测。

为此，我们构建了 FBAllocationTracker。这个工具主动跟踪 NSObject 的所有子类实例的分配和释放。它可以在任何时刻以最小的性能开销快速获取任何类的任何实例。

在客户端实现自动化，意味着只需在一个 NSTimer 上使用 FBRetainCycleDetector，并结合使用 FBAllocationTracker 来获取我们想要检查的实例。

现在让我们仔细看看后端发生了什么。

保留环可以由任意数量的对象组成。当一个错误的链接导致产生多个循环时，事情就变得复杂多了：

![](https://engineering.fb.com/wp-content/uploads/2016/04/GO1LxgBIsPz1vjIGANOhgG8AAAAAbj0JAAAB.jpg)

<sub>A→B 是一个循环中的错误链接，由此产生了两种循环：A-B-C-D 和 A-B-C-E。</sub>

这导致了两个问题：

1. 我们不想将由同一个错误链接引起的两个保留环分别标记。
2. 如果两个保留环可能代表两个不同的问题，即使它们共享一个链接，我们也不想把它们标记在一起。

因此，我们需要为保留环定义集群。我们编写了一个算法，使用以下启发式方法来查找这些集群：

1. 收集一天内检测到的所有保留环。
2. 对于每个保留环，提取 Facebook 特定的类名。
3. 对于每个保留环，找到已被报告且包含在此保留环中的最小保留环。
4. 将每个保留环添加到由上述最小保留环代表的组中。
5. 仅报告最小保留环。

有了这些，最后一步就是找出谁可能意外地引入了保留环。我们通过对保留环涉及的代码部分运行 'git/hg blame'，猜测最可能是最近的改动导致了问题。最后修改该代码的人会收到一个需要修复问题的任务。

整个系统可以示意如下：

![](https://engineering.fb.com/wp-content/uploads/2016/04/GNlLxgCSeC_a8M4AABSqX0oAAAAAbj0JAAAB.jpg)

## 手动性能分析

虽然自动化有助于简化查找保留环的过程并减少开发者的开销，但手动性能分析仍有其用武之地。我们构建的另一个工具允许任何人查看 App 的内存使用情况，甚至无需将手机连接到电脑。

FBMemoryProfiler 可以轻松地添加到任何 App 中，让你能够手动分析你的构建版本，并在 App 内部运行保留环检测。它通过同时利用 FBAllocationTracker 和 FBRetainCycleDetector 来实现这一点。

### 代（Generations）

FBMemoryProfiler 提供的重要功能之一是“代跟踪（generation tracking）”，类似于 Apple Instruments 中的代跟踪。代就是在两个时间标记之间分配的所有存活对象的快照（snapshot）。

使用 FBMemoryProfiler 的界面，我们可以标记一个代，例如，分配三个对象。然后标记另一个代，继续分配对象。第一个代包含我们的前三个对象。如果任何对象被释放，它将被从第二个代中移除。

![](https://engineering.fb.com/wp-content/uploads/2016/04/GNhLxgAq1aLxqu0AAF9_FxMAAAAAbj0JAAAB.jpg)

当我们有一项重复性任务，认为可能导致内存泄漏时，代跟踪就非常有用，例如，在视图控制器中反复进入和退出。我们每次开始任务时都标记一个代，然后调查每个代中剩下了什么。如果一个对象存活的时间超出了预期，我们可以在 FBMemoryProfiler 界面上清晰地看到它。

## 快来试试吧

无论你的 App 是大是小，功能繁多还是寥寥无几，良好的内存管理都是优秀的工程实践。借助这些工具，我们能够更轻松地发现和修复内存泄漏，从而将更少的时间花在手动流程上，更多的时间用于编写更好的代码。希望它们也能对你有用。现在就来 GitHub 上看看吧：[FBRetainCycleDetector](https://github.com/facebook/FBRetainCycleDetector)、[FBAllocationTracker](https://github.com/facebook/FBAllocationTracker) 和 [FBMemoryProfiler](https://github.com/facebook/FBMemoryProfiler)。
