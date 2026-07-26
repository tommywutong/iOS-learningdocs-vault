---
title: 'collectionView(_:shouldBeginMultipleSelectionInteractionAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:shouldbeginmultipleselectioninteractionat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:shouldbeginmultipleselectioninteractionat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Ashouldbeginmultipleselectioninteractionat%3A%29.json'
content_hash: 'sha256:3b03437e1596a2b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:shouldBeginMultipleSelectionInteractionAt:)

<sub>Instance Method</sub>

Asks the delegate whether the user can select multiple items using a two-finger pan gesture in a collection view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, shouldBeginMultipleSelectionInteractionAt indexPath: IndexPath) -> Bool
```

## Parameters

- `collectionView` — The collection view calling this method.

- `indexPath` — The index path of the item that the user touched to start the two-finger pan gesture.

## Return Value

[true](../../swift/true.md) to allow the user to select multiple items using a two-finger pan gesture; otherwise, [false](../../swift/false.md) to disable the behavior. The default value is [false](../../swift/false.md).

## Discussion

When the system recognizes a two-finger pan gesture, it calls this method before it sets [editing](../uicollectionview/isediting.md) to [true](../../swift/true.md). If you return [true](../../swift/true.md) from this method, the user can select multiple items using a two-finger pan gesture.

Users can select multiple items using the two-finger pan gesture on collection views that scroll either horizontally or vertically, but not both. Collection views that scroll in both directions won’t recognize the gesture or call this method.

If you don’t implement this method, the system uses the value of [allowsMultipleSelectionDuringEditing](../uicollectionview/allowsmultipleselectionduringediting.md) to determine whether a user can select multiple items using a pan gesture.

## See Also

### Managing the selected cells

- [Changing the appearance of selected and highlighted cells](../changing-the-appearance-of-selected-and-highlighted-cells.md) — Provide visual feedback to the user about the state of a cell and the transition between states.
- [Selecting multiple items with a two-finger pan gesture](../selecting-multiple-items-with-a-two-finger-pan-gesture.md) — Accelerate user selection of multiple items using the multiselect gesture on table and collection views.
- [- collectionView:shouldSelectItemAtIndexPath:](<collectionview(__shouldselectitemat_).md>) — Asks the delegate if the specified item should be selected.
- [- collectionView:didSelectItemAtIndexPath:](<collectionview(__didselectitemat_).md>) — Tells the delegate that the item at the specified index path was selected.
- [- collectionView:shouldDeselectItemAtIndexPath:](<collectionview(__shoulddeselectitemat_).md>) — Asks the delegate if the specified item should be deselected.
- [- collectionView:didDeselectItemAtIndexPath:](<collectionview(__diddeselectitemat_).md>) — Tells the delegate that the item at the specified path was deselected.
- [- collectionView:didBeginMultipleSelectionInteractionAtIndexPath:](<collectionview(__didbeginmultipleselectioninteractionat_).md>) — Tells the delegate when the user starts using a two-finger pan gesture to select multiple items in a collection view.
- [- collectionViewDidEndMultipleSelectionInteraction:](<collectionviewdidendmultipleselectioninteraction(__).md>) — Tells the delegate when the user stops using a two-finger pan gesture to select multiple items in a collection view.
