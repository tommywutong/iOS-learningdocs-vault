---
title: 'dropInteraction(_:item:willAnimateDropWith:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:item:willanimatedropwith:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:item:willanimatedropwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidropinteractiondelegate/dropinteraction%28_%3Aitem%3Awillanimatedropwith%3A%29.json'
content_hash: 'sha256:26e2da5904a1764d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDropInteractionDelegate](../uidropinteractiondelegate.md)

# dropInteraction(_:item:willAnimateDropWith:)

<sub>Instance Method</sub>

Tells the delegate the system’s drop animation is about to start.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func dropInteraction(_ interaction: UIDropInteraction, item: UIDragItem, willAnimateDropWith animator: any UIDragAnimating)
```

## Parameters

- `interaction` — The interaction that called this method.

- `item` — The current drag item.

- `animator` — The animator that provides custom animations to run alongside the system’s drop animation. You can also use it to add a completion block that runs after the animations have finished.

## Discussion

This method is called for each drag item in the session, whether the item’s visible or not.

## See Also

### Animating the drop

- [- dropInteraction:previewForDroppingItem:withDefault:](<dropinteraction(__previewfordropping_withdefault_).md>) — Asks the delegate for the targeted drag item preview to show during the drop animation.
- [- dropInteraction:concludeDrop:](<dropinteraction(__concludedrop_).md>) — Tells the delegate the drop activity and its related animations have finished.
