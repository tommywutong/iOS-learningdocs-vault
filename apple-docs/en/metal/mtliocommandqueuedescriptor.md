---
title: MTLIOCommandQueueDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliocommandqueuedescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandqueuedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandqueuedescriptor.json'
content_hash: 'sha256:05b4df77f61215d7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIOCommandQueueDescriptor

<sub>Class</sub>

A configuration template you use to create a new input/output command queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLIOCommandQueueDescriptor
```

## Overview

Use this descriptor type to configure the settings of each input/output command queue that you create using [- newIOCommandQueueWithDescriptor:error:](<mtldevice/makeiocommandqueue(descriptor_).md>). To create additional input/output command queues, you can reuse a descriptor instance and optionally reconfigure its properties.

> [!note] Note
> Changing a descriptor’s properties doesn’t affect command queues you’ve already created with the descriptor.

Create each input/output queue to meet your apps needs by setting the descriptor’s properties.

- Select a queue’s relative level of importance with the [priority](mtliocommandqueuedescriptor/priority.md) property.
- Create a queue that runs multiple input/output command buffers in parallel by setting the [type](mtliocommandqueuedescriptor/type.md) property to [MTLIOCommandQueueTypeConcurrent](mtliocommandqueuetype/concurrent.md).
- Decide how many individual commands a queue can run simultaneously with the [maxCommandsInFlight](mtliocommandqueuedescriptor/maxcommandsinflight.md) property.
- Choose how many command buffers a queue can have waiting to run with [maxCommandBufferCount](mtliocommandqueuedescriptor/maxcommandbuffercount.md) property.
- Take control of the queue’s scratch memory allocation by implementing [MTLIOScratchBufferAllocator](mtlioscratchbufferallocator.md) and assign an instance of it to the [scratchBufferAllocator](mtliocommandqueuedescriptor/scratchbufferallocator.md) property.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the input/output command queue

- [priority](mtliocommandqueuedescriptor/priority.md) — Configures the priority for a new input/output command queue.
- [type](mtliocommandqueuedescriptor/type.md) — Configures the queue type for a new input/output command queue.
- [maxCommandsInFlight](mtliocommandqueuedescriptor/maxcommandsinflight.md) — Sets the largest number of individual commands that an input/output command queue can run at a time.
- [maxCommandBufferCount](mtliocommandqueuedescriptor/maxcommandbuffercount.md) — Sets the largest number of outstanding input/output command buffers a queue can have at any point in time.

### Providing your own a scratch buffer

- [scratchBufferAllocator](mtliocommandqueuedescriptor/scratchbufferallocator.md) — An optional memory allocator that you implement to manage the scratch memory that an input/output command queue requests.

## See Also

### I/O command queues

- [MTLIOCommandQueue](mtliocommandqueue.md) — A command queue that schedules input/output commands for reading files in the file system, and writing to GPU resources and memory.
- [MTLIOPriority](mtliopriority.md) — Designates the priority for a new input/output command queue.
- [MTLIOCommandQueueType](mtliocommandqueuetype.md) — Designates the queue type for a new input/output command queue.
- [MTLIOScratchBufferAllocator](mtlioscratchbufferallocator.md) — A protocol your app implements to provide scratch memory to an input/output command queue.
- [MTLIOScratchBuffer](mtlioscratchbuffer.md) — A protocol your app implements that wraps a Metal buffer instance to serve as scratch memory for an input/output command queue.
