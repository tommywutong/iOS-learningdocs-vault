---
title: opaque
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuregeometrydescriptor/opaque
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuregeometrydescriptor/opaque'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuregeometrydescriptor/opaque.json'
content_hash: 'sha256:341464ee8508a490'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureGeometryDescriptor](../mtlaccelerationstructuregeometrydescriptor.md)

# opaque

<sub>Instance Property</sub>

A Boolean value that determines whether the geometry data in the acceleration structure needs to skip triangle-intersection tests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var opaque: Bool { get set }
```

## Discussion

By default, after Metal finds an intersection between a ray and a primitive, it runs your specified intersection function to determine whether the ray actually hit the primitive. If you specify that triangle geometry is opaque, Metal skips the intersection function and processes any intersection as a hit.

If you are using bounding box geometry, Metal calls your intersection function, passing a Boolean value that indicates that the bounding box that the ray intersected with is opaque.

## See Also

### Specifying base geometry properties

- [label](label.md) — A label for the geometry structure, suitable for debugging.
- [intersectionFunctionTableOffset](intersectionfunctiontableoffset.md) — An index into the intersection table for determining which intersection function Metal calls when it intersects a ray with the acceleration structure.
- [allowDuplicateIntersectionFunctionInvocation](allowduplicateintersectionfunctioninvocation.md) — A Boolean value that indicates whether Metal calls the ray-intersection test more than once per primitive on the structure.
