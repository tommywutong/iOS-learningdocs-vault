---
title: locale
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurementformatter/locale
source_url: 'https://developer.apple.com/documentation/foundation/measurementformatter/locale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurementformatter/locale.json'
content_hash: 'sha256:dda93008cfcbb85a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [MeasurementFormatter](../measurementformatter.md)

# locale

<sub>Instance Property</sub>

The locale of the formatter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var locale: Locale! { get set }
```

## Discussion

If unspecified, an [NSLocale](../nslocale.md) object representing the current system locale is used.

## See Also

### Specifying the Format

- [unitOptions](unitoptions-swift.property.md) — The options for how the unit is formatted.
- [UnitOptions](unitoptions-swift.struct.md) — Measurement formatter options.
- [unitStyle](unitstyle.md) — The unit style.
- [numberFormatter](numberformatter.md) — The number formatter used to format the quantity of a measurement.
