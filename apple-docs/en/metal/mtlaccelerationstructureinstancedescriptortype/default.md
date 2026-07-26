---
title: MTLAccelerationStructureInstanceDescriptorType.default
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureinstancedescriptortype/default
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstancedescriptortype/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureinstancedescriptortype/default.json'
content_hash: 'sha256:5766ea887b55b622'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureInstanceDescriptorType](../mtlaccelerationstructureinstancedescriptortype.md)

# MTLAccelerationStructureInstanceDescriptorType.default

<sub>Case</sub>

An option specifying that the instance uses the default characteristics.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case `default`
```

## Discussion

This instance type corresponds to the [MTLAccelerationStructureInstanceDescriptor](../mtlaccelerationstructureinstancedescriptor.md)  structure memory layout.

## See Also

### Specifying the instance descriptor type

- [MTLAccelerationStructureInstanceDescriptorTypeUserID](userid.md) — An option specifying that the instance contains a user identifier.
- [MTLAccelerationStructureInstanceDescriptorTypeMotion](motion.md) — An option specifying that the instance contains motion data.
- [MTLAccelerationStructureInstanceDescriptorTypeIndirect](indirect.md) — An option that enables an instance descriptor memory layout the GPU can populate.
- [MTLAccelerationStructureInstanceDescriptorTypeIndirectMotion](indirectmotion.md) — An option specifying that the instance contains motion data, and enables using an instance descriptor memory layout that the GPU can populate.
