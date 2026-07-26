---
title: 'collectionView(_:canFocusItemAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:canfocusitemat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:canfocusitemat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Acanfocusitemat%3A%29.json'
content_hash: 'sha256:aef348301f732461'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:canFocusItemAt:)

<sub>Instance Method</sub>

Asks the delegate whether the item at the specified index path can be focused.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, canFocusItemAt indexPath: IndexPath) -> Bool
```

## Parameters

- `collectionView` — The collection view object requesting this information.

- `indexPath` — The index path of an item in the collection view.

## Return Value

[true](../../swift/true.md) if the item can receive be focused or [false](../../swift/false.md) if it can not.

## Discussion

You can use this method, or a cell’s [canBecomeFocused](../uiview/canbecomefocused.md) method, to control which items in the collection view can receive focus. The focus engine calls the cell’s [canBecomeFocused](../uiview/canbecomefocused.md) method first, the default implementation of which defers to the collection view and this delegate method.

If you do not implement this method, the ability to focus on items depends on whether the collection view’s items are selectable. When the items are selectable, they can also be focused as if this method had returned [true](../../swift/true.md); otherwise, they do not receive focus.

## See Also

### Related Documentation

- [allowsSelection](../uicollectionview/allowsselection.md) — A Boolean value that indicates whether users can select items in the collection view.

### Working with focus

- [- indexPathForPreferredFocusedViewInCollectionView:](<indexpathforpreferredfocusedview(in_).md>) — Asks the delegate for the index path of the cell that should be focused.
- [- collectionView:shouldUpdateFocusInContext:](<collectionview(__shouldupdatefocusin_).md>) — Asks the delegate whether a change in focus should occur.
- [- collectionView:didUpdateFocusInContext:withAnimationCoordinator:](<collectionview(__didupdatefocusin_with_).md>) — Tells the delegate that a focus update occurred.
- [- collectionView:selectionFollowsFocusForItemAtIndexPath:](<collectionview(__selectionfollowsfocusforitemat_).md>) — Asks the delegate whether to relate selection and focus behavior for the cell at the corresponding index path.
