---
title: MTLAccelerationStructureInstanceDescriptorType.indirectMotion
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureinstancedescriptortype/indirectmotion
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstancedescriptortype/indirectmotion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureinstancedescriptortype/indirectmotion.json'
content_hash: 'sha256:27dc93b449faecc4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureInstanceDescriptorType](../mtlaccelerationstructureinstancedescriptortype.md)

# MTLAccelerationStructureInstanceDescriptorType.indirectMotion

<sub>Case</sub>

An option specifying that the instance contains motion data, and enables using an instance descriptor memory layout that the GPU can populate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case indirectMotion
```

## Discussion

This instance type corresponds to the [MTLIndirectAccelerationStructureMotionInstanceDescriptor](../mtlindirectaccelerationstructuremotioninstancedescriptor.md) memory layout.

## See Also

### Specifying the instance descriptor type

- [MTLAccelerationStructureInstanceDescriptorTypeDefault](default.md) — An option specifying that the instance uses the default characteristics.
- [MTLAccelerationStructureInstanceDescriptorTypeUserID](userid.md) — An option specifying that the instance contains a user identifier.
- [MTLAccelerationStructureInstanceDescriptorTypeMotion](motion.md) — An option specifying that the instance contains motion data.
- [MTLAccelerationStructureInstanceDescriptorTypeIndirect](indirect.md) — An option that enables an instance descriptor memory layout the GPU can populate.
