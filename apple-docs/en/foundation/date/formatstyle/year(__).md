---
title: 'year(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/year(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/year(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/year%28_%3A%29.json'
content_hash: 'sha256:10155ae641dbfd3d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [FormatStyle](../formatstyle.md)

# year(_:)

<sub>Instance Method</sub>

Modifies the date format style to use the specified year format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func year(_ format: Date.FormatStyle.Symbol.Year = .defaultDigits) -> Date.FormatStyle
```

## Parameters

- `format` — The year format style applied to the date format style.

## Return Value

A date format style modified to include the specified year format style.

## Discussion

Possible values of [Year](symbol/year.md) include [twoDigits](symbol/year/twodigits.md), [padded(_:)](<symbol/year/padded(__).md>), [relatedGregorian(minimumLength:)](<symbol/year/relatedgregorian(minimumlength_).md>), and [extended(minimumLength:)](<symbol/year/extended(minimumlength_).md>).

This example shows a variety of [Year](symbol/year.md) formats applied to a date:

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().year(.defaultDigits)) // 2021
meetingDate.formatted(Date.FormatStyle().year(.twoDigits)) // 21
meetingDate.formatted(Date.FormatStyle().year(.padded(6))) // 002021
```

If you don’t provide a format, the [defaultDigits](symbol/day/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see [FormatStyle](../formatstyle.md).

## See Also

### Specifying the Date Format

- [day(_:)](<day(__).md>) — Modifies the date format style to use the specified day format style.
- [dayOfYear(_:)](<dayofyear(__).md>) — Modifies the date format style to use the specified day of the year format style.
- [era(_:)](<era(__).md>) — Modifies the date format style to use the specified era format style.
- [month(_:)](<month(__).md>) — Modifies the date format style to use the specified month format style.
- [quarter(_:)](<quarter(__).md>) — Modifies the date format style to use the specified quarter format style.
- [week(_:)](<week(__).md>) — Modifies the date format style to use the specified week format style.
- [weekday(_:)](<weekday(__).md>) — Modifies the date format style to use the specified weekday format style.
- [DateStyle](datestyle.md) — Type that defines date styles varied in length or components included.
