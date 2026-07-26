---
title: narrow
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/hour/ampmstyle/narrow
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/hour/ampmstyle/narrow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/hour/ampmstyle/narrow.json'
content_hash: 'sha256:7500f287f61d9367'
translated: false
---

> Navigation: [Technologies](../../../../../../technologies.md) · [Foundation](../../../../../../foundation.md) · [Date](../../../../../date.md) · [FormatStyle](../../../../formatstyle.md) · [Symbol](../../../symbol.md) · [Hour](../../hour.md) · [AMPMStyle](../ampmstyle.md)

# narrow

<sub>Type Property</sub>

A type that specifies the narrow day period if the locale prefers using day period with hour.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let narrow: Date.FormatStyle.Symbol.Hour.AMPMStyle
```

## Discussion

This type represents the hour period in a narrow format where appropriate. For example, when used with `defaultDigits`, this style may represent 8 a.m. as `8` or `8a`, and 1 p.m. as `13`, or `1p`. With `twoDigits`, this style produces `08` or `08a`, and `13` or `01p`, respectively.

## See Also

### Creating AMPM Styles

- [abbreviated](abbreviated.md) — A type that specifies the abbreviated day period for when the locale prefers using day period with hour.
- [omitted](omitted.md) — A type that hides the day period marker.
- [wide](wide.md) — A type that represents the wide day period if the locale prefers using day period with hour.
