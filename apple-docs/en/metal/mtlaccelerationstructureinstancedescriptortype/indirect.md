---
title: MTLAccelerationStructureInstanceDescriptorType.indirect
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureinstancedescriptortype/indirect
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstancedescriptortype/indirect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureinstancedescriptortype/indirect.json'
content_hash: 'sha256:914e1fda772b568a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureInstanceDescriptorType](../mtlaccelerationstructureinstancedescriptortype.md)

# MTLAccelerationStructureInstanceDescriptorType.indirect

<sub>Case</sub>

An option that enables an instance descriptor memory layout the GPU can populate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case indirect
```

## Discussion

This instance type corresponds to the [MTLIndirectAccelerationStructureInstanceDescriptor](../mtlindirectaccelerationstructureinstancedescriptor.md) memory layout.

## See Also

### Specifying the instance descriptor type

- [MTLAccelerationStructureInstanceDescriptorTypeDefault](default.md) — An option specifying that the instance uses the default characteristics.
- [MTLAccelerationStructureInstanceDescriptorTypeUserID](userid.md) — An option specifying that the instance contains a user identifier.
- [MTLAccelerationStructureInstanceDescriptorTypeMotion](motion.md) — An option specifying that the instance contains motion data.
- [MTLAccelerationStructureInstanceDescriptorTypeIndirectMotion](indirectmotion.md) — An option specifying that the instance contains motion data, and enables using an instance descriptor memory layout that the GPU can populate.
