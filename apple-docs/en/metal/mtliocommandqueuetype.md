---
title: MTLIOCommandQueueType
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliocommandqueuetype
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandqueuetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandqueuetype.json'
content_hash: 'sha256:5f4f1b4af3152047'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIOCommandQueueType

<sub>Enumeration</sub>

Designates the queue type for a new input/output command queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLIOCommandQueueType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### I/O command queue types

- [MTLIOCommandQueueTypeConcurrent](mtliocommandqueuetype/concurrent.md) — Sets a new input/output command queue’s type to a queue that runs commands concurrently.
- [MTLIOCommandQueueTypeSerial](mtliocommandqueuetype/serial.md) — Sets a new input/output command queue’s type to a queue that runs commands serially.

### Initializers

- [init(rawValue:)](<mtliocommandqueuetype/init(rawvalue_).md>)

## See Also

### I/O command queues

- [MTLIOCommandQueue](mtliocommandqueue.md) — A command queue that schedules input/output commands for reading files in the file system, and writing to GPU resources and memory.
- [MTLIOCommandQueueDescriptor](mtliocommandqueuedescriptor.md) — A configuration template you use to create a new input/output command queue.
- [MTLIOPriority](mtliopriority.md) — Designates the priority for a new input/output command queue.
- [MTLIOScratchBufferAllocator](mtlioscratchbufferallocator.md) — A protocol your app implements to provide scratch memory to an input/output command queue.
- [MTLIOScratchBuffer](mtlioscratchbuffer.md) — A protocol your app implements that wraps a Metal buffer instance to serve as scratch memory for an input/output command queue.
