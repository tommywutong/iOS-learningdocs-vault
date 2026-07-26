---
title: MTLCommandQueue
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandqueue
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandqueue.json'
content_hash: 'sha256:7d474e3a724eb768'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCommandQueue

<sub>Protocol</sub>

An instance you use to create, submit, and schedule command buffers to a specific GPU device to run the commands within those buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLCommandQueue : NSObjectProtocol, Sendable
```

## Overview

A command queue maintains an ordered list of command buffers. You use a command queue to:

- Create command buffers, which you fill with commands for the GPU device that creates the queue
- Submit command buffers to run on that GPU

Create a command queue from an [MTLDevice](mtldevice.md) instance by calling its [- newCommandQueue](<mtldevice/makecommandqueue().md>) or [- newCommandQueueWithMaxCommandBufferCount:](<mtldevice/makecommandqueue(maxcommandbuffercount_).md>) method. Typically, you create one or more command queues when your app launches and then keep them throughout your app’s lifetime.

With each [MTLCommandQueue](mtlcommandqueue.md) instance you create, you can create [MTLCommandBuffer](mtlcommandbuffer.md) instances for that queue by calling its [- commandBuffer](<mtlcommandqueue/makecommandbuffer().md>) or [- commandBufferWithUnretainedReferences](<mtlcommandqueue/makecommandbufferwithunretainedreferences().md>) method.

> [!note] Note
> Each command queue is thread-safe and allows you to encode commands in multiple command buffers simultaneously.

For more information about command buffers and encoding GPU commands to them — such as rendering images and computing data in parallel — see [Setting up a command structure](setting-up-a-command-structure.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating command buffers

- [- commandBufferWithDescriptor:](<mtlcommandqueue/makecommandbuffer(descriptor_).md>) — Returns a command buffer from the command queue that you configure with a descriptor.
- [- commandBuffer](<mtlcommandqueue/makecommandbuffer().md>) — Returns a command buffer from the command queue that maintains strong references to resources.
- [- commandBufferWithUnretainedReferences](<mtlcommandqueue/makecommandbufferwithunretainedreferences().md>) — Returns a command buffer from the command queue that doesn’t maintain strong references to resources.

### Attaching residency sets

- [- addResidencySet:](<mtlcommandqueue/addresidencyset(__).md>) — Applies a residency set to a queue, which Metal applies to the queue’s command buffers as you commit them.
- [addResidencySets(_:)](<mtlcommandqueue/addresidencysets(__).md>) — Applies multiple residency sets to a queue, which Metal applies to the queue’s command buffers as you commit them.

### Detaching residency sets

- [- removeResidencySet:](<mtlcommandqueue/removeresidencyset(__).md>) — Removes a residency set from a command queue’s list, which means Metal doesn’t apply it to the queue’s command buffers as you commit them.
- [removeResidencySets(_:)](<mtlcommandqueue/removeresidencysets(__).md>) — Removes multiple residency sets from a command queue’s list, which means Metal doesn’t apply them to the queue’s command buffers as you commit them.

### Identifying the command queue

- [device](mtlcommandqueue/device.md) — The GPU device that creates the command queue.
- [label](mtlcommandqueue/label.md) — An optional name that can help you identify the command queue.

### Deprecated

- [- insertDebugCaptureBoundary](<mtlcommandqueue/insertdebugcaptureboundary().md>) — Informs Xcode about when GPU Frame Capture starts and stops. _(deprecated)_

## See Also

### Submitting work to a GPU with Metal

- [Setting up a command structure](setting-up-a-command-structure.md) — Discover how Metal executes commands on a GPU.
- [MTLCommandQueueDescriptor](mtlcommandqueuedescriptor.md) — A configuration that customizes the behavior for a new command queue.
- [MTLCommandBuffer](mtlcommandbuffer.md) — A container that stores a sequence of GPU commands that you encode into it.
- [MTLCommandBufferDescriptor](mtlcommandbufferdescriptor.md) — A configuration that customizes the behavior for a new command buffer.
- [MTLCommandBufferError](mtlcommandbuffererror-swift.struct.md) — The command buffer error codes that indicate why the GPU doesn’t finish executing a command buffer.
- [MTLCommandEncoder](mtlcommandencoder.md) — An encoder that writes GPU commands into a command buffer.
