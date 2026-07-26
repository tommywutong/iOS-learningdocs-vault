---
title: 'tableView(_:dropSessionDidExit:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdropdelegate/tableview(_:dropsessiondidexit:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdropdelegate/tableview(_:dropsessiondidexit:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdropdelegate/tableview%28_%3Adropsessiondidexit%3A%29.json'
content_hash: 'sha256:1d7d956e2581869b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDropDelegate](../uitableviewdropdelegate.md)

# tableView(_:dropSessionDidExit:)

<sub>Instance Method</sub>

Notifies the delegate when dragged content exits the table view’s bounds rectangle.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, dropSessionDidExit session: any UIDropSession)
```

## Parameters

- `tableView` — The collection view that was tracking the dragged content.

- `session` — The drop session object containing information about the data being dragged.

## Discussion

The table view calls this method when dragged content exits its bounds rectangle. This method isn’t called again until the dragged content enters the table view’s bounds (triggering a call to the [- tableView:dropSessionDidEnter:](<tableview(__dropsessiondidenter_).md>) method) and exits again.

Use this method to clean up any state information that you configured in your [- tableView:dropSessionDidEnter:](<tableview(__dropsessiondidenter_).md>) method.

## See Also

### Tracking the drag movements

- [- tableView:dropSessionDidUpdate:withDestinationIndexPath:](<tableview(__dropsessiondidupdate_withdestinationindexpath_).md>) — Proposes how to handle a drop at the specified location in the table view.
- [- tableView:dropSessionDidEnter:](<tableview(__dropsessiondidenter_).md>) — Notifies the delegate when dragged content enters the table view’s bounds rectangle.
- [- tableView:dropSessionDidEnd:](<tableview(__dropsessiondidend_).md>) — Notifies the delegate when the drag operation ends.
