---
title: NSOperation
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/nsoperation/'
original_language: en
published: 2014-07-14
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:22574defdd3168e4'
translated: true
---

> 原文：[NSOperation](https://nshipster.com/nsoperation/)　·　NSHipster (Mattt)

# [NSOperation](https://nshipster.com/nsoperation/)

作者：[Mattt](https://nshipster.com/authors/mattt/)　2014 年 7 月 14 日

生活中总有做不完的事。每一天都会带来源源不断的任务和杂务，填满我们存在的每个工作小时。

然而，无论个人待办清单变得多么繁重，与 iOS App 的工作量相比都相形见绌——它需要完成数百万次计算，同时还要每 16 毫秒绘制一帧。

无论在生活还是编程中，生产力归根结底都是关于调度、优先级排序和任务多任务处理的问题，以便维持良好的表现。

让 App 响应迅速的秘密在于尽可能将不必要的工作转移到后台。在这方面，现代 Cocoa 开发者有两个选择：[Grand Central Dispatch](https://en.wikipedia.org/wiki/Grand_Central_Dispatch) 和 [`NSOperation`](https://developer.apple.com/library/mac/#documentation/Cocoa/Reference/NSOperation_class/Reference/Reference.html)。本文将主要关注后者，但需要注意的是两者相辅相成（稍后会详细说明）。

---

`NSOperation` 表示一个单一的工作单元。它是一个抽象类，提供了一个有用的、线程安全的结构，用于对状态、优先级、依赖关系和管理进行建模。

> 对于构建自定义 `NSOperation` 子类不合适的场景，Foundation 提供了具体实现 [`NSBlockOperation`](https://developer.apple.com/library/ios/documentation/cocoa/reference/NSBlockOperation_class/Reference/Reference.html) 和 [`NSInvocationOperation`](https://developer.apple.com/library/mac/documentation/cocoa/reference/NSInvocationOperation_Class/Reference/Reference.html)。

非常适合 `NSOperation` 的任务示例包括[网络请求](https://github.com/AFNetworking/AFNetworking/blob/master/AFNetworking/AFURLConnectionOperation.h)、图像大小调整、文本处理，或任何其他可重复、结构化、运行时间长且会产生相关状态或数据的任务。

但是，仅仅将计算包装到对象中，如果没有一点监督，作用并不大。这就是 `NSOperationQueue` 的用武之地：

## NSOperationQueue

`NSOperationQueue` 调节操作的并发执行。它充当一个优先级队列，使得操作大致按[先进先出（First-In-First-Out）](https://en.wikipedia.org/wiki/FIFO)的方式执行，优先级更高的操作（`NSOperation.queuePriority`）可以排在优先级较低的操作之前。`NSOperationQueue` 还可以使用 `maxConcurrentOperationCount` 属性限制在任何给定时刻可以执行的并发操作的最大数量。

> NSOperationQueue 本身由 Grand Central Dispatch 队列支持，不过这是一个私有的实现细节。

要启动一个 `NSOperation`，可以调用 `start`，或者将其添加到一个 `NSOperationQueue` 中，让它一旦到达队列前端就开始执行。**由于 `NSOperation` 的很多好处都来自 `NSOperationQueue`，因此几乎总是将操作添加到队列中，而不是直接调用 `start`。**

## 状态

`NSOperation` 编码了一个相当优雅的状态机来描述操作的执行：

> `ready` → `executing` → `finished`

没有显式的 `state` 属性，状态是通过对这些关键路径的 KVO 通知隐式确定的。当一个操作准备就绪可以执行时，它会发送一个针对 `ready` 关键路径的 KVO 通知，相应的属性随后会返回 `true`。

每个属性必须彼此互斥，以编码一致的状态：

- `ready`：返回 `true` 表示操作已准备好执行，或返回 `false` 表示仍有依赖的未完成的初始化步骤。
- `executing`：如果操作当前正在处理其任务，则返回 `true`，否则返回 `false`。
- `finished`：如果操作的任务成功完成执行，或者操作被取消，则返回 `true`。`NSOperationQueue` 在 `finished` 变为 `true` 之前不会将操作出队，因此在子类中正确实现这一点以避免死锁至关重要。

## 取消

提前取消操作以防止执行不必要的工作通常很有用，无论是由于依赖操作失败还是用户显式取消。

与执行状态类似，`NSOperation` 通过 `cancelled` 关键路径的 KVO 来传达取消信息。当一个操作被取消时，它应该尽快清理任何内部细节并尽快进入合适的最终状态。具体来说，`cancelled` 和 `finished` 的值都需要变为 `true`，而 `executing` 需要变为 `false`。

需要注意的一件事是单词“cancel”的拼写特殊性。尽管拼写因方言而异，但对于 `NSOperation`：

- `cancel`：函数（动词）使用一个 L
- `cancelled`：属性（形容词）使用两个 L

## 优先级

并非所有操作都同等重要。设置 `queuePriority` 属性将根据以下排名提升或推迟 `NSOperationQueue` 中的操作：

### NSOperationQueuePriority

```
public enum NSOperationQueuePriority : Int {
    case VeryLow
    case Low
    case Normal
    case High
    case VeryHigh
}
```

```
typedef NS_ENUM(NSInteger, NSOperationQueuePriority) {
    NSOperationQueuePriorityVeryLow = -8L,
    NSOperationQueuePriorityLow = -4L,
    NSOperationQueuePriorityNormal = 0,
    NSOperationQueuePriorityHigh = 4,
    NSOperationQueuePriorityVeryHigh = 8
};
```

## 服务质量

服务质量（Quality of Service）是 iOS 8 和 OS X Yosemite 中引入的一个新概念，它为调度系统资源提供了一致的、高级别的语义。针对 [XPC](https://developer.apple.com/library/mac/documentation/macosx/conceptual/bpsystemstartup/chapters/CreatingXPCServices.html) 和 `NSOperation` 都引入了使用此抽象的 API。

对于 `NSOperation`，`threadPriority` 属性已废弃，取而代之的是这个新的 `qualityOfService` 属性。（真是谢天谢地——`threadPriority` 过于笨重，对大多数开发者来说只能是负累。）

服务级别根据分配的 CPU、网络和磁盘资源数量来建立操作的系统级优先级。更高的服务质量意味着将提供更多资源来更快地执行操作工作。

> QoS 似乎底层使用了 [OS X Mavericks 中引入的 XNU 内核任务策略功能](http://www.opensource.apple.com/source/xnu/xnu-1456.1.26/osfmk/mach/task_policy.h)。

以下枚举值用于表示操作的性质和紧迫性。鼓励应用程序为操作选择最合适的值，以确保出色的用户体验：

### NSQualityOfService

```
@available(iOS 8.0, OSX 10.10, *)
public enum NSQualityOfService : Int {    
    case UserInteractive
    case UserInitiated
    case Utility
    case Background
    case Default
}
```

```
typedef NS_ENUM(NSInteger, NSQualityOfService) {
    NSQualityOfServiceUserInteractive = 0x21,    
    NSQualityOfServiceUserInitiated = 0x19,    
    NSQualityOfServiceUtility = 0x11,    
    NSQualityOfServiceBackground = 0x09,
    NSQualityOfServiceDefault = -1
} NS_ENUM_AVAILABLE(10_10, 8_0);
```

- `.UserInteractive`：UserInteractive QoS 用于直接参与提供交互式 UI 的工作，例如处理事件或绘制屏幕。
- `.UserInitiated`：UserInitiated QoS 用于执行用户显式请求的工作，并且其结果必须立即呈现以允许进一步的用户交互。例如，用户在邮件列表中选择了某封邮件后加载该邮件。
- `.Utility`：Utility QoS 用于执行用户不太可能立即等待结果的工作。这项工作可能是由用户请求或自动启动的，不会阻止用户进一步交互，通常以用户可见的时间尺度运行，并且可以通过非模态进度指示符向用户指示其进度。这项工作将以节能的方式运行，在资源受限时会为更高 QoS 的工作让路。例如，定期内容更新或批量文件操作（如媒体导入）。
- `.Background`：Background QoS 用于非用户启动或不可见的工作。通常，用户甚至不知道这些工作在发生，它会以最有效的方式运行，同时为更高的 QoS 工作让路。例如，预取内容、搜索索引、备份以及与外部系统的数据同步。
- `.Default`：Default QoS 表示缺少 QoS 信息。只要可能，QoS 信息会从其他来源推断。如果无法推断，则会使用介于 UserInitiated 和 Utility 之间的 QoS。

```
let backgroundOperation = NSOperation()
backgroundOperation.queuePriority = .Low
backgroundOperation.qualityOfService = .Background

let operationQueue = NSOperationQueue.mainQueue()
operationQueue.addOperation(backgroundOperation)
```

```
NSOperation *backgroundOperation = [[NSOperation alloc] init];
backgroundOperation.queuePriority = NSOperationQueuePriorityLow;
backgroundOperation.qualityOfService = NSOperationQualityOfServiceBackground;

[[NSOperationQueue mainQueue] addOperation:backgroundOperation];
```

## 异步操作

iOS 8 / OS X Yosemite 中的另一个变化是 `concurrent` 属性已废弃，取而代之的是新的 `asynchronous` 属性。

最初，`concurrent` 属性用于区分在其单一 `main` 方法中执行所有工作的操作，以及那些在执行异步时自行管理状态的操作。此属性还用于确定 `NSOperationQueue` 是否会在单独的线程中执行方法。在 `NSOperationQueue` 改为在内部调度队列上运行而不是直接管理线程后，此属性的这方面就被忽略了。新的 `asynchronous` 属性清除了 `concurrent` 的语义混乱，现在是确定 `NSOperation` 应在 `main` 中同步执行还是异步执行的唯一决定因素。

## 依赖关系

根据应用程序的复杂性，将大型任务分解为一系列可组合的子任务可能是有意义的。这可以通过 `NSOperation` 依赖关系来完成。

例如，要描述从服务器下载并调整图像大小的过程，可以将网络操作分成一个操作，将调整大小操作分成另一个操作（可能是为了重用网络操作来下载其他资源，或者也使用调整大小操作来处理已缓存到内存中的图像）。但是，由于图像在下载之前无法调整大小，因此网络操作是调整大小操作的依赖项，必须在调整大小操作开始之前完成。

用代码表示：

```
let networkingOperation: NSOperation = ...
let resizingOperation: NSOperation = ...
resizingOperation.addDependency(networkingOperation)

let operationQueue = NSOperationQueue.mainQueue()
operationQueue.addOperations([networkingOperation, resizingOperation], waitUntilFinished: false)
```

```
NSOperation *networkingOperation = ...
NSOperation *resizingOperation = ...
[resizingOperation addDependency:networkingOperation];

NSOperationQueue *operationQueue = [NSOperationQueue mainQueue];
[operationQueue addOperation:networkingOperation];
[operationQueue addOperation:resizingOperation];
```

一个操作在其所有依赖项的 `finished` 返回 `true` 之前不会启动。

注意不要意外创建依赖循环，例如 A 依赖于 B，而 B 依赖于 A。这会导致死锁和麻烦。

## `completionBlock`

当一个 `NSOperation` 完成时，它将执行其 `completionBlock` 恰好一次。这提供了一种非常好的方式，可以在模型或视图控制器中自定义操作的行为。

```
let operation = NSOperation()
operation.completionBlock = {
    print("Completed")
}

NSOperationQueue.mainQueue().addOperation(operation)
```

```
NSOperation *operation = ...;
operation.completionBlock = ^{
    NSLog("Completed");
};

[[NSOperationQueue mainQueue] addOperation:operation];
```

例如，你可以在网络操作上设置一个完成块，以便在加载完成后对来自服务器的响应数据进行处理。

---

`NSOperation` 仍然是 iOS 或 OS X 开发者工具箱中的必备工具。虽然 GCD 非常适合内联异步处理，但 `NSOperation` 提供了一个更全面、面向对象的计算模型，用于封装应用程序中结构化、可重复任务周围的所有数据。

开发者应尽可能为任何给定问题使用最高级别的抽象，而对于调度一致的、重复的工作，这种抽象就是 `NSOperation`。其他时候，加入一些 GCD（包括在 `NSOperation` 子类实现中）则更有意义。

## 何时使用 Grand Central Dispatch

调度队列、组、信号量、源和屏障构成了基本并发原语集，所有系统框架都构建在此之上。

对于一次性计算，或仅是加快现有方法的速度，使用轻量级的 GCD `dispatch` 通常比使用 `NSOperation` 更方便。

## 何时使用 NSOperation

`NSOperation` 可以按特定的队列优先级和服务质量，并带有一组依赖关系进行调度。与在 GCD 队列上调度的 block 不同，`NSOperation` 可以被取消，并且可以查询其操作状态。而且通过派生子类，`NSOperation` 可以将其工作结果关联到自身，供以后参考。

---

请记住：**NSOperation 和 Grand Central Dispatch 并非互斥**。创造性和有效地使用两者是开发健壮且高性能的 iOS 或 OS X 应用程序的关键。
