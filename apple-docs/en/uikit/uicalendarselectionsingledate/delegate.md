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
doc_path: /documentation/uikit/uicalendarselectionsingledate/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarselectionsingledate/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarselectionsingledate/delegate.json'
content_hash: 'sha256:e3273404ee9297ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarSelectionSingleDate](../uicalendarselectionsingledate.md)

# delegate

<sub>Instance Property</sub>

A delegate object that a calendar view asks about selectable dates and informs of changes to the selection of a single date.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UICalendarSelectionSingleDateDelegate)? { get }
```

## See Also

### Setting the selection delegate

- [UICalendarSelectionSingleDateDelegate](../uicalendarselectionsingledatedelegate.md) — A set of methods you implement to provide selectable dates and handle changes to the selection of a single date.
