---
title: outputImage
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/outputimage
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/outputimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/outputimage.json'
content_hash: 'sha256:b64020d33098fec2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# outputImage

<sub>Instance Property</sub>

Returns a [CIImage](../ciimage.md) object that encapsulates the operations configured in the filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var outputImage: CIImage? { get }
```

## See Also

### Getting filter parameters and attributes

- [name](name.md) — A name associated with a filter.
- [enabled](isenabled.md) — A Boolean value that determines whether the filter is enabled. Animatable.
- [attributes](attributes.md) — A dictionary of key-value pairs that describe the filter.
- [inputKeys](inputkeys.md) — The names of all input parameters to the filter.
- [outputKeys](outputkeys.md) — The names of all output parameters from the filter.
