---
title: 'week(ofYearSelection:canSelectWeekOfYear:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicalendarselectionweekofyeardelegate/week(ofyearselection:canselectweekofyear:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarselectionweekofyeardelegate/week(ofyearselection:canselectweekofyear:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarselectionweekofyeardelegate/week%28ofyearselection%3Acanselectweekofyear%3A%29.json'
content_hash: 'sha256:f3617ba0773e3346'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarSelectionWeekOfYearDelegate](../uicalendarselectionweekofyeardelegate.md)

# week(ofYearSelection:canSelectWeekOfYear:)

<sub>Instance Method</sub>

Determines if a week is available for selection.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func week(ofYearSelection selection: UICalendarSelectionWeekOfYear, canSelectWeekOfYear weekOfYearComponents: DateComponents?) -> Bool
```

## See Also

### Handling week-of-year selections

- [- weekOfYearSelection:didSelectWeekOfYear:](<week(ofyearselection_didselectweekofyear_).md>) — Notifies the delegate after a person selects a week in the calendar view.
