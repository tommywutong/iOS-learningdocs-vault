---
title: 'tableView(_:dropSessionDidEnter:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdropdelegate/tableview(_:dropsessiondidenter:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdropdelegate/tableview(_:dropsessiondidenter:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdropdelegate/tableview%28_%3Adropsessiondidenter%3A%29.json'
content_hash: 'sha256:24ef6ae4a652b526'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDropDelegate](../uitableviewdropdelegate.md)

# tableView(_:dropSessionDidEnter:)

<sub>Instance Method</sub>

Notifies the delegate when dragged content enters the table view’s bounds rectangle.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, dropSessionDidEnter session: any UIDropSession)
```

## Parameters

- `tableView` — The table view that’s now the potential target of the drop.

- `session` — The drop session object containing information about the data being dragged.

## Discussion

The table view calls this method when dragged content first enters its bounds rectangle. This method isn’t called again until the dragged content exits the table view’s bounds (triggering a call to the [- tableView:dropSessionDidExit:](<tableview(__dropsessiondidexit_).md>) method) and enters again.

Use this method to perform any one-time setup associated with tracking dragged content over the table view.

## See Also

### Tracking the drag movements

- [- tableView:dropSessionDidUpdate:withDestinationIndexPath:](<tableview(__dropsessiondidupdate_withdestinationindexpath_).md>) — Proposes how to handle a drop at the specified location in the table view.
- [- tableView:dropSessionDidExit:](<tableview(__dropsessiondidexit_).md>) — Notifies the delegate when dragged content exits the table view’s bounds rectangle.
- [- tableView:dropSessionDidEnd:](<tableview(__dropsessiondidend_).md>) — Notifies the delegate when the drag operation ends.
