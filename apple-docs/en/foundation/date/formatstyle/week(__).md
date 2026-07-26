---
title: 'week(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/week(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/week(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/week%28_%3A%29.json'
content_hash: 'sha256:15b538b877fe585d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [FormatStyle](../formatstyle.md)

# week(_:)

<sub>Instance Method</sub>

Modifies the date format style to use the specified week format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func week(_ format: Date.FormatStyle.Symbol.Week = .defaultDigits) -> Date.FormatStyle
```

## Parameters

- `format` — The week format style applied to the date format style.

## Return Value

A date format style modified to include the specified week format style.

## Discussion

Possible values of [Week](symbol/week.md) include [defaultDigits](symbol/week/defaultdigits.md), [twoDigits](symbol/week/twodigits.md), and [weekOfMonth](symbol/week/weekofmonth.md).

This example shows a variety of [Week](symbol/week.md) format styles applied to a date:

```swift
let meetingDate = Date() // May 3, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().week(.defaultDigits)) // 19
meetingDate.formatted(Date.FormatStyle().week(.twoDigits)) // 19
meetingDate.formatted(Date.FormatStyle().week(.weekOfMonth)) // 2
meetingDate.formatted(Date.FormatStyle().week()) // 19

```

An incomplete week at the start of a month is the first week of the month `1`. If you don’t provide a format, the [defaultDigits](symbol/week/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see [FormatStyle](../formatstyle.md).

## See Also

### Specifying the Date Format

- [day(_:)](<day(__).md>) — Modifies the date format style to use the specified day format style.
- [dayOfYear(_:)](<dayofyear(__).md>) — Modifies the date format style to use the specified day of the year format style.
- [era(_:)](<era(__).md>) — Modifies the date format style to use the specified era format style.
- [month(_:)](<month(__).md>) — Modifies the date format style to use the specified month format style.
- [quarter(_:)](<quarter(__).md>) — Modifies the date format style to use the specified quarter format style.
- [weekday(_:)](<weekday(__).md>) — Modifies the date format style to use the specified weekday format style.
- [year(_:)](<year(__).md>) — Modifies the date format style to use the specified year format style.
- [DateStyle](datestyle.md) — Type that defines date styles varied in length or components included.
