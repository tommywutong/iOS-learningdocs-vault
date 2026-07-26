---
title: UITableViewRowAction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+（13.0 起废弃）, iPadOS 8.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uitableviewrowaction
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewrowaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewrowaction.json'
content_hash: 'sha256:7357279e82127d01'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITableViewRowAction

<sub>Class</sub>

A single action to present when the user swipes horizontally in a table row.

> [!warning] Deprecated
> Use [UISwipeActionsConfiguration](uiswipeactionsconfiguration.md) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor class UITableViewRowAction
```

## Overview

Create a [UITableViewRowAction](uitableviewrowaction.md) object to define a single, custom action for a table row. Users swipe horizontally in a table view to reveal the actions associated with a row. Each row-action object contains the text display, the action to perform, and any specific formatting to apply to that action.

To add custom actions to your table view’s rows, implement the [- tableView:editActionsForRowAtIndexPath:](<uitableviewdelegate/tableview(__editactionsforrowat_).md>) method in your table view’s delegate object. In that method, create and return the actions for the indicated row. The table displays your action buttons and executes the appropriate handler block when the user taps one of them.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a table row action

- [+ rowActionWithStyle:title:handler:](<uitableviewrowaction/init(style_title_handler_).md>) — Creates and returns a new table view row action object. _(deprecated)_

### Configuring the action’s appearance

- [style](uitableviewrowaction/style-swift.property.md) — The style applied to the action button. _(deprecated)_
- [Style](uitableviewrowaction/style-swift.enum.md) — Constants that specify the appearance of action buttons. _(deprecated)_
- [title](uitableviewrowaction/title.md) — The title of the action button. _(deprecated)_
- [backgroundColor](uitableviewrowaction/backgroundcolor.md) — The background color of the action button. _(deprecated)_
- [backgroundEffect](uitableviewrowaction/backgroundeffect.md) — The visual effect to apply to the button. _(deprecated)_

## See Also

### Row actions

- [UISwipeActionsConfiguration](uiswipeactionsconfiguration.md) — The set of actions to perform when swiping on rows of a table.
- [UIContextualAction](uicontextualaction.md) — An action to display when the user swipes a table row.
