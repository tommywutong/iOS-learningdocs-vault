---
title: 'collectionViewDidEndMultipleSelectionInteraction(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionviewdidendmultipleselectioninteraction(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionviewdidendmultipleselectioninteraction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionviewdidendmultipleselectioninteraction%28_%3A%29.json'
content_hash: 'sha256:7a7a21951d8c6879'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionViewDidEndMultipleSelectionInteraction(_:)

<sub>Instance Method</sub>

Tells the delegate when the user stops using a two-finger pan gesture to select multiple items in a collection view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func collectionViewDidEndMultipleSelectionInteraction(_ collectionView: UICollectionView)
```

## Parameters

- `collectionView` — The collection view calling this method.

## Discussion

The collection view calls this method after the user lifts their finger from the device.

## See Also

### Managing the selected cells

- [Changing the appearance of selected and highlighted cells](../changing-the-appearance-of-selected-and-highlighted-cells.md) — Provide visual feedback to the user about the state of a cell and the transition between states.
- [Selecting multiple items with a two-finger pan gesture](../selecting-multiple-items-with-a-two-finger-pan-gesture.md) — Accelerate user selection of multiple items using the multiselect gesture on table and collection views.
- [- collectionView:shouldSelectItemAtIndexPath:](<collectionview(__shouldselectitemat_).md>) — Asks the delegate if the specified item should be selected.
- [- collectionView:didSelectItemAtIndexPath:](<collectionview(__didselectitemat_).md>) — Tells the delegate that the item at the specified index path was selected.
- [- collectionView:shouldDeselectItemAtIndexPath:](<collectionview(__shoulddeselectitemat_).md>) — Asks the delegate if the specified item should be deselected.
- [- collectionView:didDeselectItemAtIndexPath:](<collectionview(__diddeselectitemat_).md>) — Tells the delegate that the item at the specified path was deselected.
- [- collectionView:shouldBeginMultipleSelectionInteractionAtIndexPath:](<collectionview(__shouldbeginmultipleselectioninteractionat_).md>) — Asks the delegate whether the user can select multiple items using a two-finger pan gesture in a collection view.
- [- collectionView:didBeginMultipleSelectionInteractionAtIndexPath:](<collectionview(__didbeginmultipleselectioninteractionat_).md>) — Tells the delegate when the user starts using a two-finger pan gesture to select multiple items in a collection view.
