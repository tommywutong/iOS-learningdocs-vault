---
title: 'multiDateSelection(_:canSelectDate:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicalendarselectionmultidatedelegate/multidateselection(_:canselectdate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarselectionmultidatedelegate/multidateselection(_:canselectdate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarselectionmultidatedelegate/multidateselection%28_%3Acanselectdate%3A%29.json'
content_hash: 'sha256:06a8c8fed1d37394'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarSelectionMultiDateDelegate](../uicalendarselectionmultidatedelegate.md)

# multiDateSelection(_:canSelectDate:)

<sub>Instance Method</sub>

Returns whether a user can select a date represented by date components in the calendar view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func multiDateSelection(_ selection: UICalendarSelectionMultiDate, canSelectDate dateComponents: DateComponents) -> Bool
```

## Parameters

- `selection` — An object that tracks multiple dates that a user selects from a calendar view.

- `dateComponents` — Date components that represent a date to select.

## Return Value

A Boolean value that indicates whether the calendar view can select the date you provide.

## Discussion

The calendar view displays non-selectable dates as disabled.

## See Also

### Getting selectable dates

- [- multiDateSelection:canDeselectDate:](<multidateselection(__candeselectdate_).md>) — Returns whether a user can deselect a date represented by date components in the calendar view.
