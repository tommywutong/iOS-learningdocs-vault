---
title: commandQueue
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffer/commandqueue
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/commandqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/commandqueue.json'
content_hash: 'sha256:515accd871915481'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# commandQueue

<sub>Instance Property</sub>

The command queue that creates the command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var commandQueue: any MTLCommandQueue { get }
```

## Discussion

Each command buffer can only submit its commands to the queue that creates it.

## See Also

### Identifying the command buffer

- [label](label.md) — An optional name that can help you identify the command buffer.
- [device](device.md) — The GPU device that indirectly owns the command buffer because you create it from a command queue the device also owns.
