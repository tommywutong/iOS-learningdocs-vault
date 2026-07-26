---
title: numberFormatter
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurementformatter/numberformatter
source_url: 'https://developer.apple.com/documentation/foundation/measurementformatter/numberformatter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurementformatter/numberformatter.json'
content_hash: 'sha256:2c7c1bc8901b4744'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [MeasurementFormatter](../measurementformatter.md)

# numberFormatter

<sub>Instance Property</sub>

The number formatter used to format the quantity of a measurement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var numberFormatter: NumberFormatter! { get set }
```

## Discussion

If unspecified, an [NumberFormatter](../numberformatter.md) object with [NSNumberFormatterDecimalStyle](../numberformatter/style/decimal.md) style is used.

## See Also

### Specifying the Format

- [unitOptions](unitoptions-swift.property.md) — The options for how the unit is formatted.
- [UnitOptions](unitoptions-swift.struct.md) — Measurement formatter options.
- [unitStyle](unitstyle.md) — The unit style.
- [locale](locale.md) — The locale of the formatter.
