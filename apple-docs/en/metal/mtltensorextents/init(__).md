---
title: 'init(_:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtltensorextents/init(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtltensorextents/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensorextents/init%28_%3A%29.json'
content_hash: 'sha256:2d60bced4afb4903'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensorExtents](../mtltensorextents.md)

# init(_:)

<sub>Initializer</sub>

Creates a tensor with extents from an array of dimension values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init?(_ values: [Int])
```

## Discussion

You are responsible for ensuring the array contains at most `MTL_TENSOR_MAX_RANK` (`16`) elements.
