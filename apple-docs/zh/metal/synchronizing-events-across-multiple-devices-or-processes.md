---
title: 跨多个设备或进程同步事件
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/synchronizing-events-across-multiple-devices-or-processes
source_url: 'https://developer.apple.com/documentation/metal/synchronizing-events-across-multiple-devices-or-processes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/synchronizing-events-across-multiple-devices-or-processes.json'
content_hash: 'sha256:c75eb4feb9aaad08'
translated: true
---

> 导航：[技术](../technologies.md) · [Metal](../metal.md) · [资源同步](resource-synchronization.md)

# 跨多个设备或进程同步事件

<sub>文章</sub>

使用可共享事件来同步你的 App 在多个设备或进程间的工作。

## 概述

下图和代码展示了一个可共享事件，它将一个设备上的图形渲染与另一个设备上的计算处理进行了同步。

![](../../../attachments/8f7ba4dbc1f70a4e848435f95ff8bac8/synchronizing-events-across-multiple-devices-or-processes-1@2x.png)

<sub>一幅时间线图，展示了编码到两个设备中的可共享同步事件。设备 A 显示图形渲染命令，设备 B 显示计算处理命令。</sub>

**Swift**

```swift
func setupMultipleDeviceEvent() {
    // 可共享事件
    sharedEvent = deviceA.makeSharedEvent()
    
    // 内置 GPU 命令队列
    commandQueueA = deviceA.makeCommandQueue()
    
    // 外置 GPU 命令队列
    commandQueueB = deviceB.makeCommandQueue()
}

func renderFrame() {
    guard
        let sharedEvent = sharedEvent,
        let commandBufferA = commandQueueA?.makeCommandBuffer(),
        let commandBufferB = commandQueueB?.makeCommandBuffer()
        else { return }
    
    // 设备 A（图形渲染）
    /* 编码第一个渲染通道 */
    commandBufferA.encodeSignalEvent(sharedEvent, value: 1)
    /* 编码第二个渲染通道 */
    commandBufferA.encodeWaitForEvent(sharedEvent, value: 2)
    /* 编码第三个渲染通道 */
    commandBufferA.commit()
    
    // 设备 B（计算处理）
    /* 编码第一个计算通道 */
    commandBufferB.encodeWaitForEvent(sharedEvent, value: 1)
    /* 编码第二个计算通道  */
    commandBufferB.encodeSignalEvent(sharedEvent, value: 2)
    /* 编码第三个计算通道 */
    commandBufferB.commit()
}
```

**Objective-C**

```objective-c
- (void)setupMultipleDeviceEvent
{
    // 可共享事件
    _sharedEvent = [_deviceA newSharedEvent];
    
    // 内置 GPU 命令队列
    _commandQueueA = [_deviceA newCommandQueue];
    
    // 外置 GPU 命令队列
    _commandQueueB = [_deviceB newCommandQueue];
}

- (void)renderFrame
{
    // 设备 A（图形渲染）
    id<MTLCommandBuffer> commandBufferA = [_commandQueueA commandBuffer];
    /* 编码第一个渲染通道 */
    [commandBufferA encodeSignalEvent:_sharedEvent value:1];
    /* 编码第二个渲染通道  */
    [commandBufferA encodeWaitForEvent:_sharedEvent value:2];
    /* 编码第三个渲染通道  */
    [commandBufferA commit];
    
    // 设备 B（计算处理）
    id<MTLCommandBuffer> commandBufferB = [_commandQueueB commandBuffer];
    /* 编码第一个计算通道 */
    [commandBufferB encodeWaitForEvent:_sharedEvent value:1];
    /* 编码第二个计算通道 */
    [commandBufferB encodeSignalEvent:_sharedEvent value:2];
    /* 编码第三个计算通道 */
    [commandBufferB commit];
}
```

在设置过程中，代码在两个不同的设备上创建了一个可共享事件（[MTLSharedEvent](mtlsharedevent.md)）和各自的命令队列。如[在单个设备内同步事件](synchronizing-events-within-a-single-device.md)中的示例所示，它将渲染命令编码到第一个队列，将计算命令编码到第二个队列。

在对共享事件发送信号和进行等待时，你调用的方法与在单个设备上使用事件时相同。唯一的区别在于，这些命令队列与不同的设备相关联，并且用于同步访问的事件是一个可共享事件。

上述代码假设你已在两个设备对象上分别创建了每个资源，并且每对资源共享单一内存分配。这种策略意味着一个设备对象所做的更改对另一个设备对象可见。关于如何实现这一点的示例，请参阅[选择用于计算处理的设备对象](selecting-device-objects-for-compute-processing.md)。

## 另请参阅

### 使用事件进行同步

- [使用堆和事件实现多级图像滤镜](implementing-a-multistage-image-filter-using-heaps-and-events.md) — 使用事件同步对堆上分配资源的访问。
- [关于同步事件](about-synchronization-events.md) — 通过发送事件信号来同步对 App 中资源的访问。
- [在单个设备内同步事件](synchronizing-events-within-a-single-device.md) — 使用不可共享事件在单个设备内同步你的 App 的工作。
- [在 GPU 与 CPU 之间同步事件](synchronizing-events-between-a-gpu-and-the-cpu.md) — 使用可共享事件在 GPU 与 CPU 之间同步你的 App 的工作。
- [MTLEvent](mtlevent.md) — 一种类型，用于同步单个 Metal 设备内一个或多个资源的内存操作。
- [MTLSharedEvent](mtlsharedevent.md) — 一种类型，用于跨多个 CPU、GPU 和进程同步一个或多个资源的内存操作。
- [MTLSharedEventHandle](mtlsharedeventhandle.md) — 用于重新创建可共享事件的实例。
- [MTLSharedEventListener](mtlsharedeventlistener.md) — 可共享事件通知的监听器。
- [MTLSharedEventNotificationBlock](mtlsharedeventnotificationblock.md) — 在可共享事件的信号值达到或超过给定值后调用的代码 block。
