---
title: abbreviated
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/datestyle/abbreviated
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/datestyle/abbreviated'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/datestyle/abbreviated.json'
content_hash: 'sha256:00a7da6aae96aba4'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [FormatStyle](../../formatstyle.md) · [DateStyle](../datestyle.md)

# abbreviated

<sub>Type Property</sub>

A date style with some components abbreviated for space-constrained applications.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let abbreviated: Date.FormatStyle.DateStyle
```

## Discussion

A shortened date style that presents an abbreviated month, day of month, and year components of a date. For example, `Oct 17, 2020`, for locale `en_US`.

## See Also

### Modifying a Date Style

- [complete](complete.md) — A date style with all components represented.
- [long](long.md) — A lengthened date style with the full month, day of month, and year components represented.
- [numeric](numeric.md) — A date style with the month, day of month, and year components represented as numeric values.
- [omitted](omitted.md) — A date style with no date-related components represented.
