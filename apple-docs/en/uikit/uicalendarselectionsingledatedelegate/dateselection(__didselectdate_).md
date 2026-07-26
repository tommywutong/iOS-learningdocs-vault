---
title: 'dateSelection(_:didSelectDate:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicalendarselectionsingledatedelegate/dateselection(_:didselectdate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarselectionsingledatedelegate/dateselection(_:didselectdate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarselectionsingledatedelegate/dateselection%28_%3Adidselectdate%3A%29.json'
content_hash: 'sha256:44985d83a9bd9f57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarSelectionSingleDateDelegate](../uicalendarselectionsingledatedelegate.md)

# dateSelection(_:didSelectDate:)

<sub>Instance Method</sub>

Informs the delegate that a user selected a date represented by date components.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func dateSelection(_ selection: UICalendarSelectionSingleDate, didSelectDate dateComponents: DateComponents?)
```

## Parameters

- `selection` — An object that tracks a date that a user selects from a calendar view.

- `dateComponents` — Date components that represent a date the user selected, or `nil` if the user deselected a date.
