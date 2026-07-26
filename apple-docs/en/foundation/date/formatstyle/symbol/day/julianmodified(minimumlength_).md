---
title: 'julianModified(minimumLength:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/symbol/day/julianmodified(minimumlength:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/day/julianmodified(minimumlength:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/day/julianmodified%28minimumlength%3A%29.json'
content_hash: 'sha256:f1bedb5a5eb7d25a'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [Day](../day.md)

# julianModified(minimumLength:)

<sub>Type Method</sub>

Creates a custom day format style representing the modified Julian day.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func julianModified(minimumLength: Int = 1) -> Date.FormatStyle.Symbol.Day
```

## Parameters

- `minimumLength` — Specifies the minimum number of digits.

## Return Value

The minimum length specifies the minimum number of digits, zero-padded if necessary. For example, `002451334`.

## See Also

### Modifying a Day Format

- [defaultDigits](defaultdigits.md) — Custom format style portraying the minimum number of digits that represents the numeric day of month.
- [ordinalOfDayInMonth](ordinalofdayinmonth.md) — Custom format style portraying the ordinal of the day in the month.
- [twoDigits](twodigits.md) — Custom format style portraying the two-digit numeric day of month, zero-padded if necessary.
