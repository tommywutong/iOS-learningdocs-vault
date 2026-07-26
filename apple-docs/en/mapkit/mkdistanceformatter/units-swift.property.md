---
title: units
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkdistanceformatter/units-swift.property
source_url: 'https://developer.apple.com/documentation/mapkit/mkdistanceformatter/units-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdistanceformatter/units-swift.property.json'
content_hash: 'sha256:b1d1637a858c4b69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKDistanceFormatter](../mkdistanceformatter.md)

# units

<sub>Instance Property</sub>

The measuring system — imperial or metric — to use for units.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var units: MKDistanceFormatter.Units { get set }
```

## Discussion

You can use this property to explicitly set the measuring system for units. The default value of this property is [MKDistanceFormatterUnitsDefault](units-swift.enum/default.md), which bases the measuring system on the user’s locale.

## See Also

### Specifying the format

- [locale](locale.md) — The locale to use when formatting strings.
- [Units](units-swift.enum.md) — Constants that reflect the type of units to use in the string.
- [unitStyle](unitstyle.md) — The preferred style for units.
- [DistanceUnitStyle](distanceunitstyle.md) — Constants that indicate the format style to use for strings.
