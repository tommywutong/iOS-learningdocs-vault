---
title: motionTransformBufferOffset
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlinstanceaccelerationstructuredescriptor/motiontransformbufferoffset
source_url: 'https://developer.apple.com/documentation/metal/mtlinstanceaccelerationstructuredescriptor/motiontransformbufferoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlinstanceaccelerationstructuredescriptor/motiontransformbufferoffset.json'
content_hash: 'sha256:427173b373eaed50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLInstanceAccelerationStructureDescriptor](../mtlinstanceaccelerationstructuredescriptor.md)

# motionTransformBufferOffset

<sub>Instance Property</sub>

The offset, in bytes, to the descripton of the first motion transform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var motionTransformBufferOffset: Int { get set }
```

## Discussion

The offset needs to be a multiple of 64 bytes. Check the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for potential alignment restrictions.

## See Also

### Specifying motion data

- [motionTransformCount](motiontransformcount.md) — The number of motion transforms in the motion transform buffer.
- [motionTransformBuffer](motiontransformbuffer.md) — A buffer that contains descriptions of each motion transform in the acceleration structure.
