---
title: 'quarter(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/quarter(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/quarter(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/quarter%28_%3A%29.json'
content_hash: 'sha256:0db94d9180ecc522'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [FormatStyle](../formatstyle.md)

# quarter(_:)

<sub>Instance Method</sub>

Modifies the date format style to use the specified quarter format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func quarter(_ format: Date.FormatStyle.Symbol.Quarter = .abbreviated) -> Date.FormatStyle
```

## Parameters

- `format` — The quarter format style applied to the date format style.

## Return Value

A date format style modified to include the specified quarter style.

## Discussion

Possible values of [Quarter](symbol/quarter.md) include [abbreviated](symbol/quarter/abbreviated.md), [narrow](symbol/quarter/narrow.md), [oneDigit](symbol/quarter/onedigit.md), [twoDigits](symbol/month/twodigits.md), and [wide](symbol/month/wide.md).

This example shows a variety of [Quarter](symbol/quarter.md) format styles applied to a date:

```swift
let meetingDate = Date() // Oct 7, 2020 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().quarter(.abbreviated)) // Q4
meetingDate.formatted(Date.FormatStyle().quarter(.narrow)) // 4th quarter
meetingDate.formatted(Date.FormatStyle().quarter(.oneDigit)) // 4
meetingDate.formatted(Date.FormatStyle().quarter(.twoDigits)) // 04
meetingDate.formatted(Date.FormatStyle().quarter(.wide)) // 4th quarter
meetingDate.formatted(Date.FormatStyle().quarter()) // Q4

```

If you don’t provide a format, the [abbreviated](symbol/quarter/abbreviated.md) static variable is the default format.

For more information about formatting dates, see [FormatStyle](../formatstyle.md).

## See Also

### Specifying the Date Format

- [day(_:)](<day(__).md>) — Modifies the date format style to use the specified day format style.
- [dayOfYear(_:)](<dayofyear(__).md>) — Modifies the date format style to use the specified day of the year format style.
- [era(_:)](<era(__).md>) — Modifies the date format style to use the specified era format style.
- [month(_:)](<month(__).md>) — Modifies the date format style to use the specified month format style.
- [week(_:)](<week(__).md>) — Modifies the date format style to use the specified week format style.
- [weekday(_:)](<weekday(__).md>) — Modifies the date format style to use the specified weekday format style.
- [year(_:)](<year(__).md>) — Modifies the date format style to use the specified year format style.
- [DateStyle](datestyle.md) — Type that defines date styles varied in length or components included.
