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
doc_path: /documentation/foundation/date/formatstyle/symbol/year/defaultdigits
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/year/defaultdigits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/year/defaultdigits.json'
content_hash: 'sha256:10969a9be311a501'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [Year](../year.md)

# defaultDigits

<sub>Type Property</sub>

The custom year format style showing the minimum number of digits that represents the numeric year.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var defaultDigits: Date.FormatStyle.Symbol.Year { get }
```

## Discussion

This style represents years like `1`, `18`, `202`, and `2020`.

## See Also

### Modifying a Year

- [twoDigits](twodigits.md) — The custom format style portraying the two-digit numeric year, zero-padded if necessary.
- [padded(_:)](<padded(__).md>) — Returns a custom format style that portrays the year of the calendar system of the provided length, zero-padded if necessary.
- [relatedGregorian(minimumLength:)](<relatedgregorian(minimumlength_).md>) — Returns a custom format style that portrays the year of a non-Gregorian calendar system in the corresponding Gregorian year.
- [extended(minimumLength:)](<extended(minimumlength_).md>) — Returns a custom format style that portrays the year of the calendar system, encompassing all supra-year fields.
