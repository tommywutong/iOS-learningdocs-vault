---
title: 'collectionView(_:canMoveItemAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdatasource/collectionview(_:canmoveitemat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/collectionview(_:canmoveitemat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdatasource/collectionview%28_%3Acanmoveitemat%3A%29.json'
content_hash: 'sha256:103e3381479782cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDataSource](../uicollectionviewdatasource.md)

# collectionView(_:canMoveItemAt:)

<sub>Instance Method</sub>

Asks your data source object whether the specified item can move to another location in the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, canMoveItemAt indexPath: IndexPath) -> Bool
```

## Parameters

- `collectionView` — The collection view requesting this information.

- `indexPath` — The index path of the item that the collection view is trying to move.

## Return Value

[true](../../swift/true.md) if the item is allowed to move, or [false](../../swift/false.md) if it isn’t.

## Discussion

Use this method to selectively allow or disallow the movement of items within a collection view. If you don’t implement this method, but you do implement the [- collectionView:moveItemAtIndexPath:toIndexPath:](<collectionview(__moveitemat_to_).md>) method, the collection view allows all items to be reordered.

## See Also

### Reordering items

- [- collectionView:moveItemAtIndexPath:toIndexPath:](<collectionview(__moveitemat_to_).md>) — Tells your data source object to move the specified item to its new location.
