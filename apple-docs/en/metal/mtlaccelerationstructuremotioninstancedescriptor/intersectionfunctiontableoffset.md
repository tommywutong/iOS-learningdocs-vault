---
title: intersectionFunctionTableOffset
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/intersectionfunctiontableoffset
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/intersectionfunctiontableoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/intersectionfunctiontableoffset.json'
content_hash: 'sha256:782a732fcbcc31f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureMotionInstanceDescriptor](../mtlaccelerationstructuremotioninstancedescriptor.md)

# intersectionFunctionTableOffset

<sub>Instance Property</sub>

An offset into the intersection-function table for ray tracing, which applies to the next acceleration-structure motion instance you create with the descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var intersectionFunctionTableOffset: UInt32
```

## Discussion

By default, after Metal finds an intersection between a ray and a primitive, it runs your specified intersection function to determine whether the ray actually hit the primitive. To determine which function in the intersection table to call, Metal adds this property to the value specified in the instance’s [intersectionFunctionTableOffset](../mtlaccelerationstructuregeometrydescriptor/intersectionfunctiontableoffset.md), and looks up the entry at that index.

## See Also

### Customizing intersection and hit tests for the instance

- [options](options.md) — An option set which applies to the next acceleration structure motion-instance you create with the descriptor.
- [mask](mask.md) — A mask for testing ray-tracing rays with a scene’s geometry, which applies to the next acceleration-structure motion instance you create with the descriptor.
