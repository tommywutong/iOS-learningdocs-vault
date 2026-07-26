---
title: region
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/components/region
source_url: 'https://developer.apple.com/documentation/foundation/locale/components/region'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/components/region.json'
content_hash: 'sha256:0f2b445d0cbd62ae'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Components](../components.md)

# region

<sub>Instance Property</sub>

The region used by the locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var region: Locale.Region?
```

## Discussion

Set this property to override the region for region-related preferences, such as measuring system, calendar, and first day of the week. If unset, the locale uses the region of the language component.

This property corresponds to the `rg` key of the Unicode BCP 47 extension.

## See Also

### Specifying region components

- [Region](../region-swift.struct.md) — A type that represents a geographic region, for use in specifying a locale or language.
- [subdivision](subdivision.md) — The optional subdivision of the region used by this locale.
- [Subdivision](../subdivision-swift.struct.md) — A type that represents a subdivision of a region, such as a state in the US or a province in Canada.
- [variant](variant.md) — An optional variant used by the locale.
- [Variant](../variant-swift.struct.md) — A type that represents a locale’s language variant.
