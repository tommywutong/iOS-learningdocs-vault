---
title: CFRunLoop
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunloop
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloop.json'
content_hash: 'sha256:b2335f207e29ae7c'
translated: true
---

> 导航：[技术](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoop

<sub>类</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFRunLoop
```

## 概述

CFRunLoop 对象监视任务的输入源，并在它们准备好处理时调度控制。输入源的示例可能包括用户输入设备、网络连接、周期性或定时延迟事件以及异步回调。

运行循环（run loop）可以监视三种类型的对象：源（[CFRunLoopSource](cfrunloopsource.md)）、定时器（[CFRunLoopTimer](cfrunlooptimer.md)）和观察者（[CFRunLoopObserver](cfrunloopobserver.md)）。为了在这些对象需要处理时接收回调，你必须首先使用 [CFRunLoopAddSource](<cfrunloopaddsource(______).md>)、[CFRunLoopAddTimer](<cfrunloopaddtimer(______).md>) 或 [CFRunLoopAddObserver](<cfrunloopaddobserver(______).md>) 将这些对象放入运行循环。之后，你可以将对象从运行循环中移除（或使其失效），以停止接收其回调。

添加到运行循环的每个源、定时器和观察者都必须与一个或多个运行循环模式相关联。模式决定了在给定迭代中运行循环处理哪些事件。每次运行循环执行时，它都会在特定模式下进行。在该模式下，运行循环仅处理与该模式关联的源、定时器和观察者的事件。你将大多数源分配给默认运行循环模式（由 [kCFRunLoopDefaultMode](cfrunloopmode/defaultmode.md) 常量指定），该模式用于在应用程序（或线程）空闲时处理事件。然而，系统定义了其他模式，并可能在这些其他模式下执行运行循环，以限制处理哪些源、定时器和观察者。由于运行循环模式只是作为字符串指定，你也可以定义自己的自定义模式来限制事件的处理。

Core Foundation 定义了一个特殊的伪模式，称为通用模式（common modes），它允许你将多个模式与给定的源、定时器或观察者相关联。要指定通用模式，请在配置对象时对模式使用 [kCFRunLoopCommonModes](cfrunloopmode/commonmodes.md) 常量。每个运行循环都有自己独立的通用模式集，并且默认模式（[kCFRunLoopDefaultMode](cfrunloopmode/defaultmode.md)）始终是该集合的成员。要将模式添加到通用模式集，请使用 [CFRunLoopAddCommonMode](<cfrunloopaddcommonmode(____).md>) 函数。

每个线程恰好有一个运行循环。你既不创建也不销毁线程的运行循环。Core Foundation 会根据需要自动为你创建它。你通过 [CFRunLoopGetCurrent](<cfrunloopgetcurrent().md>) 获取当前线程的运行循环。调用 [CFRunLoopRun](<cfrunlooprun().md>) 以默认模式运行当前线程的运行循环，直到运行循环被 [CFRunLoopStop](<cfrunloopstop(__).md>) 停止。你还可以调用 [CFRunLoopRunInMode](<cfrunloopruninmode(______).md>) 以指定模式运行当前线程的运行循环一段设定的时间（或直到运行循环停止）。仅当请求的模式中至少有一个源或定时器需要监视时，运行循环才能运行。

运行循环可以递归运行。你可以从任何运行循环回调中调用 [CFRunLoopRun](<cfrunlooprun().md>) 或 [CFRunLoopRunInMode](<cfrunloopruninmode(______).md>)，并在当前线程的调用栈上创建嵌套的运行循环激活。你不受限于在回调中可以运行哪些模式。你可以在任何可用的运行循环模式下创建另一个运行循环激活，包括已在调用栈中更高级别运行的任何模式。

Cocoa 应用程序在 CFRunLoop 的基础上构建，以实现其自己的更高级别事件循环。编写应用程序时，你可以将自己的源、定时器和观察者添加到它们的运行循环对象和模式中。然后，你的对象将作为常规应用程序事件循环的一部分受到监视。使用 [RunLoop](../foundation/runloop.md) 的 [getCFRunLoop()](<../foundation/runloop/getcfrunloop().md>) 方法来获取对应的 [CFRunLoop](cfrunloop.md) 类型。在 Carbon 应用程序中，使用 `GetCFRunLoopFromEventLoop` 函数。

有关运行循环行为的更多信息，请参阅《[线程编程指南](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)》中的[运行循环](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/RunLoopManagement/RunLoopManagement.html#//apple_ref/doc/uid/10000057i-CH16)。

## 关系

- **遵循**：[Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## 主题

### 获取运行循环

- [CFRunLoopGetCurrent](<cfrunloopgetcurrent().md>) — 返回当前线程的 CFRunLoop 对象。
- [CFRunLoopGetMain](<cfrunloopgetmain().md>) — 返回主 CFRunLoop 对象。

### 启动与停止运行循环

- [CFRunLoopRun](<cfrunlooprun().md>) — 以默认模式无限期运行当前线程的 CFRunLoop 对象。
- [CFRunLoopRunInMode](<cfrunloopruninmode(______).md>) — 以特定模式运行当前线程的 CFRunLoop 对象。
- [CFRunLoopWakeUp](<cfrunloopwakeup(__).md>) — 唤醒一个正在等待的 CFRunLoop 对象。
- [CFRunLoopStop](<cfrunloopstop(__).md>) — 强制一个 CFRunLoop 对象停止运行。
- [CFRunLoopIsWaiting](<cfrunloopiswaiting(__).md>) — 返回一个布尔值，指示运行循环是否正在等待事件。

### 管理源

- [CFRunLoopAddSource](<cfrunloopaddsource(______).md>) — 将一个 CFRunLoopSource 对象添加到运行循环模式。
- [CFRunLoopContainsSource](<cfrunloopcontainssource(______).md>) — 返回一个布尔值，指示运行循环模式是否包含特定的 CFRunLoopSource 对象。
- [CFRunLoopRemoveSource](<cfrunloopremovesource(______).md>) — 从运行循环模式中移除一个 CFRunLoopSource 对象。

### 管理观察者

- [CFRunLoopAddObserver](<cfrunloopaddobserver(______).md>) — 将一个 CFRunLoopObserver 对象添加到运行循环模式。
- [CFRunLoopContainsObserver](<cfrunloopcontainsobserver(______).md>) — 返回一个布尔值，指示运行循环模式是否包含特定的 CFRunLoopObserver 对象。
- [CFRunLoopRemoveObserver](<cfrunloopremoveobserver(______).md>) — 从运行循环模式中移除一个 CFRunLoopObserver 对象。

### 管理运行循环模式

- [CFRunLoopAddCommonMode](<cfrunloopaddcommonmode(____).md>) — 将一个模式添加到运行循环通用模式集。
- [CFRunLoopCopyAllModes](<cfrunloopcopyallmodes(__).md>) — 返回一个数组，包含 CFRunLoop 对象的所有已定义模式。
- [CFRunLoopCopyCurrentMode](<cfrunloopcopycurrentmode(__).md>) — 返回给定运行循环当前正在运行模式的名称。

### 管理定时器

- [CFRunLoopAddTimer](<cfrunloopaddtimer(______).md>) — 将一个 CFRunLoopTimer 对象添加到运行循环模式。
- [CFRunLoopGetNextTimerFireDate](<cfrunloopgetnexttimerfiredate(____).md>) — 返回下一个定时器触发的时间。
- [CFRunLoopRemoveTimer](<cfrunloopremovetimer(______).md>) — 从运行循环模式中移除一个 CFRunLoopTimer 对象。
- [CFRunLoopContainsTimer](<cfrunloopcontainstimer(______).md>) — 返回一个布尔值，指示运行循环模式是否包含特定的 CFRunLoopTimer 对象。

### 调度 Block

- [CFRunLoopPerformBlock](<cfrunloopperformblock(______).md>) — 将一个 block 对象排入给定运行循环的队列，以在运行循环于指定模式中循环时执行。

### 获取 CFRunLoop 类型 ID

- [CFRunLoopGetTypeID](<cfrunloopgettypeid().md>) — 返回 CFRunLoop 不透明类型的类型标识符。

### 常量

- [CFRunLoopRunInMode 退出码](cfrunloopruninmode_exit_codes.md) — `CFRunLoopRunInMode` 的返回码，标识运行循环退出的原因。
- [通用模式标志](common-mode-flag.md) — 一个运行循环伪模式，用于管理在“通用”模式下监视的对象。
- [默认运行循环模式](default-run-loop-mode.md) — 默认运行循环模式。

## 另请参阅

### 不透明类型

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
- [CFBitVector](cfbitvector.md)
- [CFBoolean](cfboolean.md)
- [CFBundle](cfbundle.md)
- [CFCalendar](cfcalendar.md)
- [CFCharacterSet](cfcharacterset.md)
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)
