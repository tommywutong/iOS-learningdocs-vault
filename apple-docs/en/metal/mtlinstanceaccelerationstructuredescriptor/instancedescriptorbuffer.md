---
title: instanceDescriptorBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancedescriptorbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancedescriptorbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancedescriptorbuffer.json'
content_hash: 'sha256:952fa9c392d9e9e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLInstanceAccelerationStructureDescriptor](../mtlinstanceaccelerationstructuredescriptor.md)

# instanceDescriptorBuffer

<sub>Instance Property</sub>

A buffer that contains descriptions of each instance in the acceleration structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var instanceDescriptorBuffer: (any MTLBuffer)? { get set }
```

## Discussion

You need to set a buffer before creating the instanced acceleration structure. The buffer needs to contain a list of instance data structures, each defining the characteristics of an instance. The descriptor’s [instanceDescriptorType](instancedescriptortype.md) property determines which memory layout to use for the instance data; see [MTLAccelerationStructureInstanceDescriptorType](../mtlaccelerationstructureinstancedescriptortype.md) for more information.

## See Also

### Specifying the list of instances

- [instanceCount](instancecount.md) — The number of instances in the instance descriptor buffer.
- [instanceDescriptorBufferOffset](instancedescriptorbufferoffset.md) — The offset, in bytes, to the descripton of the first instance.
- [instanceDescriptorStride](instancedescriptorstride.md) — The stride, in bytes, between instance descriptions.
