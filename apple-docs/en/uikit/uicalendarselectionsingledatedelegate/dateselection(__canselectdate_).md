---
title: 'dateSelection(_:canSelectDate:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicalendarselectionsingledatedelegate/dateselection(_:canselectdate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarselectionsingledatedelegate/dateselection(_:canselectdate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarselectionsingledatedelegate/dateselection%28_%3Acanselectdate%3A%29.json'
content_hash: 'sha256:13e5db95b28162a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarSelectionSingleDateDelegate](../uicalendarselectionsingledatedelegate.md)

# dateSelection(_:canSelectDate:)

<sub>Instance Method</sub>

Returns whether a user can select a date represented by date components in the calendar view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func dateSelection(_ selection: UICalendarSelectionSingleDate, canSelectDate dateComponents: DateComponents?) -> Bool
```

## Parameters

- `selection` — An object that tracks a date that a user selects from a calendar view.

- `dateComponents` — Date components that represent a date to select.

## Return Value

A Boolean value that indicates whether the calendar view can select the date you provide.

## Discussion

The calendar view displays nonselectable dates as disabled.
