---
title: 关于同步事件
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/about-synchronization-events
source_url: 'https://developer.apple.com/documentation/metal/about-synchronization-events'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/about-synchronization-events.json'
content_hash: 'sha256:22d8c71e78270214'
translated: true
---

> 导航：[技术](../technologies.md) · [Metal](../metal.md) · [资源同步](resource-synchronization.md)

# 关于同步事件

<sub>文章</sub>

通过发送事件信号来同步 App 中对资源的访问。

## 概述

使用事件来指定 App 中的同步点。例如，你可以使用事件来同步一个命令队列上运行的图形渲染命令与另一个命令队列上执行的计算处理工作。

Metal 提供两种不同类型的事件：

- 不可共享事件。[MTLEvent](mtlevent.md) 对象在单个设备对象内同步事件。
- 可共享事件。[MTLSharedEvent](mtlsharedevent.md) 对象跨多个设备对象、处理器或进程同步事件。

可共享事件的开销高于不可共享事件。不要使用 [MTLSharedEvent](mtlsharedevent.md) 来同步单个设备对象内的事件；应改用 [MTLEvent](mtlevent.md)。

### 事件信号发送与等待

事件包含一个单调递增的无符号 64 位整数。事件的初始值为 `0`。你可以通过 _发送信号_ 来更新事件的值，或者通过 _等待_ 该事件来 `block` 后续执行。通常，你会在 App 中为每个事件跟踪一个整数值，并在每次需要在该事件上进行同步时递增该值。例如，你可以在每次渲染新一帧动画时递增该数字。

要发送事件变更信号，请在命令缓冲区上调用 [- encodeSignalEvent:value:](<mtlcommandbuffer/encodesignalevent(__value_).md>)，并传入该事件的新值。Metal 会在所有先于该事件调度的命令完成后发送事件信号，并在新值大于当前值时更新事件的值。

要等待某个事件被发送信号，请在命令缓冲区上调用 [- encodeWaitForEvent:value:](<mtlcommandbuffer/encodewaitforevent(__value_).md>)，并传入要等待的值。在队列中位于此等待事件之后的命令，只有在事件的值至少等于你提供的值之后才会执行。

> [!note] 注意
> 你只能在命令编码器边界之外编码事件，而不能在命令编码器的已编码命令之间编码事件。

## 另请参阅

### 使用事件进行同步

- [使用堆和事件实现多级图像滤镜](implementing-a-multistage-image-filter-using-heaps-and-events.md) — 使用事件来同步对堆上分配的资源的访问。
- [在单个设备内同步事件](synchronizing-events-within-a-single-device.md) — 使用不可共享事件在单个设备内同步 App 的工作。
- [跨多个设备或进程同步事件](synchronizing-events-across-multiple-devices-or-processes.md) — 使用可共享事件跨多个设备或进程同步 App 的工作。
- [在 GPU 和 CPU 之间同步事件](synchronizing-events-between-a-gpu-and-the-cpu.md) — 使用可共享事件在 GPU 和 CPU 之间同步 App 的工作。
- [MTLEvent](mtlevent.md) — 一种类型，用于在单个 Metal 设备内同步对一个或多个资源的内存操作。
- [MTLSharedEvent](mtlsharedevent.md) — 一种类型，用于跨多个 CPU、GPU 和进程同步对一个或多个资源的内存操作。
- [MTLSharedEventHandle](mtlsharedeventhandle.md) — 一个实例，用于重新创建可共享事件。
- [MTLSharedEventListener](mtlsharedeventlistener.md) — 可共享事件通知的监听器。
- [MTLSharedEventNotificationBlock](mtlsharedeventnotificationblock.md) — 一个代码 `block`，会在可共享事件的信号值等于或超过给定值后调用。
