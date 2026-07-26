---
title: MTLIOCommandQueue
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliocommandqueue
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandqueue.json'
content_hash: 'sha256:c41f128e4f19153c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIOCommandQueue

<sub>Protocol</sub>

A command queue that schedules input/output commands for reading files in the file system, and writing to GPU resources and memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLIOCommandQueue : NSObjectProtocol, Sendable
```

## Overview

Use an input/output command queue to submit commands, in command buffers, that load assets from the file system directly into GPU resources. Your app can then use those resources with other commands it submits to an [MTLCommandQueue](mtlcommandqueue.md) that comes from the same [MTLDevice](mtldevice.md).

You make input/output command queues by creating and configuring an [MTLIOCommandQueueDescriptor](mtliocommandqueuedescriptor.md) instance and calling an [MTLDevice](mtldevice.md) instance’s [- newIOCommandQueueWithDescriptor:error:](<mtldevice/makeiocommandqueue(descriptor_).md>) method.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a input/output command buffer

- [- commandBuffer](<mtliocommandqueue/makecommandbuffer().md>) — Creates an input/output command buffer for the command queue.
- [- commandBufferWithUnretainedReferences](<mtliocommandqueue/makecommandbufferwithunretainedreferences().md>) — Creates an input/output command buffer for the command queue that doesn’t retain the instances you pass to its methods.

### Adding a barrier to the queue

- [- enqueueBarrier](<mtliocommandqueue/enqueuebarrier().md>) — Appends a barrier that tells the input/output command queue to finish running all in-flight command buffers before running any new command buffers.

### Naming the queue

- [label](mtliocommandqueue/label.md) — An optional name for the input/output command queue.

## See Also

### I/O command queues

- [MTLIOCommandQueueDescriptor](mtliocommandqueuedescriptor.md) — A configuration template you use to create a new input/output command queue.
- [MTLIOPriority](mtliopriority.md) — Designates the priority for a new input/output command queue.
- [MTLIOCommandQueueType](mtliocommandqueuetype.md) — Designates the queue type for a new input/output command queue.
- [MTLIOScratchBufferAllocator](mtlioscratchbufferallocator.md) — A protocol your app implements to provide scratch memory to an input/output command queue.
- [MTLIOScratchBuffer](mtlioscratchbuffer.md) — A protocol your app implements that wraps a Metal buffer instance to serve as scratch memory for an input/output command queue.
