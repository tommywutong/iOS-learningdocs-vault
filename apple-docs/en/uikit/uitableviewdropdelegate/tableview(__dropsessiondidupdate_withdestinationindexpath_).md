---
title: 'tableView(_:dropSessionDidUpdate:withDestinationIndexPath:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdropdelegate/tableview(_:dropsessiondidupdate:withdestinationindexpath:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdropdelegate/tableview(_:dropsessiondidupdate:withdestinationindexpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdropdelegate/tableview%28_%3Adropsessiondidupdate%3Awithdestinationindexpath%3A%29.json'
content_hash: 'sha256:afced1e85cd38f61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDropDelegate](../uitableviewdropdelegate.md)

# tableView(_:dropSessionDidUpdate:withDestinationIndexPath:)

<sub>Instance Method</sub>

Proposes how to handle a drop at the specified location in the table view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, dropSessionDidUpdate session: any UIDropSession, withDestinationIndexPath destinationIndexPath: IndexPath?) -> UITableViewDropProposal
```

## Parameters

- `tableView` — The table view currently being targeted to receive the drop.

- `session` — The drop session object containing information about the data being dragged.

- `destinationIndexPath` — The index path of the row currently being targeted by the drop. Use this value to determine an appropriate course of action for the drop.

## Return Value

The [UITableViewDropProposal](../uitableviewdropproposal.md) object indicating how to incorporate the dropped data.

## Discussion

While the user is dragging content, the table view calls this method repeatedly to determine how you would handle the drop if it occurred at the specified location. The table view provides visual feedback to the user based on your proposal.

In your implementation of this method, create a [UITableViewDropProposal](../uitableviewdropproposal.md) object and use it to convey your intentions. Because this method is called repeatedly while the user drags over the table view, your implementation should return as quickly as possible.

## See Also

### Tracking the drag movements

- [- tableView:dropSessionDidEnter:](<tableview(__dropsessiondidenter_).md>) — Notifies the delegate when dragged content enters the table view’s bounds rectangle.
- [- tableView:dropSessionDidExit:](<tableview(__dropsessiondidexit_).md>) — Notifies the delegate when dragged content exits the table view’s bounds rectangle.
- [- tableView:dropSessionDidEnd:](<tableview(__dropsessiondidend_).md>) — Notifies the delegate when the drag operation ends.
