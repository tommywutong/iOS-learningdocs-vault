---
title: instanceCount
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancecount
source_url: 'https://developer.apple.com/documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancecount.json'
content_hash: 'sha256:876c929a680341ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLInstanceAccelerationStructureDescriptor](../mtlinstanceaccelerationstructuredescriptor.md)

# instanceCount

<sub>Instance Property</sub>

The number of instances in the instance descriptor buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var instanceCount: Int { get set }
```

## See Also

### Specifying the list of instances

- [instanceDescriptorBuffer](instancedescriptorbuffer.md) — A buffer that contains descriptions of each instance in the acceleration structure.
- [instanceDescriptorBufferOffset](instancedescriptorbufferoffset.md) — The offset, in bytes, to the descripton of the first instance.
- [instanceDescriptorStride](instancedescriptorstride.md) — The stride, in bytes, between instance descriptions.
