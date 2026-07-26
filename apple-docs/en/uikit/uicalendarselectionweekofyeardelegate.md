---
title: UICalendarSelectionWeekOfYearDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicalendarselectionweekofyeardelegate
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarselectionweekofyeardelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarselectionweekofyeardelegate.json'
content_hash: 'sha256:8c4fcda711f1451f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICalendarSelectionWeekOfYearDelegate

<sub>Protocol</sub>

A set of methods you implement to provide selectable weeks and handle changes to the week selection in a calendar view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UICalendarSelectionWeekOfYearDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Handling week-of-year selections

- [- weekOfYearSelection:canSelectWeekOfYear:](<uicalendarselectionweekofyeardelegate/week(ofyearselection_canselectweekofyear_).md>) — Determines if a week is available for selection.
- [- weekOfYearSelection:didSelectWeekOfYear:](<uicalendarselectionweekofyeardelegate/week(ofyearselection_didselectweekofyear_).md>) — Notifies the delegate after a person selects a week in the calendar view.

## See Also

### Setting the selection delegate

- [delegate](uicalendarselectionweekofyear/delegate.md) — A delegate object that a calendar view asks about selectable weeks and informs of changes to the week selection.
