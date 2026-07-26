---
title: strides
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltensor/strides
source_url: 'https://developer.apple.com/documentation/metal/mtltensor/strides'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensor/strides.json'
content_hash: 'sha256:cc5211b3ca057aad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensor](../mtltensor.md)

# strides

<sub>Instance Property</sub>

An array of strides, in elements, one for each dimension of this tensor, if applicable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var strides: MTLTensorExtents? { get }
```

## Discussion

This property is non-nil only for tensors created from a buffer.
