---
title: label
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffer/label
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/label.json'
content_hash: 'sha256:84a6cb1666a8a422'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# label

<sub>Instance Property</sub>

An optional name that can help you identify the command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String? { get set }
```

## Discussion

Set labels to help you quickly identify a command buffer at runtime in the Metal debugging and profiling tools. See [Naming resources and commands](../../xcode/naming-resources-and-commands.md).

## See Also

### Identifying the command buffer

- [commandQueue](commandqueue.md) — The command queue that creates the command buffer.
- [device](device.md) — The GPU device that indirectly owns the command buffer because you create it from a command queue the device also owns.
