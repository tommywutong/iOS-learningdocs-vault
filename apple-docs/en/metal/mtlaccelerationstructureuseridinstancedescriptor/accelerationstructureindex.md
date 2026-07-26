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
doc_path: /documentation/metal/mtlaccelerationstructureuseridinstancedescriptor/accelerationstructureindex
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureuseridinstancedescriptor/accelerationstructureindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureuseridinstancedescriptor/accelerationstructureindex.json'
content_hash: 'sha256:4c3846d341b21372'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureUserIDInstanceDescriptor](../mtlaccelerationstructureuseridinstancedescriptor.md)

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
