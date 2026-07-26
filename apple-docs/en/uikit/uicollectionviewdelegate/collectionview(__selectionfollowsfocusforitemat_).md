---
title: 'collectionView(_:selectionFollowsFocusForItemAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:selectionfollowsfocusforitemat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:selectionfollowsfocusforitemat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Aselectionfollowsfocusforitemat%3A%29.json'
content_hash: 'sha256:5d7f9ee339588f32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:selectionFollowsFocusForItemAt:)

<sub>Instance Method</sub>

Asks the delegate whether to relate selection and focus behavior for the cell at the corresponding index path.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, selectionFollowsFocusForItemAt indexPath: IndexPath) -> Bool
```

## Parameters

- `collectionView` — The collection view making the request.

- `indexPath` — The index path of the cell to determine selection and focus behavior for.

## Return Value

[true](../../swift/true.md) if you want to automatically select the cell at the specified index path when focus moves to it; otherwise, [false](../../swift/false.md).

## Discussion

If the collection view’s [selectionFollowsFocus](../uicollectionview/selectionfollowsfocus.md) property is [true](../../swift/true.md) and you return [false](../../swift/false.md) from this delegate method, focus still moves to the cell when the user selects it. However, when focus moves to the cell, the cell doesn’t automatically select.

## See Also

### Working with focus

- [- collectionView:canFocusItemAtIndexPath:](<collectionview(__canfocusitemat_).md>) — Asks the delegate whether the item at the specified index path can be focused.
- [- indexPathForPreferredFocusedViewInCollectionView:](<indexpathforpreferredfocusedview(in_).md>) — Asks the delegate for the index path of the cell that should be focused.
- [- collectionView:shouldUpdateFocusInContext:](<collectionview(__shouldupdatefocusin_).md>) — Asks the delegate whether a change in focus should occur.
- [- collectionView:didUpdateFocusInContext:withAnimationCoordinator:](<collectionview(__didupdatefocusin_with_).md>) — Tells the delegate that a focus update occurred.
