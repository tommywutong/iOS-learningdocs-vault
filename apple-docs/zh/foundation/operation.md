---
title: Operation
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/operation
source_url: 'https://developer.apple.com/documentation/foundation/operation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operation.json'
content_hash: 'sha256:fd9f6a0d280e2fd8'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# Operation

<sub>类</sub>

一个抽象类，表示与单个任务关联的代码和数据。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Operation
```

## 概述

由于 [Operation](operation.md) 类是抽象类，你不会直接使用它，而是派生子类或使用系统定义的子类（[NSInvocationOperation](nsinvocationoperation.md) 或 [BlockOperation](blockoperation.md)）来执行实际任务。尽管是抽象的，[Operation](operation.md) 的基础实现确实包含了用于协调任务安全执行的重要逻辑。这种内建逻辑的存在让你可以专注于任务的实际实现，而不必编写胶水代码来确保它能与其他系统对象正确协作。

操作对象是一次性对象——也就是说，它执行任务一次，不能被用来再次执行。你通常通过将操作添加到操作队列（operation queue，即 [OperationQueue](operationqueue.md) 类的实例）中来执行它们。操作队列要么直接在辅助线程上运行操作，要么间接使用 `libdispatch` 库（也称为 Grand Central Dispatch）来执行其操作。关于队列如何执行操作的更多信息，请参阅 [OperationQueue](operationqueue.md)。

如果你不想使用操作队列，你可以直接从代码中调用其 [- start](<operation/start().md>) 方法来自行执行操作。手动执行操作会给你的代码带来更多负担，因为启动一个未处于就绪状态的操作会触发异常。[ready](operation/isready.md) 属性报告操作的就绪状态。

### 操作依赖

依赖（dependency）是一种以特定顺序执行操作的便捷方式。你可以使用 [- addDependency:](<operation/adddependency(__).md>) 和 [- removeDependency:](<operation/removedependency(__).md>) 方法为操作添加和移除依赖。默认情况下，具有依赖项的操作对象在其所有依赖操作对象都执行完毕之前，不会被视为就绪。然而，一旦最后一个依赖操作完成，操作对象就变为就绪状态并可执行。

`NSOperation` 支持的依赖不区分依赖操作是成功完成还是失败完成。（换句话说，取消一个操作同样会将其标记为已完成。）当依赖操作被取消或未能成功完成任务时，是否需要让具有依赖关系的操作继续执行，这由你自行决定。这可能需要你在操作对象中融入一些额外的错误跟踪能力。

### KVO 合规属性

`NSOperation` 类对其多个属性实现了键值编码（KVC）和键值观察（KVO）合规。根据需要，你可以观察这些属性来控制 App 的其他部分。要观察这些属性，请使用以下键路径（key path）：

- `isCancelled` - 只读
- `isAsynchronous` - 只读
- `isExecuting` - 只读
- `isFinished` - 只读
- `isReady` - 只读
- `dependencies` - 只读
- `queuePriority` - 可读可写
- `completionBlock` - 可读可写

虽然你可以为这些属性附加观察者，但你不应该使用 Cocoa 绑定将它们绑定到 App 的用户界面元素上。与用户界面关联的代码通常只能在 App 的主线程中执行。由于操作可以在任何线程中执行，因此与该操作关联的 KVO 通知也可能会在任何线程中发生。

如果你为上述任何属性提供了自定义实现，这些实现必须维护 KVC 和 KVO 合规性。如果你为 `NSOperation` 对象定义了其他属性，建议你也让这些属性符合 KVC 和 KVO。关于如何支持键值编码，请参阅[键值编码编程指南](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)。关于如何支持键值观察，请参阅[键值观察编程指南](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i)。

### 多核注意事项

`NSOperation` 类本身就具有多核感知能力。因此，可以在多个线程中安全地调用 `NSOperation` 对象的方法，而无需创建额外的锁来同步对对象的访问。这种行为是必要的，因为操作通常在与创建并监视它的线程不同的线程中运行。

当你派生子类 `NSOperation` 时，你必须确保所有重写的方法在从多个线程调用时仍然是安全的。如果你在子类中实现了自定义方法，例如自定义数据存取器，你也必须确保这些方法是线程安全的。因此，对操作中任何数据变量的访问都必须同步，以防止潜在的数据损坏。关于同步的更多信息，请参阅[线程编程指南](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)。

### 异步操作与同步操作

如果你计划手动执行操作对象，而不是将其添加到队列中，你可以将操作设计为同步（synchronous）或异步（asynchronous）方式执行。操作对象默认为同步。在同步操作中，操作对象不会创建单独的线程来运行其任务。当你直接从代码中调用同步操作的 [- start](<operation/start().md>) 方法时，操作会在当前线程中立即执行。当此类对象的 [- start](<operation/start().md>) 方法将控制权返回给调用者时，任务本身已经完成。

当你调用异步操作的 [- start](<operation/start().md>) 方法时，该方法可能在相应任务完成之前返回。异步操作对象负责在单独的线程上调度其任务。操作可以通过直接启动新线程、调用异步方法或将要执行的 block 提交到调度队列来完成此操作。当控制权返回给调用者时，操作是否正在进行并不重要，重要的是它可能正在进行。

如果你始终计划使用队列来执行操作，那么将它们定义为同步会更简单。但是，如果你手动执行操作，你可能希望将操作对象定义为异步。定义异步操作需要更多的工作，因为你必须监视任务的持续状态，并使用 KVO 通知报告该状态的变化。但是，在你想确保手动执行的操作不会阻塞调用线程的情况下，定义异步操作是很有用的。

当你向操作队列添加操作时，队列会忽略 [asynchronous](operation/isasynchronous.md) 属性的值，并始终从单独的线程调用 [- start](<operation/start().md>) 方法。因此，如果你总是通过将操作添加到操作队列来运行它们，就没有理由让它们成为异步的。

关于如何定义同步和异步操作的信息，请参阅子类化说明。

### 子类化说明

`NSOperation` 类提供了跟踪操作执行状态的基本逻辑，但除此之外必须派生子类才能执行任何实际工作。如何创建子类取决于你的操作是设计为并发执行还是非并发执行。

#### 要重写的方法

对于非并发操作，你通常只需要重写一个方法：

- [- main](<operation/main().md>)

在这个方法中，你放置执行给定任务所需的代码。当然，你还应该定义一个自定义初始化方法，以便更容易地创建自定义类的实例。你可能还需要定义 getter 和 setter 方法来访问操作中的数据。但是，如果你确实定义了自定义的 getter 和 setter 方法，你必须确保这些方法可以从多个线程中安全地调用。

如果你正在创建一个并发操作，你需要至少重写以下方法和属性：

- [- start](<operation/start().md>)
- [asynchronous](operation/isasynchronous.md)
- [executing](operation/isexecuting.md)
- [finished](operation/isfinished.md)

在并发操作中，你的 [- start](<operation/start().md>) 方法负责以异步方式启动操作。无论你是生成一个线程还是调用一个异步函数，你都在这个方法中进行。启动操作后，你的 [- start](<operation/start().md>) 方法还应更新由 [executing](operation/isexecuting.md) 属性报告的操作执行状态。你通过为 [executing](operation/isexecuting.md) 键路径发送 KVO 通知来实现这一点，这会让感兴趣的客户端知道操作正在运行。你的 [executing](operation/isexecuting.md) 属性还必须以线程安全的方式提供状态。

在任务完成或被取消后，你的并发操作对象必须为 `isExecuting` 和 `isFinished` 这两个键路径生成 KVO 通知，以标记操作最终状态的变化。（在取消的情况下，即使操作没有完全完成其任务，更新 `isFinished` 键路径仍然很重要。队列中的操作必须先报告它们已完成，然后才能从队列中移除。）除了生成 KVO 通知之外，你对 [executing](operation/isexecuting.md) 和 [finished](operation/isfinished.md) 属性的重写也应继续基于操作的状态报告准确的值。

关于如何定义并发操作的更多信息和指导，请参阅[并发编程指南](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091)。

> [!important] 重要
> 在任何时候，你都不应该在 [- start](<operation/start().md>) 方法中调用 `super`。当你定义并发操作时，你需要自行提供默认的 [- start](<operation/start().md>) 方法所提供的行为，包括启动任务和生成适当的 KVO 通知。你的 [- start](<operation/start().md>) 方法还应在实际启动任务之前检查操作本身是否已被取消。关于取消语义的更多信息，请参阅[响应取消命令](operation.md#Responding-to-the-Cancel-Command)。

即使对于并发操作，也几乎不需要重写上述描述之外的方法。但是，如果你自定义了操作的依赖特性，你可能需要重写额外的方法并提供额外的 KVO 通知。对于依赖关系，这很可能只需要为 `isReady` 键路径提供通知即可。由于 [dependencies](operation/dependencies.md) 属性包含了依赖操作的列表，对其的更改已由默认的 `NSOperation` 类处理。

#### 维护操作对象状态

操作对象内部维护状态信息，以确定何时可以安全执行，以及通知外部客户端操作生命周期的进展。你的自定义子类维护这些状态信息，以确保代码中操作的正确执行。与操作状态关联的键路径是：

- ****`isReady`**** — `isReady` 键路径让客户端知道操作何时准备就绪可以执行。当操作现在可以执行时，[ready](operation/isready.md) 属性包含值 `true`；如果仍有依赖的未完成操作，则包含 `false`。

在大多数情况下，你不必自行管理此键路径的状态。但是，如果操作的就绪状态是由依赖操作以外的因素决定的——例如程序中的某些外部条件——你可以提供自己的 [ready](operation/isready.md) 属性实现，并自行跟踪操作的就绪状态。然而，通常更简单的做法是仅在外部状态允许时才创建操作对象。

在 macOS 10.6 及更高版本中，如果你在操作等待一个或多个依赖操作完成时将其取消，这些依赖关系之后将被忽略，并且此属性的值会更新以反映它现在已准备好运行。这种行为使操作队列能够更快地将已取消的操作从其队列中清除。

- ****`isExecuting`**** — `isExecuting` 键路径让客户端知道操作是否正在积极处理其分配的任务。如果操作正在处理其任务，[executing](operation/isexecuting.md) 属性必须报告值 `true`；如果未在处理，则报告 `false`。

如果你替换了操作对象的 [- start](<operation/start().md>) 方法，当操作的执行状态发生变化时，你还必须替换 [executing](operation/isexecuting.md) 属性并生成 KVO 通知。

- ****`isFinished`**** — `isFinished` 键路径让客户端知道操作已成功完成任务或被取消并正在退出。在 `isFinished` 键路径的值变为 `true` 之前，操作对象不会清除依赖。类似地，在 [finished](operation/isfinished.md) 属性包含值 `true` 之前，操作队列不会将操作出队。因此，将操作标记为已完成对于防止队列因正在处理或已取消的操作而积压至关重要。

如果你替换了操作对象的 [- start](<operation/start().md>) 方法，当操作完成执行或被取消时，你还必须替换 [finished](operation/isfinished.md) 属性并生成 KVO 通知。

- ****`isCancelled`**** — `isCancelled` 键路径让客户端知道已请求取消操作。对取消的支持是可选的但鼓励这样做，并且你自己的代码不应为此键路径发送 KVO 通知。操作中处理取消通知的详情在[响应取消命令](operation.md#Responding-to-the-Cancel-Command)中有更详细的描述。

#### 响应取消命令

一旦你将操作添加到队列中，操作就不在你的控制之下了。队列接手并处理该任务的调度。但是，如果你后来决定不想执行该操作——例如，因为用户点击了进度面板中的取消按钮或退出了 App——你可以取消该操作，以防止它不必要地消耗 CPU 时间。你可以通过调用操作对象本身的 [- cancel](<operation/cancel().md>) 方法或 [OperationQueue](operationqueue.md) 类的 [- cancelAllOperations](<operationqueue/cancelalloperations().md>) 方法来实现这一点。

取消操作不会立即强制它停止正在做的事情。尽管所有操作都应尊重 [cancelled](operation/iscancelled.md) 属性的值，但你的代码必须显式检查此属性的值，并在需要时中止。`NSOperation` 的默认实现包含了对取消的检查。例如，如果你在调用其 [- start](<operation/start().md>) 方法之前取消了一个操作，[- start](<operation/start().md>) 方法会在不启动任务的情况下退出。

> [!note] 注意
> 在 macOS 10.6 及更高版本中，如果你对操作队列中且具有未完成依赖操作的操作调用 [- cancel](<operation/cancel().md>) 方法，则这些依赖操作随后会被忽略。由于操作已被取消，此行为允许队列调用操作的 [- start](<operation/start().md>) 方法以从队列中移除操作，而无需调用其 [- main](<operation/main().md>) 方法。如果你对不在队列中的操作调用 [- cancel](<operation/cancel().md>) 方法，则该操作会立即被标记为已取消。在每种情况下，将操作标记为就绪或已完成都会导致生成适当的 KVO 通知。

你应该始终在你编写的任何自定义代码中支持取消语义。特别是，你的主任务代码应定期检查 [cancelled](operation/iscancelled.md) 属性的值。如果该属性报告值 [true](../swift/true.md)，你的操作对象应尽快清理并退出。如果你实现了自定义的 [- start](<operation/start().md>) 方法，该方法应包括对取消的早期检查并做出适当的行为。你的自定义 [- start](<operation/start().md>) 方法必须准备好处理这种类型的提前取消。

除了在操作被取消时简单地退出之外，将已取消的操作移动到适当的最终状态也很重要。具体来说，如果你自己管理 [finished](operation/isfinished.md) 和 [executing](operation/isexecuting.md) 属性的值（可能是因为你在实现并发操作），你必须相应地更新这些属性。具体来说，你必须将 [finished](operation/isfinished.md) 返回的值改为 [true](../swift/true.md)，并将 [executing](operation/isexecuting.md) 返回的值改为 [false](../swift/false.md)。即使操作在开始执行之前就被取消，你也必须进行这些更改。

## 关系

- **继承自**：[NSObject](../objectivec/nsobject-swift.class.md)

- **继承者**：[BlockOperation](blockoperation.md)

- **遵循**：[CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## 主题

### 执行操作

- [- start](<operation/start().md>) — 开始执行操作。
- [- main](<operation/main().md>) — 执行接收者的非并发任务。
- [completionBlock](operation/completionblock.md) — 在操作的主任务完成后执行的 block。

### 取消操作

- [- cancel](<operation/cancel().md>) — 建议操作对象应停止执行其任务。

### 获取操作状态

- [cancelled](operation/iscancelled.md) — 一个布尔值，指示操作是否已被取消。
- [executing](operation/isexecuting.md) — 一个布尔值，指示操作当前是否正在执行。
- [finished](operation/isfinished.md) — 一个布尔值，指示操作是否已完成执行其任务。
- [concurrent](operation/isconcurrent.md) — 一个布尔值，指示操作是否异步执行其任务。
- [asynchronous](operation/isasynchronous.md) — 一个布尔值，指示操作是否异步执行其任务。
- [ready](operation/isready.md) — 一个布尔值，指示操作现在是否可以执行。
- [name](operation/name.md) — 操作的名称。

### 管理依赖

- [- addDependency:](<operation/adddependency(__).md>) — 使接收者依赖于指定操作的完成。
- [- removeDependency:](<operation/removedependency(__).md>) — 移除接收者对指定操作的依赖。
- [dependencies](operation/dependencies.md) — 必须在当前对象可以开始执行之前完成执行的操作对象数组。

### 配置执行优先级

- [qualityOfService](operation/qualityofservice.md) — 将系统资源授予操作的相关重要性。
- [threadPriority](operation/threadpriority.md) — 执行操作时要使用的线程优先级 _(已废弃)_
- [queuePriority](operation/queuepriority-swift.property.md) — 操作在操作队列中的执行优先级。

### 等待操作对象

- [- waitUntilFinished](<operation/waituntilfinished().md>) — 阻塞当前线程的执行，直到操作对象完成其任务。

### 常量

- [QueuePriority](operation/queuepriority-swift.enum.md) — 这些常量让你确定操作的执行顺序。
- [QualityOfService](qualityofservice.md) — 向系统指示工作性质和重要性的常量。

## 另请参阅

### 操作

- [OperationQueue](operationqueue.md) — 一个调节操作执行的队列。
- [BlockOperation](blockoperation.md) — 一个管理一个或多个 block 并发执行的操作。
