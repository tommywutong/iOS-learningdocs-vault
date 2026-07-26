---
title: screenSize
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrasterizationratemapdescriptor/screensize
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratemapdescriptor/screensize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratemapdescriptor/screensize.json'
content_hash: 'sha256:930a1df89aa94b75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateMapDescriptor](../mtlrasterizationratemapdescriptor.md)

# screenSize

<sub>Instance Property</sub>

The size of the viewport coordinate system, in logical pixels.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var screenSize: MTLSize { get set }
```

## Discussion

Metal ignores the depth component of this property.

The viewport coordinate system’s origin is always at `(0,0)` and this property determines its size.
