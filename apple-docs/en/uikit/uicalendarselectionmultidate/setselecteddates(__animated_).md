---
title: 'setSelectedDates(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicalendarselectionmultidate/setselecteddates(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarselectionmultidate/setselecteddates(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarselectionmultidate/setselecteddates%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:9c2bff3b9f35e93d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarSelectionMultiDate](../uicalendarselectionmultidate.md)

# setSelectedDates(_:animated:)

<sub>Instance Method</sub>

Updates the array of date component objects that represent selected dates in a calendar view, with an option to animate the change.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setSelectedDates(_ selectedDates: [DateComponents], animated: Bool)
```

## Parameters

- `selectedDates` — An array of date component objects that represent dates to select in a calendar view.

- `animated` — A Boolean value that indicates whether the calendar view should animate changing the selected dates.

## See Also

### Updating the selected dates

- [selectedDates](selecteddates.md) — An array of date component objects that represent selected dates in a calendar view.
