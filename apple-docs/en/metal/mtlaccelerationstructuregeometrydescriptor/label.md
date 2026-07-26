---
title: label
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuregeometrydescriptor/label
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuregeometrydescriptor/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuregeometrydescriptor/label.json'
content_hash: 'sha256:1e9946651250ace1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureGeometryDescriptor](../mtlaccelerationstructuregeometrydescriptor.md)

# label

<sub>Instance Property</sub>

A label for the geometry structure, suitable for debugging.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String? { get set }
```

## See Also

### Specifying base geometry properties

- [intersectionFunctionTableOffset](intersectionfunctiontableoffset.md) — An index into the intersection table for determining which intersection function Metal calls when it intersects a ray with the acceleration structure.
- [opaque](opaque.md) — A Boolean value that determines whether the geometry data in the acceleration structure needs to skip triangle-intersection tests.
- [allowDuplicateIntersectionFunctionInvocation](allowduplicateintersectionfunctioninvocation.md) — A Boolean value that indicates whether Metal calls the ray-intersection test more than once per primitive on the structure.
