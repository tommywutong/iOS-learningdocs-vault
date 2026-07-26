---
title: 'setSelected(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicalendarselectionsingledate/setselected(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarselectionsingledate/setselected(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarselectionsingledate/setselected%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:2c83ee79f0b62b2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarSelectionSingleDate](../uicalendarselectionsingledate.md)

# setSelected(_:animated:)

<sub>Instance Method</sub>

Updates the date component object that represents a selected date in a calendar view, with an option to animate the change.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setSelected(_ selectedDate: DateComponents?, animated: Bool)
```

## Parameters

- `selectedDate` — A date component object that represents a date to select in a calendar view.

- `animated` — A Boolean value that indicates whether the calendar view should animate changing the selected date.

## See Also

### Updating the selected date

- [selectedDate](selecteddate.md) — A date component object that represents a selected date in a calendar view.
