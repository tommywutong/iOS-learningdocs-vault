---
title: locale
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkdistanceformatter/locale
source_url: 'https://developer.apple.com/documentation/mapkit/mkdistanceformatter/locale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdistanceformatter/locale.json'
content_hash: 'sha256:36fd47d7d44d3ccf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKDistanceFormatter](../mkdistanceformatter.md)

# locale

<sub>Instance Property</sub>

The locale to use when formatting strings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var locale: Locale! { get set }
```

## Discussion

If you don’t specify an explicit locale, the formatter uses the user’s current locale information.

## See Also

### Specifying the format

- [units](units-swift.property.md) — The measuring system — imperial or metric — to use for units.
- [Units](units-swift.enum.md) — Constants that reflect the type of units to use in the string.
- [unitStyle](unitstyle.md) — The preferred style for units.
- [DistanceUnitStyle](distanceunitstyle.md) — Constants that indicate the format style to use for strings.
