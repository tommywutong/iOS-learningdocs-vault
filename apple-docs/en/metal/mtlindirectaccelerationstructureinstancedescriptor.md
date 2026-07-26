---
title: MTLIndirectAccelerationStructureInstanceDescriptor
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectaccelerationstructureinstancedescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectaccelerationstructureinstancedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectaccelerationstructureinstancedescriptor.json'
content_hash: 'sha256:73586a730a3fc43f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIndirectAccelerationStructureInstanceDescriptor

<sub>Structure</sub>

A description of an instance in an instanced geometry acceleration structure that the GPU can populate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLIndirectAccelerationStructureInstanceDescriptor
```

## Overview

This memory layout corresponds to the [MTLAccelerationStructureInstanceDescriptorTypeIndirect](mtlaccelerationstructureinstancedescriptortype/indirect.md) instance type.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<mtlindirectaccelerationstructureinstancedescriptor/init().md>)
- [init(transformationMatrix:options:mask:intersectionFunctionTableOffset:userID:accelerationStructureID:)](<mtlindirectaccelerationstructureinstancedescriptor/init(transformationmatrix_options_mask_intersectionfunctiontableoffset_userid_accelerationstructureid_).md>)

### Instance Properties

- [accelerationStructureID](mtlindirectaccelerationstructureinstancedescriptor/accelerationstructureid.md)
- [intersectionFunctionTableOffset](mtlindirectaccelerationstructureinstancedescriptor/intersectionfunctiontableoffset.md)
- [mask](mtlindirectaccelerationstructureinstancedescriptor/mask.md)
- [options](mtlindirectaccelerationstructureinstancedescriptor/options.md)
- [transformationMatrix](mtlindirectaccelerationstructureinstancedescriptor/transformationmatrix.md)
- [userID](mtlindirectaccelerationstructureinstancedescriptor/userid.md)

## See Also

### Instance descriptors

- [MTLAccelerationStructureInstanceDescriptor](mtlaccelerationstructureinstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure.
- [MTLAccelerationStructureUserIDInstanceDescriptor](mtlaccelerationstructureuseridinstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier for the instance.
- [MTLAccelerationStructureMotionInstanceDescriptor](mtlaccelerationstructuremotioninstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier and motion data for the instance.
- [MTLAccelerationStructureInstanceOptions](mtlaccelerationstructureinstanceoptions.md) — Options for adjusting the behavior of an instanced acceleration structure.
- [MTL4IndirectInstanceAccelerationStructureDescriptor](mtl4indirectinstanceaccelerationstructuredescriptor.md) — Descriptor for an “indirect” instance acceleration structure that allows providing the instance count and motion transform count indirectly, through buffer references.
- [MTLIndirectInstanceAccelerationStructureDescriptor](mtlindirectinstanceaccelerationstructuredescriptor.md) — A description of an acceleration structure that Metal derives from instances of primitive acceleration structures that the GPU can populate.
- [MTLIndirectAccelerationStructureMotionInstanceDescriptor](mtlindirectaccelerationstructuremotioninstancedescriptor.md) — A description of an instance in an acceleration structure that the GPU can populate, with motion data for the instance.
