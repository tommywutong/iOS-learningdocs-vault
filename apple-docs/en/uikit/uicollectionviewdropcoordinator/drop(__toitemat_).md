---
title: 'drop(_:toItemAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdropcoordinator/drop(_:toitemat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdropcoordinator/drop(_:toitemat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdropcoordinator/drop%28_%3Atoitemat%3A%29.json'
content_hash: 'sha256:15de62dac278e299'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDropCoordinator](../uicollectionviewdropcoordinator.md)

# drop(_:toItemAt:)

<sub>Instance Method</sub>

Animates the item to the specified index path in the collection view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func drop(_ dragItem: UIDragItem, toItemAt indexPath: IndexPath) -> any UIDragAnimating
```

## Parameters

- `dragItem` — The dragged item that you want to animate into position.

- `indexPath` — The index path to use as the destination for the animation.

## Discussion

Use this method to animate the dragged item to the specific location in the collection view. Typically, you use this method for content that originated in the collection view and is moving to a new location.

## See Also

### Animating Items to Their Destination

- [- dropItem:intoItemAtIndexPath:rect:](<drop(__intoitemat_rect_).md>) — Animates the item to the specified rectangle in the collection view.
- [- dropItem:toTarget:](<drop(__to_)-7w5rn.md>) — Animates the item to an arbitrary location in your view hierarchy.
- [- dropItem:toPlaceholder:](<drop(__to_)-l5tg.md>) — Animates the item to the specified location and inserts a placeholder cell at that location.
