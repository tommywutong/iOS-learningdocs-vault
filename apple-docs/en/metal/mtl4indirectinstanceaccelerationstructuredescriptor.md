---
title: MTL4IndirectInstanceAccelerationStructureDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor.json'
content_hash: 'sha256:742791e9603a38dd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4IndirectInstanceAccelerationStructureDescriptor

<sub>Class</sub>

Descriptor for an “indirect” instance acceleration structure that allows providing the instance count and motion transform count indirectly, through buffer references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTL4IndirectInstanceAccelerationStructureDescriptor
```

## Overview

An instance acceleration structure references other acceleration structures, and provides the ability to “instantiate” them multiple times, each one with potentially a different transformation matrix.

You specify the properties of the instances in the acceleration structure this descriptor builds by providing a buffer of `structs` via its [instanceDescriptorBuffer](mtl4indirectinstanceaccelerationstructuredescriptor/instancedescriptorbuffer.md) property.

Compared to [MTL4InstanceAccelerationStructureDescriptor](mtl4instanceaccelerationstructuredescriptor.md), this descriptor allows you to provide the number of instances it references indirectly through a buffer reference, as well as the number of motion transforms.

This enables you to determine these counts indirectly in the GPU timeline via a compute pipeline. Metal needs only to know the maximum possible number of instances and motion transforms to support, which you specify via the [maxInstanceCount](mtl4indirectinstanceaccelerationstructuredescriptor/maxinstancecount.md) and [maxMotionTransformCount](mtl4indirectinstanceaccelerationstructuredescriptor/maxmotiontransformcount.md) properties.

Use a [MTLResidencySet](mtlresidencyset.md) to mark residency of all buffers and acceleration structures this descriptor references when you build this acceleration structure.

## Relationships

- **Inherits From**: [MTL4AccelerationStructureDescriptor](mtl4accelerationstructuredescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [instanceCountBuffer](mtl4indirectinstanceaccelerationstructuredescriptor/instancecountbuffer.md) — Provides a reference to a buffer containing the number of instances in the instance descriptor buffer, formatted as a 32-bit unsigned integer.
- [instanceDescriptorBuffer](mtl4indirectinstanceaccelerationstructuredescriptor/instancedescriptorbuffer.md) — Assigns a reference to a buffer containing instance descriptors for acceleration structures to reference.
- [instanceDescriptorStride](mtl4indirectinstanceaccelerationstructuredescriptor/instancedescriptorstride.md) — Sets the stride, in bytes, between instance descriptors in the instance descriptor buffer.
- [instanceDescriptorType](mtl4indirectinstanceaccelerationstructuredescriptor/instancedescriptortype.md) — Controls the type of instance descriptor that the instance descriptor buffer references.
- [instanceTransformationMatrixLayout](mtl4indirectinstanceaccelerationstructuredescriptor/instancetransformationmatrixlayout.md) — Specifies the layout for the transformation matrices in the instance descriptor buffer and the motion transformation matrix buffer.
- [maxInstanceCount](mtl4indirectinstanceaccelerationstructuredescriptor/maxinstancecount.md) — Controls the maximum number of instance descriptors the instance descriptor buffer can reference.
- [maxMotionTransformCount](mtl4indirectinstanceaccelerationstructuredescriptor/maxmotiontransformcount.md) — Controls the maximum number of motion transforms in the motion transform buffer.
- [motionTransformBuffer](mtl4indirectinstanceaccelerationstructuredescriptor/motiontransformbuffer.md) — A buffer containing transformation information for instance motion keyframes, formatted according to the motion transform type.
- [motionTransformCountBuffer](mtl4indirectinstanceaccelerationstructuredescriptor/motiontransformcountbuffer.md) — Associates a buffer reference containing the number of motion transforms in the motion transform buffer, formatted as a 32-bit unsigned integer.
- [motionTransformStride](mtl4indirectinstanceaccelerationstructuredescriptor/motiontransformstride.md) — Sets the stride for motion transform.
- [motionTransformType](mtl4indirectinstanceaccelerationstructuredescriptor/motiontransformtype.md) — Sets the type of motion transforms, either as a matrix or individual components.

## See Also

### Instance descriptors

- [MTLAccelerationStructureInstanceDescriptor](mtlaccelerationstructureinstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure.
- [MTLAccelerationStructureUserIDInstanceDescriptor](mtlaccelerationstructureuseridinstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier for the instance.
- [MTLAccelerationStructureMotionInstanceDescriptor](mtlaccelerationstructuremotioninstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier and motion data for the instance.
- [MTLAccelerationStructureInstanceOptions](mtlaccelerationstructureinstanceoptions.md) — Options for adjusting the behavior of an instanced acceleration structure.
- [MTLIndirectInstanceAccelerationStructureDescriptor](mtlindirectinstanceaccelerationstructuredescriptor.md) — A description of an acceleration structure that Metal derives from instances of primitive acceleration structures that the GPU can populate.
- [MTLIndirectAccelerationStructureInstanceDescriptor](mtlindirectaccelerationstructureinstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure that the GPU can populate.
- [MTLIndirectAccelerationStructureMotionInstanceDescriptor](mtlindirectaccelerationstructuremotioninstancedescriptor.md) — A description of an instance in an acceleration structure that the GPU can populate, with motion data for the instance.
