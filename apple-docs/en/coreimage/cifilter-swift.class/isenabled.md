---
title: isEnabled
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/isenabled
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/isenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/isenabled.json'
content_hash: 'sha256:1acbd3bded521ab1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# isEnabled

<sub>Instance Property</sub>

A Boolean value that determines whether the filter is enabled. Animatable.

<sub>macOS</sub>

```swift
var isEnabled: Bool { get set }
```

## Discussion

The filter is applied to its input when this property is set to `true` (the default).

Use this property in conjunction with the [name](name.md) property when attaching filters to Core Animation layers and accessing or animating filter properties through key-value animations.  Core Animation can animate this property on a layer.

## See Also

### Getting filter parameters and attributes

- [name](name.md) — A name associated with a filter.
- [attributes](attributes.md) — A dictionary of key-value pairs that describe the filter.
- [inputKeys](inputkeys.md) — The names of all input parameters to the filter.
- [outputKeys](outputkeys.md) — The names of all output parameters from the filter.
- [outputImage](outputimage.md) — Returns a [CIImage](../ciimage.md) object that encapsulates the operations configured in the filter.
