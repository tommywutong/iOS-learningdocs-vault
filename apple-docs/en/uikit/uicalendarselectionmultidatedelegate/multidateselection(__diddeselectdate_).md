---
title: 'multiDateSelection(_:didDeselectDate:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicalendarselectionmultidatedelegate/multidateselection(_:diddeselectdate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarselectionmultidatedelegate/multidateselection(_:diddeselectdate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarselectionmultidatedelegate/multidateselection%28_%3Adiddeselectdate%3A%29.json'
content_hash: 'sha256:f5768802e632c933'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarSelectionMultiDateDelegate](../uicalendarselectionmultidatedelegate.md)

# multiDateSelection(_:didDeselectDate:)

<sub>Instance Method</sub>

Informs the delegate that a user deselected a date represented by date components.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func multiDateSelection(_ selection: UICalendarSelectionMultiDate, didDeselectDate dateComponents: DateComponents)
```

## Parameters

- `selection` — An object that tracks multiple dates that a user selects from a calendar view.

- `dateComponents` — Date components that represent a date the user deselected.

## See Also

### Changing selected dates

- [- multiDateSelection:didSelectDate:](<multidateselection(__didselectdate_).md>) — Informs the delegate that a user selected a date represented by date components.
