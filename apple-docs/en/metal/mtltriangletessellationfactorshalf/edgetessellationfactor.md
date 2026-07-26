---
title: edgeTessellationFactor
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltriangletessellationfactorshalf/edgetessellationfactor
source_url: 'https://developer.apple.com/documentation/metal/mtltriangletessellationfactorshalf/edgetessellationfactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltriangletessellationfactorshalf/edgetessellationfactor.json'
content_hash: 'sha256:13531284ce4fa240'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTriangleTessellationFactorsHalf](../mtltriangletessellationfactorshalf.md)

# edgeTessellationFactor

<sub>Instance Property</sub>

The edge tessellation factors, with each index value providing the tessellation factor for a particular edge.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var edgeTessellationFactor: (UInt16, UInt16, UInt16)
```

## Discussion

- The value in index 0 provides the tessellation factor for the upper-left edge of the patch.
- The value in index 1 provides the tessellation factor for the bottom edge of the patch.
- The value in index 2 provides the tessellation factor for the upper-right edge of the patch.
