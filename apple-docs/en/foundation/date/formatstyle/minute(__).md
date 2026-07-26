---
title: 'minute(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/minute(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/minute(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/minute%28_%3A%29.json'
content_hash: 'sha256:cacb06806395f47a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [FormatStyle](../formatstyle.md)

# minute(_:)

<sub>Instance Method</sub>

Modifies the date format style to use the specified minute format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func minute(_ format: Date.FormatStyle.Symbol.Minute = .defaultDigits) -> Date.FormatStyle
```

## Parameters

- `format` — The minute format style applied to the date format style.

## Return Value

A date format style modified to include the specified minute style.

## Discussion

Values of [Minute](symbol/minute.md) are [defaultDigits](symbol/minute/defaultdigits.md) and [twoDigits](symbol/minute/twodigits.md).

This example shows a variety of [Minute](symbol/minute.md) format styles applied to a date:

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:05 PM
meetingDate.formatted(Date.FormatStyle().minute(.defaultDigits)) // 5
meetingDate.formatted(Date.FormatStyle().minute(.twoDigits)) // 05
meetingDate.formatted(Date.FormatStyle().minute()) // 5
```

If you don’t provide a format, the [defaultDigits](symbol/minute/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see [FormatStyle](../formatstyle.md).

## See Also

### Specifying the Time Format

- [hour(_:)](<hour(__).md>) — Modifies the date format style to use the specified hour format style.
- [second(_:)](<second(__).md>) — Modifies the date format style to use the specified second format style.
- [secondFraction(_:)](<secondfraction(__).md>) — Modifies the date format style to use the specified second fraction format style.
- [timeZone(_:)](<timezone(__).md>) — Modifies the date format style to use the specified time zone format style.
- [TimeStyle](timestyle.md) — Type that defines time styles varied in length or components included.
