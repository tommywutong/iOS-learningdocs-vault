---
title: day()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/intervalformatstyle/day()
source_url: 'https://developer.apple.com/documentation/foundation/date/intervalformatstyle/day()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/intervalformatstyle/day%28%29.json'
content_hash: 'sha256:23036311d5671df4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [IntervalFormatStyle](../intervalformatstyle.md)

# day()

<sub>Instance Method</sub>

Modifies the date interval format style to include the day.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func day() -> Date.IntervalFormatStyle
```

## Return Value

A date interval format style that includes the day.

## Discussion

Use a combination of modifier instance methods to customize the format of the date interval. The following example shows several combinations of year, month, and day components in the date interval:

```swift
if let today = Calendar.current.date(byAdding: .day, value: -140, to: Date()),
   let sevenDaysBeforeToday = Calendar.current.date(byAdding: .day, value: -7, to: today) {

    // Create a Range<Date>.
    let weekBefore = sevenDaysBeforeToday..<today

    print(weekBefore.formatted(.interval))
    print(weekBefore.formatted(.interval.day()))
    print(weekBefore.formatted(.interval.day().month(.defaultDigits)))
    print(weekBefore.formatted(.interval.day().month(.wide).year()))
}
// 2/5/21, 6:37 AM – 2/12/21, 6:37 AM
// 5 – 12
// 2/5 – 2/12
// February 5 – 12, 2021
```

## See Also

### Modifying Date Interval Format Styles

- [hour(_:)](<hour(__).md>) — Modifies the date interval format style to use the specified hour format style.
- [minute()](<minute().md>) — Modifies the date interval format style to include the minutes.
- [month(_:)](<month(__).md>) — Modifies the date interval format style to include the month.
- [second()](<second().md>) — Modifies the date interval format style to include the seconds.
- [weekday(_:)](<weekday(__).md>) — Modifies the date interval format style to include the specified weekday style.
- [year()](<year().md>) — Modifies the date interval format style to include the year.
