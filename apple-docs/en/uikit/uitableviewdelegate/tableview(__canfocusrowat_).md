---
title: 'tableView(_:canFocusRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:canfocusrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:canfocusrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Acanfocusrowat%3A%29.json'
content_hash: 'sha256:2702eace199d9d57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:canFocusRowAt:)

<sub>Instance Method</sub>

Asks the delegate whether the cell at the specified index path is itself focusable.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, canFocusRowAt indexPath: IndexPath) -> Bool
```

## Parameters

- `tableView` — The table view requesting this information.

- `indexPath` — An index path locating a row in `tableView`.

## Return Value

[true](../../swift/true.md) if the row indicated by `indexPath`; otherwise, [false](../../swift/false.md).

## Discussion

The functionality of this delegate method is equivalent to overriding the cell’s [canBecomeFocused](../uiview/canbecomefocused.md) method. If [true](../../swift/true.md) is returned, then the cell at the specified index path is focusable, meaning none of its contents can be focused. Returning[false](../../swift/false.md) means the cell itself is not focusable, however this does not prevent any of its contents from being focused. If this method is not implemented, then the return value is assumed to be [true](../../swift/true.md).

## See Also

### Managing table view focus

- [- tableView:shouldUpdateFocusInContext:](<tableview(__shouldupdatefocusin_).md>) — Asks the delegate whether the focus update specified by the context is allowed to occur.
- [- tableView:didUpdateFocusInContext:withAnimationCoordinator:](<tableview(__didupdatefocusin_with_).md>) — Tells the delegate that a focus update specified by the context has just occurred.
- [- indexPathForPreferredFocusedViewInTableView:](<indexpathforpreferredfocusedview(in_).md>) — Asks the delegate for the table view’s index path for the preferred focused view.
- [- tableView:selectionFollowsFocusForRowAtIndexPath:](<tableview(__selectionfollowsfocusforrowat_).md>) — Asks the delegate whether to relate selection and focus behavior for the row at the corresponding index path.
