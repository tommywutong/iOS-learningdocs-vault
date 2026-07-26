---
title: 'tableView(_:dragSessionWillBegin:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdragdelegate/tableview(_:dragsessionwillbegin:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdragdelegate/tableview(_:dragsessionwillbegin:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdragdelegate/tableview%28_%3Adragsessionwillbegin%3A%29.json'
content_hash: 'sha256:d836e9afc30da09a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDragDelegate](../uitableviewdragdelegate.md)

# tableView(_:dragSessionWillBegin:)

<sub>Instance Method</sub>

Signals the start of a drag operation involving content from the specified table view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, dragSessionWillBegin session: any UIDragSession)
```

## Parameters

- `tableView` — The table view from which the drag operation originated.

- `session` — The drag session object providing context for the drag operation.

## Discussion

This method is called after it has been determined that a drag will begin, after any lift animations have occurred, and before the position of the drag changes significantly. Use this method to perform any tasks related to the management of the drag session in your app.

Each call to this method is always balanced by a call to the [- tableView:dragSessionDidEnd:](<tableview(__dragsessiondidend_).md>) method.

## See Also

### Tracking the drag session

- [- tableView:dragSessionDidEnd:](<tableview(__dragsessiondidend_).md>) — Signals the end of a drag operation involving content from the specified table view.
- [- tableView:dragSessionIsRestrictedToDraggingApplication:](<tableview(__dragsessionisrestrictedtodraggingapplication_).md>) — Returns a Boolean value indicating whether the dragged content must be dropped in the same app.
- [- tableView:dragSessionAllowsMoveOperation:](<tableview(__dragsessionallowsmoveoperation_).md>) — Returns a Boolean value indicating whether your app supports a move operation for the dragged content.
