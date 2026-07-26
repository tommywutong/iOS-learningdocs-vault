---
title: MTLAccelerationStructureInstanceOptions
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureinstanceoptions
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstanceoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureinstanceoptions.json'
content_hash: 'sha256:2a382927ea0a7c74'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLAccelerationStructureInstanceOptions

<sub>Structure</sub>

Options for adjusting the behavior of an instanced acceleration structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLAccelerationStructureInstanceOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Creating instance flags

- [init(rawValue:)](<mtlaccelerationstructureinstanceoptions/init(rawvalue_).md>) — Creates new usage options from a raw integer value.

### Usage options

- [MTLAccelerationStructureInstanceOptionDisableTriangleCulling](mtlaccelerationstructureinstanceoptions/disabletriangleculling.md) — An option that turns off culling for this instance if ray intersector has culling enabled.
- [MTLAccelerationStructureInstanceOptionTriangleFrontFacingWindingCounterClockwise](mtlaccelerationstructureinstanceoptions/trianglefrontfacingwindingcounterclockwise.md) — Specifies that the instance specifies front facing triangles in counter-clockwise order.
- [MTLAccelerationStructureInstanceOptionOpaque](mtlaccelerationstructureinstanceoptions/opaque.md) — Specifies that intersectors should treat the instance as opaque.
- [MTLAccelerationStructureInstanceOptionNonOpaque](mtlaccelerationstructureinstanceoptions/nonopaque.md) — Specifies that intersectors should treat the instance as non-opaque.

## See Also

### Instance descriptors

- [MTLAccelerationStructureInstanceDescriptor](mtlaccelerationstructureinstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure.
- [MTLAccelerationStructureUserIDInstanceDescriptor](mtlaccelerationstructureuseridinstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier for the instance.
- [MTLAccelerationStructureMotionInstanceDescriptor](mtlaccelerationstructuremotioninstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier and motion data for the instance.
- [MTL4IndirectInstanceAccelerationStructureDescriptor](mtl4indirectinstanceaccelerationstructuredescriptor.md) — Descriptor for an “indirect” instance acceleration structure that allows providing the instance count and motion transform count indirectly, through buffer references.
- [MTLIndirectInstanceAccelerationStructureDescriptor](mtlindirectinstanceaccelerationstructuredescriptor.md) — A description of an acceleration structure that Metal derives from instances of primitive acceleration structures that the GPU can populate.
- [MTLIndirectAccelerationStructureInstanceDescriptor](mtlindirectaccelerationstructureinstancedescriptor.md) — A description of an instance in an instanced geometry acceleration structure that the GPU can populate.
- [MTLIndirectAccelerationStructureMotionInstanceDescriptor](mtlindirectaccelerationstructuremotioninstancedescriptor.md) — A description of an instance in an acceleration structure that the GPU can populate, with motion data for the instance.
