---
title: 'hour(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/hour(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/hour(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/hour%28_%3A%29.json'
content_hash: 'sha256:5cf490225edff2da'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [FormatStyle](../formatstyle.md)

# hour(_:)

<sub>Instance Method</sub>

Modifies the date format style to use the specified hour format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hour(_ format: Date.FormatStyle.Symbol.Hour = .defaultDigits(amPM: .abbreviated)) -> Date.FormatStyle
```

## Parameters

- `format` — The hour format style applied to the date format style.

## Return Value

A date format style modified to include the specified hour style.

## Discussion

Values of [Hour](symbol/hour.md) are [defaultDigitsNoAMPM](symbol/hour/defaultdigitsnoampm.md) and [twoDigitsNoAMPM](symbol/hour/twodigitsnoampm.md).

Static methods that return [Hour](symbol/hour.md) objects include [conversationalDefaultDigits(amPM:)](<symbol/hour/conversationaldefaultdigits(ampm_).md>), [conversationalTwoDigits(amPM:)](<symbol/hour/conversationaltwodigits(ampm_).md>), [defaultDigits(amPM:)](<symbol/hour/defaultdigits(ampm_).md>), and [twoDigitsNoAMPM](symbol/hour/twodigitsnoampm.md).

This example shows a variety of [Hour](symbol/hour.md) format styles applied to a date:

```swift
let meetingDate = Date() // Feb 9, 2021 at 7:00 PM
meetingDate.formatted(Date.FormatStyle().hour(.defaultDigitsNoAMPM)) 
// 7

meetingDate.formatted(Date.FormatStyle().hour(.twoDigitsNoAMPM)) 
// 07

meetingDate.formatted(Date.FormatStyle().hour(.defaultDigits(amPM: .narrow))) 
// 7p

meetingDate.formatted(Date.FormatStyle().hour(.twoDigits(amPM: .abbreviated))
// 07 PM

meetingDate.formatted(Date.FormatStyle().hour(.conversationalDefaultDigits(amPM: .wide))
// 7 P.M.
```

If you don’t provide a format, the [defaultDigits](symbol/minute/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see [FormatStyle](../formatstyle.md).

## See Also

### Specifying the Time Format

- [minute(_:)](<minute(__).md>) — Modifies the date format style to use the specified minute format style.
- [second(_:)](<second(__).md>) — Modifies the date format style to use the specified second format style.
- [secondFraction(_:)](<secondfraction(__).md>) — Modifies the date format style to use the specified second fraction format style.
- [timeZone(_:)](<timezone(__).md>) — Modifies the date format style to use the specified time zone format style.
- [TimeStyle](timestyle.md) — Type that defines time styles varied in length or components included.
