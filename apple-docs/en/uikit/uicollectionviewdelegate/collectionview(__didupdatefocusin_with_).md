---
title: 'collectionView(_:didUpdateFocusIn:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:didupdatefocusin:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:didupdatefocusin:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Adidupdatefocusin%3Awith%3A%29.json'
content_hash: 'sha256:8a92d7e525384f05'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:didUpdateFocusIn:with:)

<sub>Instance Method</sub>

Tells the delegate that a focus update occurred.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, didUpdateFocusIn context: UICollectionViewFocusUpdateContext, with coordinator: UIFocusAnimationCoordinator)
```

## Parameters

- `collectionView` — The collection view object notifying you of the focus change.

- `context` — The context object containing metadata associated with the focus change. This object contains the index path of the previously focused item and the currently focused item.

- `coordinator` — The animation coordinator to use when creating any additional animations.

## Discussion

The collection view calls this method when a focus-related change occurs. You can use this method to update your app’s state information or to animate changes to your app’s visual appearance.

If you subclass [UICollectionView](../uicollectionview.md), you can also implement the same behavior by overriding the [- didUpdateFocusInContext:withAnimationCoordinator:](<../uifocusenvironment/didupdatefocus(in_with_).md>) method, which is defined by the [UIFocusEnvironment](../uifocusenvironment.md) protocol and adopted by all views.

## See Also

### Related Documentation

- [- didUpdateFocusInContext:withAnimationCoordinator:](<../uifocusenvironment/didupdatefocus(in_with_).md>) — Called immediately after the system updates the focus to a new view.

### Working with focus

- [- collectionView:canFocusItemAtIndexPath:](<collectionview(__canfocusitemat_).md>) — Asks the delegate whether the item at the specified index path can be focused.
- [- indexPathForPreferredFocusedViewInCollectionView:](<indexpathforpreferredfocusedview(in_).md>) — Asks the delegate for the index path of the cell that should be focused.
- [- collectionView:shouldUpdateFocusInContext:](<collectionview(__shouldupdatefocusin_).md>) — Asks the delegate whether a change in focus should occur.
- [- collectionView:selectionFollowsFocusForItemAtIndexPath:](<collectionview(__selectionfollowsfocusforitemat_).md>) — Asks the delegate whether to relate selection and focus behavior for the cell at the corresponding index path.
