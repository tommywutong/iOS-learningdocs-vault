---
title: device
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffer/device
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/device.json'
content_hash: 'sha256:fbbaf97011f714cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# device

<sub>Instance Property</sub>

The GPU device that indirectly owns the command buffer because you create it from a command queue the device also owns.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var device: any MTLDevice { get }
```

## Discussion

The command buffer can only work with other instances that [device](device.md) creates, directly or indirectly, such as buffers and textures.

## See Also

### Identifying the command buffer

- [label](label.md) — An optional name that can help you identify the command buffer.
- [commandQueue](commandqueue.md) — The command queue that creates the command buffer.
