---
title: MTLIndirectAccelerationStructureMotionInstanceDescriptor
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectaccelerationstructuremotioninstancedescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectaccelerationstructuremotioninstancedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectaccelerationstructuremotioninstancedescriptor.json'
content_hash: 'sha256:ae820fe525e3232f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIndirectAccelerationStructureMotionInstanceDescriptor

<sub>Structure</sub>

A description of an instance in an acceleration structure that the GPU can populate, with motion data for the instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLIndirectAccelerationStructureMotionInstanceDescriptor
```

## Overview

This memory layout corresponds to the [MTLAccelerationStructureInstanceDescriptorTypeIndirectMotion](mtlaccelerationstructureinstancedescriptortype/indirectmotion.md) instance type.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Specifying the instance

- [accelerationStructureID](mtlindirectaccelerationstructuremotioninstancedescriptor/accelerationstructureid.md) — The acceleration resource handle to use for this instance.

### Specifying motion data

- [motionStartTime](mtlindirectaccelerationstructuremotioninstancedescriptor/motionstarttime.md) — The start time of the motion instance.
- [motionStartBorderMode](mtlindirectaccelerationstructuremotioninstancedescriptor/motionstartbordermode.md) — The motion border mode describing what happens if Metal samples the acceleration structure before the motion start time.
- [motionEndTime](mtlindirectaccelerationstructuremotioninstancedescriptor/motionendtime.md) — The end time of the motion instance.
- [motionEndBorderMode](mtlindirectaccelerationstructuremotioninstancedescriptor/motionendbordermode.md) — The motion border mode describing what happens if Metal samples the acceleration structure after the motion end time.
- [motionTransformsCount](mtlindirectaccelerationstructuremotioninstancedescriptor/motiontransformscount.md) — The number of motion transforms belonging to the motion instance.
- [motionTransformsStartIndex](mtlindirectaccelerationstructuremotioninstancedescriptor/motiontransformsstartindex.md) — The index of the first set of transforms describing one keyframe of the animation.

### Specifying the user identifier

- [userID](mtlindirectaccelerationstructuremotioninstancedescriptor/userid.md) — A user-assigned ID to help identify the instance.

### Initializers

- [init()](<mtlindirectaccelerationstructuremotioninstancedescriptor/init().md>) — Creates a default indirect acceleration structure instance.
- [init(options:mask:intersectionFunctionTableOffset:userID:accelerationStructureID:motionTransformsStartIndex:motionTransformsCount:motionStartBorderMode:motionEndBorderMode:motionStartTime:motionEndTime:)](<mtlindirectaccelerationstructuremotioninstancedescriptor/init(options_mask_intersectionfunctiontableoffset_userid_accelerationstructureid_motiontransformsstartindex_motiontransformscount_motionstartbordermode_motionen-9ce5dc8079.md>) — Creates an indirect acceleration structure instance.

### Instance Properties

- [intersectionFunctionTableOffset](mtlindirectaccelerationstructuremotioninstancedescriptor/intersectionfunctiontableoffset.md) — An offset for determining which function in the intersection function table Metal calls when testing a ray against the instance.
- [mask](mtlindirectaccelerationstructuremotioninstancedescriptor/mask.md) — An instance mask to ignore geometry during ray tracing.
- [options](mtlindirectaccelerationstructuremotioninstancedescriptor/options.md) — The options for this instance.

## See Also

### Instance descriptors

- [MTLAccelerationStructureInstanceDescriptor](mtlaccelerationstructureinstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure.
- [MTLAccelerationStructureUserIDInstanceDescriptor](mtlaccelerationstructureuseridinstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier for the instance.
- [MTLAccelerationStructureMotionInstanceDescriptor](mtlaccelerationstructuremotioninstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier and motion data for the instance.
- [MTLAccelerationStructureInstanceOptions](mtlaccelerationstructureinstanceoptions.md) — Options for adjusting the behavior of an instanced acceleration structure.
- [MTL4IndirectInstanceAccelerationStructureDescriptor](mtl4indirectinstanceaccelerationstructuredescriptor.md) — Descriptor for an “indirect” instance acceleration structure that allows providing the instance count and motion transform count indirectly, through buffer references.
- [MTLIndirectInstanceAccelerationStructureDescriptor](mtlindirectinstanceaccelerationstructuredescriptor.md) — A description of an acceleration structure that Metal derives from instances of primitive acceleration structures that the GPU can populate.
- [MTLIndirectAccelerationStructureInstanceDescriptor](mtlindirectaccelerationstructureinstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure that the GPU can populate.
