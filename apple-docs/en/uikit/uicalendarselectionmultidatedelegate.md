---
title: UICalendarSelectionMultiDateDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicalendarselectionmultidatedelegate
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarselectionmultidatedelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarselectionmultidatedelegate.json'
content_hash: 'sha256:837d9feff1119eb2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICalendarSelectionMultiDateDelegate

<sub>Protocol</sub>

A set of methods you implement to provide selectable dates and handle changes to the selection of multiple dates.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UICalendarSelectionMultiDateDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting selectable dates

- [- multiDateSelection:canSelectDate:](<uicalendarselectionmultidatedelegate/multidateselection(__canselectdate_).md>) — Returns whether a user can select a date represented by date components in the calendar view.
- [- multiDateSelection:canDeselectDate:](<uicalendarselectionmultidatedelegate/multidateselection(__candeselectdate_).md>) — Returns whether a user can deselect a date represented by date components in the calendar view.

### Changing selected dates

- [- multiDateSelection:didSelectDate:](<uicalendarselectionmultidatedelegate/multidateselection(__didselectdate_).md>) — Informs the delegate that a user selected a date represented by date components.
- [- multiDateSelection:didDeselectDate:](<uicalendarselectionmultidatedelegate/multidateselection(__diddeselectdate_).md>) — Informs the delegate that a user deselected a date represented by date components.

## See Also

### Setting the selection delegate

- [delegate](uicalendarselectionmultidate/delegate.md) — A delegate object that a calendar view asks for selectable dates and informs of changes to the selection of multiple dates.
