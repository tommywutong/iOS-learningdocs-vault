---
title: visibleDateComponents
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicalendarview/visibledatecomponents
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarview/visibledatecomponents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarview/visibledatecomponents.json'
content_hash: 'sha256:b140d8c0d242c9ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarView](../uicalendarview.md)

# visibleDateComponents

<sub>Instance Property</sub>

The date components that represent the visible date in the calendar view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var visibleDateComponents: DateComponents { get set }
```

## Discussion

If `visibleDateComponents.calendar` is `nil` or isn’t equal to [calendar](calendar.md), the calendar view uses [calendar](calendar.md), which may result in an invalid date from the date components.

## See Also

### Setting the visible date and range

- [- setVisibleDateComponents:animated:](<setvisibledatecomponents(__animated_).md>) — Sets the date components that represent the date for the calendar view to make visible, with an option to animate the date change.
- [availableDateRange](availabledaterange.md) — The range of dates that the calendar view displays.
