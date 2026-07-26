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
doc_path: /documentation/metal/mtlrasterizationratemapdescriptor/label
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratemapdescriptor/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratemapdescriptor/label.json'
content_hash: 'sha256:e96c02e02d8f7b2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateMapDescriptor](../mtlrasterizationratemapdescriptor.md)

# label

<sub>Instance Property</sub>

A string used to identify the rate map you create with the descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String? { get set }
```

## Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See [Naming resources and commands](../../xcode/naming-resources-and-commands.md).
