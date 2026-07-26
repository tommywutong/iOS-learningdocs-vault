---
title: disableTriangleCulling
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureinstanceoptions/disabletriangleculling
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstanceoptions/disabletriangleculling'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureinstanceoptions/disabletriangleculling.json'
content_hash: 'sha256:e51091bd06547bf0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureInstanceOptions](../mtlaccelerationstructureinstanceoptions.md)

# disableTriangleCulling

<sub>Type Property</sub>

An option that turns off culling for this instance if ray intersector has culling enabled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var disableTriangleCulling: MTLAccelerationStructureInstanceOptions { get }
```

## See Also

### Usage options

- [MTLAccelerationStructureInstanceOptionTriangleFrontFacingWindingCounterClockwise](trianglefrontfacingwindingcounterclockwise.md) — Specifies that the instance specifies front facing triangles in counter-clockwise order.
- [MTLAccelerationStructureInstanceOptionOpaque](opaque.md) — Specifies that intersectors should treat the instance as opaque.
- [MTLAccelerationStructureInstanceOptionNonOpaque](nonopaque.md) — Specifies that intersectors should treat the instance as non-opaque.
