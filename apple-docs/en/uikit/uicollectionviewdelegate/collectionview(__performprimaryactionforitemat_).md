---
title: 'collectionView(_:performPrimaryActionForItemAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:performprimaryactionforitemat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:performprimaryactionforitemat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Aperformprimaryactionforitemat%3A%29.json'
content_hash: 'sha256:0e532bd5805f4d83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:performPrimaryActionForItemAt:)

<sub>Instance Method</sub>

Tells the delegate to perform the primary action for the cell at the specified index path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, performPrimaryActionForItemAt indexPath: IndexPath)
```

## Parameters

- `collectionView` — The collection view object on which to perform the primary action.

- `indexPath` — The index path of the cell.

## Discussion

Primary actions allow you to distinguish between a distinct user action and a change in selection (like a focus change or other indirect selection change). A primary action occurs when a person selects a single cell without extending an existing selection.

UIKit calls this method after [- collectionView:shouldSelectItemAtIndexPath:](<collectionview(__shouldselectitemat_).md>) and [- collectionView:didSelectItemAtIndexPath:](<collectionview(__didselectitemat_).md>), regardless of whether the cell selection state changes. Use [- collectionView:didSelectItemAtIndexPath:](<collectionview(__didselectitemat_).md>) to update the state of the current view controller (like its buttons, title, and so on), and use [- collectionView:performPrimaryActionForItemAtIndexPath:](<collectionview(__performprimaryactionforitemat_).md>) for actions like navigation or showing another split view column.

If [- collectionView:shouldSelectItemAtIndexPath:](<collectionview(__shouldselectitemat_).md>) returns [true](../../swift/true.md) to allow selection for the cell at `indexPath`, only that cell has selection when the system calls this method. If [- collectionView:shouldSelectItemAtIndexPath:](<collectionview(__shouldselectitemat_).md>) returns [false](../../swift/false.md), the system preserves the existing cell selection in the collection view. You can use this behavior to perform primary actions on nonselectable, button-style cells without changing the selection.

## See Also

### Managing actions for cells

- [- collectionView:canPerformPrimaryActionForItemAtIndexPath:](<collectionview(__canperformprimaryactionforitemat_).md>) — Asks the delegate whether to perform a primary action for the cell at the specified index path.
