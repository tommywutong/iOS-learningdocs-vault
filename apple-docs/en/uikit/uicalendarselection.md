---
title: UICalendarSelection
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicalendarselection
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarselection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarselection.json'
content_hash: 'sha256:51766d0325c5d153'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICalendarSelection

<sub>Class</sub>

A base object that tracks one or more dates a user selects from a calendar view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UICalendarSelection
```

## Overview

Don’t use this object directly in your calendar view to track date selection. Use the subclass [UICalendarSelectionSingleDate](uicalendarselectionsingledate.md) to track a single date selection, or [UICalendarSelectionMultiDate](uicalendarselectionmultidate.md) to track multiple date selections.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UICalendarSelectionMultiDate](uicalendarselectionmultidate.md), [UICalendarSelectionSingleDate](uicalendarselectionsingledate.md), [UICalendarSelectionWeekOfYear](uicalendarselectionweekofyear.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Updating selectable dates

- [- updateSelectableDates](<uicalendarselection/updateselectabledates().md>) — Informs the calendar view to update the view for selectable dates.

## See Also

### Handling date selections

- [selectionBehavior](uicalendarview/selectionbehavior.md) — The current date selection method of the calendar view.
- [UICalendarSelectionSingleDate](uicalendarselectionsingledate.md) — An object that tracks a date the user selects from a calendar view.
- [UICalendarSelectionMultiDate](uicalendarselectionmultidate.md) — An object that tracks multiple dates the user selects from a calendar view.
- [UICalendarSelectionWeekOfYear](uicalendarselectionweekofyear.md) — An object that tracks a specific week a person selects from a calendar view.
