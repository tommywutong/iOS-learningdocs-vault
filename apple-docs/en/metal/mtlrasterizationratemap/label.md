---
title: label
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrasterizationratemap/label
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratemap/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratemap/label.json'
content_hash: 'sha256:135682da3553d362'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateMap](../mtlrasterizationratemap.md)

# label

<sub>Instance Property</sub>

A string that identifies the rate map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String? { get }
```

## Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. For more information, see [Naming resources and commands](../../xcode/naming-resources-and-commands.md).

## See Also

### Identifying the rate map

- [device](device.md) — The device object that created the rate map.
