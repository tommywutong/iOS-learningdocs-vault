---
title: 'collectionView(_:shouldHighlightItemAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:shouldhighlightitemat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:shouldhighlightitemat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Ashouldhighlightitemat%3A%29.json'
content_hash: 'sha256:ed85ecb69fc9aed5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:shouldHighlightItemAt:)

<sub>Instance Method</sub>

Asks the delegate if the item should be highlighted during tracking.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, shouldHighlightItemAt indexPath: IndexPath) -> Bool
```

## Parameters

- `collectionView` — The collection view object that is asking about the highlight change.

- `indexPath` — The index path of the cell to be highlighted.

## Return Value

[true](../../swift/true.md) if the item should be highlighted or [false](../../swift/false.md) if it should not.

## Discussion

As touch events arrive, the collection view highlights items in anticipation of the user selecting them. As it processes those touch events, the collection view calls this method to ask your delegate if a given cell should be highlighted. It calls this method only in response to user interactions and does not call it if you programmatically set the highlighting on a cell.

If you return [false](../../swift/false.md) in your implementation, the cell does not get highlighted and the system bypasses the entire selection process. That is, the system does not call [- collectionView:shouldSelectItemAtIndexPath:](<collectionview(__shouldselectitemat_).md>) or any other selection-related methods. If you return [true](../../swift/true.md), [highlighted](../uicollectionviewcell/ishighlighted.md) is set to [true](../../swift/true.md), [- collectionView:didHighlightItemAtIndexPath:](<collectionview(__didhighlightitemat_).md>) is called, and the system begins the selection process.

If you do not implement this method, the default return value is [true](../../swift/true.md).

## See Also

### Managing cell highlighting

- [- collectionView:didHighlightItemAtIndexPath:](<collectionview(__didhighlightitemat_).md>) — Tells the delegate that the item at the specified index path was highlighted.
- [- collectionView:didUnhighlightItemAtIndexPath:](<collectionview(__didunhighlightitemat_).md>) — Tells the delegate that the highlight was removed from the item at the specified index path.
