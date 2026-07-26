---
title: twoDigits
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/day/twodigits
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/day/twodigits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/day/twodigits.json'
content_hash: 'sha256:ebece8421418a7f5'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [Day](../day.md)

# twoDigits

<sub>Type Property</sub>

Custom format style portraying the two-digit numeric day of month, zero-padded if necessary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var twoDigits: Date.FormatStyle.Symbol.Day { get }
```

## Discussion

This style produces `01` for the first day of the month and `18` for the eighteenth. To use single digits when possible, use [defaultDigits](defaultdigits.md).

## See Also

### Modifying a Day Format

- [defaultDigits](defaultdigits.md) — Custom format style portraying the minimum number of digits that represents the numeric day of month.
- [ordinalOfDayInMonth](ordinalofdayinmonth.md) — Custom format style portraying the ordinal of the day in the month.
- [julianModified(minimumLength:)](<julianmodified(minimumlength_).md>) — Creates a custom day format style representing the modified Julian day.
