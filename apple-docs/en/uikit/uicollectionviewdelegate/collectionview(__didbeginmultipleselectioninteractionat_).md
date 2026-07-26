---
title: 'collectionView(_:didBeginMultipleSelectionInteractionAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:didbeginmultipleselectioninteractionat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:didbeginmultipleselectioninteractionat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Adidbeginmultipleselectioninteractionat%3A%29.json'
content_hash: 'sha256:b5031941dfe7bbe9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:didBeginMultipleSelectionInteractionAt:)

<sub>Instance Method</sub>

Tells the delegate when the user starts using a two-finger pan gesture to select multiple items in a collection view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, didBeginMultipleSelectionInteractionAt indexPath: IndexPath)
```

## Parameters

- `collectionView` — The collection view calling this method.

- `indexPath` — The index path of the item that the user touched to start the two-finger pan gesture.

## Discussion

Your implementation of this method is a good place to indicate, in the app’s user interface, that the user is selecting multiple items; for example, you could replace an Edit or Select button with a Done button.

```swift
func collectionView(_ collectionView: UICollectionView, didBeginMultipleSelectionInteractionAt indexPath: IndexPath) {
    // Replace the Select button with Done, and put the 
    // collection view into editing mode.
    setEditing(true, animated: true)
}
```

## See Also

### Managing the selected cells

- [Changing the appearance of selected and highlighted cells](../changing-the-appearance-of-selected-and-highlighted-cells.md) — Provide visual feedback to the user about the state of a cell and the transition between states.
- [Selecting multiple items with a two-finger pan gesture](../selecting-multiple-items-with-a-two-finger-pan-gesture.md) — Accelerate user selection of multiple items using the multiselect gesture on table and collection views.
- [- collectionView:shouldSelectItemAtIndexPath:](<collectionview(__shouldselectitemat_).md>) — Asks the delegate if the specified item should be selected.
- [- collectionView:didSelectItemAtIndexPath:](<collectionview(__didselectitemat_).md>) — Tells the delegate that the item at the specified index path was selected.
- [- collectionView:shouldDeselectItemAtIndexPath:](<collectionview(__shoulddeselectitemat_).md>) — Asks the delegate if the specified item should be deselected.
- [- collectionView:didDeselectItemAtIndexPath:](<collectionview(__diddeselectitemat_).md>) — Tells the delegate that the item at the specified path was deselected.
- [- collectionView:shouldBeginMultipleSelectionInteractionAtIndexPath:](<collectionview(__shouldbeginmultipleselectioninteractionat_).md>) — Asks the delegate whether the user can select multiple items using a two-finger pan gesture in a collection view.
- [- collectionViewDidEndMultipleSelectionInteraction:](<collectionviewdidendmultipleselectioninteraction(__).md>) — Tells the delegate when the user stops using a two-finger pan gesture to select multiple items in a collection view.
