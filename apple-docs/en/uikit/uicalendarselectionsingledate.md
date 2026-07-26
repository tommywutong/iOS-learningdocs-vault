---
title: UICalendarSelectionSingleDate
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicalendarselectionsingledate
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarselectionsingledate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarselectionsingledate.json'
content_hash: 'sha256:76a33d244e66888c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICalendarSelectionSingleDate

<sub>Class</sub>

An object that tracks a date the user selects from a calendar view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UICalendarSelectionSingleDate
```

## Relationships

- **Inherits From**: [UICalendarSelection](uicalendarselection.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a single date selection

- [- initWithDelegate:](<uicalendarselectionsingledate/init(delegate_).md>) — Creates an object that tracks a date a user selects from a calendar view, with an optional delegate to manage selectable dates and selection changes.

### Setting the selection delegate

- [delegate](uicalendarselectionsingledate/delegate.md) — A delegate object that a calendar view asks about selectable dates and informs of changes to the selection of a single date.
- [UICalendarSelectionSingleDateDelegate](uicalendarselectionsingledatedelegate.md) — A set of methods you implement to provide selectable dates and handle changes to the selection of a single date.

### Updating the selected date

- [selectedDate](uicalendarselectionsingledate/selecteddate.md) — A date component object that represents a selected date in a calendar view.
- [- setSelectedDate:animated:](<uicalendarselectionsingledate/setselected(__animated_).md>) — Updates the date component object that represents a selected date in a calendar view, with an option to animate the change.

## See Also

### Handling date selections

- [selectionBehavior](uicalendarview/selectionbehavior.md) — The current date selection method of the calendar view.
- [UICalendarSelectionMultiDate](uicalendarselectionmultidate.md) — An object that tracks multiple dates the user selects from a calendar view.
- [UICalendarSelectionWeekOfYear](uicalendarselectionweekofyear.md) — An object that tracks a specific week a person selects from a calendar view.
- [UICalendarSelection](uicalendarselection.md) — A base object that tracks one or more dates a user selects from a calendar view.
