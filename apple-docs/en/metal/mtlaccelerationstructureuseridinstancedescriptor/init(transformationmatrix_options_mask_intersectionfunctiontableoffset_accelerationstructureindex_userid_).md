---
title: 'init(transformationMatrix:options:mask:intersectionFunctionTableOffset:accelerationStructureIndex:userID:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlaccelerationstructureuseridinstancedescriptor/init(transformationmatrix:options:mask:intersectionfunctiontableoffset:accelerationstructureindex:userid:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureuseridinstancedescriptor/init(transformationmatrix:options:mask:intersectionfunctiontableoffset:accelerationstructureindex:userid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureuseridinstancedescriptor/init%28transformationmatrix%3Aoptions%3Amask%3Aintersectionfunctiontableoffset%3Aaccelerationstructureindex%3Auserid%3A%29.json'
content_hash: 'sha256:e4554e8cb96ab61e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureUserIDInstanceDescriptor](../mtlaccelerationstructureuseridinstancedescriptor.md)

# init(transformationMatrix:options:mask:intersectionFunctionTableOffset:accelerationStructureIndex:userID:)

<sub>Initializer</sub>

Creates a new acceleration structure instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(transformationMatrix: MTLPackedFloat4x3, options: MTLAccelerationStructureInstanceOptions, mask: UInt32, intersectionFunctionTableOffset: UInt32, accelerationStructureIndex: UInt32, userID: UInt32)
```

## Parameters

- `transformationMatrix` — The transform for placing and orienting the instance in the scene.

- `options` — The options for the instance.

- `mask` — A mask to use for the instance when testing a ray against the geometry.

- `intersectionFunctionTableOffset` — An offset to apply to the intersection function table when testing a ray against the instance.

- `accelerationStructureIndex` — The index of the acceleration structure to use for the instance.

- `userID` — The user identifier for the instance.

## See Also

### Creating an instance descriptor

- [init()](<init().md>) — Creates a default acceleration structure instance.
