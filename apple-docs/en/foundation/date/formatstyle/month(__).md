---
title: 'month(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/month(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/month(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/month%28_%3A%29.json'
content_hash: 'sha256:0116434e278ec987'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [FormatStyle](../formatstyle.md)

# month(_:)

<sub>Instance Method</sub>

Modifies the date format style to use the specified month format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func month(_ format: Date.FormatStyle.Symbol.Month = .abbreviated) -> Date.FormatStyle
```

## Parameters

- `format` — The month format style applied to the date format style.

## Return Value

A date format style modified to include the specified month style.

## Discussion

Possible values of [Month](symbol/month.md) include [abbreviated](symbol/month/abbreviated.md), [defaultDigits](symbol/month/defaultdigits.md), [narrow](symbol/month/narrow.md), [twoDigits](symbol/month/twodigits.md), and [wide](symbol/month/wide.md).

This example shows a variety of [Month](symbol/month.md) format styles applied to a date:

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().month(.abbreviated)) // Feb
meetingDate.formatted(Date.FormatStyle().month(.narrow)) // F
meetingDate.formatted(Date.FormatStyle().month(.defaultDigits)) // 2
meetingDate.formatted(Date.FormatStyle().month(.twoDigits)) // 02
meetingDate.formatted(Date.FormatStyle().month(.wide)) // February
meetingDate.formatted(Date.FormatStyle().month()) // Feb
```

If you don’t provide a format, the [abbreviated](symbol/month/abbreviated.md) static variable is the default format.

For more information about formatting dates, see [FormatStyle](../formatstyle.md).

## See Also

### Specifying the Date Format

- [day(_:)](<day(__).md>) — Modifies the date format style to use the specified day format style.
- [dayOfYear(_:)](<dayofyear(__).md>) — Modifies the date format style to use the specified day of the year format style.
- [era(_:)](<era(__).md>) — Modifies the date format style to use the specified era format style.
- [quarter(_:)](<quarter(__).md>) — Modifies the date format style to use the specified quarter format style.
- [week(_:)](<week(__).md>) — Modifies the date format style to use the specified week format style.
- [weekday(_:)](<weekday(__).md>) — Modifies the date format style to use the specified weekday format style.
- [year(_:)](<year(__).md>) — Modifies the date format style to use the specified year format style.
- [DateStyle](datestyle.md) — Type that defines date styles varied in length or components included.
