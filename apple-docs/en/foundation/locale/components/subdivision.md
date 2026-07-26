---
title: subdivision
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/components/subdivision
source_url: 'https://developer.apple.com/documentation/foundation/locale/components/subdivision'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/components/subdivision.json'
content_hash: 'sha256:6790613a0d14f77b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Components](../components.md)

# subdivision

<sub>Instance Property</sub>

The optional subdivision of the region used by this locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var subdivision: Locale.Subdivision?
```

## Discussion

Set this property to override the locale’s regional subdivision of [region](region.md).

This property corresponds to the `sd` key of the Unicode BCP 47 extension.

## See Also

### Specifying region components

- [region](region.md) — The region used by the locale.
- [Region](../region-swift.struct.md) — A type that represents a geographic region, for use in specifying a locale or language.
- [Subdivision](../subdivision-swift.struct.md) — A type that represents a subdivision of a region, such as a state in the US or a province in Canada.
- [variant](variant.md) — An optional variant used by the locale.
- [Variant](../variant-swift.struct.md) — A type that represents a locale’s language variant.
