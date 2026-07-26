---
title: accelerationStructureIndex
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureinstancedescriptor/accelerationstructureindex
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstancedescriptor/accelerationstructureindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureinstancedescriptor/accelerationstructureindex.json'
content_hash: 'sha256:53b1e15ac4c03d50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureInstanceDescriptor](../mtlaccelerationstructureinstancedescriptor.md)

# accelerationStructureIndex

<sub>Instance Property</sub>

The index of the acceleration structure to use for the instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var accelerationStructureIndex: UInt32
```

## Discussion

This index refers to a bottom-level instance in the [instancedAccelerationStructures](../mtlinstanceaccelerationstructuredescriptor/instancedaccelerationstructures.md) of the [MTLInstanceAccelerationStructureDescriptor](../mtlinstanceaccelerationstructuredescriptor.md) that you use to create the new instance acceleration structure.

## See Also

### Related Documentation

- [instancedAccelerationStructures](../mtlinstanceaccelerationstructuredescriptor/instancedaccelerationstructures.md) — The bottom-level acceleration structures that instances use in the instance acceleration structure .
