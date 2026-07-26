---
title: 'drop(_:intoItemAt:rect:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdropcoordinator/drop(_:intoitemat:rect:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdropcoordinator/drop(_:intoitemat:rect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdropcoordinator/drop%28_%3Aintoitemat%3Arect%3A%29.json'
content_hash: 'sha256:5b6ca86ec9e57267'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDropCoordinator](../uicollectionviewdropcoordinator.md)

# drop(_:intoItemAt:rect:)

<sub>Instance Method</sub>

Animates the item to the specified rectangle in the collection view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func drop(_ dragItem: UIDragItem, intoItemAt indexPath: IndexPath, rect: CGRect) -> any UIDragAnimating
```

## Parameters

- `dragItem` — The dragged item that you want to animate into position.

- `indexPath` — The index path in the collection view at which to incorporate the item.

- `rect` — The destination rectangle to use for the animation. Specify the rectangle in the coordinate system of the cell at the specified `indexPath`. UIKit animates the drag item to the specified rectangle.

## Discussion

Use this method to animate drops where you incorporate the dragged items into another item of your collection view. For example, when incorporating items into a folder, you’d use this method to animate the items in a way that makes it look like they were placed into the folder.

## See Also

### Animating Items to Their Destination

- [- dropItem:toItemAtIndexPath:](<drop(__toitemat_).md>) — Animates the item to the specified index path in the collection view.
- [- dropItem:toTarget:](<drop(__to_)-7w5rn.md>) — Animates the item to an arbitrary location in your view hierarchy.
- [- dropItem:toPlaceholder:](<drop(__to_)-l5tg.md>) — Animates the item to the specified location and inserts a placeholder cell at that location.
