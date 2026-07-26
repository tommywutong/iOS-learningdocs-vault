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
doc_path: /documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/motiontransformstride
source_url: 'https://developer.apple.com/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/motiontransformstride'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/motiontransformstride.json'
content_hash: 'sha256:5814d684b49769d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4IndirectInstanceAccelerationStructureDescriptor](../mtl4indirectinstanceaccelerationstructuredescriptor.md)

# motionTransformStride

<sub>Instance Property</sub>

Sets the stride for motion transform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var motionTransformStride: Int { get set }
```

## Discussion

Defaults to `0`, indicating that transforms are tightly packed according to the motion transform type.
