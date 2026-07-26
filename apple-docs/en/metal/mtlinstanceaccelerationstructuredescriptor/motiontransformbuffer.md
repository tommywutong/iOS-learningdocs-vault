---
title: motionTransformBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlinstanceaccelerationstructuredescriptor/motiontransformbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtlinstanceaccelerationstructuredescriptor/motiontransformbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlinstanceaccelerationstructuredescriptor/motiontransformbuffer.json'
content_hash: 'sha256:5322380f1905fb26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLInstanceAccelerationStructureDescriptor](../mtlinstanceaccelerationstructuredescriptor.md)

# motionTransformBuffer

<sub>Instance Property</sub>

A buffer that contains descriptions of each motion transform in the acceleration structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var motionTransformBuffer: (any MTLBuffer)? { get set }
```

## See Also

### Specifying motion data

- [motionTransformCount](motiontransformcount.md) — The number of motion transforms in the motion transform buffer.
- [motionTransformBufferOffset](motiontransformbufferoffset.md) — The offset, in bytes, to the descripton of the first motion transform.
