---
title: MTLIndirectInstanceAccelerationStructureDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectinstanceaccelerationstructuredescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectinstanceaccelerationstructuredescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectinstanceaccelerationstructuredescriptor.json'
content_hash: 'sha256:13a7cd64701b8aab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIndirectInstanceAccelerationStructureDescriptor

<sub>Class</sub>

A description of an acceleration structure that Metal derives from instances of primitive acceleration structures that the GPU can populate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLIndirectInstanceAccelerationStructureDescriptor
```

## Relationships

- **Inherits From**: [MTLAccelerationStructureDescriptor](mtlaccelerationstructuredescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [instanceCountBuffer](mtlindirectinstanceaccelerationstructuredescriptor/instancecountbuffer.md)
- [instanceCountBufferOffset](mtlindirectinstanceaccelerationstructuredescriptor/instancecountbufferoffset.md)
- [instanceDescriptorBuffer](mtlindirectinstanceaccelerationstructuredescriptor/instancedescriptorbuffer.md)
- [instanceDescriptorBufferOffset](mtlindirectinstanceaccelerationstructuredescriptor/instancedescriptorbufferoffset.md)
- [instanceDescriptorStride](mtlindirectinstanceaccelerationstructuredescriptor/instancedescriptorstride.md)
- [instanceDescriptorType](mtlindirectinstanceaccelerationstructuredescriptor/instancedescriptortype.md)
- [instanceTransformationMatrixLayout](mtlindirectinstanceaccelerationstructuredescriptor/instancetransformationmatrixlayout.md)
- [maxInstanceCount](mtlindirectinstanceaccelerationstructuredescriptor/maxinstancecount.md)
- [maxMotionTransformCount](mtlindirectinstanceaccelerationstructuredescriptor/maxmotiontransformcount.md)
- [motionTransformBuffer](mtlindirectinstanceaccelerationstructuredescriptor/motiontransformbuffer.md)
- [motionTransformBufferOffset](mtlindirectinstanceaccelerationstructuredescriptor/motiontransformbufferoffset.md) — The offset, in bytes, to the descripton of the first motion transform.
- [motionTransformCountBuffer](mtlindirectinstanceaccelerationstructuredescriptor/motiontransformcountbuffer.md)
- [motionTransformCountBufferOffset](mtlindirectinstanceaccelerationstructuredescriptor/motiontransformcountbufferoffset.md)
- [motionTransformStride](mtlindirectinstanceaccelerationstructuredescriptor/motiontransformstride.md)
- [motionTransformType](mtlindirectinstanceaccelerationstructuredescriptor/motiontransformtype.md)

## See Also

### Instance descriptors

- [MTLAccelerationStructureInstanceDescriptor](mtlaccelerationstructureinstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure.
- [MTLAccelerationStructureUserIDInstanceDescriptor](mtlaccelerationstructureuseridinstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier for the instance.
- [MTLAccelerationStructureMotionInstanceDescriptor](mtlaccelerationstructuremotioninstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier and motion data for the instance.
- [MTLAccelerationStructureInstanceOptions](mtlaccelerationstructureinstanceoptions.md) — Options for adjusting the behavior of an instanced acceleration structure.
- [MTL4IndirectInstanceAccelerationStructureDescriptor](mtl4indirectinstanceaccelerationstructuredescriptor.md) — Descriptor for an “indirect” instance acceleration structure that allows providing the instance count and motion transform count indirectly, through buffer references.
- [MTLIndirectAccelerationStructureInstanceDescriptor](mtlindirectaccelerationstructureinstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure that the GPU can populate.
- [MTLIndirectAccelerationStructureMotionInstanceDescriptor](mtlindirectaccelerationstructuremotioninstancedescriptor.md) — A description of an instance in an acceleration structure that the GPU can populate, with motion data for the instance.
