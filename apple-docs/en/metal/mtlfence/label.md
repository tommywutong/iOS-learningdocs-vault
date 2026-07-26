---
title: label
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfence/label
source_url: 'https://developer.apple.com/documentation/metal/mtlfence/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfence/label.json'
content_hash: 'sha256:0aa464b77233cfa8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFence](../mtlfence.md)

# label

<sub>Instance Property</sub>

A string that identifies the fence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String? { get set }
```

## Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See [Naming resources and commands](../../xcode/naming-resources-and-commands.md).

## See Also

### Identifying a fence

- [device](device.md) — The device object that created the fence.
