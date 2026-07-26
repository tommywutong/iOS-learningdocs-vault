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
doc_path: '/documentation/foundation/date/intervalformatstyle/weekday(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/intervalformatstyle/weekday(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/intervalformatstyle/weekday%28_%3A%29.json'
content_hash: 'sha256:3f06c05374ea8d65'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [IntervalFormatStyle](../intervalformatstyle.md)

# weekday(_:)

<sub>Instance Method</sub>

Modifies the date interval format style to include the specified weekday style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func weekday(_ format: Date.IntervalFormatStyle.Symbol.Weekday = .abbreviated) -> Date.IntervalFormatStyle
```

## Parameters

- `format` — The weekday format style to apply to the date interval format style.

## Return Value

A date interval format style that includes the specified weekday style.

## Discussion

Use a combination of modifier instance methods to customize the format of the date interval. The following example shows a combination date interval format styles that include the weekday:

```swift
if let today = Calendar.current.date(byAdding: .day, value: -140, to: Date()),
   let sevenDaysBeforeToday = Calendar.current.date(byAdding: .day, value: -7, to: today) {

    // Create a Range<Date>.
    let weekBefore = sevenDaysBeforeToday..<today

    print(weekBefore.formatted(.interval.day().month(.wide).year().weekday(.wide)))
    print(weekBefore.formatted(.interval.day().weekday(.abbreviated)))
    print(weekBefore.formatted(.interval.day().month(.wide).weekday(.narrow)))
}
// Friday, February 5 – Friday, February 12, 2021
// 5 Fri – 12 Fri
// F, February 5 – F, February 12
```

## See Also

### Modifying Date Interval Format Styles

- [day()](<day().md>) — Modifies the date interval format style to include the day.
- [hour(_:)](<hour(__).md>) — Modifies the date interval format style to use the specified hour format style.
- [minute()](<minute().md>) — Modifies the date interval format style to include the minutes.
- [month(_:)](<month(__).md>) — Modifies the date interval format style to include the month.
- [second()](<second().md>) — Modifies the date interval format style to include the seconds.
- [year()](<year().md>) — Modifies the date interval format style to include the year.
