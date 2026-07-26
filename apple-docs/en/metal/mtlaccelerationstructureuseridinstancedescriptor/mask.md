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
doc_path: /documentation/metal/mtlaccelerationstructureuseridinstancedescriptor/mask
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureuseridinstancedescriptor/mask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureuseridinstancedescriptor/mask.json'
content_hash: 'sha256:d4b261cae3703a99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureUserIDInstanceDescriptor](../mtlaccelerationstructureuseridinstancedescriptor.md)

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

- [intersectionFunctionTableOffset](intersectionfunctiontableoffset.md) — An offset for determining which function in the intersection function table Metal calls when testing a ray against the instance.
- [options](options.md) — The options for the instance.
