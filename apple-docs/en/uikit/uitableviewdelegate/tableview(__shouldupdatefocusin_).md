---
title: 'tableView(_:shouldUpdateFocusIn:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:shouldupdatefocusin:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:shouldupdatefocusin:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Ashouldupdatefocusin%3A%29.json'
content_hash: 'sha256:b2bfa0a19115ac70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:shouldUpdateFocusIn:)

<sub>Instance Method</sub>

Asks the delegate whether the focus update specified by the context is allowed to occur.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, shouldUpdateFocusIn context: UITableViewFocusUpdateContext) -> Bool
```

## Parameters

- `tableView` — A table view in which the focus update is occurring.

- `context` — An instance of [UIFocusUpdateContext](../uifocusupdatecontext.md) class, contains metadata for the focus related update.

## Return Value

[true](../../swift/true.md) if the focus should update; otherwise [false](../../swift/false.md).

## Discussion

The functionality of this delegate method is equivalent to overriding [UITableView](../uitableview.md) class’s  [- shouldUpdateFocusInContext:](<../uifocusenvironment/shouldupdatefocus(in_).md>) method. This delegate method provides additional [UITableView](../uitableview.md)-related information in its context parameter, such as the index paths for the previously and next focused views. Note that, these index paths are only available if their views are contained within the table view. To learn more about the information provided by the context, see [UITableViewFocusUpdateContext](../uitableviewfocusupdatecontext.md).

## See Also

### Managing table view focus

- [- tableView:canFocusRowAtIndexPath:](<tableview(__canfocusrowat_).md>) — Asks the delegate whether the cell at the specified index path is itself focusable.
- [- tableView:didUpdateFocusInContext:withAnimationCoordinator:](<tableview(__didupdatefocusin_with_).md>) — Tells the delegate that a focus update specified by the context has just occurred.
- [- indexPathForPreferredFocusedViewInTableView:](<indexpathforpreferredfocusedview(in_).md>) — Asks the delegate for the table view’s index path for the preferred focused view.
- [- tableView:selectionFollowsFocusForRowAtIndexPath:](<tableview(__selectionfollowsfocusforrowat_).md>) — Asks the delegate whether to relate selection and focus behavior for the row at the corresponding index path.
