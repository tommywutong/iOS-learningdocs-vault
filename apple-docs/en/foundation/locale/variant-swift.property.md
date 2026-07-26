---
title: variant
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/variant-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/locale/variant-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/variant-swift.property.json'
content_hash: 'sha256:4e48093ce11b3e91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# variant

<sub>Instance Property</sub>

An optional variant used by the locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var variant: Locale.Variant? { get }
```

## Discussion

This property corresponds to the `va` key of the Unicode BCP 47 extension.

For locale instances created with the `va` specifier (such as `en-US@va=posix`), or with a custom [Components](components.md), this property represents the custom variant. Otherwise, it represents the locale’s default variant.

## See Also

### Getting region components

- [region](region-swift.property.md) — The region used by the locale.
- [Region](region-swift.struct.md) — A type that represents a geographic region, for use in specifying a locale or language.
- [subdivision](subdivision-swift.property.md) — The optional subdivision of the region used by this locale.
- [Subdivision](subdivision-swift.struct.md) — A type that represents a subdivision of a region, such as a state in the US or a province in Canada.
- [Variant](variant-swift.struct.md) — A type that represents a locale’s language variant.
