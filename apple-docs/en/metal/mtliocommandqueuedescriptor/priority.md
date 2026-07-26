---
title: priority
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliocommandqueuedescriptor/priority
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandqueuedescriptor/priority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandqueuedescriptor/priority.json'
content_hash: 'sha256:ca8d1dd402ee692e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOCommandQueueDescriptor](../mtliocommandqueuedescriptor.md)

# priority

<sub>Instance Property</sub>

Configures the priority for a new input/output command queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var priority: MTLIOPriority { get set }
```

## See Also

### Configuring the input/output command queue

- [type](type.md) — Configures the queue type for a new input/output command queue.
- [maxCommandsInFlight](maxcommandsinflight.md) — Sets the largest number of individual commands that an input/output command queue can run at a time.
- [maxCommandBufferCount](maxcommandbuffercount.md) — Sets the largest number of outstanding input/output command buffers a queue can have at any point in time.
