---
title: 'tableView(_:didUpdateFocusIn:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:didupdatefocusin:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:didupdatefocusin:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Adidupdatefocusin%3Awith%3A%29.json'
content_hash: 'sha256:94e2e02e4500ef01'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:didUpdateFocusIn:with:)

<sub>Instance Method</sub>

Tells the delegate that a focus update specified by the context has just occurred.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, didUpdateFocusIn context: UITableViewFocusUpdateContext, with coordinator: UIFocusAnimationCoordinator)
```

## Parameters

- `tableView` — A table view informing the delegate about the new focus.

- `context` — An instance of the [UIFocusUpdateContext](../uifocusupdatecontext.md) class, containing metadata for the focus related update.

- `coordinator` — An instance of the [UIFocusUpdateContext](../uifocusupdatecontext.md) class, containing metadata for the focus related update.

## Discussion

This functionality of this delegate method is equivalent to overriding [UITableView](../uitableview.md) class’s  implementation of [- tableView:didUpdateFocusInContext:withAnimationCoordinator:](<tableview(__didupdatefocusin_with_).md>). This delegate method provides additional UITableView-related information in its context parameter, such as the index paths for the previously and next focused views. Note that, these index paths are available only if their views are contained within the table view. To learn more about the information provided by the context, see see [UITableViewFocusUpdateContext](../uitableviewfocusupdatecontext.md).

## See Also

### Managing table view focus

- [- tableView:canFocusRowAtIndexPath:](<tableview(__canfocusrowat_).md>) — Asks the delegate whether the cell at the specified index path is itself focusable.
- [- tableView:shouldUpdateFocusInContext:](<tableview(__shouldupdatefocusin_).md>) — Asks the delegate whether the focus update specified by the context is allowed to occur.
- [- indexPathForPreferredFocusedViewInTableView:](<indexpathforpreferredfocusedview(in_).md>) — Asks the delegate for the table view’s index path for the preferred focused view.
- [- tableView:selectionFollowsFocusForRowAtIndexPath:](<tableview(__selectionfollowsfocusforrowat_).md>) — Asks the delegate whether to relate selection and focus behavior for the row at the corresponding index path.
