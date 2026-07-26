---
title: selectedWeekOfYear
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicalendarselectionweekofyear/selectedweekofyear
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarselectionweekofyear/selectedweekofyear'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarselectionweekofyear/selectedweekofyear.json'
content_hash: 'sha256:96f62484839ca274'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarSelectionWeekOfYear](../uicalendarselectionweekofyear.md)

# selectedWeekOfYear

<sub>Instance Property</sub>

The current week-of-year selection in the calendar view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var selectedWeekOfYear: DateComponents? { get set }
```

## Discussion

The components need to include `[.yearForWeekOfYear, .weekOfYear]`.

## See Also

### Updating the selected week

- [- setSelectedWeekOfYear:animated:](<setselected(__animated_).md>) — Updates the date component object that represents a selected week in a calendar view, with an option to animate the change.
