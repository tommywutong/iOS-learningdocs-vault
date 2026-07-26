---
title: 'tableView(_:itemsForAddingTo:at:point:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdragdelegate/tableview(_:itemsforaddingto:at:point:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdragdelegate/tableview(_:itemsforaddingto:at:point:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdragdelegate/tableview%28_%3Aitemsforaddingto%3Aat%3Apoint%3A%29.json'
content_hash: 'sha256:bfd1a7366678231b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDragDelegate](../uitableviewdragdelegate.md)

# tableView(_:itemsForAddingTo:at:point:)

<sub>Instance Method</sub>

Adds the specified items to an existing drag session.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, itemsForAddingTo session: any UIDragSession, at indexPath: IndexPath, point: CGPoint) -> [UIDragItem]
```

## Parameters

- `tableView` — The table view from which the drag operation originated.

- `session` — The drag session object providing context for the drag operation.

- `indexPath` — The index path of the row being added to the drag operation.

- `point` — The location of the touch that caused the row to be added. This point is in the coordinate space of the table view.

## Return Value

An array of [UIDragItem](../uidragitem.md) objects representing the contents of the specified row. Return an empty array if you do not want the user to add the row to the drag session.

## Discussion

Implement this method to allow the user to add items to an active drag session. When a drag session is active and the user taps a row, the table view calls this method. Your implementation should return the drag items to add to the drag operation. If you don’t implement this method, additional touches in the table view are handled as normal table view interactions. For example, additional taps cause rows to be selected or deselected.

In your implementation, create one or more [UIDragItem](../uidragitem.md) objects representing the contents at the specified index path. Normally, you return only one drag item, but you may return more than one item if the specified row represents a container for other content.

## See Also

### Providing the items to drag

- [- tableView:itemsForBeginningDragSession:atIndexPath:](<tableview(__itemsforbeginning_at_).md>) — Provides the initial set of items (if any) to drag.
