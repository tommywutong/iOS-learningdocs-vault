---
title: unitStyle
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurementformatter/unitstyle
source_url: 'https://developer.apple.com/documentation/foundation/measurementformatter/unitstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurementformatter/unitstyle.json'
content_hash: 'sha256:d1ae6ccf81aebe7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [MeasurementFormatter](../measurementformatter.md)

# unitStyle

<sub>Instance Property</sub>

The unit style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var unitStyle: Formatter.UnitStyle { get set }
```

## Discussion

The possible values are [NSFormattingUnitStyleShort](../formatter/unitstyle/short.md), [NSFormattingUnitStyleMedium](../formatter/unitstyle/medium.md), and [NSFormattingUnitStyleLong](../formatter/unitstyle/long.md). The default value is [NSFormattingUnitStyleMedium](../formatter/unitstyle/medium.md).

## See Also

### Specifying the Format

- [unitOptions](unitoptions-swift.property.md) — The options for how the unit is formatted.
- [UnitOptions](unitoptions-swift.struct.md) — Measurement formatter options.
- [locale](locale.md) — The locale of the formatter.
- [numberFormatter](numberformatter.md) — The number formatter used to format the quantity of a measurement.
