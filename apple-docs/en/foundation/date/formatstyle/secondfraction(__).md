---
title: 'secondFraction(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/secondfraction(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/secondfraction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/secondfraction%28_%3A%29.json'
content_hash: 'sha256:f059e9f0f7bef4ce'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [FormatStyle](../formatstyle.md)

# secondFraction(_:)

<sub>Instance Method</sub>

Modifies the date format style to use the specified second fraction format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func secondFraction(_ format: Date.FormatStyle.Symbol.SecondFraction) -> Date.FormatStyle
```

## Parameters

- `format` — The second fraction format style applied to the date format style.

## Return Value

A date format style modified to include the specified second fraction style.

## Discussion

Static methods that return [SecondFraction](symbol/secondfraction.md) objects include [fractional(_:)](<symbol/secondfraction/fractional(__).md>) and [milliseconds(_:)](<symbol/secondfraction/milliseconds(__).md>).

This example shows a variety of [SecondFraction](symbol/secondfraction.md) format styles applied to a date:

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:05:41.827 PM
meetingDate.formatted(Date.FormatStyle().secondFraction(.fractional(3))) // 827
meetingDate.formatted(Date.FormatStyle().secondFraction(.fractional(1))) // 8
meetingDate.formatted(Date.FormatStyle().secondFraction(.milliseconds(4))) // 11122827
```

For more information about formatting dates, see [FormatStyle](../formatstyle.md).

## See Also

### Specifying the Time Format

- [hour(_:)](<hour(__).md>) — Modifies the date format style to use the specified hour format style.
- [minute(_:)](<minute(__).md>) — Modifies the date format style to use the specified minute format style.
- [second(_:)](<second(__).md>) — Modifies the date format style to use the specified second format style.
- [timeZone(_:)](<timezone(__).md>) — Modifies the date format style to use the specified time zone format style.
- [TimeStyle](timestyle.md) — Type that defines time styles varied in length or components included.
