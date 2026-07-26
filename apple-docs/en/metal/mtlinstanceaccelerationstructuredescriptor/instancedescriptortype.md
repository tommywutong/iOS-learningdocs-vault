---
title: instanceDescriptorType
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancedescriptortype
source_url: 'https://developer.apple.com/documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancedescriptortype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancedescriptortype.json'
content_hash: 'sha256:0aa5666371205eeb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLInstanceAccelerationStructureDescriptor](../mtlinstanceaccelerationstructuredescriptor.md)

# instanceDescriptorType

<sub>Instance Property</sub>

The format of the instance data in the descriptor buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var instanceDescriptorType: MTLAccelerationStructureInstanceDescriptorType { get set }
```

## See Also

### Related Documentation

- [instanceDescriptorBuffer](instancedescriptorbuffer.md) — A buffer that contains descriptions of each instance in the acceleration structure.

### Specifying the instance structures

- [instancedAccelerationStructures](instancedaccelerationstructures.md) — The bottom-level acceleration structures that instances use in the instance acceleration structure .
- [MTLAccelerationStructureInstanceDescriptorType](../mtlaccelerationstructureinstancedescriptortype.md) — Options for specifying different kinds of instance types.
