---
title: rasterizationRateMap
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpassdescriptor/rasterizationratemap
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/rasterizationratemap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassdescriptor/rasterizationratemap.json'
content_hash: 'sha256:76efdf373d6cbe8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md)

# rasterizationRateMap

<sub>Instance Property</sub>

The rasterization rate map to use when executing the render pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var rasterizationRateMap: (any MTLRasterizationRateMap)? { get set }
```

## Discussion

The default value is `nil`, which means that viewport coordinates are in the same coordinate system as the physical coordinates in the render target. Otherwise, Metal uses the rate map to convert between viewport coordinates and physical coordinates in the render target.
