---
title: unitStyle
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkdistanceformatter/unitstyle
source_url: 'https://developer.apple.com/documentation/mapkit/mkdistanceformatter/unitstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdistanceformatter/unitstyle.json'
content_hash: 'sha256:6c6e6ed85c74cf93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKDistanceFormatter](../mkdistanceformatter.md)

# unitStyle

<sub>Instance Property</sub>

The preferred style for units.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var unitStyle: MKDistanceFormatter.DistanceUnitStyle { get set }
```

## Discussion

You can abbreviate or fully spell out units. The default value of this property is [MKDistanceFormatterUnitStyleDefault](distanceunitstyle/default.md), which bases the style on the user’s locale and language settings.

## See Also

### Specifying the format

- [locale](locale.md) — The locale to use when formatting strings.
- [units](units-swift.property.md) — The measuring system — imperial or metric — to use for units.
- [Units](units-swift.enum.md) — Constants that reflect the type of units to use in the string.
- [DistanceUnitStyle](distanceunitstyle.md) — Constants that indicate the format style to use for strings.
