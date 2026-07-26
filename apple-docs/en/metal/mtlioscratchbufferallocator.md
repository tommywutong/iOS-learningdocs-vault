---
title: MTLIOScratchBufferAllocator
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlioscratchbufferallocator
source_url: 'https://developer.apple.com/documentation/metal/mtlioscratchbufferallocator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlioscratchbufferallocator.json'
content_hash: 'sha256:89e58a57e0a662a2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIOScratchBufferAllocator

<sub>Protocol</sub>

A protocol your app implements to provide scratch memory to an input/output command queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLIOScratchBufferAllocator : NSObjectProtocol
```

## Overview

An allocator returns instances of [MTLIOScratchBuffer](mtlioscratchbuffer.md), another type your app implements.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Providing scratch memory to a queue

- [- newScratchBufferWithMinimumSize:](<mtlioscratchbufferallocator/makescratchbuffer(minimumsize_).md>) — Creates a scratch memory buffer for an input/output command queue.

## See Also

### I/O command queues

- [MTLIOCommandQueue](mtliocommandqueue.md) — A command queue that schedules input/output commands for reading files in the file system, and writing to GPU resources and memory.
- [MTLIOCommandQueueDescriptor](mtliocommandqueuedescriptor.md) — A configuration template you use to create a new input/output command queue.
- [MTLIOPriority](mtliopriority.md) — Designates the priority for a new input/output command queue.
- [MTLIOCommandQueueType](mtliocommandqueuetype.md) — Designates the queue type for a new input/output command queue.
- [MTLIOScratchBuffer](mtlioscratchbuffer.md) — A protocol your app implements that wraps a Metal buffer instance to serve as scratch memory for an input/output command queue.
