---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicalendarselectionweekofyear/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarselectionweekofyear/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarselectionweekofyear/delegate.json'
content_hash: 'sha256:e689bdb34aa9ae1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarSelectionWeekOfYear](../uicalendarselectionweekofyear.md)

# delegate

<sub>Instance Property</sub>

A delegate object that a calendar view asks about selectable weeks and informs of changes to the week selection.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UICalendarSelectionWeekOfYearDelegate)? { get }
```

## See Also

### Setting the selection delegate

- [UICalendarSelectionWeekOfYearDelegate](../uicalendarselectionweekofyeardelegate.md) — A set of methods you implement to provide selectable weeks and handle changes to the week selection in a calendar view.
