---
title: intersectionFunctionTableOffset
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuregeometrydescriptor/intersectionfunctiontableoffset
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuregeometrydescriptor/intersectionfunctiontableoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuregeometrydescriptor/intersectionfunctiontableoffset.json'
content_hash: 'sha256:6ea2e9e7d046f5cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureGeometryDescriptor](../mtl4accelerationstructuregeometrydescriptor.md)

# intersectionFunctionTableOffset

<sub>Instance Property</sub>

Sets the offset that this geometry contributes to determining the intersection function to invoke when a ray intersects it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var intersectionFunctionTableOffset: Int { get set }
```

## Discussion

When you perform a ray tracing operation in the Metal Shading Language, and provide the ray intersector object with an instance of [MTLIntersectionFunctionTable](../mtlintersectionfunctiontable.md), Metal adds this offset to the instance offset from structs such as:

- [MTLAccelerationStructureInstanceDescriptor](../mtlaccelerationstructureinstancedescriptor.md)
- [MTLAccelerationStructureUserIDInstanceDescriptor](../mtlaccelerationstructureuseridinstancedescriptor.md)
- [MTLAccelerationStructureMotionInstanceDescriptor](../mtlaccelerationstructuremotioninstancedescriptor.md)
- [MTLIndirectAccelerationStructureInstanceDescriptor](../mtlindirectaccelerationstructureinstancedescriptor.md)
- [MTLIndirectAccelerationStructureMotionInstanceDescriptor](../mtlindirectaccelerationstructuremotioninstancedescriptor.md)

The sum of these offsets provides an index into the intersection function table that the ray tracing system uses to retrieve and invoke the function at this index, allowing you to customize the intersection evaluation process.
