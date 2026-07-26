---
title: 'day(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/day(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/day(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/day%28_%3A%29.json'
content_hash: 'sha256:3cf43fc52853a68c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [FormatStyle](../formatstyle.md)

# day(_:)

<sub>Instance Method</sub>

Modifies the date format style to use the specified day format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func day(_ format: Date.FormatStyle.Symbol.Day = .defaultDigits) -> Date.FormatStyle
```

## Parameters

- `format` — The day format style applied to the date format style.

## Return Value

A date format style modified to include the specified day style.

## Discussion

Possible values of [Day](symbol/day.md) are [defaultDigits](symbol/day/defaultdigits.md), [ordinalOfDayInMonth](symbol/day/ordinalofdayinmonth.md), and [twoDigits](symbol/day/twodigits.md).

This example shows a variety of [Day](symbol/day.md) formats applied to a date:

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().day(.defaultDigits)) // 9
meetingDate.formatted(Date.FormatStyle().day(.ordinalOfDayInMonth)) // 2 (second Tuesday of the month)
meetingDate.formatted(Date.FormatStyle().day(.twoDigits)) // 09
meetingDate.formatted(Date.FormatStyle().day()) // 9
```

If you don’t provide a format, the [defaultDigits](symbol/day/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see [FormatStyle](../formatstyle.md).

## See Also

### Specifying the Date Format

- [dayOfYear(_:)](<dayofyear(__).md>) — Modifies the date format style to use the specified day of the year format style.
- [era(_:)](<era(__).md>) — Modifies the date format style to use the specified era format style.
- [month(_:)](<month(__).md>) — Modifies the date format style to use the specified month format style.
- [quarter(_:)](<quarter(__).md>) — Modifies the date format style to use the specified quarter format style.
- [week(_:)](<week(__).md>) — Modifies the date format style to use the specified week format style.
- [weekday(_:)](<weekday(__).md>) — Modifies the date format style to use the specified weekday format style.
- [year(_:)](<year(__).md>) — Modifies the date format style to use the specified year format style.
- [DateStyle](datestyle.md) — Type that defines date styles varied in length or components included.
