---
title: 'collectionView(_:shouldUpdateFocusIn:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:shouldupdatefocusin:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:shouldupdatefocusin:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Ashouldupdatefocusin%3A%29.json'
content_hash: 'sha256:665c1b1b3ca4987c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:shouldUpdateFocusIn:)

<sub>Instance Method</sub>

Asks the delegate whether a change in focus should occur.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, shouldUpdateFocusIn context: UICollectionViewFocusUpdateContext) -> Bool
```

## Parameters

- `collectionView` — The collection view object requesting this information.

- `context` — The context object containing metadata associated with the focus change. This object contains the index path of the previously focused item and the item targeted to receive focus next. Use this information to determine if the focus change should occur.

## Return Value

[true](../../swift/true.md) if the focus change should occur or [false](../../swift/false.md) if it should not.

## Discussion

Before a focus change can occur, the focus engine asks all affected views if such a change should occur. In response, the collection view calls this method to give you the opportunity to allow or prevent the change. Return this method to prevent changes that should not occur. For example, you might use it to ensure that the navigation between cells occurs in a specific order.

If you do not implement this method, the collection view assumes a return value of [true](../../swift/true.md).

If you subclass [UICollectionView](../uicollectionview.md), you can also implement the same behavior by overriding the [- shouldUpdateFocusInContext:](<../uifocusenvironment/shouldupdatefocus(in_).md>) method, which is defined by the [UIFocusEnvironment](../uifocusenvironment.md) protocol and adopted by all views.

## See Also

### Related Documentation

- [- shouldUpdateFocusInContext:](<../uifocusenvironment/shouldupdatefocus(in_).md>) — Returns a Boolean value indicating whether the focus engine should allow the focus update described by the specified context to occur.

### Working with focus

- [- collectionView:canFocusItemAtIndexPath:](<collectionview(__canfocusitemat_).md>) — Asks the delegate whether the item at the specified index path can be focused.
- [- indexPathForPreferredFocusedViewInCollectionView:](<indexpathforpreferredfocusedview(in_).md>) — Asks the delegate for the index path of the cell that should be focused.
- [- collectionView:didUpdateFocusInContext:withAnimationCoordinator:](<collectionview(__didupdatefocusin_with_).md>) — Tells the delegate that a focus update occurred.
- [- collectionView:selectionFollowsFocusForItemAtIndexPath:](<collectionview(__selectionfollowsfocusforitemat_).md>) — Asks the delegate whether to relate selection and focus behavior for the cell at the corresponding index path.
