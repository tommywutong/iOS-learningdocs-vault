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
doc_path: /documentation/metal/mtlaccelerationstructureuseridinstancedescriptor/intersectionfunctiontableoffset
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureuseridinstancedescriptor/intersectionfunctiontableoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureuseridinstancedescriptor/intersectionfunctiontableoffset.json'
content_hash: 'sha256:dc3ebad35e3dec6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureUserIDInstanceDescriptor](../mtlaccelerationstructureuseridinstancedescriptor.md)

# intersectionFunctionTableOffset

<sub>Instance Property</sub>

An offset for determining which function in the intersection function table Metal calls when testing a ray against the instance.

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
