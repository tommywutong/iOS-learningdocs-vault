---
title: 'tableView(_:dragSessionAllowsMoveOperation:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdragdelegate/tableview(_:dragsessionallowsmoveoperation:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdragdelegate/tableview(_:dragsessionallowsmoveoperation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdragdelegate/tableview%28_%3Adragsessionallowsmoveoperation%3A%29.json'
content_hash: 'sha256:7976deabf9962dfc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDragDelegate](../uitableviewdragdelegate.md)

# tableView(_:dragSessionAllowsMoveOperation:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether your app supports a move operation for the dragged content.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, dragSessionAllowsMoveOperation session: any UIDragSession) -> Bool
```

## Parameters

- `tableView` — The table view from which the drag operation originated.

- `session` — The drag session object containing information about the drag operation.

## Return Value

[true](../../swift/true.md) if your app allows content to be moved instead of copied, or [false](../../swift/false.md) if moves are not supported.

## Discussion

Implement this method if you want to prevent the dragged content from being moved. If your delegate returns [false](../../swift/false.md) and the drop operation type is [UIDropOperationMove](../uidropoperation/move.md), the system cancels the drop.

If you don’t implement this method, the table view behaves as if the method returned [true](../../swift/true.md).

## See Also

### Tracking the drag session

- [- tableView:dragSessionWillBegin:](<tableview(__dragsessionwillbegin_).md>) — Signals the start of a drag operation involving content from the specified table view.
- [- tableView:dragSessionDidEnd:](<tableview(__dragsessiondidend_).md>) — Signals the end of a drag operation involving content from the specified table view.
- [- tableView:dragSessionIsRestrictedToDraggingApplication:](<tableview(__dragsessionisrestrictedtodraggingapplication_).md>) — Returns a Boolean value indicating whether the dragged content must be dropped in the same app.
