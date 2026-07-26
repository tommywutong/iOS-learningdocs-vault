---
title: intersectionFunctionStride
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlintersectionfunctionbufferarguments/intersectionfunctionstride
source_url: 'https://developer.apple.com/documentation/metal/mtlintersectionfunctionbufferarguments/intersectionfunctionstride'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlintersectionfunctionbufferarguments/intersectionfunctionstride.json'
content_hash: 'sha256:1a65349740f79242'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIntersectionFunctionBufferArguments](../mtlintersectionfunctionbufferarguments.md)

# intersectionFunctionStride

<sub>Instance Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var intersectionFunctionStride: UInt64
```

## Discussion

The stride between intersection function entries in intersectionFunctionBuffer. The stride needs to be either 0 or aligned to 8 bytes. Note that only the first 12 bits of this value are used by Metal.
