---
title: motionTransformStride
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4instanceaccelerationstructuredescriptor/motiontransformstride
source_url: 'https://developer.apple.com/documentation/metal/mtl4instanceaccelerationstructuredescriptor/motiontransformstride'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4instanceaccelerationstructuredescriptor/motiontransformstride.json'
content_hash: 'sha256:5fe3ef75a78876fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4InstanceAccelerationStructureDescriptor](../mtl4instanceaccelerationstructuredescriptor.md)

# motionTransformStride

<sub>Instance Property</sub>

Specify the stride for motion transform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var motionTransformStride: Int { get set }
```

## Discussion

Defaults to `0`, indicating that transforms are tightly packed according to the motion transform type.
