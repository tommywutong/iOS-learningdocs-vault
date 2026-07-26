---
title: 'collectionView(_:didUnhighlightItemAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:didunhighlightitemat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:didunhighlightitemat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Adidunhighlightitemat%3A%29.json'
content_hash: 'sha256:460f642b2e3365ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:didUnhighlightItemAt:)

<sub>Instance Method</sub>

Tells the delegate that the highlight was removed from the item at the specified index path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, didUnhighlightItemAt indexPath: IndexPath)
```

## Parameters

- `collectionView` — The collection view object that is notifying you of the highlight change.

- `indexPath` — The index path of the cell that had its highlight removed.

## Discussion

The collection view calls this method only in response to user interactions and does not call it if you programmatically change the highlighting on a cell.

## See Also

### Managing cell highlighting

- [- collectionView:shouldHighlightItemAtIndexPath:](<collectionview(__shouldhighlightitemat_).md>) — Asks the delegate if the item should be highlighted during tracking.
- [- collectionView:didHighlightItemAtIndexPath:](<collectionview(__didhighlightitemat_).md>) — Tells the delegate that the item at the specified index path was highlighted.
