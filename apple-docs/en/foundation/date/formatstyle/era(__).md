---
title: 'era(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/era(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/era(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/era%28_%3A%29.json'
content_hash: 'sha256:719171884c01820c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [FormatStyle](../formatstyle.md)

# era(_:)

<sub>Instance Method</sub>

Modifies the date format style to use the specified era format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func era(_ format: Date.FormatStyle.Symbol.Era = .abbreviated) -> Date.FormatStyle
```

## Parameters

- `format` — The era format style applied to the date format style.

## Return Value

A date format style modified to include the specified era style.

## Discussion

Possible values of [Era](symbol/era.md) include [abbreviated](symbol/era/abbreviated.md), [narrow](symbol/era/narrow.md), and [wide](symbol/era/wide.md).

This example shows a variety of [Era](symbol/era.md) format styles applied to a date:

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().era(.abbreviated)) // AD
meetingDate.formatted(Date.FormatStyle().era(.narrow)) // A
meetingDate.formatted(Date.FormatStyle().era(.wide)) // Anno Domini
meetingDate.formatted(Date.FormatStyle().era()) // AD
```

If you don’t provide a format, the [abbreviated](symbol/era/abbreviated.md) static variable is the default format.

For more information about formatting dates, see [FormatStyle](../formatstyle.md).

## See Also

### Specifying the Date Format

- [day(_:)](<day(__).md>) — Modifies the date format style to use the specified day format style.
- [dayOfYear(_:)](<dayofyear(__).md>) — Modifies the date format style to use the specified day of the year format style.
- [month(_:)](<month(__).md>) — Modifies the date format style to use the specified month format style.
- [quarter(_:)](<quarter(__).md>) — Modifies the date format style to use the specified quarter format style.
- [week(_:)](<week(__).md>) — Modifies the date format style to use the specified week format style.
- [weekday(_:)](<weekday(__).md>) — Modifies the date format style to use the specified weekday format style.
- [year(_:)](<year(__).md>) — Modifies the date format style to use the specified year format style.
- [DateStyle](datestyle.md) — Type that defines date styles varied in length or components included.
