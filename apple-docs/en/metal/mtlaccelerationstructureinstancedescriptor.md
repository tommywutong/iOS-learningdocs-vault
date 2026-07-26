---
title: MTLAccelerationStructureInstanceDescriptor
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureinstancedescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstancedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureinstancedescriptor.json'
content_hash: 'sha256:f5e240ff0114ea72'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLAccelerationStructureInstanceDescriptor

<sub>Structure</sub>

A description of an instance in an instanced geometry acceleration structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLAccelerationStructureInstanceDescriptor
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md)

## Topics

### Creating an instance descriptor

- [init()](<mtlaccelerationstructureinstancedescriptor/init().md>) — Creates a default acceleration structure instance.
- [init(transformationMatrix:options:mask:intersectionFunctionTableOffset:accelerationStructureIndex:)](<mtlaccelerationstructureinstancedescriptor/init(transformationmatrix_options_mask_intersectionfunctiontableoffset_accelerationstructureindex_).md>) — Creates a new acceleration structure instance.

### Specifying the instance

- [accelerationStructureIndex](mtlaccelerationstructureinstancedescriptor/accelerationstructureindex.md) — The index of the acceleration structure to use for the instance.

### Specifying the instance transform

- [transformationMatrix](mtlaccelerationstructureinstancedescriptor/transformationmatrix.md) — The transform for placing and orienting the instance in the scene.

### Customizing intersection and hit tests for the instance

- [intersectionFunctionTableOffset](mtlaccelerationstructureinstancedescriptor/intersectionfunctiontableoffset.md) — An offset for determining which function in the intersection function table Metal needs to call when testing a ray against the instance.
- [options](mtlaccelerationstructureinstancedescriptor/options.md) — The options for the instance.
- [mask](mtlaccelerationstructureinstancedescriptor/mask.md) — A mask to use for the instance when testing a ray against the geometry.

## See Also

### Instance descriptors

- [MTLAccelerationStructureUserIDInstanceDescriptor](mtlaccelerationstructureuseridinstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier for the instance.
- [MTLAccelerationStructureMotionInstanceDescriptor](mtlaccelerationstructuremotioninstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier and motion data for the instance.
- [MTLAccelerationStructureInstanceOptions](mtlaccelerationstructureinstanceoptions.md) — Options for adjusting the behavior of an instanced acceleration structure.
- [MTL4IndirectInstanceAccelerationStructureDescriptor](mtl4indirectinstanceaccelerationstructuredescriptor.md) — Descriptor for an “indirect” instance acceleration structure that allows providing the instance count and motion transform count indirectly, through buffer references.
- [MTLIndirectInstanceAccelerationStructureDescriptor](mtlindirectinstanceaccelerationstructuredescriptor.md) — A description of an acceleration structure that Metal derives from instances of primitive acceleration structures that the GPU can populate.
- [MTLIndirectAccelerationStructureInstanceDescriptor](mtlindirectaccelerationstructureinstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure that the GPU can populate.
- [MTLIndirectAccelerationStructureMotionInstanceDescriptor](mtlindirectaccelerationstructuremotioninstancedescriptor.md) — A description of an instance in an acceleration structure that the GPU can populate, with motion data for the instance.
