---
title: 'indexPathForPreferredFocusedView(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/indexpathforpreferredfocusedview(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/indexpathforpreferredfocusedview(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/indexpathforpreferredfocusedview%28in%3A%29.json'
content_hash: 'sha256:8e07f558740a4320'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# indexPathForPreferredFocusedView(in:)

<sub>Instance Method</sub>

Asks the delegate for the table view’s index path for the preferred focused view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func indexPathForPreferredFocusedView(in tableView: UITableView) -> IndexPath?
```

## Parameters

- `tableView` — A table view requesting the index path for preferred focus view.

## Return Value

An index path for the preferred focus row, or the default preferred focus view.

## Discussion

This functionality of this delegate method is equivalent to overriding [UITableView](../uitableview.md) class’s [preferredFocusedView](../uifocusguide/preferredfocusedview.md) method in the [UIFocusEnvironment](../uifocusenvironment.md) protocol. If the [UITableView](../uitableview.md) class’s [remembersLastFocusedIndexPath](../uitableview/rememberslastfocusedindexpath.md) method is set to [true](../../swift/true.md), this method defines the index path that gets focused when the table view is focused for the first time.

The effects of this method may be ignored during or immediately after a view controller transition, such as a presentation dismissal or navigation stack pop. In such cases, the view controller attempts to restore focus to the item that was focused prior to the transition (for example, prior to the view controller being presented or pushed), which can take precedence over the effects of this method. To learn how to control or disable this behavior in the view controller, see [restoresFocusAfterTransition](../uiviewcontroller/restoresfocusaftertransition.md).

## See Also

### Managing table view focus

- [- tableView:canFocusRowAtIndexPath:](<tableview(__canfocusrowat_).md>) — Asks the delegate whether the cell at the specified index path is itself focusable.
- [- tableView:shouldUpdateFocusInContext:](<tableview(__shouldupdatefocusin_).md>) — Asks the delegate whether the focus update specified by the context is allowed to occur.
- [- tableView:didUpdateFocusInContext:withAnimationCoordinator:](<tableview(__didupdatefocusin_with_).md>) — Tells the delegate that a focus update specified by the context has just occurred.
- [- tableView:selectionFollowsFocusForRowAtIndexPath:](<tableview(__selectionfollowsfocusforrowat_).md>) — Asks the delegate whether to relate selection and focus behavior for the row at the corresponding index path.
