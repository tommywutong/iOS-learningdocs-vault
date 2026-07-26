---
title: nonOpaque
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureinstanceoptions/nonopaque
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstanceoptions/nonopaque'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureinstanceoptions/nonopaque.json'
content_hash: 'sha256:cc789d3fa6a09485'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureInstanceOptions](../mtlaccelerationstructureinstanceoptions.md)

# nonOpaque

<sub>Type Property</sub>

Specifies that intersectors should treat the instance as non-opaque.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var nonOpaque: MTLAccelerationStructureInstanceOptions { get }
```

## See Also

### Usage options

- [MTLAccelerationStructureInstanceOptionDisableTriangleCulling](disabletriangleculling.md) — An option that turns off culling for this instance if ray intersector has culling enabled.
- [MTLAccelerationStructureInstanceOptionTriangleFrontFacingWindingCounterClockwise](trianglefrontfacingwindingcounterclockwise.md) — Specifies that the instance specifies front facing triangles in counter-clockwise order.
- [MTLAccelerationStructureInstanceOptionOpaque](opaque.md) — Specifies that intersectors should treat the instance as opaque.
