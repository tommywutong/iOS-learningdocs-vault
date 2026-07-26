---
title: instanceDescriptorBufferOffset
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancedescriptorbufferoffset
source_url: 'https://developer.apple.com/documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancedescriptorbufferoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancedescriptorbufferoffset.json'
content_hash: 'sha256:64956c3cc82aabf6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLInstanceAccelerationStructureDescriptor](../mtlinstanceaccelerationstructuredescriptor.md)

# instanceDescriptorBufferOffset

<sub>Instance Property</sub>

The offset, in bytes, to the descripton of the first instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var instanceDescriptorBufferOffset: Int { get set }
```

## Discussion

The offset needs to be a multiple of 64 bytes. Check the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for potential alignment restrictions.

## See Also

### Specifying the list of instances

- [instanceCount](instancecount.md) — The number of instances in the instance descriptor buffer.
- [instanceDescriptorBuffer](instancedescriptorbuffer.md) — A buffer that contains descriptions of each instance in the acceleration structure.
- [instanceDescriptorStride](instancedescriptorstride.md) — The stride, in bytes, between instance descriptions.
