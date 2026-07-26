---
title: allowDuplicateIntersectionFunctionInvocation
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuregeometrydescriptor/allowduplicateintersectionfunctioninvocation
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuregeometrydescriptor/allowduplicateintersectionfunctioninvocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuregeometrydescriptor/allowduplicateintersectionfunctioninvocation.json'
content_hash: 'sha256:78e49bf27df9b5aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureGeometryDescriptor](../mtlaccelerationstructuregeometrydescriptor.md)

# allowDuplicateIntersectionFunctionInvocation

<sub>Instance Property</sub>

A Boolean value that indicates whether Metal calls the ray-intersection test more than once per primitive on the structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var allowDuplicateIntersectionFunctionInvocation: Bool { get set }
```

## See Also

### Specifying base geometry properties

- [label](label.md) — A label for the geometry structure, suitable for debugging.
- [intersectionFunctionTableOffset](intersectionfunctiontableoffset.md) — An index into the intersection table for determining which intersection function Metal calls when it intersects a ray with the acceleration structure.
- [opaque](opaque.md) — A Boolean value that determines whether the geometry data in the acceleration structure needs to skip triangle-intersection tests.
