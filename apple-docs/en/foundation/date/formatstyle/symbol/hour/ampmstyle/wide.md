---
title: wide
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/hour/ampmstyle/wide
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/hour/ampmstyle/wide'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/hour/ampmstyle/wide.json'
content_hash: 'sha256:db21b91c55c71b52'
translated: false
---

> Navigation: [Technologies](../../../../../../technologies.md) · [Foundation](../../../../../../foundation.md) · [Date](../../../../../date.md) · [FormatStyle](../../../../formatstyle.md) · [Symbol](../../../symbol.md) · [Hour](../../hour.md) · [AMPMStyle](../ampmstyle.md)

# wide

<sub>Type Property</sub>

A type that represents the wide day period if the locale prefers using day period with hour.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let wide: Date.FormatStyle.Symbol.Hour.AMPMStyle
```

## Discussion

This type represents the hour period in a wide format where appropriate. For example, when used with `defaultDigits`, this style may represent 8 a.m. as  `8` or `8 A.M.,` and 1 p.m. as  `13` or `1 P.M.` With `twoDigits`, this style produce `08` or `08 A.M.` and `13 or 01 P.M.`

## See Also

### Creating AMPM Styles

- [abbreviated](abbreviated.md) — A type that specifies the abbreviated day period for when the locale prefers using day period with hour.
- [narrow](narrow.md) — A type that specifies the narrow day period if the locale prefers using day period with hour.
- [omitted](omitted.md) — A type that hides the day period marker.
