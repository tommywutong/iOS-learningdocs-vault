---
title: outputKeys
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/outputkeys
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/outputkeys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/outputkeys.json'
content_hash: 'sha256:498f36af50285917'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# outputKeys

<sub>Instance Property</sub>

The names of all output parameters from the filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var outputKeys: [String] { get }
```

## See Also

### Getting filter parameters and attributes

- [name](name.md) — A name associated with a filter.
- [enabled](isenabled.md) — A Boolean value that determines whether the filter is enabled. Animatable.
- [attributes](attributes.md) — A dictionary of key-value pairs that describe the filter.
- [inputKeys](inputkeys.md) — The names of all input parameters to the filter.
- [outputImage](outputimage.md) — Returns a [CIImage](../ciimage.md) object that encapsulates the operations configured in the filter.
