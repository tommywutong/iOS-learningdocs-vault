---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicalendarselectionmultidate/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarselectionmultidate/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarselectionmultidate/delegate.json'
content_hash: 'sha256:4b463100154d1217'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarSelectionMultiDate](../uicalendarselectionmultidate.md)

# delegate

<sub>Instance Property</sub>

A delegate object that a calendar view asks for selectable dates and informs of changes to the selection of multiple dates.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UICalendarSelectionMultiDateDelegate)? { get }
```

## See Also

### Setting the selection delegate

- [UICalendarSelectionMultiDateDelegate](../uicalendarselectionmultidatedelegate.md) — A set of methods you implement to provide selectable dates and handle changes to the selection of multiple dates.
