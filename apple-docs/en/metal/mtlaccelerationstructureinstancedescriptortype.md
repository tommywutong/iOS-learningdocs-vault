---
title: MTLAccelerationStructureInstanceDescriptorType
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureinstancedescriptortype
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstancedescriptortype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureinstancedescriptortype.json'
content_hash: 'sha256:555e8e64a27e3ee2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLAccelerationStructureInstanceDescriptorType

<sub>Enumeration</sub>

Options for specifying different kinds of instance types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLAccelerationStructureInstanceDescriptorType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Specifying the instance descriptor type

- [MTLAccelerationStructureInstanceDescriptorTypeDefault](mtlaccelerationstructureinstancedescriptortype/default.md) — An option specifying that the instance uses the default characteristics.
- [MTLAccelerationStructureInstanceDescriptorTypeUserID](mtlaccelerationstructureinstancedescriptortype/userid.md) — An option specifying that the instance contains a user identifier.
- [MTLAccelerationStructureInstanceDescriptorTypeMotion](mtlaccelerationstructureinstancedescriptortype/motion.md) — An option specifying that the instance contains motion data.
- [MTLAccelerationStructureInstanceDescriptorTypeIndirect](mtlaccelerationstructureinstancedescriptortype/indirect.md) — An option that enables an instance descriptor memory layout the GPU can populate.
- [MTLAccelerationStructureInstanceDescriptorTypeIndirectMotion](mtlaccelerationstructureinstancedescriptortype/indirectmotion.md) — An option specifying that the instance contains motion data, and enables using an instance descriptor memory layout that the GPU can populate.

### Initializers

- [init(rawValue:)](<mtlaccelerationstructureinstancedescriptortype/init(rawvalue_).md>)

## See Also

### Specifying the instance structures

- [instanceDescriptorType](mtlinstanceaccelerationstructuredescriptor/instancedescriptortype.md) — The format of the instance data in the descriptor buffer.
- [instancedAccelerationStructures](mtlinstanceaccelerationstructuredescriptor/instancedaccelerationstructures.md) — The bottom-level acceleration structures that instances use in the instance acceleration structure .
