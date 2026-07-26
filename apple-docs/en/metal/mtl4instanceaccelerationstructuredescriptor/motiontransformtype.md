---
title: motionTransformType
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4instanceaccelerationstructuredescriptor/motiontransformtype
source_url: 'https://developer.apple.com/documentation/metal/mtl4instanceaccelerationstructuredescriptor/motiontransformtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4instanceaccelerationstructuredescriptor/motiontransformtype.json'
content_hash: 'sha256:00dc7171d001065f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4InstanceAccelerationStructureDescriptor](../mtl4instanceaccelerationstructuredescriptor.md)

# motionTransformType

<sub>Instance Property</sub>

Controls the type of motion transforms, either as a matrix or individual components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var motionTransformType: MTLTransformType { get set }
```

## Discussion

Defaults to `MTLTransformTypePackedFloat4x3`. Using a `MTLTransformTypeComponent` allows you to represent the rotation by a quaternion (instead as of part of the matrix), allowing for correct motion interpolation.
