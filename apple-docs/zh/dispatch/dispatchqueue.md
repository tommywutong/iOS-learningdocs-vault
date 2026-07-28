---
title: DispatchQueue
framework: Dispatch
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqueue
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue.json'
content_hash: 'sha256:58d6fddd634e6aa7'
translated: true
---

> 导航：[技术](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchQueue

<sub>类</sub>

一个对象，用于在 App 的主线程或后台线程上以串行或并发方式管理任务的执行。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class DispatchQueue
```

## 概述

Dispatch 队列是先进先出（FIFO）队列，你的 App 可以向其提交以 `block` 对象形式表示的任务。Dispatch 队列串行或并发地执行任务。提交给 Dispatch 队列的任务在由系统管理的线程池上执行。除了代表 App 主线程的那个 Dispatch 队列外，系统不保证使用哪个线程来执行任务。

你可以同步或异步地调度工作（work）项目。当你同步调度一个工作项目时，代码会等待该项目执行完毕。当你异步调度一个工作项目时，在工作项目于其他地方运行的同时，你的代码会继续执行。

> [!important] 重要
> 尝试在主队列上同步执行工作项目会导致死锁。

### 避免创建过多线程

在设计并发执行的任务时，不要调用会阻塞当前执行线程的方法。当由并发 Dispatch 队列调度的任务阻塞了一个线程时，系统会创建额外的线程来运行其他已排队的并发任务。如果阻塞的任务过多，系统可能会耗尽你的 App 可用的线程。

App 消耗过多线程的另一种方式是创建过多的私有并发 Dispatch 队列。由于每个 Dispatch 队列都会消耗线程资源，创建额外的并发 Dispatch 队列会加剧线程消耗问题。与其创建私有的并发队列，不如将任务提交到某个全局并发 Dispatch 队列。对于串行任务，请将串行队列的目标设置为某个全局并发队列。这样，你就可以在保持队列的串行化行为的同时，最大限度地减少创建线程的独立队列数量。

## 关系

- **继承自**：[DispatchObject](dispatchobject.md)

- **被继承者**：[DispatchConcurrentQueue](dispatchconcurrentqueue.md)，[OS_dispatch_queue_global](os_dispatch_queue_global-swift.class.md)

- **遵循**：[CVarArg](../swift/cvararg.md)，[Copyable](../swift/copyable.md)，[Equatable](../swift/equatable.md)，[Escapable](../swift/escapable.md)，[Executor](../swift/executor.md)，[Hashable](../swift/hashable.md)，[NSObjectProtocol](../objectivec/nsobjectprotocol.md)，[Scheduler](../combine/scheduler.md)，[Sendable](../swift/sendable.md)，[SendableMetatype](../swift/sendablemetatype.md)，[TaskExecutor](../swift/taskexecutor.md)

## 主题

### 创建 Dispatch 队列

- [main](dispatchqueue/main.md) — 与当前进程主线程关联的 Dispatch 队列。
- [global(qos:)](<dispatchqueue/global(qos_).md>) — 返回指定服务质量（quality-of-service）类的全局系统队列。
- [init(label:qos:attributes:autoreleaseFrequency:target:)](<dispatchqueue/init(label_qos_attributes_autoreleasefrequency_target_).md>) — 创建一个新的 Dispatch 队列，你可以向其提交 `block`。
- [QoSClass](dispatchqos/qosclass-swift.enum.md) — 指定执行任务优先级（priority）的服务质量类。
- [Attributes](dispatchqueue/attributes.md) — 定义 Dispatch 队列行为的特性（attributes）。
- [AutoreleaseFrequency](dispatchqueue/autoreleasefrequency.md) — 指示 Dispatch 队列自动释放对象的频率的常量。
- [OS_dispatch_queue_main](os_dispatch_queue_main-swift.class.md) — 一个系统提供的 Dispatch 队列，用于在 App 的主线程上调度任务进行串行执行。
- [OS_dispatch_queue_global](os_dispatch_queue_global-swift.class.md) — 一个系统提供的 Dispatch 队列，用于调度任务进行并发执行。
- [DispatchSerialQueue](dispatchserialqueue.md) — 一个自定义的 Dispatch 队列，用于在任意线程上调度任务进行串行执行。
- [DispatchConcurrentQueue](dispatchconcurrentqueue.md) — 一个自定义的 Dispatch 队列，用于调度任务进行并发执行。
- [dispatch_queue_main_t](dispatch_queue_main_t.md) — 一个绑定到 App 主线程的 Dispatch 队列，在该线程上串行执行任务。
- [dispatch_queue_global_t](dispatch_queue_global_t.md) — 一个使用全局线程池中的线程并发执行任务的 Dispatch 队列。
- [dispatch_queue_serial_t](dispatch_queue_serial_t.md) — 一个按先进先出（FIFO）顺序串行执行任务的 Dispatch 队列。
- [dispatch_queue_concurrent_t](dispatch_queue_concurrent_t.md) — 一个并发且以任意顺序执行任务的 Dispatch 队列，但会遵循任何可能存在的屏障（barrier）。

### 异步执行任务

- [async(execute:)](<dispatchqueue/async(execute_).md>) — 调度一个工作项目立即执行，并立即返回。
- [asyncAfter(deadline:execute:)](<dispatchqueue/asyncafter(deadline_execute_).md>) — 调度一个工作项目在指定时间执行，并立即返回。
- [asyncAfter(deadline:qos:flags:execute:)](<dispatchqueue/asyncafter(deadline_qos_flags_execute_).md>) — 使用指定的特性调度一个 `block` 执行，并立即返回。
- [asyncAfter(wallDeadline:execute:)](<dispatchqueue/asyncafter(walldeadline_execute_).md>) — 调度一个工作项目在指定时间之后执行，并立即返回。
- [asyncAfter(wallDeadline:qos:flags:execute:)](<dispatchqueue/asyncafter(walldeadline_qos_flags_execute_).md>) — 使用指定的特性调度一个 `block` 执行，并立即返回。

### 同步执行任务

- [sync(execute:)](<dispatchqueue/sync(execute_)-2fzvo.md>) — 提交一个工作项目到当前队列执行，并在该 `block` 完成执行后返回。
- [dispatch_sync](<dispatchqueue/sync(execute_)-3segw.md>) — 提交一个 `block` 对象执行，并在该 `block` 完成执行后返回。
- [sync(execute:)](<dispatchqueue/sync(execute_)-20xby.md>) — 提交一个工作项目执行，并在该工作项目完成执行后返回其结果。
- [sync(flags:execute:)](<dispatchqueue/sync(flags_execute_).md>) — 使用指定的特性提交一个工作项目执行，并在该工作项目完成执行后返回其结果。
- [dispatch_async_and_wait](<dispatchqueue/asyncandwait(execute_)-1udeu.md>) — 提交一个工作项目执行，并且仅在它完成执行后才返回。

### 并行执行任务

- [concurrentPerform(iterations:execute:)](<dispatchqueue/concurrentperform(iterations_execute_).md>) — 向 Dispatch 队列提交一个单独的 `block`，并使其执行指定次数。

### 分发工作到组

- [async(group:execute:)](<dispatchqueue/async(group_execute_).md>) — 异步调度一个工作项目执行，并将其与指定的 Dispatch 组关联。
- [async(group:qos:flags:execute:)](<dispatchqueue/async(group_qos_flags_execute_).md>) — 异步调度一个 `block` 执行，并可选择将其与一个 Dispatch 组关联。

### 管理队列特性

- [label](dispatchqueue/label.md) — 你在创建 Dispatch 队列时为其分配的标签（label）。
- [qos](dispatchqueue/qos.md) — 分配给队列的服务质量（Quality-of-Service）级别。
- [dispatch_set_target_queue](<dispatchobject/settarget(queue_).md>) — 指定用于执行与当前对象相关的工作的 Dispatch 队列。

### 获取和设置上下文数据

- [setSpecific(key:value:)](<dispatchqueue/setspecific(key_value_).md>) — 为指定的 Dispatch 队列设置键/值数据。
- [getSpecific(key:)](<dispatchqueue/getspecific(key_)-swift.method.md>) — 返回与此 Dispatch 队列关联的键的值。
- [getSpecific(key:)](<dispatchqueue/getspecific(key_)-swift.type.method.md>) — 返回与当前执行上下文关联的键的值。
- [DispatchSpecificKey](dispatchspecifickey.md) — 与 Dispatch 队列上特定上下文值关联的键。

### 管理主 Dispatch 队列

- [dispatch_main](<dispatchmain().md>) — 执行提交到主队列的 `block`。

### 调度 Combine Publisher

- [SchedulerTimeType](dispatchqueue/schedulertimetype.md) — Dispatch 队列使用的调度器时间类型。
- [SchedulerOptions](dispatchqueue/scheduleroptions.md) — 一组影响调度器（scheduler）操作的可选项，该调度器由 Dispatch 队列使用。

### 已废弃

- [global(priority:)](<dispatchqueue/global(priority_).md>)
- [GlobalQueuePriority](dispatchqueue/globalqueuepriority.md) — 用于队列优先级的旧版常量。

### 实例方法

- [asyncAfterUnsafe(deadline:qos:flags:execute:)](<dispatchqueue/asyncafterunsafe(deadline_qos_flags_execute_).md>)
- [asyncAfterUnsafe(wallDeadline:qos:flags:execute:)](<dispatchqueue/asyncafterunsafe(walldeadline_qos_flags_execute_).md>)
- [asyncAndWait(execute:)](<dispatchqueue/asyncandwait(execute_)-52p9n.md>)
- [asyncAndWait(execute:)](<dispatchqueue/asyncandwait(execute_)-pfxy.md>)
- [asyncAndWait(flags:execute:)](<dispatchqueue/asyncandwait(flags_execute_).md>)
- [asyncUnsafe(group:qos:flags:execute:)](<dispatchqueue/asyncunsafe(group_qos_flags_execute_).md>)

### 默认实现

- [Scheduler 实现](dispatchqueue/scheduler-implementations.md)

## 另请参阅

### 队列与任务

- [DispatchWorkItem](dispatchworkitem.md) — 你想要执行的工作，以一种允许你附加完成句柄或执行依赖关系的方式封装。
- [DispatchGroup](dispatchgroup.md) — 一组任务，你可以将它们作为一个单一单元进行监控。
- [Dispatch Queue](dispatch-queue.md) — 一个对象，用于在 App 的主线程或后台线程上以串行或并发方式管理任务的执行。
- [Dispatch Work Item](dispatch-work-item.md) — 你想要执行的工作，以一种允许你附加完成句柄或执行依赖关系的方式封装。
- [Dispatch Group](dispatch-group.md) — 一组任务，你可以将它们作为一个单一单元进行监控。
- [Workloop](workloop.md) — 一个 Dispatch 对象，它根据任务的服务质量（QoS）级别来确定其执行优先级。
