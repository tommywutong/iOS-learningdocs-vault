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
doc_path: /documentation/foundation/date/formatstyle/symbol/day/defaultdigits
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/day/defaultdigits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/day/defaultdigits.json'
content_hash: 'sha256:351ea27b78926193'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [Day](../day.md)

# defaultDigits

<sub>Type Property</sub>

Custom format style portraying the minimum number of digits that represents the numeric day of month.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var defaultDigits: Date.FormatStyle.Symbol.Day { get }
```

## Discussion

This style produces `1` for the  first day of the month and `18` for the eighteenth. To force two-digit display in all cases, use [twoDigits](twodigits.md).

## See Also

### Modifying a Day Format

- [ordinalOfDayInMonth](ordinalofdayinmonth.md) — Custom format style portraying the ordinal of the day in the month.
- [twoDigits](twodigits.md) — Custom format style portraying the two-digit numeric day of month, zero-padded if necessary.
- [julianModified(minimumLength:)](<julianmodified(minimumlength_).md>) — Creates a custom day format style representing the modified Julian day.
