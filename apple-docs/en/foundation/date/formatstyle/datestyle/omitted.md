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
doc_path: /documentation/foundation/date/formatstyle/datestyle/omitted
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/datestyle/omitted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/datestyle/omitted.json'
content_hash: 'sha256:72eb6c4da747ad5b'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [FormatStyle](../../formatstyle.md) · [DateStyle](../datestyle.md)

# omitted

<sub>Type Property</sub>

A date style with no date-related components represented.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let omitted: Date.FormatStyle.DateStyle
```

## Discussion

If both the date style and time style are set to `omitted`, the date is represented using the default style of `abbreviated`.

## See Also

### Modifying a Date Style

- [abbreviated](abbreviated.md) — A date style with some components abbreviated for space-constrained applications.
- [complete](complete.md) — A date style with all components represented.
- [long](long.md) — A lengthened date style with the full month, day of month, and year components represented.
- [numeric](numeric.md) — A date style with the month, day of month, and year components represented as numeric values.
