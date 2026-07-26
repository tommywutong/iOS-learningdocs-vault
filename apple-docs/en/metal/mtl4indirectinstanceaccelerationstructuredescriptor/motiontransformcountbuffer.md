---
title: motionTransformCountBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/motiontransformcountbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/motiontransformcountbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/motiontransformcountbuffer.json'
content_hash: 'sha256:ad21f9ca851649ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4IndirectInstanceAccelerationStructureDescriptor](../mtl4indirectinstanceaccelerationstructuredescriptor.md)

# motionTransformCountBuffer

<sub>Instance Property</sub>

Associates a buffer reference containing the number of motion transforms in the motion transform buffer, formatted as a 32-bit unsigned integer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var motionTransformCountBuffer: MTL4BufferRange { get set }
```

## Discussion

You are responsible for ensuring that the final number of motion transforms at build time in the buffer this property references is less than or equal to the value of property [maxMotionTransformCount](maxmotiontransformcount.md).
