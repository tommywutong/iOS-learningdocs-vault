---
title: 'collectionView(_:shouldDeselectItemAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:shoulddeselectitemat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:shoulddeselectitemat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Ashoulddeselectitemat%3A%29.json'
content_hash: 'sha256:89a875b0f95e66f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:shouldDeselectItemAt:)

<sub>Instance Method</sub>

Asks the delegate if the specified item should be deselected.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, shouldDeselectItemAt indexPath: IndexPath) -> Bool
```

## Parameters

- `collectionView` — The collection view object that is asking whether the selection should change.

- `indexPath` — The index path of the cell to be deselected.

## Return Value

[true](../../swift/true.md) if the item should be deselected or [false](../../swift/false.md) if it should not.

## Discussion

The collection view calls this method when the user tries to deselect an item in the collection view. It does not call this method when you programmatically deselect items.

If you do not implement this method, the default return value is [true](../../swift/true.md).

## See Also

### Managing the selected cells

- [Changing the appearance of selected and highlighted cells](../changing-the-appearance-of-selected-and-highlighted-cells.md) — Provide visual feedback to the user about the state of a cell and the transition between states.
- [Selecting multiple items with a two-finger pan gesture](../selecting-multiple-items-with-a-two-finger-pan-gesture.md) — Accelerate user selection of multiple items using the multiselect gesture on table and collection views.
- [- collectionView:shouldSelectItemAtIndexPath:](<collectionview(__shouldselectitemat_).md>) — Asks the delegate if the specified item should be selected.
- [- collectionView:didSelectItemAtIndexPath:](<collectionview(__didselectitemat_).md>) — Tells the delegate that the item at the specified index path was selected.
- [- collectionView:didDeselectItemAtIndexPath:](<collectionview(__diddeselectitemat_).md>) — Tells the delegate that the item at the specified path was deselected.
- [- collectionView:shouldBeginMultipleSelectionInteractionAtIndexPath:](<collectionview(__shouldbeginmultipleselectioninteractionat_).md>) — Asks the delegate whether the user can select multiple items using a two-finger pan gesture in a collection view.
- [- collectionView:didBeginMultipleSelectionInteractionAtIndexPath:](<collectionview(__didbeginmultipleselectioninteractionat_).md>) — Tells the delegate when the user starts using a two-finger pan gesture to select multiple items in a collection view.
- [- collectionViewDidEndMultipleSelectionInteraction:](<collectionviewdidendmultipleselectioninteraction(__).md>) — Tells the delegate when the user stops using a two-finger pan gesture to select multiple items in a collection view.
