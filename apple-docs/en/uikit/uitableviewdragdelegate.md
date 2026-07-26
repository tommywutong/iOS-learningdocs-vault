---
title: UITableViewDragDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewdragdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdragdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdragdelegate.json'
content_hash: 'sha256:ab26841b09b14ccb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITableViewDragDelegate

<sub>Protocol</sub>

The interface for initiating drags from a table view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UITableViewDragDelegate : NSObjectProtocol
```

## Overview

Implement this protocol in the object that you use to initiate drags from your table view. The only required method of this protocol is the [- tableView:itemsForBeginningDragSession:atIndexPath:](<uitableviewdragdelegate/tableview(__itemsforbeginning_at_).md>) method, but you can implement other methods as needed to customize the drag behavior of your table view.

Assign your custom delegate object to the [dragDelegate](uitableview/dragdelegate.md) property of your table view.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Providing the items to drag

- [- tableView:itemsForBeginningDragSession:atIndexPath:](<uitableviewdragdelegate/tableview(__itemsforbeginning_at_).md>) — Provides the initial set of items (if any) to drag.
- [- tableView:itemsForAddingToDragSession:atIndexPath:point:](<uitableviewdragdelegate/tableview(__itemsforaddingto_at_point_).md>) — Adds the specified items to an existing drag session.

### Tracking the drag session

- [- tableView:dragSessionWillBegin:](<uitableviewdragdelegate/tableview(__dragsessionwillbegin_).md>) — Signals the start of a drag operation involving content from the specified table view.
- [- tableView:dragSessionDidEnd:](<uitableviewdragdelegate/tableview(__dragsessiondidend_).md>) — Signals the end of a drag operation involving content from the specified table view.
- [- tableView:dragSessionIsRestrictedToDraggingApplication:](<uitableviewdragdelegate/tableview(__dragsessionisrestrictedtodraggingapplication_).md>) — Returns a Boolean value indicating whether the dragged content must be dropped in the same app.
- [- tableView:dragSessionAllowsMoveOperation:](<uitableviewdragdelegate/tableview(__dragsessionallowsmoveoperation_).md>) — Returns a Boolean value indicating whether your app supports a move operation for the dragged content.

### Providing a custom preview

- [- tableView:dragPreviewParametersForRowAtIndexPath:](<uitableviewdragdelegate/tableview(__dragpreviewparametersforrowat_).md>) — Returns custom information about how to display the row at the specified location during the drag.

## See Also

### Drag and drop

- [Supporting drag and drop in table views](supporting-drag-and-drop-in-table-views.md) — Initiate drags and handle drops from a table view.
- [Adopting drag and drop in a table view](adopting-drag-and-drop-in-a-table-view.md) — Demonstrates how to enable and implement drag and drop for a table view.
- [UITableViewDropDelegate](uitableviewdropdelegate.md) — The interface for handling drops in a table view.
- [UITableViewDropCoordinator](uitableviewdropcoordinator.md) — An interface for coordinating your custom drop-related actions with the table view.
- [UITableViewDropItem](uitableviewdropitem.md) — The data associated with an item being dropped into the table view.
- [UITableViewDropProposal](uitableviewdropproposal.md) — Your proposed solution for handling a drop in a table view.
