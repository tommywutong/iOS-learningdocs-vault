---
title: 'addScheduledHandler(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandbuffer/addscheduledhandler(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/addscheduledhandler(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/addscheduledhandler%28_%3A%29.json'
content_hash: 'sha256:1698c505e29b1223'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# addScheduledHandler(_:)

<sub>Instance Method</sub>

Registers a completion handler the GPU device calls immediately after it schedules the command buffer to run on the GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addScheduledHandler(_ block: @escaping MTLCommandBufferHandler)
```

## Parameters

- `block` — A Swift closure or an Objective-C block that Metal calls after it schedules the command buffer to run on the GPU.

## Discussion

You can register one or more scheduling completion handlers for the same command buffer. The GPU device’s driver (on the CPU) calls the completion handlers after it finishes scheduling the command buffer to run on the GPU.

> [!important] Important
> You can only call this method before calling the command buffer’s [- commit](<commit().md>) method.

The GPU device schedules each command buffer — along with tasks from other command buffers — after it identifies the command buffer’s dependencies. At that time, the GPU device sets the command buffer’s status to [MTLCommandBufferStatusScheduled](../mtlcommandbufferstatus/scheduled.md) and calls your completion handler.

> [!note] Note
> The command buffer’s [status](status.md) property may be equal to another (larger) value by the time your completion handler runs, including [MTLCommandBufferStatusCompleted](../mtlcommandbufferstatus/completed.md).

You can use the command buffer’s [kernelEndTime](kernelendtime.md) and [kernelStartTime](kernelstarttime.md) properties to calculate how much time the CPU spends scheduling the command buffer.

**Swift**

```swift
commandBuffer.addScheduledHandler { commandBuffer in
    let start = commandBuffer.kernelStartTime
    let end = commandBuffer.kernelEndTime

    let scheduleDuration = end - start

    /* ... */
}
```

**Objective-C**

```objective-c
[commandBuffer addScheduledHandler:^(id<MTLCommandBuffer> commandBuffer) {
    CFTimeInterval start = commandBuffer.kernelStartTime;
    CFTimeInterval end = commandBuffer.kernelEndTime;

    CFTimeInterval scheduleDuration = end - start;

    /* ... */
}];

```

## See Also

### Registering state change handlers

- [- addCompletedHandler:](<addcompletedhandler(__).md>) — Registers a completion handler the GPU device calls immediately after the GPU finishes running the commands in the command buffer.
- [MTLCommandBufferHandler](../mtlcommandbufferhandler.md) — A completion handler signature a GPU device calls when it finishes scheduling a command buffer, or when the GPU finishes running it.
