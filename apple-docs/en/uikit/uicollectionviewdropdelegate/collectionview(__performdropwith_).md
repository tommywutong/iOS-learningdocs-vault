---
title: 'collectionView(_:performDropWith:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdropdelegate/collectionview(_:performdropwith:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdropdelegate/collectionview(_:performdropwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdropdelegate/collectionview%28_%3Aperformdropwith%3A%29.json'
content_hash: 'sha256:b465747fc6eba03b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDropDelegate](../uicollectionviewdropdelegate.md)

# collectionView(_:performDropWith:)

<sub>Instance Method</sub>

Tells your delegate to incorporate the drop data into the collection view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func collectionView(_ collectionView: UICollectionView, performDropWith coordinator: any UICollectionViewDropCoordinator)
```

## Parameters

- `collectionView` — The collection view that received the drop.

- `coordinator` — The coordinator object to use when handling the drop. Use this object to coordinate your custom behavior with the default behavior of the collection view.

## Discussion

Use this method to accept the dropped content and integrate it into your collection view. In your implementation, iterate over the [items](../uicollectionviewdropcoordinator/items.md) property of the `coordinator` object and fetch the data from each [UIDragItem](../uidragitem.md). Incorporate the data into your collection view’s data source and update the collection view itself by inserting any needed items. When incorporating items, use the methods of the `coordinator` object to animate the transition from the drag item’s preview to the corresponding item in your collection view. For items that you incorporate immediately, you can use the [- dropItem:toTarget:](<../uicollectionviewdropcoordinator/drop(__to_)-7w5rn.md>) or [- dropItem:toItemAtIndexPath:](<../uicollectionviewdropcoordinator/drop(__toitemat_).md>) method to perform the animation.
