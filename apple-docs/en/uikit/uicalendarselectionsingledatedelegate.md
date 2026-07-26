---
title: UICalendarSelectionSingleDateDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicalendarselectionsingledatedelegate
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarselectionsingledatedelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarselectionsingledatedelegate.json'
content_hash: 'sha256:205a6fc679b0d66e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICalendarSelectionSingleDateDelegate

<sub>Protocol</sub>

A set of methods you implement to provide selectable dates and handle changes to the selection of a single date.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UICalendarSelectionSingleDateDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting selectable dates

- [- dateSelection:canSelectDate:](<uicalendarselectionsingledatedelegate/dateselection(__canselectdate_).md>) — Returns whether a user can select a date represented by date components in the calendar view.

### Changing the selected date

- [- dateSelection:didSelectDate:](<uicalendarselectionsingledatedelegate/dateselection(__didselectdate_).md>) — Informs the delegate that a user selected a date represented by date components.

## See Also

### Setting the selection delegate

- [delegate](uicalendarselectionsingledate/delegate.md) — A delegate object that a calendar view asks about selectable dates and informs of changes to the selection of a single date.
