---
title: 'tableView(_:selectionFollowsFocusForRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:selectionfollowsfocusforrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:selectionfollowsfocusforrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Aselectionfollowsfocusforrowat%3A%29.json'
content_hash: 'sha256:6d4403e35cc18ae0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:selectionFollowsFocusForRowAt:)

<sub>Instance Method</sub>

Asks the delegate whether to relate selection and focus behavior for the row at the corresponding index path.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, selectionFollowsFocusForRowAt indexPath: IndexPath) -> Bool
```

## Parameters

- `tableView` — The table view making the request.

- `indexPath` — The index path of the row to determine selection behavior for.

## Return Value

[true](../../swift/true.md) if you want to automatically select the row at the specified index path when focus moves to it; otherwise, [false](../../swift/false.md).

## Discussion

If the table view’s [selectionFollowsFocus](../uitableview/selectionfollowsfocus.md) property is [true](../../swift/true.md) and you return [false](../../swift/false.md) from this delegate method, focus still moves to the row when the user selects it. However, when focus moves to the row, the row doesn’t automatically select.

## See Also

### Managing table view focus

- [- tableView:canFocusRowAtIndexPath:](<tableview(__canfocusrowat_).md>) — Asks the delegate whether the cell at the specified index path is itself focusable.
- [- tableView:shouldUpdateFocusInContext:](<tableview(__shouldupdatefocusin_).md>) — Asks the delegate whether the focus update specified by the context is allowed to occur.
- [- tableView:didUpdateFocusInContext:withAnimationCoordinator:](<tableview(__didupdatefocusin_with_).md>) — Tells the delegate that a focus update specified by the context has just occurred.
- [- indexPathForPreferredFocusedViewInTableView:](<indexpathforpreferredfocusedview(in_).md>) — Asks the delegate for the table view’s index path for the preferred focused view.
