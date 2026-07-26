---
title: omitted
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/hour/ampmstyle/omitted
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/hour/ampmstyle/omitted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/hour/ampmstyle/omitted.json'
content_hash: 'sha256:9ba9e603904e9e88'
translated: false
---

> Navigation: [Technologies](../../../../../../technologies.md) · [Foundation](../../../../../../foundation.md) · [Date](../../../../../date.md) · [FormatStyle](../../../../formatstyle.md) · [Symbol](../../../symbol.md) · [Hour](../../hour.md) · [AMPMStyle](../ampmstyle.md)

# omitted

<sub>Type Property</sub>

A type that hides the day period marker.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let omitted: Date.FormatStyle.Symbol.Hour.AMPMStyle
```

## Discussion

This type represents the hour period numerically only. For example, `8` (for 8 a.m.) or `1` (for 1 p.m.) if used with `defaultDigits`, and `08` or `01` if used with `twoDigits`.

## See Also

### Creating AMPM Styles

- [abbreviated](abbreviated.md) — A type that specifies the abbreviated day period for when the locale prefers using day period with hour.
- [narrow](narrow.md) — A type that specifies the narrow day period if the locale prefers using day period with hour.
- [wide](wide.md) — A type that represents the wide day period if the locale prefers using day period with hour.
