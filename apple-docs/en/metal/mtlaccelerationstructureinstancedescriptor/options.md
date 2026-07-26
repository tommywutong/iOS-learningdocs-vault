---
title: options
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureinstancedescriptor/options
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstancedescriptor/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureinstancedescriptor/options.json'
content_hash: 'sha256:f90a2869ba5d722b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureInstanceDescriptor](../mtlaccelerationstructureinstancedescriptor.md)

# options

<sub>Instance Property</sub>

The options for the instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var options: MTLAccelerationStructureInstanceOptions
```

## See Also

### Customizing intersection and hit tests for the instance

- [intersectionFunctionTableOffset](intersectionfunctiontableoffset.md) — An offset for determining which function in the intersection function table Metal needs to call when testing a ray against the instance.
- [mask](mask.md) — A mask to use for the instance when testing a ray against the geometry.
