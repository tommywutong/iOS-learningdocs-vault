---
title: subdivision
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/subdivision-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/locale/subdivision-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/subdivision-swift.property.json'
content_hash: 'sha256:44a73e87d5ddacc6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# subdivision

<sub>Instance Property</sub>

The optional subdivision of the region used by this locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var subdivision: Locale.Subdivision? { get }
```

## Discussion

This property corresponds to the `sd` key of the Unicode BCP 47 extension.

## See Also

### Getting region components

- [region](region-swift.property.md) — The region used by the locale.
- [Region](region-swift.struct.md) — A type that represents a geographic region, for use in specifying a locale or language.
- [Subdivision](subdivision-swift.struct.md) — A type that represents a subdivision of a region, such as a state in the US or a province in Canada.
- [variant](variant-swift.property.md) — An optional variant used by the locale.
- [Variant](variant-swift.struct.md) — A type that represents a locale’s language variant.
