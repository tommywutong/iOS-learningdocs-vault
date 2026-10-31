---
title: Dispatch
framework: Dispatch
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch
source_url: 'https://developer.apple.com/documentation/dispatch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch.json'
content_hash: 'sha256:a921e6657185f2fb'
translated: true
---

> 导航： [技术](technologies.md)

# Dispatch

<sub>框架</sub>

通过将工作提交到由系统管理的 dispatch 队列，在多核硬件上并发执行代码。

## 概述

Dispatch（也称为 Grand Central Dispatch，GCD）包含语言特性、运行时库以及系统增强，为 macOS、iOS、watchOS 和 tvOS 上多核硬件的并发代码执行提供系统性、全面的支持改进。

BSD 子系统、Core Foundation 以及 Cocoa API 都已扩展以使用这些增强功能，从而帮助系统和你的应用程序运行得更快、更高效，并具有更好的响应性。请考虑一下，单个应用程序要有效利用多个核心有多么困难，更不用说要在具有不同计算核心数量的不同计算机上做到这一点，或者在多个应用程序争夺这些核心的环境中做到这一点。GCD 在系统层面运行，能更好地兼顾所有正在运行的应用程序的需求，并以均衡的方式将它们与可用系统资源相匹配。

### Dispatch 对象与 ARC

当你使用 Objective-C 编译器构建 App 时，所有 dispatch 对象都是 Objective-C 对象。因此，当启用自动引用计数（ARC）时，dispatch 对象会像任何其他 Objective-C 对象一样被自动保留和释放。未启用 ARC 时，请使用 [dispatch_retain](dispatch/dispatch_retain.md) 和 [dispatch_release](dispatch/dispatch_release.md) 函数（或 Objective-C 语义）来保留和释放你的 dispatch 对象。你不能使用 Core Foundation 的保留和释放函数。

如果你需要在启用 ARC、部署目标较新的 App 中使用保留和释放语义（以便与现有代码保持兼容），可以通过在编译器标志中添加 `-DOS_OBJECT_USE_OBJC=0` 来禁用基于 Objective-C 的 dispatch 对象。

## 主题

### 队列与任务

- [DispatchQueue](dispatch/dispatchqueue.md) — 一个对象，用于在 App 的主线程或后台线程上以串行或并发方式管理任务的执行。
- [DispatchWorkItem](dispatch/dispatchworkitem.md) — 你想要执行的工作，以一种可以为其附加完成处理程序或执行依赖关系的方式封装起来。
- [DispatchGroup](dispatch/dispatchgroup.md) — 一组作为单一整体来监控的任务。
- [Dispatch 队列](dispatch/dispatch-queue.md) — 一个用于管理你的 App 主线程或后台线程上串行或并发执行任务的对象。
- [Dispatch 工作项](dispatch/dispatch-work-item.md) — 你想要执行的工作，以一种可以为其附加完成处理程序或执行依赖关系的方式封装起来。
- [Dispatch 组](dispatch/dispatch-group.md) — 一组作为单一整体来监控的任务。
- [工作循环](dispatch/workloop.md) — 一个根据服务质量（QoS）级别对任务执行进行优先级排序的 dispatch 对象。

### 线程调度

- [DispatchQoS](dispatch/dispatchqos.md) — 要应用于任务的服务质量，也就是执行优先级。

### 系统事件监视

- [DispatchSource](dispatch/dispatchsource.md) — 一个用于协调处理特定底层系统事件的对象，例如文件系统事件、定时器和 UNIX 信号。
- [Dispatch 源](dispatch/dispatch-source.md) — 一个协调处理特定底层系统事件（例如文件系统事件、定时器和 UNIX 信号）的对象。
- [DispatchIO](dispatch/dispatchio.md) — 一个使用基于流或随机存取语义来管理文件描述符操作的对象。
- [DispatchData](dispatch/dispatchdata.md) — 一个管理基于内存的数据缓冲区、并将其呈现为一整块连续内存的对象。
- [DispatchDataIterator](dispatch/dispatchdataiterator.md) — 对 dispatch 数据对象内容的逐字节迭代器。
- [Dispatch 输入输出](dispatch/dispatch-i-o.md) — 一个使用基于流或随机存取语义来管理文件描述符操作的对象。
- [Dispatch 数据](dispatch/dispatch-data.md) — 一个管理基于内存的数据缓冲区、并将其呈现为一整块连续内存的对象。
- [DispatchSourceProtocol](dispatch/dispatchsourceprotocol.md) — 定义所有 dispatch 源类型共享的一组通用属性与方法。

### 任务同步

- [DispatchSemaphore](dispatch/dispatchsemaphore.md) — 一个通过传统计数信号量在多个执行上下文间控制对资源访问的对象。
- [Dispatch 信号量](dispatch/dispatch-semaphore.md) — 一个通过传统计数信号量在多个执行上下文间控制对资源访问的对象。
- [Dispatch 屏障](dispatch/dispatch-barrier.md) — 并发 dispatch queue 中执行任务的一个同步点。

### 时间构造

- [DispatchTime](dispatch/dispatchtime.md) — 相对于默认时钟的一个时间点，精度为纳秒。
- [DispatchWallTime](dispatch/dispatchwalltime.md) — 根据挂钟时间的一个绝对时间点，精度为微秒。
- [DispatchTimeInterval](dispatch/dispatchtimeinterval.md) — 以秒、毫秒、微秒或纳秒表示的一段时长。
- [DispatchTimeoutResult](dispatch/dispatchtimeoutresult.md) — 表示某个 dispatch 操作是否在指定时间之前完成的结果值。
- [dispatch_time_t](dispatch/dispatch_time_t.md) — 时间的一种抽象表示。
- [DISPATCH_WALLTIME_NOW](dispatch/dispatch_walltime_now.md) — 当前时间。
- [挂钟时间常量](dispatch/2963138-wall-time-constants.md) — 用于表示挂钟时间（wall time）值的常量。

### Dispatch 对象

- [DispatchObject](dispatch/dispatchobject.md) — 大多数 dispatch 类型的基类。
- [DispatchPredicate](dispatch/dispatchpredicate.md) — 在给定执行上下文中求值的逻辑条件。
- [dispatchPrecondition(condition:)](<dispatch/dispatchprecondition(condition_).md>) — 检查进一步执行所必需的 dispatch 条件。
- [Dispatch 对象](dispatch/dispatch-objects.md) — 所有 dispatch 类型都支持的基本行为。

### 已废弃

- [已废弃符号](dispatch/deprecated-symbols.md)

### 类

- [DispatchWorkloop](dispatch/dispatchworkloop.md)

### 参考

- [Dispatch 常量](dispatch/dispatch-constants.md)
- [Dispatch 数据类型](dispatch/dispatch-data-types.md)
- [Dispatch 函数](dispatch/dispatch-functions.md)
