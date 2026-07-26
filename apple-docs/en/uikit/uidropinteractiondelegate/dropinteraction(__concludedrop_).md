---
title: 'dropInteraction(_:concludeDrop:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:concludedrop:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:concludedrop:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidropinteractiondelegate/dropinteraction%28_%3Aconcludedrop%3A%29.json'
content_hash: 'sha256:dae5b510b2af5074'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDropInteractionDelegate](../uidropinteractiondelegate.md)

# dropInteraction(_:concludeDrop:)

<sub>Instance Method</sub>

Tells the delegate the drop activity and its related animations have finished.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func dropInteraction(_ interaction: UIDropInteraction, concludeDrop session: any UIDropSession)
```

## Parameters

- `interaction` — The interaction that called this method.

- `session` — The drop session that has finished.

## Discussion

When the interaction calls this method, update the interaction’s view with its post-drop appearance.

## See Also

### Animating the drop

- [- dropInteraction:item:willAnimateDropWithAnimator:](<dropinteraction(__item_willanimatedropwith_).md>) — Tells the delegate the system’s drop animation is about to start.
- [- dropInteraction:previewForDroppingItem:withDefault:](<dropinteraction(__previewfordropping_withdefault_).md>) — Asks the delegate for the targeted drag item preview to show during the drop animation.
