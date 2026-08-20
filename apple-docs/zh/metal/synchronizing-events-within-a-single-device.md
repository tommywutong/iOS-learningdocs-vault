---
title: 在单个设备内同步事件
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/synchronizing-events-within-a-single-device
source_url: 'https://developer.apple.com/documentation/metal/synchronizing-events-within-a-single-device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/synchronizing-events-within-a-single-device.json'
content_hash: 'sha256:dcc082896d2d568a'
translated: true
---

> 导航：[技术](../technologies.md) · [Metal](../metal.md) · [资源同步](resource-synchronization.md)

# 在单个设备内同步事件

<sub>文章</sub>

使用不可共享事件（nonshareable event）在单个设备内同步你的 App 的工作。

## 概述

下图和代码展示了一个不可共享事件，它在一个命令队列上同步图形渲染，并在另一个命令队列上同步计算处理。

![](../../../attachments/9579ce601b5d1e22efed4f32680415f9/synchronizing-events-within-a-single-device-1@2x.png)

<sub>时间线图，展示一个不可共享的同步事件编码到两个命令队列中。命令队列 A 显示图形渲染命令，命令队列 B 显示计算处理命令。</sub>

**Swift**

```swift
func setupSingleDeviceEvent() {
    // Nonshareable event
    event = device.makeEvent()
    
    // Command queues
    commandQueueA = device.makeCommandQueue()
    commandQueueB = device.makeCommandQueue()
}

func renderFrame() {
    guard
        let event = event,
        let commandBufferA = commandQueueA?.makeCommandBuffer(),
        let commandBufferB = commandQueueB?.makeCommandBuffer()
        else { return }
    
    // Command Queue A (Graphics Rendering)
    /* Encode first render pass */
    commandBufferA.encodeSignalEvent(event, value: 1)
    /* Encode second render pass */
    commandBufferA.encodeWaitForEvent(event, value: 2)
    /* Encode third render pass */
    commandBufferA.commit()
    
    // Command Queue B (Compute Processing)
    /* Encode first compute pass */
    commandBufferB.encodeWaitForEvent(event, value: 1)
    /* Encode second compute pass */
    commandBufferB.encodeSignalEvent(event, value: 2)
    /* Encode third compute pass */
    commandBufferB.commit()
}
```

**Objective-C**

```objective-c
- (void)setupSingleDeviceEvent
{
    // Nonshareable event
    _event = [_device newEvent];

    // Command queues
    _commandQueueA = [_device newCommandQueue];
    _commandQueueB = [_device newCommandQueue];
}

- (void)renderFrame
{
    // Command Queue A (Graphics Rendering)
    id<MTLCommandBuffer> commandBufferA = [_commandQueueA commandBuffer];
    /* Encode first render pass */
    [commandBufferA encodeSignalEvent:_event value:1];
    /* Encode second render pass */
    [commandBufferA encodeWaitForEvent:_event value:2];
    /* Encode third render pass */
    [commandBufferA commit];
    
    // Command Queue B (Compute Processing)
    id<MTLCommandBuffer> commandBufferB = [_commandQueueB commandBuffer];
    /* Encode first compute pass */
    [commandBufferB encodeWaitForEvent:_event value:1];
    /* Encode second compute pass */
    [commandBufferB encodeSignalEvent:_event value:2];
    /* Encode third compute pass */
    [commandBufferB commit];
}
```

在设置过程中，代码创建了一个不可共享事件和两个命令队列。然后，为了渲染一帧，代码将渲染命令编码到第一个队列，将计算命令编码到第二个队列。虽然代码显示这些命令是按顺序编码的，但在实际的 App 中，你应该确定是否可以在不同的线程上为每个命令队列编码命令。

假设第一个渲染通道和第一个计算通道不依赖于彼此的结果，并且修改相同的数据。通过将它们编码到不同的队列，设备对象可以并发调度这些命令。

当两组命令彼此之间存在依赖关系时，代码通过发出信号或等待事件来表达这些依赖关系。当每个队列到达等待事件的命令时，该队列会阻塞进一步执行，直到该事件被发出信号。

## 另请参阅

### 使用事件进行同步

- [使用堆和事件实现多阶段图像滤镜](implementing-a-multistage-image-filter-using-heaps-and-events.md) —— 使用事件同步对堆上分配的资源的访问。
- [关于同步事件](about-synchronization-events.md) —— 通过发出事件信号来同步对 App 中资源的访问。
- [跨多个设备或进程同步事件](synchronizing-events-across-multiple-devices-or-processes.md) —— 使用可共享事件（shareable event）跨多个设备或进程同步你的 App 的工作。
- [在 GPU 与 CPU 之间同步事件](synchronizing-events-between-a-gpu-and-the-cpu.md) —— 使用可共享事件在 GPU 和 CPU 之间同步你的 App 的工作。
- [MTLEvent](mtlevent.md) —— 一种在单个 Metal 设备内同步对一个或多个资源的内存操作的类型。
- [MTLSharedEvent](mtlsharedevent.md) —— 一种在跨多个 CPU、GPU 和进程时同步对一个或多个资源的内存操作的类型。
- [MTLSharedEventHandle](mtlsharedeventhandle.md) —— 用于重新创建可共享事件的实例。
- [MTLSharedEventListener](mtlsharedeventlistener.md) —— 用于可共享事件通知的监听器。
- [MTLSharedEventNotificationBlock](mtlsharedeventnotificationblock.md) —— 在可共享事件的信号值等于或超过给定值后调用的 block。
