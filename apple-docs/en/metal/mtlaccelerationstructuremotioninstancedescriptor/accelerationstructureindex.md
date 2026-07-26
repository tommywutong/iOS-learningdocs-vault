---
title: accelerationStructureIndex
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/accelerationstructureindex
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/accelerationstructureindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/accelerationstructureindex.json'
content_hash: 'sha256:4c3e62dba0d75f21'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureMotionInstanceDescriptor](../mtlaccelerationstructuremotioninstancedescriptor.md)

# accelerationStructureIndex

<sub>Instance Property</sub>

The index of an acceleration structure which applies to the next acceleration-structure motion instance you create with the descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var accelerationStructureIndex: UInt32
```

## Discussion

This index refers to a bottom-level instance specified in the [instancedAccelerationStructures](../mtlinstanceaccelerationstructuredescriptor/instancedaccelerationstructures.md) of the [MTLInstanceAccelerationStructureDescriptor](../mtlinstanceaccelerationstructuredescriptor.md) used to create the new instance acceleration structure.

## See Also

### Related Documentation

- [instancedAccelerationStructures](../mtlinstanceaccelerationstructuredescriptor/instancedaccelerationstructures.md) — The bottom-level acceleration structures that instances use in the instance acceleration structure .
