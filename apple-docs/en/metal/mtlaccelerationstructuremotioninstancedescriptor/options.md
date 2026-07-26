---
title: options
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/options
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/options.json'
content_hash: 'sha256:15d79f4cf436c95a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureMotionInstanceDescriptor](../mtlaccelerationstructuremotioninstancedescriptor.md)

# options

<sub>Instance Property</sub>

An option set which applies to the next acceleration structure motion-instance you create with the descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var options: MTLAccelerationStructureInstanceOptions
```

## See Also

### Customizing intersection and hit tests for the instance

- [intersectionFunctionTableOffset](intersectionfunctiontableoffset.md) — An offset into the intersection-function table for ray tracing, which applies to the next acceleration-structure motion instance you create with the descriptor.
- [mask](mask.md) — A mask for testing ray-tracing rays with a scene’s geometry, which applies to the next acceleration-structure motion instance you create with the descriptor.
