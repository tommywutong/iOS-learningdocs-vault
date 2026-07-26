---
title: 'tableView(_:dropSessionDidEnd:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdropdelegate/tableview(_:dropsessiondidend:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdropdelegate/tableview(_:dropsessiondidend:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdropdelegate/tableview%28_%3Adropsessiondidend%3A%29.json'
content_hash: 'sha256:2e01a830727abb4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDropDelegate](../uitableviewdropdelegate.md)

# tableView(_:dropSessionDidEnd:)

<sub>Instance Method</sub>

Notifies the delegate when the drag operation ends.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, dropSessionDidEnd session: any UIDropSession)
```

## Parameters

- `tableView` — The table view that is no longer the target of the drop.

- `session` — The drop session object containing information about the data being dragged.

## Discussion

The table view calls this method at the conclusion of a drag that was over the table view at one point. Use it to clean up any state information that you used to handle the drag. This method is called regardless of whether the data was actually dropped onto the table view.

## See Also

### Tracking the drag movements

- [- tableView:dropSessionDidUpdate:withDestinationIndexPath:](<tableview(__dropsessiondidupdate_withdestinationindexpath_).md>) — Proposes how to handle a drop at the specified location in the table view.
- [- tableView:dropSessionDidEnter:](<tableview(__dropsessiondidenter_).md>) — Notifies the delegate when dragged content enters the table view’s bounds rectangle.
- [- tableView:dropSessionDidExit:](<tableview(__dropsessiondidexit_).md>) — Notifies the delegate when dragged content exits the table view’s bounds rectangle.
