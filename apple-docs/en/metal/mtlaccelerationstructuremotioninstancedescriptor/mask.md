---
title: mask
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/mask
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/mask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/mask.json'
content_hash: 'sha256:a52d3bb9bf1b7cd7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureMotionInstanceDescriptor](../mtlaccelerationstructuremotioninstancedescriptor.md)

# mask

<sub>Instance Property</sub>

A mask for testing ray-tracing rays with a scene’s geometry, which applies to the next acceleration-structure motion instance you create with the descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var mask: UInt32
```

## See Also

### Customizing intersection and hit tests for the instance

- [intersectionFunctionTableOffset](intersectionfunctiontableoffset.md) — An offset into the intersection-function table for ray tracing, which applies to the next acceleration-structure motion instance you create with the descriptor.
- [options](options.md) — An option set which applies to the next acceleration structure motion-instance you create with the descriptor.
