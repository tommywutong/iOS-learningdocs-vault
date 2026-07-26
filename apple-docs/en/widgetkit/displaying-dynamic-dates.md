---
title: Displaying dynamic dates in widgets
framework: WidgetKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/displaying-dynamic-dates
source_url: 'https://developer.apple.com/documentation/widgetkit/displaying-dynamic-dates'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/displaying-dynamic-dates.json'
content_hash: 'sha256:4c93c0566b3e0671'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md) · [SwiftUI views for widgets](swiftui-views.md)

# Displaying dynamic dates in widgets

<sub>Article</sub>

Show up-to-date, time-based information in your widget even when it isn’t running.

## Overview

Because your widget extension isn’t always running, you can’t directly update your widget’s content. Instead, WidgetKit renders your widget’s view on your behalf and displays the result. However, some SwiftUI views let you display content that continues updating while your widget is visible.

Using a [Text](../swiftui/text.md) view in your widget, you can display dates and times that stay up to date onscreen. The following examples show the combinations available.

To display a relative time that updates automatically:

```swift
let components = DateComponents(minute: 11, second: 14)
let futureDate = Calendar.current.date(byAdding: components, to: Date())!

Text(futureDate, style: .relative)
// Displays:
// 11 min, 14 sec

Text(futureDate, style: .offset)
// Displays:
// -11 minutes
```

Using the [relative](../swiftui/text/datestyle/relative.md) style shows the absolute difference between the current date and time and the date specified, regardless of whether the date is in the future or the past. The [offset](../swiftui/text/datestyle/offset.md) style shows the difference between the current date and time and the date specified, indicating dates in the future with a minus sign (`-`) prefix and dates in the past with a plus sign (`+`) prefix.

To display a timer that continues updating automatically:

```swift
let components = DateComponents(minute: 15)
let futureDate = Calendar.current.date(byAdding: components, to: Date())!

Text(futureDate, style: .timer)
// Displays:
// 15:00
```

For dates in the future, the [timer](../swiftui/text/datestyle/timer.md) style counts down until the current time reaches the specified date and time, and counts up when the date passes.

To display an absolute date or time:

```swift
// Absolute Date or Time
let components = DateComponents(year: 2020, month: 4, day: 1, hour: 9, minute: 41)
let aprilFirstDate = Calendar.current(components)!

Text(aprilFirstDate, style: .date)
Text("Date: \(aprilFirstDate, style: .date)")
Text("Time: \(aprilFirstDate, style: .time)")

// Displays:
// April 1, 2020
// Date: April 1, 2020
// Time: 9:41AM
```

And finally, to display a time interval between two dates:

```swift
let startComponents = DateComponents(hour: 9, minute: 30)
let startDate = Calendar.current.date(from: startComponents)!

let endComponents = DateComponents(hour: 14, minute: 45)
let endDate = Calendar.current.date(from: endComponents)!

Text(startDate ... endDate)
Text("The meeting will take place: \(startDate ... endDate)")

// Displays:
// 9:30AM-2:45PM
// The meeting will take place: 9:30AM-2:45PM
```

## See Also

### Displaying text

- [Text](../swiftui/text.md) — A view that displays one or more lines of read-only text.
