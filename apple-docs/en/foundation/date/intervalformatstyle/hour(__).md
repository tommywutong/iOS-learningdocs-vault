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
doc_path: '/documentation/foundation/date/intervalformatstyle/hour(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/intervalformatstyle/hour(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/intervalformatstyle/hour%28_%3A%29.json'
content_hash: 'sha256:79b3616359a7bae5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [IntervalFormatStyle](../intervalformatstyle.md)

# hour(_:)

<sub>Instance Method</sub>

Modifies the date interval format style to use the specified hour format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hour(_ format: Date.IntervalFormatStyle.Symbol.Hour = .defaultDigits(amPM: .abbreviated)) -> Date.IntervalFormatStyle
```

## Parameters

- `format` — The hour format style to apply to the date interval format style.

## Return Value

A date interval format style that includes the specified hour style.

## Discussion

The values of `Date.FormatStyle.Symbol.Hour` are `defaultDigitsNoAMPM` and `twoDigitsNoAMPM`.

The static methods that return [Hour](../formatstyle/symbol/hour.md) objects include [conversationalDefaultDigits(amPM:)](<../formatstyle/symbol/hour/conversationaldefaultdigits(ampm_).md>), [conversationalTwoDigits(amPM:)](<../formatstyle/symbol/hour/conversationaltwodigits(ampm_).md>), and [defaultDigits(amPM:)](<../formatstyle/symbol/hour/defaultdigits(ampm_).md>).

This example shows a variety of [Hour](../formatstyle/symbol/hour.md) format styles for a date interval:

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
- [minute()](<minute().md>) — Modifies the date interval format style to include the minutes.
- [month(_:)](<month(__).md>) — Modifies the date interval format style to include the month.
- [second()](<second().md>) — Modifies the date interval format style to include the seconds.
- [weekday(_:)](<weekday(__).md>) — Modifies the date interval format style to include the specified weekday style.
- [year()](<year().md>) — Modifies the date interval format style to include the year.
