---
title: 'multiDateSelection(_:didSelectDate:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicalendarselectionmultidatedelegate/multidateselection(_:didselectdate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarselectionmultidatedelegate/multidateselection(_:didselectdate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarselectionmultidatedelegate/multidateselection%28_%3Adidselectdate%3A%29.json'
content_hash: 'sha256:b4cf1e831c138621'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarSelectionMultiDateDelegate](../uicalendarselectionmultidatedelegate.md)

# multiDateSelection(_:didSelectDate:)

<sub>Instance Method</sub>

Informs the delegate that a user selected a date represented by date components.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func multiDateSelection(_ selection: UICalendarSelectionMultiDate, didSelectDate dateComponents: DateComponents)
```

## Parameters

- `selection` — An object that tracks one or more dates that a user selects from a calendar view.

- `dateComponents` — Date components that represent a date the user selected.

## See Also

### Changing selected dates

- [- multiDateSelection:didDeselectDate:](<multidateselection(__diddeselectdate_).md>) — Informs the delegate that a user deselected a date represented by date components.
