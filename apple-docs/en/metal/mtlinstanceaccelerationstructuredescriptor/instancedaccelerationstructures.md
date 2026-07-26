---
title: instancedAccelerationStructures
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancedaccelerationstructures
source_url: 'https://developer.apple.com/documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancedaccelerationstructures'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlinstanceaccelerationstructuredescriptor/instancedaccelerationstructures.json'
content_hash: 'sha256:4180f71d8095cf35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLInstanceAccelerationStructureDescriptor](../mtlinstanceaccelerationstructuredescriptor.md)

# instancedAccelerationStructures

<sub>Instance Property</sub>

The bottom-level acceleration structures that instances use in the instance acceleration structure .

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var instancedAccelerationStructures: [any MTLAccelerationStructure]? { get set }
```

## Discussion

Each instance in the instance descriptor buffer has an index into this array, specifying which acceleration structure to use for that instance.

## See Also

### Related Documentation

- [accelerationStructureIndex](../mtlaccelerationstructureinstancedescriptor/accelerationstructureindex.md) — The index of the acceleration structure to use for the instance.

### Specifying the instance structures

- [instanceDescriptorType](instancedescriptortype.md) — The format of the instance data in the descriptor buffer.
- [MTLAccelerationStructureInstanceDescriptorType](../mtlaccelerationstructureinstancedescriptortype.md) — Options for specifying different kinds of instance types.
