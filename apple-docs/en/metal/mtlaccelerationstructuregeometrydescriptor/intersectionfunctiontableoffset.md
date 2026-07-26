---
title: intersectionFunctionTableOffset
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuregeometrydescriptor/intersectionfunctiontableoffset
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuregeometrydescriptor/intersectionfunctiontableoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuregeometrydescriptor/intersectionfunctiontableoffset.json'
content_hash: 'sha256:a484f16bf1f6ee6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureGeometryDescriptor](../mtlaccelerationstructuregeometrydescriptor.md)

# intersectionFunctionTableOffset

<sub>Instance Property</sub>

An index into the intersection table for determining which intersection function Metal calls when it intersects a ray with the acceleration structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var intersectionFunctionTableOffset: Int { get set }
```

## See Also

### Specifying base geometry properties

- [label](label.md) — A label for the geometry structure, suitable for debugging.
- [opaque](opaque.md) — A Boolean value that determines whether the geometry data in the acceleration structure needs to skip triangle-intersection tests.
- [allowDuplicateIntersectionFunctionInvocation](allowduplicateintersectionfunctioninvocation.md) — A Boolean value that indicates whether Metal calls the ray-intersection test more than once per primitive on the structure.
