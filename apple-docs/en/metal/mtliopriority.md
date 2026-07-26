---
title: MTLIOPriority
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliopriority
source_url: 'https://developer.apple.com/documentation/metal/mtliopriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliopriority.json'
content_hash: 'sha256:e3fcc47dd3d1f381'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIOPriority

<sub>Enumeration</sub>

Designates the priority for a new input/output command queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLIOPriority
```

## Overview

Set a new input/output command queue’s priority that you create with an [MTLIOCommandQueueDescriptor](mtliocommandqueuedescriptor.md) instance by setting its [priority](mtliocommandqueuedescriptor/priority.md) property. Create a queue that minimizes an asset’s loading latency by setting a descriptor’s priority to [MTLIOPriorityHigh](mtliopriority/high.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### I/O command queue priorities

- [MTLIOPriorityNormal](mtliopriority/normal.md) — Designates the normal priority for a new input/output command queue.
- [MTLIOPriorityLow](mtliopriority/low.md) — Designates the low priority for a new input/output command queue.
- [MTLIOPriorityHigh](mtliopriority/high.md) — Sets a new input/output command queue’s priority to a high priority.

### Initializers

- [init(rawValue:)](<mtliopriority/init(rawvalue_).md>)

## See Also

### I/O command queues

- [MTLIOCommandQueue](mtliocommandqueue.md) — A command queue that schedules input/output commands for reading files in the file system, and writing to GPU resources and memory.
- [MTLIOCommandQueueDescriptor](mtliocommandqueuedescriptor.md) — A configuration template you use to create a new input/output command queue.
- [MTLIOCommandQueueType](mtliocommandqueuetype.md) — Designates the queue type for a new input/output command queue.
- [MTLIOScratchBufferAllocator](mtlioscratchbufferallocator.md) — A protocol your app implements to provide scratch memory to an input/output command queue.
- [MTLIOScratchBuffer](mtlioscratchbuffer.md) — A protocol your app implements that wraps a Metal buffer instance to serve as scratch memory for an input/output command queue.
