---
title: MTLAccelerationStructureInstanceDescriptorType.motion
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureinstancedescriptortype/motion
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstancedescriptortype/motion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureinstancedescriptortype/motion.json'
content_hash: 'sha256:821327246a31974d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureInstanceDescriptorType](../mtlaccelerationstructureinstancedescriptortype.md)

# MTLAccelerationStructureInstanceDescriptorType.motion

<sub>Case</sub>

An option specifying that the instance contains motion data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case motion
```

## Discussion

This instance type corresponds to the [MTLAccelerationStructureMotionInstanceDescriptor](../mtlaccelerationstructuremotioninstancedescriptor.md) structure memory layout.

## See Also

### Specifying the instance descriptor type

- [MTLAccelerationStructureInstanceDescriptorTypeDefault](default.md) — An option specifying that the instance uses the default characteristics.
- [MTLAccelerationStructureInstanceDescriptorTypeUserID](userid.md) — An option specifying that the instance contains a user identifier.
- [MTLAccelerationStructureInstanceDescriptorTypeIndirect](indirect.md) — An option that enables an instance descriptor memory layout the GPU can populate.
- [MTLAccelerationStructureInstanceDescriptorTypeIndirectMotion](indirectmotion.md) — An option specifying that the instance contains motion data, and enables using an instance descriptor memory layout that the GPU can populate.
