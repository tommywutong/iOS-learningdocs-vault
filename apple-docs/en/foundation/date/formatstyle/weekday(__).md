---
title: 'weekday(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/weekday(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/weekday(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/weekday%28_%3A%29.json'
content_hash: 'sha256:74112f58256f1ad2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [FormatStyle](../formatstyle.md)

# weekday(_:)

<sub>Instance Method</sub>

Modifies the date format style to use the specified weekday format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func weekday(_ format: Date.FormatStyle.Symbol.Weekday = .abbreviated) -> Date.FormatStyle
```

## Parameters

- `format` — The weekday format style applied to the date format style.

## Return Value

A date format style modified to include the specified week format style.

## Discussion

Possible values of [Weekday](symbol/weekday.md) include [abbreviated](symbol/weekday/abbreviated.md), [narrow](symbol/weekday/narrow.md), [oneDigit](symbol/weekday/onedigit.md), [short](symbol/weekday/short.md), [twoDigits](symbol/weekday/twodigits.md), and [wide](symbol/weekday/wide.md).

## See Also

### Specifying the Date Format

- [day(_:)](<day(__).md>) — Modifies the date format style to use the specified day format style.
- [dayOfYear(_:)](<dayofyear(__).md>) — Modifies the date format style to use the specified day of the year format style.
- [era(_:)](<era(__).md>) — Modifies the date format style to use the specified era format style.
- [month(_:)](<month(__).md>) — Modifies the date format style to use the specified month format style.
- [quarter(_:)](<quarter(__).md>) — Modifies the date format style to use the specified quarter format style.
- [week(_:)](<week(__).md>) — Modifies the date format style to use the specified week format style.
- [year(_:)](<year(__).md>) — Modifies the date format style to use the specified year format style.
- [DateStyle](datestyle.md) — Type that defines date styles varied in length or components included.
