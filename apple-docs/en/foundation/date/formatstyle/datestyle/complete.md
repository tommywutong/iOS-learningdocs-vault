---
title: complete
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/datestyle/complete
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/datestyle/complete'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/datestyle/complete.json'
content_hash: 'sha256:e70209b34ad516a2'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [FormatStyle](../../formatstyle.md) · [DateStyle](../datestyle.md)

# complete

<sub>Type Property</sub>

A date style with all components represented.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let complete: Date.FormatStyle.DateStyle
```

## Discussion

A `complete` date style represents the day, month, day of month, and year components in the format. For example, `Saturday, October 17, 2020`,` `for locale `en_US`.

## See Also

### Modifying a Date Style

- [abbreviated](abbreviated.md) — A date style with some components abbreviated for space-constrained applications.
- [long](long.md) — A lengthened date style with the full month, day of month, and year components represented.
- [numeric](numeric.md) — A date style with the month, day of month, and year components represented as numeric values.
- [omitted](omitted.md) — A date style with no date-related components represented.
