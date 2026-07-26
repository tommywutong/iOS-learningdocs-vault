---
title: 'drop(_:toRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdropcoordinator/drop(_:torowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdropcoordinator/drop(_:torowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdropcoordinator/drop%28_%3Atorowat%3A%29.json'
content_hash: 'sha256:762d2bee6dc28caf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDropCoordinator](../uitableviewdropcoordinator.md)

# drop(_:toRowAt:)

<sub>Instance Method</sub>

Animates the item to the specified index path in the table view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func drop(_ dragItem: UIDragItem, toRowAt indexPath: IndexPath) -> any UIDragAnimating
```

## Parameters

- `dragItem` — The dragged item that you want to animate into position.

- `indexPath` — The index path to use as the destination for the animation.

## Discussion

Use this method to animate the dragged item to the specific location in the table view. Typically, you use this method for content that originated in the collection view and is moving to a new location.

## See Also

### Animating rows to their destination

- [- dropItem:intoRowAtIndexPath:rect:](<drop(__intorowat_rect_).md>)
- [- dropItem:toTarget:](<drop(__to_)-57wx.md>) — Animates the item to an arbitrary location in your view hierarchy.
- [- dropItem:toPlaceholder:](<drop(__to_)-3znax.md>) — Animates the item to the specified location and inserts a placeholder cell at that location.
