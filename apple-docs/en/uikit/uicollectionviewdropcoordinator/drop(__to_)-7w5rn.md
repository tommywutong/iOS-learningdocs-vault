---
title: 'drop(_:to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdropcoordinator/drop(_:to:)-7w5rn'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdropcoordinator/drop(_:to:)-7w5rn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdropcoordinator/drop%28_%3Ato%3A%29-7w5rn.json'
content_hash: 'sha256:e08708062274b508'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDropCoordinator](../uicollectionviewdropcoordinator.md)

# drop(_:to:)

<sub>Instance Method</sub>

Animates the item to an arbitrary location in your view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func drop(_ dragItem: UIDragItem, to target: UIDragPreviewTarget) -> any UIDragAnimating
```

## Parameters

- `dragItem` — The item that you want to drop.

- `target` — The location at which to drop the item, specified as a point in a view. You can also use the [UIDragPreviewTarget](../uidragpreviewtarget.md) object to specify a final transform to apply to the content.

## Discussion

Use this method to animate drops to any view in your app. For example, you might use this method to drop items onto a tab bar or toolbar that’s part of your interface.

## See Also

### Animating Items to Their Destination

- [- dropItem:toItemAtIndexPath:](<drop(__toitemat_).md>) — Animates the item to the specified index path in the collection view.
- [- dropItem:intoItemAtIndexPath:rect:](<drop(__intoitemat_rect_).md>) — Animates the item to the specified rectangle in the collection view.
- [- dropItem:toPlaceholder:](<drop(__to_)-l5tg.md>) — Animates the item to the specified location and inserts a placeholder cell at that location.
