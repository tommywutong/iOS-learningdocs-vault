---
title: 'relatedGregorian(minimumLength:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/symbol/year/relatedgregorian(minimumlength:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/year/relatedgregorian(minimumlength:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/year/relatedgregorian%28minimumlength%3A%29.json'
content_hash: 'sha256:f2a859b625916b4e'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [Year](../year.md)

# relatedGregorian(minimumLength:)

<sub>Type Method</sub>

Returns a custom format style that portrays the year of a non-Gregorian calendar system in the corresponding Gregorian year.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func relatedGregorian(minimumLength: Int = 1) -> Date.FormatStyle.Symbol.Year
```

## Parameters

- `minimumLength` — The minimum length to display the full year.

## Return Value

A custom year format style that portrays the year of the calendar system with the provided minimum length.

## Discussion

For non-Gregorian calendars, output corresponds to the extended Gregorian year in which the calendar’s year begins. The default length is the minimum needed to show the full year.

## See Also

### Modifying a Year

- [defaultDigits](defaultdigits.md) — The custom year format style showing the minimum number of digits that represents the numeric year.
- [twoDigits](twodigits.md) — The custom format style portraying the two-digit numeric year, zero-padded if necessary.
- [padded(_:)](<padded(__).md>) — Returns a custom format style that portrays the year of the calendar system of the provided length, zero-padded if necessary.
- [extended(minimumLength:)](<extended(minimumlength_).md>) — Returns a custom format style that portrays the year of the calendar system, encompassing all supra-year fields.
