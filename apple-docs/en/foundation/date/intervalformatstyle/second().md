---
title: second()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/intervalformatstyle/second()
source_url: 'https://developer.apple.com/documentation/foundation/date/intervalformatstyle/second()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/intervalformatstyle/second%28%29.json'
content_hash: 'sha256:314f27d3d2bca094'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [IntervalFormatStyle](../intervalformatstyle.md)

# second()

<sub>Instance Method</sub>

Modifies the date interval format style to include the seconds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func second() -> Date.IntervalFormatStyle
```

## Return Value

A date interval format style that includes the seconds.

## Discussion

This example shows a combination of date interval format styles that include the hour, minutes, and seconds:

```swift
if let today = Calendar.current.date(byAdding: .day, value: -140, to: Date()),
   let sevenDaysBeforeToday = Calendar.current.date(byAdding: .day, value: -7, to: today) {

    // Create a Range<Date>.
    let weekBefore = sevenDaysBeforeToday..<today

    print(weekBefore.formatted(.interval.minute()))
    print(weekBefore.formatted(.interval.day().minute().hour().second()))
}
// 2/5/2021, 17 – 2/12/2021, 17
// 5, 8:17:19 AM – 12, 8:17:19 AM
```

## See Also

### Modifying Date Interval Format Styles

- [day()](<day().md>) — Modifies the date interval format style to include the day.
- [hour(_:)](<hour(__).md>) — Modifies the date interval format style to use the specified hour format style.
- [minute()](<minute().md>) — Modifies the date interval format style to include the minutes.
- [month(_:)](<month(__).md>) — Modifies the date interval format style to include the month.
- [weekday(_:)](<weekday(__).md>) — Modifies the date interval format style to include the specified weekday style.
- [year()](<year().md>) — Modifies the date interval format style to include the year.
