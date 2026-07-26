---
title: rasterizationRateMap
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4renderpassdescriptor/rasterizationratemap
source_url: 'https://developer.apple.com/documentation/metal/mtl4renderpassdescriptor/rasterizationratemap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4renderpassdescriptor/rasterizationratemap.json'
content_hash: 'sha256:42197f122ed3887c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderPassDescriptor](../mtl4renderpassdescriptor.md)

# rasterizationRateMap

<sub>Instance Property</sub>

Assigns an optional variable rasterization rate map that Metal uses in the render pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var rasterizationRateMap: (any MTLRasterizationRateMap)? { get set }
```

## Discussion

Enabling variable rasterization rate allows Metal to decrease the rasterization rate, typically in unimportant regions of color attachments, to accelerate processing.

When set to `nil`, the default, Metal doesn’t use variable rasterization rate.
