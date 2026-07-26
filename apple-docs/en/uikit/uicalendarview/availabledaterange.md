---
title: availableDateRange
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicalendarview/availabledaterange
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarview/availabledaterange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarview/availabledaterange.json'
content_hash: 'sha256:0fc52f99f78f58b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarView](../uicalendarview.md)

# availableDateRange

<sub>Instance Property</sub>

The range of dates that the calendar view displays.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var availableDateRange: DateInterval { get set }
```

## Discussion

Set `availableDateRange` to restrict the earliest or latest dates that the calendar view displays. The default date range starts with [distantPast](../../foundation/date/distantpast.md) (Swift) or [distantPast](../../foundation/nsdate/distantpast.md) (Objective-C), and ends with [distantFuture](../../foundation/date/distantfuture.md) (Swift) or [distantFuture](../../foundation/nsdate/distantfuture.md) (Objective-C).

## See Also

### Setting the visible date and range

- [visibleDateComponents](visibledatecomponents.md) — The date components that represent the visible date in the calendar view.
- [- setVisibleDateComponents:animated:](<setvisibledatecomponents(__animated_).md>) — Sets the date components that represent the date for the calendar view to make visible, with an option to animate the date change.
