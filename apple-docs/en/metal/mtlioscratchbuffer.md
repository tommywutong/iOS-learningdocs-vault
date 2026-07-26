---
title: MTLIOScratchBuffer
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlioscratchbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtlioscratchbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlioscratchbuffer.json'
content_hash: 'sha256:2638736b304d21e2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIOScratchBuffer

<sub>Protocol</sub>

A protocol your app implements that wraps a Metal buffer instance to serve as scratch memory for an input/output command queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLIOScratchBuffer : NSObjectProtocol
```

## Overview

Your app can reintegrate an [MTLIOScratchBuffer](mtlioscratchbuffer.md) instance’s underlying memory back into a memory pool by overriding your type’s [dealloc](../objectivec/nsobject-swift.class/dealloc.md) method. The system calls the method when an input/output command queue no longer needs a scratch buffer.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Wrapping a buffer

- [buffer](mtlioscratchbuffer/buffer.md) — A Metal buffer that serves as scratch memory for an input/output command queue.

## See Also

### I/O command queues

- [MTLIOCommandQueue](mtliocommandqueue.md) — A command queue that schedules input/output commands for reading files in the file system, and writing to GPU resources and memory.
- [MTLIOCommandQueueDescriptor](mtliocommandqueuedescriptor.md) — A configuration template you use to create a new input/output command queue.
- [MTLIOPriority](mtliopriority.md) — Designates the priority for a new input/output command queue.
- [MTLIOCommandQueueType](mtliocommandqueuetype.md) — Designates the queue type for a new input/output command queue.
- [MTLIOScratchBufferAllocator](mtlioscratchbufferallocator.md) — A protocol your app implements to provide scratch memory to an input/output command queue.
