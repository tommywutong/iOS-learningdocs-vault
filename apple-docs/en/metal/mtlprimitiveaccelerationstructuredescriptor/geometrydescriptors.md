---
title: geometryDescriptors
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlprimitiveaccelerationstructuredescriptor/geometrydescriptors
source_url: 'https://developer.apple.com/documentation/metal/mtlprimitiveaccelerationstructuredescriptor/geometrydescriptors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlprimitiveaccelerationstructuredescriptor/geometrydescriptors.json'
content_hash: 'sha256:86152cd3dfc4f38a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPrimitiveAccelerationStructureDescriptor](../mtlprimitiveaccelerationstructuredescriptor.md)

# geometryDescriptors

<sub>Instance Property</sub>

An array that contains the individual pieces of geometry that compose the acceleration structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var geometryDescriptors: [MTLAccelerationStructureGeometryDescriptor]? { get set }
```

## Discussion

The value of the [motionKeyframeCount](motionkeyframecount.md) property determines what kinds of geometry descriptors you can assign to this property and how you need to configure them.

If the value of [motionKeyframeCount](motionkeyframecount.md) is greater than 1, then the geometry descriptors need to be either [MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor](../mtlaccelerationstructuremotionboundingboxgeometrydescriptor.md) or [MTLAccelerationStructureMotionTriangleGeometryDescriptor](../mtlaccelerationstructuremotiontrianglegeometrydescriptor.md) objects. Further, you need to provide exactly that many keyframes of data when creating those geometry descriptors. If [motionKeyframeCount](motionkeyframecount.md)  is 1, use [MTLAccelerationStructureBoundingBoxGeometryDescriptor](../mtlaccelerationstructureboundingboxgeometrydescriptor.md) or [MTLAccelerationStructureTriangleGeometryDescriptor](../mtlaccelerationstructuretrianglegeometrydescriptor.md) objects instead.

## See Also

### Related Documentation

- [motionKeyframeCount](motionkeyframecount.md) — The number of keyframes in the geometry data.
