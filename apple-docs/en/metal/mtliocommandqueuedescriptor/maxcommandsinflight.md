---
title: maxCommandsInFlight
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliocommandqueuedescriptor/maxcommandsinflight
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandqueuedescriptor/maxcommandsinflight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandqueuedescriptor/maxcommandsinflight.json'
content_hash: 'sha256:01bd16cacef97266'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOCommandQueueDescriptor](../mtliocommandqueuedescriptor.md)

# maxCommandsInFlight

<sub>Instance Property</sub>

Sets the largest number of individual commands that an input/output command queue can run at a time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxCommandsInFlight: Int { get set }
```

## Discussion

Set to `0` to instruct Metal to select an appropriate value for you — based on the system’s available memory.

## See Also

### Configuring the input/output command queue

- [priority](priority.md) — Configures the priority for a new input/output command queue.
- [type](type.md) — Configures the queue type for a new input/output command queue.
- [maxCommandBufferCount](maxcommandbuffercount.md) — Sets the largest number of outstanding input/output command buffers a queue can have at any point in time.
