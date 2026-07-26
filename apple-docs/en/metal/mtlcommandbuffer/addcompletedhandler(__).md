---
title: 'addCompletedHandler(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandbuffer/addcompletedhandler(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/addcompletedhandler(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/addcompletedhandler%28_%3A%29.json'
content_hash: 'sha256:8f7e7ed09db0a4ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# addCompletedHandler(_:)

<sub>Instance Method</sub>

Registers a completion handler the GPU device calls immediately after the GPU finishes running the commands in the command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addCompletedHandler(_ block: @escaping MTLCommandBufferHandler)
```

## Parameters

- `block` — A Swift closure or an Objective-C block that Metal calls after the GPU finishes running the commands in the command buffer.

## Discussion

You can register one or more completion handlers for the same command buffer. The GPU device’s driver (on the CPU) calls the completion handlers after the GPU finishes executing the command buffer.

> [!important] Important
> You can only call this method before calling the command buffer’s [- commit](<commit().md>) method.

For example, you can use the command buffer’s [GPUEndTime](gpuendtime.md) and [GPUStartTime](gpustarttime.md) properties to calculate how much time the GPU spends running the command buffer.

**Swift**

```swift
commandBuffer.addCompletedHandler { commandBuffer in
    let start = commandBuffer.gpuStartTime
    let end = commandBuffer.gpuEndTime

    let gpuRuntimeDuration = end - start

    /* ... */
}
```

**Objective-C**

```objective-c
[commandBuffer addCompletedHandler:^(id<MTLCommandBuffer> commandBuffer) {
    CFTimeInterval start = commandBuffer.GPUStartTime;
    CFTimeInterval end = commandBuffer.GPUEndTime;

    CFTimeInterval gpuRuntimeDuration = end - start;

    /* ... */
}];
```

The completion handler is also a good place to check the [status](status.md) property to determine whether the GPU successfully completes the buffer’s commands. If the status is equal to [MTLCommandBufferStatusError](../mtlcommandbufferstatus/error.md), you can investigate further by checking the [error](error.md) and log properties for more details about the issue. See [Command buffer debugging](../command-buffer-debugging.md) for more methods and properties that can help you isolate the issue.

> [!warning] Warning
> Avoid calling the [- insertDebugCaptureBoundary](<../mtlcommandqueue/insertdebugcaptureboundary().md>) method within the completion handler, which can cause a debug-time deadlock if you request GPU frame capture.

## See Also

### Registering state change handlers

- [- addScheduledHandler:](<addscheduledhandler(__).md>) — Registers a completion handler the GPU device calls immediately after it schedules the command buffer to run on the GPU.
- [MTLCommandBufferHandler](../mtlcommandbufferhandler.md) — A completion handler signature a GPU device calls when it finishes scheduling a command buffer, or when the GPU finishes running it.
