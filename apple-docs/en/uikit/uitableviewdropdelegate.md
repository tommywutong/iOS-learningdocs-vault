---
title: UITableViewDropDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewdropdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdropdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdropdelegate.json'
content_hash: 'sha256:2f260772e4e9b8da'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITableViewDropDelegate

<sub>Protocol</sub>

The interface for handling drops in a table view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UITableViewDropDelegate : NSObjectProtocol
```

## Overview

Implement this protocol in the object that you use to incorporate dropped data into your table view. The only required method of this protocol is the [- tableView:performDropWithCoordinator:](<uitableviewdropdelegate/tableview(__performdropwith_).md>) method, but you can implement other methods as needed to customize the drop behavior of your table view.

Assign your custom delegate object to the [dropDelegate](uitableview/dropdelegate.md) property of your table view.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Declaring support for handling drops

- [- tableView:canHandleDropSession:](<uitableviewdropdelegate/tableview(__canhandle_).md>) — Asks your delegate whether it can accept the specified type of data.

### Providing a custom drop preview

- [- tableView:dropPreviewParametersForRowAtIndexPath:](<uitableviewdropdelegate/tableview(__droppreviewparametersforrowat_).md>) — Returns custom information about how to display the row at the specified location during the drop.

### Incorporating the dropped data

- [- tableView:performDropWithCoordinator:](<uitableviewdropdelegate/tableview(__performdropwith_).md>) — Incorporates the dropped data into your data structures and updates the table.

### Tracking the drag movements

- [- tableView:dropSessionDidUpdate:withDestinationIndexPath:](<uitableviewdropdelegate/tableview(__dropsessiondidupdate_withdestinationindexpath_).md>) — Proposes how to handle a drop at the specified location in the table view.
- [- tableView:dropSessionDidEnter:](<uitableviewdropdelegate/tableview(__dropsessiondidenter_).md>) — Notifies the delegate when dragged content enters the table view’s bounds rectangle.
- [- tableView:dropSessionDidExit:](<uitableviewdropdelegate/tableview(__dropsessiondidexit_).md>) — Notifies the delegate when dragged content exits the table view’s bounds rectangle.
- [- tableView:dropSessionDidEnd:](<uitableviewdropdelegate/tableview(__dropsessiondidend_).md>) — Notifies the delegate when the drag operation ends.

## See Also

### Drag and drop

- [Supporting drag and drop in table views](supporting-drag-and-drop-in-table-views.md) — Initiate drags and handle drops from a table view.
- [Adopting drag and drop in a table view](adopting-drag-and-drop-in-a-table-view.md) — Demonstrates how to enable and implement drag and drop for a table view.
- [UITableViewDragDelegate](uitableviewdragdelegate.md) — The interface for initiating drags from a table view.
- [UITableViewDropCoordinator](uitableviewdropcoordinator.md) — An interface for coordinating your custom drop-related actions with the table view.
- [UITableViewDropItem](uitableviewdropitem.md) — The data associated with an item being dropped into the table view.
- [UITableViewDropProposal](uitableviewdropproposal.md) — Your proposed solution for handling a drop in a table view.
