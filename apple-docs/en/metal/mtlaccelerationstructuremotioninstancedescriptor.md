---
title: MTLAccelerationStructureMotionInstanceDescriptor
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuremotioninstancedescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor.json'
content_hash: 'sha256:808ca221c1e637d8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLAccelerationStructureMotionInstanceDescriptor

<sub>Structure</sub>

A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier and motion data for the instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLAccelerationStructureMotionInstanceDescriptor
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Creating an instance descriptor

- [init()](<mtlaccelerationstructuremotioninstancedescriptor/init().md>) — Creates an acceleration-structure motion instance with default property values.
- [init(options:mask:intersectionFunctionTableOffset:accelerationStructureIndex:userID:motionTransformsStartIndex:motionTransformsCount:motionStartBorderMode:motionEndBorderMode:motionStartTime:motionEndTime:)](<mtlaccelerationstructuremotioninstancedescriptor/init(options_mask_intersectionfunctiontableoffset_accelerationstructureindex_userid_motiontransformsstartindex_motiontransformscount_motionstartbordermode_motio-efcf4a6fd4.md>) — Creates an acceleration-structure motion instance with the property values you provide.

### Specifying the instance

- [accelerationStructureIndex](mtlaccelerationstructuremotioninstancedescriptor/accelerationstructureindex.md) — The index of an acceleration structure which applies to the next acceleration-structure motion instance you create with the descriptor.

### Specifying motion data

- [motionStartTime](mtlaccelerationstructuremotioninstancedescriptor/motionstarttime.md) — A starting time for the range of motion that the key-frame data represents.
- [motionEndTime](mtlaccelerationstructuremotioninstancedescriptor/motionendtime.md) — An ending time for the range of motion that the key-frame data represents.
- [motionStartBorderMode](mtlaccelerationstructuremotioninstancedescriptor/motionstartbordermode.md) — A behavior that configures how a motion instance handles timestamps before a starting time.
- [motionEndBorderMode](mtlaccelerationstructuremotioninstancedescriptor/motionendbordermode.md) — A behavior that configures how a motion instance handles timestamps after an ending time.
- [motionTransformsStartIndex](mtlaccelerationstructuremotioninstancedescriptor/motiontransformsstartindex.md) — The index of motion data that represents the first key-frame motion data, which applies to the next acceleration-structure motion instance you create with the descriptor.
- [motionTransformsCount](mtlaccelerationstructuremotioninstancedescriptor/motiontransformscount.md) — The number of motion data key-frames, which applies to the next acceleration-structure motion instance you create with the descriptor.

### Customizing intersection and hit tests for the instance

- [intersectionFunctionTableOffset](mtlaccelerationstructuremotioninstancedescriptor/intersectionfunctiontableoffset.md) — An offset into the intersection-function table for ray tracing, which applies to the next acceleration-structure motion instance you create with the descriptor.
- [options](mtlaccelerationstructuremotioninstancedescriptor/options.md) — An option set which applies to the next acceleration structure motion-instance you create with the descriptor.
- [mask](mtlaccelerationstructuremotioninstancedescriptor/mask.md) — A mask for testing ray-tracing rays with a scene’s geometry, which applies to the next acceleration-structure motion instance you create with the descriptor.

### Specifying the user identifier

- [userID](mtlaccelerationstructuremotioninstancedescriptor/userid.md) — An unique identifier, which applies to the next acceleration-structure motion instance you create with the descriptor.

## See Also

### Instance descriptors

- [MTLAccelerationStructureInstanceDescriptor](mtlaccelerationstructureinstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure.
- [MTLAccelerationStructureUserIDInstanceDescriptor](mtlaccelerationstructureuseridinstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier for the instance.
- [MTLAccelerationStructureInstanceOptions](mtlaccelerationstructureinstanceoptions.md) — Options for adjusting the behavior of an instanced acceleration structure.
- [MTL4IndirectInstanceAccelerationStructureDescriptor](mtl4indirectinstanceaccelerationstructuredescriptor.md) — Descriptor for an “indirect” instance acceleration structure that allows providing the instance count and motion transform count indirectly, through buffer references.
- [MTLIndirectInstanceAccelerationStructureDescriptor](mtlindirectinstanceaccelerationstructuredescriptor.md) — A description of an acceleration structure that Metal derives from instances of primitive acceleration structures that the GPU can populate.
- [MTLIndirectAccelerationStructureInstanceDescriptor](mtlindirectaccelerationstructureinstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure that the GPU can populate.
- [MTLIndirectAccelerationStructureMotionInstanceDescriptor](mtlindirectaccelerationstructuremotioninstancedescriptor.md) — A description of an instance in an acceleration structure that the GPU can populate, with motion data for the instance.
