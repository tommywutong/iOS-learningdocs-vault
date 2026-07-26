---
title: defaultDigits
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/week/defaultdigits
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/week/defaultdigits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/week/defaultdigits.json'
content_hash: 'sha256:97fb6ffddfaa9683'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [Week](../week.md)

# defaultDigits

<sub>Type Property</sub>

Custom week format style showing the minimum number of digits that represents the numeric week.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var defaultDigits: Date.FormatStyle.Symbol.Week { get }
```

## Discussion

This style represents weeks like `1` or `18`.

## See Also

### Modifying a Week

- [twoDigits](twodigits.md) — Custom format style portraying the two-digit numeric week, zero-padded if necessary.
- [weekOfMonth](weekofmonth.md) — Custom format style portraying the numeric week of the month.
