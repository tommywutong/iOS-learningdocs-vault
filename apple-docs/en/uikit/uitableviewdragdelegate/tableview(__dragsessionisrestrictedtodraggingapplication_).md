---
title: 'tableView(_:dragSessionIsRestrictedToDraggingApplication:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdragdelegate/tableview(_:dragsessionisrestrictedtodraggingapplication:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdragdelegate/tableview(_:dragsessionisrestrictedtodraggingapplication:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdragdelegate/tableview%28_%3Adragsessionisrestrictedtodraggingapplication%3A%29.json'
content_hash: 'sha256:a17cb87939eab863'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDragDelegate](../uitableviewdragdelegate.md)

# tableView(_:dragSessionIsRestrictedToDraggingApplication:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the dragged content must be dropped in the same app.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, dragSessionIsRestrictedToDraggingApplication session: any UIDragSession) -> Bool
```

## Parameters

- `tableView` — The table view from which the drag operation originated.

- `session` — The drag session object containing information about the drag operation.

## Return Value

[true](../../swift/true.md) if the dragged content must be dropped in the same app that originated the drag, or [false](../../swift/false.md) if the content may be dragged to other apps.

## Discussion

Implement this method when you want to allow the user to drag content within your app, but prevent them from dragging that same content to other apps. If you don’t implement this method, the table view behaves as if the method returned [false](../../swift/false.md).

## See Also

### Tracking the drag session

- [- tableView:dragSessionWillBegin:](<tableview(__dragsessionwillbegin_).md>) — Signals the start of a drag operation involving content from the specified table view.
- [- tableView:dragSessionDidEnd:](<tableview(__dragsessiondidend_).md>) — Signals the end of a drag operation involving content from the specified table view.
- [- tableView:dragSessionAllowsMoveOperation:](<tableview(__dragsessionallowsmoveoperation_).md>) — Returns a Boolean value indicating whether your app supports a move operation for the dragged content.
