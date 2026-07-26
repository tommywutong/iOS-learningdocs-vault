---
title: instanceTransformationMatrixLayout
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4instanceaccelerationstructuredescriptor/instancetransformationmatrixlayout
source_url: 'https://developer.apple.com/documentation/metal/mtl4instanceaccelerationstructuredescriptor/instancetransformationmatrixlayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4instanceaccelerationstructuredescriptor/instancetransformationmatrixlayout.json'
content_hash: 'sha256:21286222f8c5a733'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4InstanceAccelerationStructureDescriptor](../mtl4instanceaccelerationstructuredescriptor.md)

# instanceTransformationMatrixLayout

<sub>Instance Property</sub>

Specifies the layout for the transformation matrices in the instance descriptor buffer and the motion transformation matrix buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var instanceTransformationMatrixLayout: MTLMatrixLayout { get set }
```

## Discussion

Metal interprets the value of this property as the layout for the buffers that both [instanceDescriptorBuffer](instancedescriptorbuffer.md) and [motionTransformBuffer](motiontransformbuffer.md) reference.

Defaults to `MTLMatrixLayoutColumnMajor`.
