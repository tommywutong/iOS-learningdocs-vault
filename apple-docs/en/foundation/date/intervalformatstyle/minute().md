---
title: minute()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/intervalformatstyle/minute()
source_url: 'https://developer.apple.com/documentation/foundation/date/intervalformatstyle/minute()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/intervalformatstyle/minute%28%29.json'
content_hash: 'sha256:6501f3bb4dd26d65'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [IntervalFormatStyle](../intervalformatstyle.md)

# minute()

<sub>Instance Method</sub>

Modifies the date interval format style to include the minutes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func minute() -> Date.IntervalFormatStyle
```

## Return Value

A date interval format style that includes the minutes.

## Discussion

This example shows a combination of date interval format styles that includes the hour and minutes:

```swift
if let today = Calendar.current.date(byAdding: .day, value: -140, to: Date()),
   let sevenDaysBeforeToday = Calendar.current.date(byAdding: .day, value: -7, to: today) {

    // Create a Range<Date>.
    let weekBefore = sevenDaysBeforeToday..<today

    print(weekBefore.formatted(.interval.minute()))
    print(weekBefore.formatted(.interval.day().minute().hour()))
    print(weekBefore.formatted(.interval.day().month().minute().hour(.defaultDigitsNoAMPM)))
    print(weekBefore.formatted(.interval.day().month().minute().hour(.conversationalDefaultDigits(amPM: .wide))))
    print(weekBefore.formatted(.interval.day().month().minute().hour(.conversationalDefaultDigits(amPM: .narrow))))
}
// 2/5/2021, 9 – 2/12/2021, 9
// 5, 7:09 AM – 12, 7:09 AM
// Feb 5, 07:09 – Feb 12, 07:09
// Feb 5, 7:09 AM – Feb 12, 7:09 AM
// Feb 5, 7:09 a – Feb 12, 7:09 a

```

## See Also

### Modifying Date Interval Format Styles

- [day()](<day().md>) — Modifies the date interval format style to include the day.
- [hour(_:)](<hour(__).md>) — Modifies the date interval format style to use the specified hour format style.
- [month(_:)](<month(__).md>) — Modifies the date interval format style to include the month.
- [second()](<second().md>) — Modifies the date interval format style to include the seconds.
- [weekday(_:)](<weekday(__).md>) — Modifies the date interval format style to include the specified weekday style.
- [year()](<year().md>) — Modifies the date interval format style to include the year.
