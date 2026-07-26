---
title: MTLAccelerationStructureInstanceDescriptorType.userID
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureinstancedescriptortype/userid
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstancedescriptortype/userid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureinstancedescriptortype/userid.json'
content_hash: 'sha256:904daacd2b099a5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureInstanceDescriptorType](../mtlaccelerationstructureinstancedescriptortype.md)

# MTLAccelerationStructureInstanceDescriptorType.userID

<sub>Case</sub>

An option specifying that the instance contains a user identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case userID
```

## Discussion

This instance type corresponds to the [MTLAccelerationStructureUserIDInstanceDescriptor](../mtlaccelerationstructureuseridinstancedescriptor.md) structure memory layout.

## See Also

### Specifying the instance descriptor type

- [MTLAccelerationStructureInstanceDescriptorTypeDefault](default.md) — An option specifying that the instance uses the default characteristics.
- [MTLAccelerationStructureInstanceDescriptorTypeMotion](motion.md) — An option specifying that the instance contains motion data.
- [MTLAccelerationStructureInstanceDescriptorTypeIndirect](indirect.md) — An option that enables an instance descriptor memory layout the GPU can populate.
- [MTLAccelerationStructureInstanceDescriptorTypeIndirectMotion](indirectmotion.md) — An option specifying that the instance contains motion data, and enables using an instance descriptor memory layout that the GPU can populate.
