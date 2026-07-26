---
title: geometryDescriptors
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4primitiveaccelerationstructuredescriptor/geometrydescriptors
source_url: 'https://developer.apple.com/documentation/metal/mtl4primitiveaccelerationstructuredescriptor/geometrydescriptors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4primitiveaccelerationstructuredescriptor/geometrydescriptors.json'
content_hash: 'sha256:809264b841436f5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4PrimitiveAccelerationStructureDescriptor](../mtl4primitiveaccelerationstructuredescriptor.md)

# geometryDescriptors

<sub>Instance Property</sub>

Associates the array of geometry descriptors that comprise this primitive acceleration structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var geometryDescriptors: [MTL4AccelerationStructureGeometryDescriptor]? { get set }
```

## Discussion

If you enable keyframe motion by setting property [motionKeyframeCount](motionkeyframecount.md) to a value greater than `1`, then all geometry descriptors this array references need to be motion geometry descriptors and have a number of primitive buffers equals to [motionKeyframeCount](motionkeyframecount.md).

Example of motion geometry descriptors include: [MTL4AccelerationStructureMotionTriangleGeometryDescriptor](../mtl4accelerationstructuremotiontrianglegeometrydescriptor.md), [MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor](../mtl4accelerationstructuremotionboundingboxgeometrydescriptor.md), [MTL4AccelerationStructureMotionCurveGeometryDescriptor](../mtl4accelerationstructuremotioncurvegeometrydescriptor.md).
