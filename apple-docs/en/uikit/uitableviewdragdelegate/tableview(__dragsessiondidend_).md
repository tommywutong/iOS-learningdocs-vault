---
title: 'tableView(_:dragSessionDidEnd:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdragdelegate/tableview(_:dragsessiondidend:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdragdelegate/tableview(_:dragsessiondidend:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdragdelegate/tableview%28_%3Adragsessiondidend%3A%29.json'
content_hash: 'sha256:3ad6c218f401fe17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDragDelegate](../uitableviewdragdelegate.md)

# tableView(_:dragSessionDidEnd:)

<sub>Instance Method</sub>

Signals the end of a drag operation involving content from the specified table view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, dragSessionDidEnd session: any UIDragSession)
```

## Parameters

- `tableView` — The table view from which the drag operation originated.

- `session` — The drag session object providing context for the drag operation.

## Discussion

This method is called after the drag session ended, usually because the content was dropped but possibly because the drag was terminated. Use this method to close out any tasks related to the management of the drag session in your app.

Each call to this method is always preceded by a call to the [- tableView:dragSessionWillBegin:](<tableview(__dragsessionwillbegin_).md>) method.

## See Also

### Tracking the drag session

- [- tableView:dragSessionWillBegin:](<tableview(__dragsessionwillbegin_).md>) — Signals the start of a drag operation involving content from the specified table view.
- [- tableView:dragSessionIsRestrictedToDraggingApplication:](<tableview(__dragsessionisrestrictedtodraggingapplication_).md>) — Returns a Boolean value indicating whether the dragged content must be dropped in the same app.
- [- tableView:dragSessionAllowsMoveOperation:](<tableview(__dragsessionallowsmoveoperation_).md>) — Returns a Boolean value indicating whether your app supports a move operation for the dragged content.
