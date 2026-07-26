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
doc_path: '/documentation/foundation/date/formatstyle/symbol/year/padded(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/year/padded(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/year/padded%28_%3A%29.json'
content_hash: 'sha256:f7ef778b6af1ef72'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [Year](../year.md)

# padded(_:)

<sub>Type Method</sub>

Returns a custom format style that portrays the year of the calendar system of the provided length, zero-padded if necessary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func padded(_ length: Int) -> Date.FormatStyle.Symbol.Year
```

## Parameters

- `length` — The length of the string to display a calendar year.

## Return Value

A custom year format style that portrays the year of the calendar system with the provided length.

## Discussion

Use [padded(_:)](<padded(__).md>) to display a year using three or more digits, zero-padded if necessary. For example, `002`, `020`, `201`, `2017`.

## See Also

### Modifying a Year

- [defaultDigits](defaultdigits.md) — The custom year format style showing the minimum number of digits that represents the numeric year.
- [twoDigits](twodigits.md) — The custom format style portraying the two-digit numeric year, zero-padded if necessary.
- [relatedGregorian(minimumLength:)](<relatedgregorian(minimumlength_).md>) — Returns a custom format style that portrays the year of a non-Gregorian calendar system in the corresponding Gregorian year.
- [extended(minimumLength:)](<extended(minimumlength_).md>) — Returns a custom format style that portrays the year of the calendar system, encompassing all supra-year fields.
