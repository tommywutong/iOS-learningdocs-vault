---
title: usage
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltensordescriptor/usage
source_url: 'https://developer.apple.com/documentation/metal/mtltensordescriptor/usage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensordescriptor/usage.json'
content_hash: 'sha256:f42534799b70e8fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensorDescriptor](../mtltensordescriptor.md)

# usage

<sub>Instance Property</sub>

A set of contexts in which you can use tensors you create with this descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var usage: MTLTensorUsage { get set }
```

## Discussion

The default value for this property is a bitwise `OR` of:

- [MTLTensorUsageRender](../mtltensorusage/render.md)
- [MTLTensorUsageCompute](../mtltensorusage/compute.md)
