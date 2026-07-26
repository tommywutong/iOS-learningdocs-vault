---
title: 'setVisibleDateComponents(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicalendarview/setvisibledatecomponents(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarview/setvisibledatecomponents(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarview/setvisibledatecomponents%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:85921d9b8627b65b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarView](../uicalendarview.md)

# setVisibleDateComponents(_:animated:)

<sub>Instance Method</sub>

Sets the date components that represent the date for the calendar view to make visible, with an option to animate the date change.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setVisibleDateComponents(_ dateComponents: DateComponents, animated: Bool)
```

## Parameters

- `dateComponents` — Date components that represent the date for the calendar view to display.

- `animated` — A Boolean value that indicates whether the calendar view animates the date change.

## Discussion

The date that `dateComponents` represents must be within the dates that [availableDateRange](availabledaterange.md) represents.

If `dateComponents.calendar` is `nil` or isn’t equal to [calendar](calendar.md), the calendar view uses [calendar](calendar.md), which may result in an invalid date from the date components.

## See Also

### Setting the visible date and range

- [visibleDateComponents](visibledatecomponents.md) — The date components that represent the visible date in the calendar view.
- [availableDateRange](availabledaterange.md) — The range of dates that the calendar view displays.
