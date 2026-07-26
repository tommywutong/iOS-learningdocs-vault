---
title: 'collectionView(_:moveItemAt:to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdatasource/collectionview(_:moveitemat:to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/collectionview(_:moveitemat:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdatasource/collectionview%28_%3Amoveitemat%3Ato%3A%29.json'
content_hash: 'sha256:f905e279e6d11105'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDataSource](../uicollectionviewdatasource.md)

# collectionView(_:moveItemAt:to:)

<sub>Instance Method</sub>

Tells your data source object to move the specified item to its new location.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, moveItemAt sourceIndexPath: IndexPath, to destinationIndexPath: IndexPath)
```

## Parameters

- `collectionView` — The collection view notifying you of the move.

- `sourceIndexPath` — The item’s original index path.

- `destinationIndexPath` — The new index path of the item.

## Discussion

You must implement this method to support the reordering of items within the collection view. If you don’t implement this method, the collection view ignores any attempts to reorder items.

When interactions with an item end, the collection view calls this method if the position of the item changed. Use this method to update your data structures with the new index path information.

## See Also

### Reordering items

- [- collectionView:canMoveItemAtIndexPath:](<collectionview(__canmoveitemat_).md>) — Asks your data source object whether the specified item can move to another location in the collection view.
