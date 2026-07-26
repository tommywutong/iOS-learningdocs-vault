---
title: instanceDescriptorStride
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancedescriptorstride
source_url: 'https://developer.apple.com/documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancedescriptorstride'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancedescriptorstride.json'
content_hash: 'sha256:3906185e94fd1ee0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLInstanceAccelerationStructureDescriptor](../mtlinstanceaccelerationstructuredescriptor.md)

# instanceDescriptorStride

<sub>Instance Property</sub>

The stride, in bytes, between instance descriptions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var instanceDescriptorStride: Int { get set }
```

## Discussion

The stride needs to be at least 64 bytes and needs to be a multiple of 4 bytes. Defaults to 64 bytes.

## See Also

### Specifying the list of instances

- [instanceCount](instancecount.md) — The number of instances in the instance descriptor buffer.
- [instanceDescriptorBuffer](instancedescriptorbuffer.md) — A buffer that contains descriptions of each instance in the acceleration structure.
- [instanceDescriptorBufferOffset](instancedescriptorbufferoffset.md) — The offset, in bytes, to the descripton of the first instance.
