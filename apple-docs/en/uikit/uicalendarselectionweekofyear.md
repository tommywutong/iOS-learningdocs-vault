---
title: UICalendarSelectionWeekOfYear
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicalendarselectionweekofyear
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarselectionweekofyear'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarselectionweekofyear.json'
content_hash: 'sha256:1fc6d71fec12b2f2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICalendarSelectionWeekOfYear

<sub>Class</sub>

An object that tracks a specific week a person selects from a calendar view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UICalendarSelectionWeekOfYear
```

## Overview

Use the [UICalendarSelectionWeekOfYear](uicalendarselectionweekofyear.md) selection behavior to allow selecting dates in a calendar view by week. The following code example shows how to configure a calendar view’s selection behavior to use week-of-year selection:

```swift
// Create a calendar view.
let calendarView = UICalendarView()
calendarView.calendar = Calendar(identifier: .gregorian)

// Set the selection behavior.
let selection = UICalendarSelectionWeekOfYear(delegate: self)
calendarView.selectionBehavior = selection

// Set the 11th week in the year 2024.
selection.selectedWeekOfYear = DateComponents(
    calendar: Calendar(identifier: .gregorian),
    weekOfYear: 11,
    yearForWeekOfYear: 2024)
```

## Relationships

- **Inherits From**: [UICalendarSelection](uicalendarselection.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a week-of-year selection

- [- initWithDelegate:](<uicalendarselectionweekofyear/init(delegate_).md>) — Creates an object that tracks a week a person selects from a calendar view, with an optional delegate to manage selectable weeks and selection changes.

### Setting the selection delegate

- [delegate](uicalendarselectionweekofyear/delegate.md) — A delegate object that a calendar view asks about selectable weeks and informs of changes to the week selection.
- [UICalendarSelectionWeekOfYearDelegate](uicalendarselectionweekofyeardelegate.md) — A set of methods you implement to provide selectable weeks and handle changes to the week selection in a calendar view.

### Updating the selected week

- [selectedWeekOfYear](uicalendarselectionweekofyear/selectedweekofyear.md) — The current week-of-year selection in the calendar view.
- [- setSelectedWeekOfYear:animated:](<uicalendarselectionweekofyear/setselected(__animated_).md>) — Updates the date component object that represents a selected week in a calendar view, with an option to animate the change.

## See Also

### Handling date selections

- [selectionBehavior](uicalendarview/selectionbehavior.md) — The current date selection method of the calendar view.
- [UICalendarSelectionSingleDate](uicalendarselectionsingledate.md) — An object that tracks a date the user selects from a calendar view.
- [UICalendarSelectionMultiDate](uicalendarselectionmultidate.md) — An object that tracks multiple dates the user selects from a calendar view.
- [UICalendarSelection](uicalendarselection.md) — A base object that tracks one or more dates a user selects from a calendar view.
