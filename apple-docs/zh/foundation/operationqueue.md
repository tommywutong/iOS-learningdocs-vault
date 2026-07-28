---
title: OperationQueue
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/operationqueue
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue.json'
content_hash: 'sha256:76f4c5f79de8e702'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# OperationQueue

<sub>类</sub>

一个调节操作执行的队列。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class OperationQueue
```

## 概述

操作队列根据其队列中 [Operation](operation.md) 对象的优先级和就绪状态来调用它们。将某个操作添加到队列后，该操作会一直留在队列中，直到它完成其任务。添加后，你不能直接从队列中移除操作。

> [!note] 注意
> 操作队列会保留操作，直到操作完成；队列本身也会一直保留，直到所有操作都完成。挂起一个包含尚未完成操作的操作队列可能会导致内存泄漏。

关于使用操作队列的更多信息，请参阅 [并发编程指南](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091)。

### 确定执行顺序

操作队列根据操作的就绪状态、优先级级别以及操作之间的依赖关系来组织和调用它们。如果所有队列中的操作都具有相同的 [queuePriority](operation/queuepriority-swift.property.md) 并且 [ready](operation/isready.md) 属性返回 [true](../swift/true.md)，则队列会按照你添加它们的顺序进行调用。否则，操作队列总是会先调用相对于其他就绪操作中优先级最高的操作。

但是，不要依赖队列语义来确保操作的特定执行顺序，因为操作就绪状态的变化可能会改变最终的执行顺序。操作之间的依赖关系可以为操作提供绝对执行顺序，即使这些操作位于不同的操作队列中也是如此。一个操作对象在其所有依赖操作都完成运行之前是不会就绪的。

关于如何设置优先级级别和依赖关系的详细信息，请参阅 [Operation](operation.md) 中的“管理依赖关系”。

### 响应操作取消

完成任务并不一定意味着该操作已彻底完成了该任务；操作也可能被取消。取消一个操作对象会使该对象留在队列中，但会通知该对象它应尽快停止其任务。对于当前正在执行的操作，这意味着操作对象的工作代码必须检查取消状态，停止正在执行的操作，并将其自身标记为已完成。对于已排队但尚未执行的操作，队列仍然必须调用操作对象的 [- start](<operation/start().md>) 方法，以便它可以处理取消事件并将其自身标记为已完成。

> [!note] 注意
> 取消一个操作会导致该操作忽略它可能拥有的任何依赖关系。这种行为使得队列能够尽快调用该操作的 [- start](<operation/start().md>) 方法。接着，[- start](<operation/start().md>) 方法会将操作转变为已完成状态，以便将其从队列中移除。

关于操作取消的更多信息，请参阅 [Operation](operation.md) 中的 [响应取消命令](operation.md#Responding-to-the-Cancel-Command)。

### 使用键值观察监控操作

[OperationQueue](operationqueue.md) 类符合键值编码（KVC）和键值观察（KVO）。你可以观察这些属性来控制 App 的其他部分。要观察这些属性，请使用以下键路径：

- [operations](operationqueue/operations.md) — 只读
- [operationCount](operationqueue/operationcount.md) — 只读
- [maxConcurrentOperationCount](operationqueue/maxconcurrentoperationcount.md) — 可读写
- [suspended](operationqueue/issuspended.md) — 可读写
- [name](operationqueue/name.md) — 可读写

虽然你可以将观察者附加到这些属性上，但不要使用 Cocoa 绑定来将这些属性绑定到 App 用户界面的元素上。与用户界面相关的代码通常只能在你 App 的主线程中运行。然而，与操作队列关联的 KVO 通知可能在任何线程中发生。

关于 KVO 以及如何将观察者附加到对象的更多信息，请参阅 [键值观察编程指南](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i)。

### 规划线程安全

你可以安全地从多个线程使用单个 [OperationQueue](operationqueue.md) 对象，而无需创建额外的锁来同步对该对象的访问。

操作队列使用 [Dispatch](../dispatch.md) 框架来启动其操作的执行。因此，无论操作是同步还是异步，队列总是在单独的线程上调用操作。

## 关系

- **继承自**：[NSObject](../objectivec/nsobject-swift.class.md)

- **遵循**：[CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [ProgressReporting](progressreporting.md), [Scheduler](../combine/scheduler.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## 主题

### 访问特定操作队列

- [mainQueue](operationqueue/main.md) — 返回与主线程关联的操作队列。
- [currentQueue](operationqueue/current.md) — 返回启动了当前操作的操作队列。

### 管理队列中的操作

- [- addOperation:](<operationqueue/addoperation(__)-64o8a.md>) — 将指定的操作添加到接收者。
- [- addOperations:waitUntilFinished:](<operationqueue/addoperations(__waituntilfinished_).md>) — 将指定的操作添加到队列。
- [- addOperationWithBlock:](<operationqueue/addoperation(__)-5s294.md>) — 将指定的 block 封装在一个操作中，并将其添加到接收者。
- [- addBarrierBlock:](<operationqueue/addbarrierblock(__).md>) — 当队列完成所有已入队操作时调用一个 block，并阻止后续操作启动，直到该 block 完成。
- [- cancelAllOperations](<operationqueue/cancelalloperations().md>) — 取消所有已排队和正在执行的操作。
- [- waitUntilAllOperationsAreFinished](<operationqueue/waituntilalloperationsarefinished().md>) — 阻塞当前线程，直到接收者的所有已排队和正在执行的操作执行完毕。
- [operations](operationqueue/operations.md) — 当前队列中的操作。 _(已废弃)_
- [operationCount](operationqueue/operationcount.md) — 当前队列中的操作数量。 _(已废弃)_

### 管理操作的执行

- [qualityOfService](operationqueue/qualityofservice.md) — 应用于队列调用的操作的默认服务级别（qualityOfService）。
- [maxConcurrentOperationCount](operationqueue/maxconcurrentoperationcount.md) — 可以同时运行的已排队操作的最大数量。
- [NSOperationQueueDefaultMaxConcurrentOperationCount](operationqueue/defaultmaxconcurrentoperationcount.md) — 队列中同时调用的操作的默认最大数量。

### 监控操作的进度

- [progress](operationqueue/progress.md) — 一个表示队列中执行操作的总进度的对象。

### 挂起执行

- [suspended](operationqueue/issuspended.md) — 一个布尔值，指示队列是否正在积极调度操作以供执行。

### 配置队列

- [name](operationqueue/name.md) — 操作队列的名称。
- [underlyingQueue](operationqueue/underlyingqueue.md) — 操作队列用于调用操作的调度队列。

### 调度操作

- [schedule(after:tolerance:options:_:)](<operationqueue/schedule(after_tolerance_options___).md>) — 在指定日期之后的某个时间执行操作，如有可能，可将容差（tolerance）纳入考量。
- [schedule(after:interval:tolerance:options:_:)](<operationqueue/schedule(after_interval_tolerance_options___).md>) — 在指定日期之后的某个时间，以指定的频率执行操作，如有可能，可将容差（tolerance）纳入考量。
- [schedule(options:_:)](<operationqueue/schedule(options___).md>) — 在下一个可能的时机执行操作。
- [now](operationqueue/now.md) — 操作队列对当前时刻的定义。
- [minimumTolerance](operationqueue/minimumtolerance.md) — 调度队列调度器允许的最小容差。
- [SchedulerTimeType](operationqueue/schedulertimetype.md) — 操作队列使用的调度器时间类型。
- [SchedulerOptions](operationqueue/scheduleroptions.md) — 一个定义操作队列接受的选项的类型。

### 默认实现

- [调度器实现](operationqueue/scheduler-implementations.md)

## 另请参阅

### 操作

- [Operation](operation.md) — 表示与单个任务相关的代码和数据的抽象类。
- [BlockOperation](blockoperation.md) — 管理一个或多个 block 并发执行的操作。
