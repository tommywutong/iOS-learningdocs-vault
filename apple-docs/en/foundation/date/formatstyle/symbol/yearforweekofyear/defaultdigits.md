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
doc_path: /documentation/foundation/date/formatstyle/symbol/yearforweekofyear/defaultdigits
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/yearforweekofyear/defaultdigits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/yearforweekofyear/defaultdigits.json'
content_hash: 'sha256:f5daf26883ed93ac'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [YearForWeekOfYear](../yearforweekofyear.md)

# defaultDigits

<sub>Type Property</sub>

Custom week of the year format style showing the minimum number of digits that represents the year in week-of-year calendars.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var defaultDigits: Date.FormatStyle.Symbol.YearForWeekOfYear { get }
```

## Discussion

This represents week-of-year values like `1` or `18`.

## See Also

### Modifying a Year for Week-of-Year

- [twoDigits](twodigits.md) — The custom format style that represents the two-digit numeric year in week-of-year calendars, zero-padded or truncated if necessary.
- [padded(_:)](<padded(__).md>) — Returns a custom format style that represents the three or more digits of the year in week-of-year calendars, zero-padded if necessary.
