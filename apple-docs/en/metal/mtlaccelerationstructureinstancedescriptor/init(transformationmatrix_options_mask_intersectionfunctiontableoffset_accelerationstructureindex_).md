---
title: 'init(transformationMatrix:options:mask:intersectionFunctionTableOffset:accelerationStructureIndex:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlaccelerationstructureinstancedescriptor/init(transformationmatrix:options:mask:intersectionfunctiontableoffset:accelerationstructureindex:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstancedescriptor/init(transformationmatrix:options:mask:intersectionfunctiontableoffset:accelerationstructureindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureinstancedescriptor/init%28transformationmatrix%3Aoptions%3Amask%3Aintersectionfunctiontableoffset%3Aaccelerationstructureindex%3A%29.json'
content_hash: 'sha256:355cf7908e7ffcc3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureInstanceDescriptor](../mtlaccelerationstructureinstancedescriptor.md)

# init(transformationMatrix:options:mask:intersectionFunctionTableOffset:accelerationStructureIndex:)

<sub>Initializer</sub>

Creates a new acceleration structure instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(transformationMatrix: MTLPackedFloat4x3, options: MTLAccelerationStructureInstanceOptions, mask: UInt32, intersectionFunctionTableOffset: UInt32, accelerationStructureIndex: UInt32)
```

## Parameters

- `transformationMatrix` — The transform for placing and orienting the instance in the scene.

- `options` — The options for this instance.

- `mask` — A mask to use for this instance when testing a ray against the geometry.

- `intersectionFunctionTableOffset` — An offset to apply to the intersection function table when testing a ray against this instance.

- `accelerationStructureIndex` — The index of the acceleration structure to use for this instance.

## See Also

### Creating an instance descriptor

- [init()](<init().md>) — Creates a default acceleration structure instance.
