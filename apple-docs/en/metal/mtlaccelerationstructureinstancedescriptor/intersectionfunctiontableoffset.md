---
title: intersectionFunctionTableOffset
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureinstancedescriptor/intersectionfunctiontableoffset
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstancedescriptor/intersectionfunctiontableoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureinstancedescriptor/intersectionfunctiontableoffset.json'
content_hash: 'sha256:50892bb6f8b6f44c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureInstanceDescriptor](../mtlaccelerationstructureinstancedescriptor.md)

# intersectionFunctionTableOffset

<sub>Instance Property</sub>

An offset for determining which function in the intersection function table Metal needs to call when testing a ray against the instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var intersectionFunctionTableOffset: UInt32
```

## Discussion

By default, after Metal finds an intersection between a ray and a primitive, it runs your specified intersection function to determine whether the ray actually hit the primitive. To determine which function in the intersection table to call, Metal adds this property to the value in the instance’s [intersectionFunctionTableOffset](../mtlaccelerationstructuregeometrydescriptor/intersectionfunctiontableoffset.md), and looks up the entry at that index.

## See Also

### Customizing intersection and hit tests for the instance

- [options](options.md) — The options for the instance.
- [mask](mask.md) — A mask to use for the instance when testing a ray against the geometry.
