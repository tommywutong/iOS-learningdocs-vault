---
title: 'padded(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/symbol/yearforweekofyear/padded(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/yearforweekofyear/padded(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/yearforweekofyear/padded%28_%3A%29.json'
content_hash: 'sha256:91d45d5edb91f257'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [YearForWeekOfYear](../yearforweekofyear.md)

# padded(_:)

<sub>Type Method</sub>

Returns a custom format style that represents the three or more digits of the year in week-of-year calendars, zero-padded if necessary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func padded(_ length: Int) -> Date.FormatStyle.Symbol.YearForWeekOfYear
```

## Parameters

- `length` — The length of the string to display a calendar year.

## Return Value

A custom year format style that portrays the year of a week of year calendar system with the provided length.

## See Also

### Modifying a Year for Week-of-Year

- [defaultDigits](defaultdigits.md) — Custom week of the year format style showing the minimum number of digits that represents the year in week-of-year calendars.
- [twoDigits](twodigits.md) — The custom format style that represents the two-digit numeric year in week-of-year calendars, zero-padded or truncated if necessary.
