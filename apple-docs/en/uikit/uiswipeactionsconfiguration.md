---
title: UISwipeActionsConfiguration
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiswipeactionsconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uiswipeactionsconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiswipeactionsconfiguration.json'
content_hash: 'sha256:1a82c4eec6366b67'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISwipeActionsConfiguration

<sub>Class</sub>

The set of actions to perform when swiping on rows of a table.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UISwipeActionsConfiguration
```

## Overview

Create a [UISwipeActionsConfiguration](uiswipeactionsconfiguration.md) object to associate custom swipe actions with a row of your table view. Users swipe horizontally left or right in a table view to reveal the actions associated with a row. Each swipe-actions object contains the set of actions to display for each type of swipe.

To add custom actions to your table view’s rows, implement the [- tableView:leadingSwipeActionsConfigurationForRowAtIndexPath:](<uitableviewdelegate/tableview(__leadingswipeactionsconfigurationforrowat_).md>) or [- tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:](<uitableviewdelegate/tableview(__trailingswipeactionsconfigurationforrowat_).md>) method of your table view’s delegate. In those methods, create and return the actions for the indicated row. The table displays your action buttons and executes the appropriate handler block when the user taps one of them.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Initializing the swipe actions

- [+ configurationWithActions:](<uiswipeactionsconfiguration/init(actions_).md>) — Creates a swipe action configuration object with the specified set of actions.

### Getting the swipe action information

- [actions](uiswipeactionsconfiguration/actions.md) — The swipe actions.
- [performsFirstActionWithFullSwipe](uiswipeactionsconfiguration/performsfirstactionwithfullswipe.md) — A Boolean value indicating whether a full swipe automatically performs the first action.

## See Also

### Row actions

- [UIContextualAction](uicontextualaction.md) — An action to display when the user swipes a table row.
- [UITableViewRowAction](uitableviewrowaction.md) — A single action to present when the user swipes horizontally in a table row. _(deprecated)_
