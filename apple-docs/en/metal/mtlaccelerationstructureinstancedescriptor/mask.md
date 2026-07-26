---
title: mask
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureinstancedescriptor/mask
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstancedescriptor/mask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureinstancedescriptor/mask.json'
content_hash: 'sha256:29485881d2d47518'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureInstanceDescriptor](../mtlaccelerationstructureinstancedescriptor.md)

# mask

<sub>Instance Property</sub>

A mask to use for the instance when testing a ray against the geometry.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var mask: UInt32
```

## Discussion

Metal reserves the top 24 bits for future use.

## See Also

### Customizing intersection and hit tests for the instance

- [intersectionFunctionTableOffset](intersectionfunctiontableoffset.md) — An offset for determining which function in the intersection function table Metal needs to call when testing a ray against the instance.
- [options](options.md) — The options for the instance.
