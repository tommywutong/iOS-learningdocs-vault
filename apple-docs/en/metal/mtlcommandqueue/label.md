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
doc_path: /documentation/metal/mtlcommandqueue/label
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandqueue/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandqueue/label.json'
content_hash: 'sha256:f0d1b6e59332da71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandQueue](../mtlcommandqueue.md)

# label

<sub>Instance Property</sub>

An optional name that can help you identify the command queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String? { get set }
```

## Discussion

Set labels to help you quickly identify a GPU at runtime in the Metal debugging and profiling tools. See [Naming resources and commands](../../xcode/naming-resources-and-commands.md).

## See Also

### Identifying the command queue

- [device](device.md) — The GPU device that creates the command queue.
