---
title: 'multiDateSelection(_:canDeselectDate:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicalendarselectionmultidatedelegate/multidateselection(_:candeselectdate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarselectionmultidatedelegate/multidateselection(_:candeselectdate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarselectionmultidatedelegate/multidateselection%28_%3Acandeselectdate%3A%29.json'
content_hash: 'sha256:1770d6be9ac0225c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarSelectionMultiDateDelegate](../uicalendarselectionmultidatedelegate.md)

# multiDateSelection(_:canDeselectDate:)

<sub>Instance Method</sub>

Returns whether a user can deselect a date represented by date components in the calendar view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func multiDateSelection(_ selection: UICalendarSelectionMultiDate, canDeselectDate dateComponents: DateComponents) -> Bool
```

## Parameters

- `selection` — An object that tracks one or more dates that a user selects from a calendar view.

- `dateComponents` — Date components that represent a date to deselect.

## Return Value

A Boolean value that indicates whether the calendar view can deselect the date you provide.

## See Also

### Getting selectable dates

- [- multiDateSelection:canSelectDate:](<multidateselection(__canselectdate_).md>) — Returns whether a user can select a date represented by date components in the calendar view.
