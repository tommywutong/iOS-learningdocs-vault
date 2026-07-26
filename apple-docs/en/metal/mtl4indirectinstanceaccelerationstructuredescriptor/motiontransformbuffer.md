---
title: motionTransformBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/motiontransformbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/motiontransformbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/motiontransformbuffer.json'
content_hash: 'sha256:06a674ec1f9a414f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4IndirectInstanceAccelerationStructureDescriptor](../mtl4indirectinstanceaccelerationstructuredescriptor.md)

# motionTransformBuffer

<sub>Instance Property</sub>

A buffer containing transformation information for instance motion keyframes, formatted according to the motion transform type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var motionTransformBuffer: MTL4BufferRange { get set }
```

## Discussion

Each instance can have a different number of keyframes that you configure via individual instance descriptors.

You are responsible for ensuring the buffer address the range references is not zero when using motion instance descriptors.
