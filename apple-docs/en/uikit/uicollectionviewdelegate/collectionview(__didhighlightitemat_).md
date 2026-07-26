---
title: 'collectionView(_:didHighlightItemAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:didhighlightitemat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:didhighlightitemat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Adidhighlightitemat%3A%29.json'
content_hash: 'sha256:b263ed7349ce346a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:didHighlightItemAt:)

<sub>Instance Method</sub>

Tells the delegate that the item at the specified index path was highlighted.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, didHighlightItemAt indexPath: IndexPath)
```

## Parameters

- `collectionView` — The collection view object that is notifying you of the highlight change.

- `indexPath` — The index path of the cell that was highlighted.

## Discussion

The collection view calls this method only in response to user interactions and does not call it if you programmatically set the highlighting on a cell.

## See Also

### Managing cell highlighting

- [- collectionView:shouldHighlightItemAtIndexPath:](<collectionview(__shouldhighlightitemat_).md>) — Asks the delegate if the item should be highlighted during tracking.
- [- collectionView:didUnhighlightItemAtIndexPath:](<collectionview(__didunhighlightitemat_).md>) — Tells the delegate that the highlight was removed from the item at the specified index path.
