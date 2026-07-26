---
title: maxCommandBufferCount
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliocommandqueuedescriptor/maxcommandbuffercount
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandqueuedescriptor/maxcommandbuffercount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandqueuedescriptor/maxcommandbuffercount.json'
content_hash: 'sha256:d2cd8e75db6e8493'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOCommandQueueDescriptor](../mtliocommandqueuedescriptor.md)

# maxCommandBufferCount

<sub>Instance Property</sub>

Sets the largest number of outstanding input/output command buffers a queue can have at any point in time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxCommandBufferCount: Int { get set }
```

## Discussion

The input/output command buffers that count against this limit are those that are currently executing in a queue or waiting to execute. The command buffers that have finished executing no longer count against this limit.

## See Also

### Configuring the input/output command queue

- [priority](priority.md) — Configures the priority for a new input/output command queue.
- [type](type.md) — Configures the queue type for a new input/output command queue.
- [maxCommandsInFlight](maxcommandsinflight.md) — Sets the largest number of individual commands that an input/output command queue can run at a time.
