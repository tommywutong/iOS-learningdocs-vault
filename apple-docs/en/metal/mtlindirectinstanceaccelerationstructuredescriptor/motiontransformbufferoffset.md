---
title: motionTransformBufferOffset
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectinstanceaccelerationstructuredescriptor/motiontransformbufferoffset
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectinstanceaccelerationstructuredescriptor/motiontransformbufferoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectinstanceaccelerationstructuredescriptor/motiontransformbufferoffset.json'
content_hash: 'sha256:3b24ec323f920bec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectInstanceAccelerationStructureDescriptor](../mtlindirectinstanceaccelerationstructuredescriptor.md)

# motionTransformBufferOffset

<sub>Instance Property</sub>

The offset, in bytes, to the descripton of the first motion transform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var motionTransformBufferOffset: Int { get set }
```

## Discussion

The offset needs to be a multiple of 64 bytes. Check the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for potential alignment restrictions.
