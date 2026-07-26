---
title: 'indexPathForPreferredFocusedView(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/indexpathforpreferredfocusedview(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/indexpathforpreferredfocusedview(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/indexpathforpreferredfocusedview%28in%3A%29.json'
content_hash: 'sha256:8adbdcd28d32dd1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# indexPathForPreferredFocusedView(in:)

<sub>Instance Method</sub>

Asks the delegate for the index path of the cell that should be focused.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func indexPathForPreferredFocusedView(in collectionView: UICollectionView) -> IndexPath?
```

## Parameters

- `collectionView` — The collection view object requesting this information.

## Return Value

The index path of the preferred cell. The index path you specify must correspond to a valid cell in the collection view.

## Discussion

When focus is about to change to a collection view, the collection view must pick which of its subviews should receive that focus. If the collection view’s [remembersLastFocusedIndexPath](../uitableview/rememberslastfocusedindexpath.md) property is set to [true](../../swift/true.md), the collection view returns the index path of the cell that was last focused. If the [remembersLastFocusedIndexPath](../uitableview/rememberslastfocusedindexpath.md) property is [false](../../swift/false.md), or if there is no saved index path because no cell was previously focused, the collection view calls this method so that you can specify which cell should receive focus. If you do not implement this method, the collection view returns an appropriate cell.

The effects of this method may be ignored during or immediately after a view controller transition, such as a presentation dismissal or navigation stack pop. In such cases, the view controller attempts to restore focus to the item that was focused prior to the transition (for example, prior to the view controller being presented or pushed), which can take precedence over the effects of this method. To learn how to control or disable this behavior in the view controller, see [restoresFocusAfterTransition](../uiviewcontroller/restoresfocusaftertransition.md).

If you subclass [UICollectionView](../uicollectionview.md), you can also implement the same behavior by overriding the [preferredFocusEnvironments](../uifocusenvironment/preferredfocusenvironments.md) property, which is defined by the [UIFocusEnvironment](../uifocusenvironment.md) protocol and adopted by all views.

## See Also

### Related Documentation

- [preferredFocusedView](../uifocusenvironment/preferredfocusedview.md) — Specifies the view that should be focused if this environment is focused. _(deprecated)_

### Working with focus

- [- collectionView:canFocusItemAtIndexPath:](<collectionview(__canfocusitemat_).md>) — Asks the delegate whether the item at the specified index path can be focused.
- [- collectionView:shouldUpdateFocusInContext:](<collectionview(__shouldupdatefocusin_).md>) — Asks the delegate whether a change in focus should occur.
- [- collectionView:didUpdateFocusInContext:withAnimationCoordinator:](<collectionview(__didupdatefocusin_with_).md>) — Tells the delegate that a focus update occurred.
- [- collectionView:selectionFollowsFocusForItemAtIndexPath:](<collectionview(__selectionfollowsfocusforitemat_).md>) — Asks the delegate whether to relate selection and focus behavior for the cell at the corresponding index path.
