---
title: long
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/datestyle/long
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/datestyle/long'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/datestyle/long.json'
content_hash: 'sha256:130978198368e8bb'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [FormatStyle](../../formatstyle.md) · [DateStyle](../datestyle.md)

# long

<sub>Type Property</sub>

A lengthened date style with the full month, day of month, and year components represented.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let long: Date.FormatStyle.DateStyle
```

## Discussion

A `long` date style represents the full date without the day of week in the format. For example, `October 17, 2020`.

## See Also

### Modifying a Date Style

- [abbreviated](abbreviated.md) — A date style with some components abbreviated for space-constrained applications.
- [complete](complete.md) — A date style with all components represented.
- [numeric](numeric.md) — A date style with the month, day of month, and year components represented as numeric values.
- [omitted](omitted.md) — A date style with no date-related components represented.
